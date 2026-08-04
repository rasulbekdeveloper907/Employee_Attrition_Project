import gradio as gr 
import librosa
import pandas as pd 
from PIL import Image



# import gradio as gr

# def words(text):

#     return len(text.split())

# with gr.Blocks() as demo:

#     txt=gr.Textbox(lines=5)

#     out=gr.Number()

#     txt.input(

#         words,

#         txt,

#         out

#     )

# demo.launch()

# import gradio as gr

# def upper(text):

#     return text.upper()

# with gr.Blocks() as demo:

#     inp=gr.Textbox()

#     out=gr.Textbox()

#     inp.input(

#         upper,

#         inp,

#         out

#     )

# demo.launch()


# import gradio as gr

# def counter(text):

#     return len(text)

# with gr.Blocks() as demo:

#     txt=gr.Textbox()

#     out=gr.Number()

#     txt.input(

#         counter,

#         txt,

#         out

#     )

# demo.launch()



# def gpu(flag):

#     return "GPU Enabled" if flag else "CPU"

# with gr.Blocks() as demo:

#     chk=gr.Checkbox()

#     txt=gr.Textbox()

#     chk.change(

#         gpu,

#         chk,

#         txt

#     )

# demo.launch()

# import gradio as gr

# def language(lang):

#     return f"You selected {lang}"

# with gr.Blocks() as demo:

#     d=gr.Dropdown(

#         [

#             "Python",

#             "Java",

#             "C++"

#         ]

#     )

#     out=gr.Textbox()

#     d.change(

#         language,

#         d,

#         out

#     )

# demo.launch()


# import gradio as gr

# def square(x):

#     return x*x

# with gr.Blocks() as demo:

#     slider=gr.Slider(0,100)

#     out=gr.Number()

#     slider.change(

#         square,

#         slider,

#         out

#     )

# demo.launch()


# import gradio as gr

# def calc(a,b):

#     return a+b,a*b

# with gr.Blocks() as demo:

#     a=gr.Number()

#     b=gr.Number()

#     add=gr.Number()

#     mul=gr.Number()

#     gr.Button("Calculate").click(

#         calc,

#         [a,b],

#         [add,mul]

#     )

# demo.launch()

# def employee(name, age):

#     return f"{name} : {age}"

# with gr.Blocks() as demo:

#     name = gr.Textbox()

#     age = gr.Number()

#     out = gr.Textbox()

#     btn = gr.Button("Show")

#     btn.click(

#         employee,

#         [name, age],

#         out

#     )

# demo.launch()



# import gradio as gr

# def predict(age):

#     if age > 30:
#         return "Stay"

#     return "Leave"

# with gr.Blocks() as demo:

#     age = gr.Number()

#     result = gr.Textbox()

#     btn = gr.Button("Predict")

#     btn.click(

#         fn=predict,

#         inputs=age,

#         outputs=result

#     )

# demo.launch()



# import gradio as gr

# def hello():

#     return "Button Clicked!"

# with gr.Blocks() as demo:

#     output = gr.Textbox()

#     button = gr.Button("Click Me")

#     button.click(

#         fn=hello,

#         outputs=output

#     )

# demo.launch()







# def predict(age,salary):

#     if age>35:

#         return "Employee will Stay"

#     return "Employee may Leave"

# css="""

# h1{

# text-align:center;

# }

# """

# with gr.Blocks(

# css=css,

# theme=gr.themes.Soft()

# ) as demo:

#     gr.Markdown("# Employee Attrition Dashboard")

#     with gr.Row():

#         with gr.Group():

#             gr.Markdown("### Employees")

#             gr.Markdown("2450")

#         with gr.Group():

#             gr.Markdown("### Accuracy")

#             gr.Markdown("96%")

#         with gr.Group():

#             gr.Markdown("### Models")

#             gr.Markdown("5")

#     with gr.Row():

#         with gr.Column(scale=2):

#             age=gr.Number(label="Age")

#             salary=gr.Number(label="Salary")

#             button=gr.Button(

#                 "Predict",

#                 variant="primary"

#             )

#         with gr.Column():

#             result=gr.Textbox(

#                 label="Prediction"

#             )

#     button.click(

#         predict,

#         [age,salary],

#         result

#     )

#     gr.Markdown("""

# ---

# ©2026

# Developed using Gradio

# """)

# demo.launch()


# import gradio as gr

# with gr.Blocks(

#     theme=gr.themes.Glass()

# ) as demo:

#     gr.Markdown("# Glass Theme")

# demo.launch()


# import gradio as gr

# with gr.Blocks(

#     theme=gr.themes.Monochrome()

# ) as demo:

#     gr.Markdown("# Monochrome")

# demo.launch()


# with gr.Blocks(

#     theme=gr.themes.Soft()

# ) as demo:

#     gr.Markdown("# Soft Theme")

# demo.launch()



# import gradio as gr

# css="""

# footer{

# display:none;

# }

# """

# with gr.Blocks(css=css) as demo:

#     gr.Markdown("# AI")

# demo.launch()

# import gradio as gr

# css="""

# button{

# font-size:18px;

# }

# """

# with gr.Blocks(css=css) as demo:

#     gr.Button("Predict")

# demo.launch()

# import gradio as gr

# css="""

# h1{

# color:#0066ff;

# text-align:center;

# }

# """

# with gr.Blocks(css=css) as demo:

#     gr.Markdown("# AI Dashboard")

# demo.launch()

# import gradio as gr

# css="""

# body{

# background:#f4f6f8;

# }

# """

# with gr.Blocks(css=css) as demo:

#     gr.Markdown("# Dashboard")

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     gr.Markdown("""

# ---

# © 2026

# Developer : Rasulbek

# Powered by Gradio

# """)

# demo.launch()


# def predict(age,salary):

#     if age>35:

#         return "Stay"

#     return "Leave"

# with gr.Blocks() as demo:

#     with gr.Row():

#         with gr.Column(scale=2):

#             age=gr.Number(label="Age")

#             salary=gr.Number(label="Salary")

#             btn=gr.Button("Predict")

#         with gr.Column():

#             result=gr.Textbox(label="Prediction")

#     btn.click(

#         predict,

#         [age,salary],

#         result

#     )

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Row():

#         with gr.Group():

#             gr.Markdown("### Highest Salary")

#             gr.Number(value=250000)

#         with gr.Group():

#             gr.Markdown("### Average Age")

#             gr.Number(value=34)

# demo.launch()

# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Row():

#         with gr.Group():

#             gr.Markdown("## 👨 Employees")

#             gr.Markdown("2450")

#         with gr.Group():

#             gr.Markdown("## 📊 Accuracy")

#             gr.Markdown("96.4 %")

#         with gr.Group():

#             gr.Markdown("## 🚀 Predictions")

#             gr.Markdown("12,584")

# demo.launch()



# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Row():

#         gr.Markdown("""

# ### 👥 Employees

# 2450

# """)

#         gr.Markdown("""

# ### 📈 Accuracy

# 96%

# """)

#         gr.Markdown("""

# ### 🤖 Models

# 12

# """)

# demo.launch()




# import gradio as gr

# with gr.Blocks() as demo:

#     gr.HTML("""

# <div style="text-align:center">

# <h1>🤖 AI Dashboard</h1>

# <h3>Machine Learning Prediction System</h3>

# </div>

# """)

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     gr.Markdown("""

# # 🤖 Employee Attrition Dashboard

# ### Machine Learning Prediction System

# Version : 1.0

# Developer : Rasulbek

# """)

# demo.launch()




# def predict(name, age):

#     if age > 30:
#         return "Likely to Stay"
#     return "High Attrition Risk"

# with gr.Blocks(title="Employee Attrition Dashboard") as demo:

#     gr.Markdown("# 🤖 Employee Attrition Dashboard")

#     with gr.Tabs():

#         with gr.Tab("Prediction"):

#             with gr.Row():

#                 with gr.Column(scale=2):

#                     with gr.Group():

#                         name = gr.Textbox(label="Employee Name")

#                         age = gr.Number(label="Age")

#                         predict_btn = gr.Button(
#                             "Predict",
#                             variant="primary"
#                         )

#                 with gr.Column(scale=1):

#                     result = gr.Textbox(
#                         label="Prediction"
#                     )

#         with gr.Tab("Model Settings"):

#             with gr.Accordion(
#                 "Advanced Parameters",
#                 open=False
#             ):

#                 gr.Slider(
#                     0,
#                     1,
#                     value=0.5,
#                     label="Confidence Threshold"
#                 )

#                 gr.Checkbox(
#                     label="Enable GPU"
#                 )

#     predict_btn.click(
#         fn=predict,
#         inputs=[name, age],
#         outputs=result
#     )

# demo.launch()




# with gr.Blocks() as demo:

#     gr.Markdown("# Employee Attrition Dashboard")

#     with gr.Tabs():

#         with gr.Tab("Prediction"):

#             with gr.Row():

#                 with gr.Column(scale=2):

#                     with gr.Group():

#                         name=gr.Textbox(label="Name")

#                         age=gr.Number(label="Age")

#                         salary=gr.Number(label="Salary")

#                         button=gr.Button(

#                             "Predict",

#                             variant="primary"

#                         )

#                 with gr.Column():

#                     result=gr.Textbox(

#                         label="Prediction"

#                     )

#         with gr.Tab("Settings"):

#             with gr.Accordion(

#                 "Advanced Settings"

#             ):

#                 gr.Checkbox(

#                     label="Use GPU"

#                 )

#                 gr.Slider(

#                     0,

#                     1,

#                     label="Confidence"

#                 )

# demo.launch()

# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Tabs():

#         with gr.Tab("Machine Learning"):

#             with gr.Tabs():

#                 with gr.Tab("Regression"):

#                     gr.Markdown("Regression")

#                 with gr.Tab("Classification"):

#                     gr.Markdown("Classification")

# demo.launch()









# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Tabs():

#         with gr.Tab("Employee"):

#             gr.Textbox(label="Name")

#             gr.Number(label="Age")

#         with gr.Tab("Prediction"):

#             gr.Textbox(label="Result")

# demo.launch()



# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Tabs():

#         with gr.Tab("Home"):

#             gr.Textbox()

#         with gr.Tab("Charts"):

#             gr.Plot()

#         with gr.Tab("About"):

#             gr.Markdown("# About")

# demo.launch()





# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Tabs():

#         with gr.Tab("Dashboard"):

#             gr.Markdown("# Dashboard")

#         with gr.Tab("Prediction"):

#             gr.Markdown("# Prediction")

# demo.launch()



# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Accordion("YOLO Settings"):

#         gr.Slider(0,1,label="Confidence")

#         gr.Slider(0,1,label="IoU")

#         gr.Number(label="Image Size")

# demo.launch()




# with gr.Blocks() as demo:

#     with gr.Accordion(

#         "Hyper Parameters",

#         open=True

#     ):

#         gr.Number(label="Batch Size")

#         gr.Number(label="Epoch")

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Accordion("Advanced Settings"):

#         gr.Slider(0,100,label="Epoch")

#         gr.Slider(0,1,label="Learning Rate")

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Group():

#         gr.Textbox(label="Username")

#         gr.Textbox(label="Password", type="password")

#         gr.Button("Login")

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     gr.Markdown("# Employee Dashboard")

#     with gr.Group():

#         gr.Markdown("## Employee Information")

#         gr.Textbox(label="Name")

#         gr.Number(label="Age")

#         gr.Button("Predict")

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Group():

#         gr.Textbox(label="Name")

#         gr.Number(label="Age")

#         gr.Number(label="Salary")

# demo.launch()






# def predict(name, age, salary):

#     if age > 35:
#         return "Stay", "92%"

