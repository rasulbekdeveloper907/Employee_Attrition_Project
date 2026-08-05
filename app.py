import gradio as gr 
import librosa
import pandas as pd 
from PIL import Image
import time
import matplotlib.pyplot as plt
import joblib
from xgboost import XGBClassifier
import xgboost as xgb
from tensorflow.keras.models import load_model
import easyocr






# import gradio as gr

# def predict(image,task):

#     return f"{task} Finished"

# with gr.Blocks() as demo:

#     image = gr.Image()

#     task = gr.Dropdown(

#         [

#             "Classification",

#             "YOLO",

#             "OCR"

#         ]

#     )

#     button = gr.Button(

#         "Run",

#         variant="primary"

#     )

#     output = gr.Textbox()

#     button.click(

#         predict,

#         [image,task],

#         output

#     )

# demo.launch()



# reader = easyocr.Reader(

#     ["en"]

# )

# def ocr(image):

#     result = reader.readtext(image)

#     return result

# gr.Interface(

#     ocr,

#     gr.Image(),

#     gr.JSON()

# ).launch()





# model = YOLO(

#     "best.pt"

# )

# def detect(image):

#     result = model(image)

#     return result[0].plot()

# gr.Interface(

#     detect,

#     gr.Image(),

#     gr.Image()

# ).launch()







# model = torch.load(

#     "model.pth"

# )

# model.eval()

# def predict(image):

#     with torch.no_grad():

#         prediction = model(image)

#     return prediction.argmax().item()

# gr.Interface(

#     predict,

#     gr.Image(),

#     gr.Number()

# ).launch()



# import torch

# model = torch.load(

#     "model.pth"

# )

# model.eval()



# import torch

# prediction = model(

#     tensor

# )




# model = load_model(

#     "model.keras"

# )

# labels = [

#     "Cat",

#     "Dog"

# ]

# def predict(image):

#     image = np.expand_dims(

#         image,

#         axis=0

#     )

#     prediction = model.predict(image)

#     return labels[

#         prediction.argmax()

#     ]

# gr.Interface(

#     predict,

#     inputs=gr.Image(),

#     outputs="text"

# ).launch()



# model = joblib.load(

#     "employee_model.pkl"

# )

# def predict(

#     age,

#     salary

# ):

#     prediction = model.predict(

#         [[age,salary]]

#     )[0]

#     probability = model.predict_proba(

#         [[age,salary]]

#     ).max()

#     return {

#         "Prediction":str(prediction),

#         "Probability":float(probability)

#     }

# gr.Interface(

#     predict,

#     [

#         gr.Number(),

#         gr.Number()

#     ],

#     gr.JSON()

# ).launch()



# model = joblib.load(

#     "employee_model.pkl"

# )

# def predict(age,salary):

#     pred=model.predict(

#         [[age,salary]]

#     )[0]

#     prob=model.predict_proba(

#         [[age,salary]]

#     ).max()

#     return pred,f"{prob:.2%}",{

#         "prediction":str(pred),

#         "probability":float(prob)

#     }

# with gr.Blocks() as demo:

#     gr.Markdown(

#         "# 🤖 Employee Attrition Predictor"

#     )

#     age=gr.Number(label="Age")

#     salary=gr.Number(label="Salary")

#     btn=gr.Button(

#         "Predict",

#         variant="primary"

#     )

#     prediction=gr.Textbox(

#         label="Prediction"

#     )

#     probability=gr.Textbox(

#         label="Probability"

#     )

#     details=gr.JSON(

#         label="Model Output"

#     )

#     btn.click(

#         predict,

#         [age,salary],

#         [prediction,probability,details]

#     )

# demo.launch()





# model = joblib.load(

#     "employee_model.pkl"

# )

# def predict(

#     age,

#     salary

# ):

#     pred = model.predict(

#         [[age,salary]]

#     )[0]

#     prob = model.predict_proba(

#         [[age,salary]]

#     ).max()

#     return pred,f"{prob:.2%}"

# with gr.Blocks() as demo:

#     age = gr.Number()

#     salary = gr.Number()

#     btn = gr.Button(

#         "Predict"

#     )

#     pred = gr.Textbox()

#     prob = gr.Textbox()

#     btn.click(

#         predict,

#         [age,salary],

#         [pred,prob]

#     )

# demo.launch()




# model = joblib.load(r"C:\Users\Rasulbekk\Desktop\Employee_Attrition_Project\Models\xgboost_model.pkl"

# )

# def predict(

#     age,

#     salary

# ):

#     result = model.predict(

#         [[age,salary]]

#     )[0]

#     return result

# with gr.Blocks() as demo:

#     gr.Markdown(

#         "# Employee Prediction"

#     )

#     age = gr.Number(

#         label="Age"

#     )

#     salary = gr.Number(

#         label="Salary"

#     )

#     button = gr.Button(

#         "Predict",

#         variant="primary"

#     )

#     output = gr.Textbox(

#         label="Prediction"

#     )

#     button.click(

#         predict,

#         [age,salary],

#         output

#     )

# demo.launch()


# def analyze(df):

#     fig=plt.figure()

#     df.hist()

#     return df.describe(),fig

# with gr.Blocks() as demo:

#     gr.Markdown(

#         "# Employee Analytics Dashboard"

#     )

#     data=gr.Dataframe()

#     btn=gr.Button(

#         "Analyze",

#         variant="primary"

#     )

#     stats=gr.Dataframe()

#     chart=gr.Plot()

#     btn.click(

#         analyze,

#         data,

#         [stats,chart]

#     )

# demo.launch()


# code="""

# def predict(x):

#     return model.predict(x)

# """

# gr.Interface(

#     lambda:code,

#     outputs=gr.Code()

# ).launch()


# import gradio as gr

# def info():
#     return {
#         "Accuracy": 0.96,
#         "Model": "XGBoost",
#         "Version": "1.0"
#     }

# demo = gr.Interface(
#     fn=info,
#     inputs=[],
#     outputs=gr.JSON()
# )

# demo.launch()

