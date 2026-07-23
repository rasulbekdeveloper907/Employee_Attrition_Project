import cv2
import numpy as np
import mediapipe as mp
import math
import random
import time
from collections import deque


CAM_INDEX = 0
FRAME_W, FRAME_H = 960, 540
NUM_STARS = 160
TRAIL_MAX_LEN = 40
PINCH_THRESHOLD = 40          
PINCH_COOLDOWN = 0.6          
GLOW_COLOR = (255, 220, 60)   
TRAIL_COLOR = (255, 220, 60)



class Starfield:
    def __init__(self, w, h, n_stars):
        self.w, self.h = w, h
        self.stars = [
            {
                "x": random.uniform(0, w),
                "y": random.uniform(0, h),
                "r": random.uniform(0.5, 1.8),
                "speed": random.uniform(2, 10),
                "phase": random.uniform(0, math.pi * 2),
            }
            for _ in range(n_stars)
        ]

    def draw(self, canvas):
        t = time.time()
        for s in self.stars:
            
            twinkle = 0.5 + 0.5 * math.sin(t * 2 + s["phase"])
            brightness = int(120 + 135 * twinkle)
            color = (brightness, brightness, brightness)
            cv2.circle(canvas, (int(s["x"]), int(s["y"])), max(1, int(s["r"])), color, -1)

            
            s["y"] += s["speed"] * 0.02
            if s["y"] > self.h:
                s["y"] = 0
                s["x"] = random.uniform(0, self.w)



def draw_glow_line(layer, pt1, pt2, color, thickness=2):
    cv2.line(layer, pt1, pt2, color, thickness, cv2.LINE_AA)


def add_glow(base, glow_layer, blur_ksize=15, intensity=1.0):
    """Blur the glow layer and additively blend it onto the base image."""
    blurred = cv2.GaussianBlur(glow_layer, (blur_ksize, blur_ksize), 0)
    return cv2.addWeighted(base, 1.0, blurred, intensity, 0)



class WireShape:
    def __init__(self, center, kind=None):
        self.center = center
        self.birth = time.time()
        self.lifetime = 4.0
        self.kind = kind or random.choice(["ring", "poly"])
        self.rot_speed = random.uniform(1.0, 2.0) * random.choice([-1, 1])

    def alive(self):
        return (time.time() - self.birth) < self.lifetime

    def draw(self, layer):
        age = time.time() - self.birth
        fade = max(0.0, 1.0 - age / self.lifetime)
        angle = age * self.rot_speed
        cx, cy = self.center

        if self.kind == "ring":
            
            axes = (int(38 * fade + 10), int(14 * fade + 4))
            cv2.ellipse(layer, (cx, cy), axes, math.degrees(angle) % 180,
                        0, 360, tuple(int(c * fade) for c in GLOW_COLOR), 2, cv2.LINE_AA)
            cv2.circle(layer, (cx, cy), int(16 * fade + 4),
                       tuple(int(c * fade) for c in GLOW_COLOR), 2, cv2.LINE_AA)
        else:
            
            n_sides = 6
            r = 30 * fade + 8
            pts = []
            for i in range(n_sides):
                a = angle + i * (2 * math.pi / n_sides)
                pts.append((int(cx + r * math.cos(a)), int(cy + r * math.sin(a))))
            color = tuple(int(c * fade) for c in GLOW_COLOR)
            for i in range(n_sides):
                cv2.line(layer, pts[i], pts[(i + 1) % n_sides], color, 2, cv2.LINE_AA)



def main():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.6,
    )

    cap = cv2.VideoCapture(CAM_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_W)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_H)

    if not cap.isOpened():
        print("Could not open webcam. Check CAM_INDEX or camera permissions.")
        return

    starfield = Starfield(FRAME_W, FRAME_H, NUM_STARS)
    trail = deque(maxlen=TRAIL_MAX_LEN)
    shapes = []
    last_pinch_time = 0.0

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (FRAME_W, FRAME_H))


        canvas = np.zeros_like(frame)
        starfield.draw(canvas)

        
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        glow_layer = np.zeros_like(frame)

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            lm = hand_landmarks.landmark

            index_tip = (int(lm[8].x * FRAME_W), int(lm[8].y * FRAME_H))
            thumb_tip = (int(lm[4].x * FRAME_W), int(lm[4].y * FRAME_H))

            
            trail.append(index_tip)

            
            dist = math.hypot(index_tip[0] - thumb_tip[0], index_tip[1] - thumb_tip[1])
            now = time.time()
            if dist < PINCH_THRESHOLD and (now - last_pinch_time) > PINCH_COOLDOWN:
                shapes.append(WireShape(index_tip))
                last_pinch_time = now

            
            cv2.circle(glow_layer, index_tip, 6, GLOW_COLOR, -1, cv2.LINE_AA)
        else:
            
            if trail:
                trail.popleft()

        
        pts = list(trail)
        for i in range(1, len(pts)):
            fade = i / len(pts)
            thickness = max(1, int(3 * fade))
            color = tuple(int(c * fade) for c in TRAIL_COLOR)
            draw_glow_line(glow_layer, pts[i - 1], pts[i], color, thickness)

        
        shapes = [s for s in shapes if s.alive()]
        for s in shapes:
            s.draw(glow_layer)

        
        output = add_glow(canvas, glow_layer, blur_ksize=15, intensity=1.4)        
        output = cv2.addWeighted(output, 1.0, glow_layer, 0.6, 0)

        cv2.putText(output, "Pinch to spawn a shape  |  'c' clear  |  'q' quit",
                    (10, FRAME_H - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (180, 180, 180), 1, cv2.LINE_AA)

        cv2.imshow("Hand Magic", output)

        key = cv2.waitKey(1) & 0xFF
        if key in (ord('q'), 27):
            break
        elif key == ord('c'):
            shapes.clear()
            trail.clear()

    cap.release()
    cv2.destroyAllWindows()
    hands.close()


if __name__ == "__main__":
    main()
