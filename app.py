import gradio as gr 
import librosa
import pandas as pd 
from PIL import Image









# def gallery():

#     return [

#         Image.open("cat1.jpg"),
#         Image.open("cat2.jpg"),
#         Image.open("cat3.jpg")
#     ]

# demo = gr.Interface(

#     fn = gallery,

#     inputs=None,

#     outputs=gr.Gallery()
# )

# demo.launch()


# gr.Gallery(
#     columns=3
# )



# gr.Gallery(

#     height=500
# )



# gr.Gallery(

#     preview=True
# )






# def read(file):

#     df = pd.read_csv(file.name)


#     return df.head()


# demo = gr.Interface(

#     fn = read,

#     inputs=gr.File(),

#     outputs=gr.DataFrame()
# )


# demo.launch()







# def upload(file):

#     return file.name

# demo = gr.Interface(

#     fn = upload,

#     inputs=gr.File(),

#     outputs="text"
# )

# demo.launch()




# gr.File(

#     file_types=[

#         ".csv"
#     ]
# )


# gr.File(

#     file_types=[

#         ".xlsx"
#     ]
# )


# gr.File(

#     file_types=[
#         ".pdf"
#     ]
# )


# gr.File(

#     file_types=[
#         ".png",

#         ".jpg",

#         ".jpeg"
#     ]
# )

# gr.File(

#     file_count="multiple"
# )


# gr.File(

#     file_count="directory"
# )




# def path(video):

#     return video

# demo = gr.Interface(

#     fn = path,

#     inputs=gr.Video(),

#     outputs="text"
# )

# demo.launch()




# def video(video):

#     return video

# demo = gr.Interface(

#     fn = video,

#     inputs= gr.Video(),

#     outputs=gr.Video()
# )


# demo.launch


# gr.Video(

#     sources=["upload"]
# )


# gr.Video(

#     sources=["webcam"]
# )


# gr.Video(

#     sources=[

#         "upload",

#         "webcam"
#     ]
# )





# def duration(audio):

#     y, sr= librosa.load(audio)

#     return librosa.get_duration(y=y, sr=sr)

# demo = gr.Interface(
#     fn = duration,
#     inputs=gr.Audio(
#         type="filepath"
#     ),

#     outputs="number"
# )

# demo.launch()





# def audio(audio):
#     return audio 

# demo = gr.Interface(

#     fn = audio,

#     inputs=gr.Audio(),

#     outputs=gr.Audio()
# )

# demo.launch()


# gr.Audio(
#     type="filepath"
# )


# gr.Audio(

#     type="numpy"
# )


# gr.Audio(

#     sources=[
#         "microphone"
#     ]
# )

# gr.Audio(
#     sources= [
#         "upload"
#     ]
# )


# gr.Audio(

#     sources=[
#         "upload",
#         "microphone"
#     ]
# )






# def size(img):

#     return str(img.shape)


# demo = gr.Interface(

#     fn = size,

#     inputs=gr.Image(),

#     outputs="text"
# )


# demo.launch()










# gr.Image(

#     label="Upload Image"
# )


# gr.Image(
#     height=400
# )

# gr.Image(

#     widht=500
# )


# gr.Image(
#     type="numpy"
# )

# gr.Image(

#     type="pil"
# )


# gr.Image(
#     type="filepath"
# )


# gr.Image(
#     format="png"
# )

# gr.Image(
#     sources=["upload"]
# )


# gr.Image(
#     sources=[
#         "upload",
#         "webcam"
#     ]
# )





# def show(image):
#     return image

# demo = gr.Interface(
#     fn = show,

#     inputs=gr.Image(),

#     outputs=gr.Image()

# )

# demo.launch












# def employee(name, gender, department, skills, remote):

#     return f"""
# Name: {name}


# Gender:  {gender}

# Department: {department}


# Skills: {", ".join(skills)}

# Remote Work: {"Yes" if remote else "No"}
# """

# demo = gr.Interface(

#     fn= employee,

#     inputs=[
#         gr.Textbox(label="Name"),

#         gr.Radio(
#             ["Male", "Female"],

#             label="Gender"
#         ),

#         gr.Dropdown(
#             [
#                 "Ai",

#                 "Backend",

#                 "Frontend",

#                 "Data Scinece"
#             ],
#             label="Department"
#         ),

#         gr.CheckboxGroup(

#             [
#                 "Python",

#                 "SQL",

#                 "Docker",

#                 "GIT"
#             ],
#             label="Skills"
#         ),

#         gr.Checkbox(
#             label="Remote Work"
#         )
#     ],

#     outputs=gr.Textbox(
#         label="Employee Summary"
#     ),

#     title="Employee Registration"
# )


# demo.launch()










# def coursera(x):

#     return f"You selected {len(x)} course(s)."

# demo=gr.Interface(
#     fn = coursera,

#     inputs=gr.CheckboxGroup(
#         [
#             "ML",
#             "DL",
#             "CV",
#             "NLP"
#         ]
#     ),

#     outputs="text"

# )

# demo.launch()





# def skills(x):

#     return x

# demo = gr.Interface(

#     fn = skills,

#     inputs=gr.CheckboxGroup(
#         [
#             "Python",
#             "SQL",
#             "FastAPI",
#             "Docker",
#             "Git"
#         ]
#     ),

#     outputs="text"
# )

# demo.launch()






# def country(x):

#     return f"Country: {x}"


# demo = gr.Interface(
#     fn = country,

#     inputs=gr.Dropdown(

#         [
#             "UZB",
#             "GRB",
#             "USA",
#             "KOR"
#         ]
#     ),


#     outputs="text"
# )

# demo.launch()



# gr.Dropdown(
#     [
#         "Python",
#         "Java",
#         "C++"
#     ],

#     value="Python"
# )





# def city(x):

#     return x 


# demo = gr.Interface(
#     fn = city,

#     inputs=gr.Dropdown(

#         [
#             "Khiva",
#             "Buhoro",
#             "Samarqand",
#             "Toshkent"
#         ]
#     ),


#     outputs="text"
# )

# demo.launch()











# def optimizer(opt):

#     return f"Optimizer {opt}" 

# demo = gr.Interface(

#     fn = optimizer,

#     inputs = gr.Radio(
#         [
#             "Adam",

#             "SGD",

#             "RMSProp"
            
#         ],

#         label="Optimizer"
#     ),

#     outputs= "text"
# )


# demo.launch()






# def language(x):

#     return f"You selected {x}" 

# demo = gr.Interface(

#     fn = language,

#     inputs = gr.Radio(
#         [
#             "Python",

#             "Java",

#             "C++",

#             "Go"
#         ]
#     ),

#     outputs= "text"
# )


# demo.launch()









# def gender(x):

#     return x 

# demo = gr.Interface(
#     fn = gender,

#     inputs = gr.Radio(
#         [
#             "Male",

#             "Female"
#         ]
#     ),

#     outputs= "text"
# )


# demo.launch()



# def theme(flag):

#     return "Dark" if flag else "Light"
    

# demo= gr.Interface(

#     fn = theme,

#     inputs = gr.Checkbox(

#         label="Dark Mode"
#     ),


#     outputs="text"
# )

# demo.launch()



# def gpu(flag):

#     if flag:
#         return "GPU Enabled"

#     return "CPU Mode"

# demo= gr.Interface(

#     fn = gpu,

#     inputs = gr.Checkbox(

#         label="USE GPU"
#     ),


#     outputs="text"
# )

# demo.launch()




# gr.Checkbox(

#     value=True
# )


# gr.Checkbox(

#     interactive=True
# )


# gr.Checkbox(

#     value=True,
#     interactive=False
# )




# def remember(flag):

#     if flag:
#         return "Remember Enabled"

#     return "Remember Disabled"



# demo = gr.Interface(

#     fn = remember,

#     inputs=gr.Checkbox(

#         label="Remember Me"
#     ),


#     outputs='text'

# )

# demo.launch()











# def status(x):

#     return x 


# demo = gr.Interface(

#     fn = status,
#     inputs=gr.Checkbox(),
#     outputs="text"

# )


# demo.launch()








# def employee(name, age, exp):

#     return f"""
# Name : {name}

# Age : {age}


# Experience : {exp} years
# """

# demo = gr.Interface(

#     fn = employee,

#     inputs= [

#         gr.Textbox(label="Name"),
#         gr.Number(label="Age"),
#         gr.Slider(

#             0, 
#             40,
#             value=2,

#             label="Experience"
#         )
#     ],


#     outputs=gr.Textbox(

#         label="Employee Information: "
#     ),

#     title="Employee Information System"
# )

# demo.launch()



# def batch(x):

#     return f"Batch Size:  {x}"


# demo = gr.Interface(

#     fn = batch,

#     inputs= gr.Slider(

#         minimum=1,

#         maximum=412,

#         value=32,

#         step= 1       

        
#     ),

#     outputs="text"
# )


# demo.launch()



# def epoch(x):

#     return f"Epoch:  {x}"


# demo = gr.Interface(

#     fn = epoch,

#     inputs= gr.Slider(

#         minimum=1,

#         maximum=500,

#         value=100,

#         step= 1       

        
#     ),

#     outputs="text"
# )


# demo.launch()




# def train(lr):

#     return f"Learning Rate :  {lr}"


# demo = gr.Interface(

#     fn = train,

#     inputs= gr.Slider(

#         minimum=0.0001,

#         maximum=0.1,

#         step= 0.0001,

#         value=0.001,

#         label="Learning Rate"
#     ),

#     outputs="text"
# )


# demo.launch()




# def predict(conf):

#     return f"Confidence :  {conf}"


# demo = gr.Interface(

#     fn = predict,

#     inputs= gr.Slider(

#         minimum=0,

#         maximum=1,

#         step= 0.01,

#         value=0.50,

#         label="Confidence"
#     ),

#     outputs="text"
# )


# demo.launch()




# gr.Slider(

#     minimum=0,

#     maximum=100,

#     step= 5
# )



# gr.Slider(

#     minimum=0,

#     maximum=100,

#     step= 50
# )



# gr.Slider(

#     minimum=0,

#     maximum=10,

#     label= "Epoch"
# )

