import gradio as gr 
import librosa
import pandas as pd 
from PIL import Image






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

#     return "Leave", "78%"

# with gr.Blocks() as demo:

#     gr.Markdown("# Employee Attrition Dashboard")

#     with gr.Row():

#         with gr.Column(scale=2):

#             name = gr.Textbox(label="Name")

#             age = gr.Number(label="Age")

#             salary = gr.Number(label="Salary")

#             button = gr.Button(
#                 "Predict",
#                 variant="primary"
#             )

#         with gr.Column():

#             status = gr.Textbox(label="Prediction")

#             probability = gr.Textbox(label="Probability")

#     button.click(
#         fn=predict,
#         inputs=[name, age, salary],
#         outputs=[status, probability]
#     )

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     gr.Markdown("# Employee Dashboard")

#     with gr.Row():

#         with gr.Column(scale=2):

#             name = gr.Textbox(label="Name")

#             age = gr.Number(label="Age")

#             salary = gr.Number(label="Salary")

#             exp = gr.Slider(0,30,label="Experience")

#             btn = gr.Button("Predict",variant="primary")

#         with gr.Column(scale=1):

#             result = gr.Textbox(label="Prediction")

# demo.launch()



# with gr.Blocks() as demo:

#     with gr.Row():

#         gr.Textbox()

#         gr.Number()

#         gr.Slider(0,100)

# demo.launch()



# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Row(equal_height=True):

#         with gr.Column():

#             gr.Textbox(lines=8)

#         with gr.Column():

#             gr.Image()

# demo.launch()








# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Row():

#         with gr.Row():

#             gr.Textbox(scale=3)

#             gr.Button(scale=1)

# demo.launch()





# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Row():

#         with gr.Column(scale=2):

#             gr.Textbox(label="Large")

#         with gr.Column(scale=1):

#             gr.Textbox(label="Small")






# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Row():

#         with gr.Column():

#             gr.Textbox(label="Name")

#             gr.Number(label="Age")

#             gr.Button("Predict")

#         with gr.Column():

#             gr.Textbox(label="Prediction")

# demo.launch()

# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Column():

#         gr.Image()

#         gr.Textbox()

#         gr.Button("Upload")

# demo.launch()




# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Column():

#         gr.Textbox()

#         gr.Number()

#         gr.Button("Predict")

# demo.launch()



# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Row():

#         gr.Textbox()

#         gr.Number()

#         gr.Button("Predict")

# demo.launch()



# import gradio as gr

# with gr.Blocks() as demo:

#     with gr.Row():

#         gr.Button("Train")

#         gr.Button("Predict")

#         gr.Button("Reset")

# demo.launch()




# import gradio as gr

# with gr.Blocks() as demo:

#     gr.Markdown("""

# # Employee Attrition Dashboard

# Predict whether an employee is likely to leave the company.

# """)

#     age = gr.Number(label="Age")

#     salary = gr.Number(label="Salary")

#     predict = gr.Button(

#         "Predict",

#         variant="primary"

#     )

#     result = gr.Textbox(

#         label="Prediction"

#     )

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     gr.Button("Predict",variant="primary")

#     gr.Button("Reset",variant="secondary")

#     gr.Button("Delete",variant="stop")

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     gr.Button(

#         value="Predict",

#         variant="secondary"

#     )

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     gr.Button("Predict")

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     gr.Button("Train Model")

# demo.launch()


# with gr.Blocks() as demo:

#     gr.HTML("""

# <center>

# <h1>

# AI Dashboard

# </h1>

# </center>

# """)

# demo.launch()



# with gr.Blocks() as demo:

#     gr.HTML("""

# <h2 style="color:blue;">

# Machine Learning

# </h2>

# """)

# demo.launch()


# import gradio as gr

# with gr.Blocks() as demo:

#     gr.HTML("""

# <h1>Employee Dashboard</h1>

# """)

# demo.launch()



# with gr.Blocks() as demo:

#     gr.Markdown("""

# # AI Dashboard

# ---

# Upload data and predict.

# ---


# """)

# demo.launch()



# with gr.Blocks() as demo:

#     gr.Markdown("""

# # Employee Attrition

# Predict employee resignation.

# Model : XGBoost

# Accuracy : 94%

# """)

# demo.launch()




# with gr.Blocks() as demo:

#     gr.Markdown("# Employee Attrition Prediction")

# demo.launch()



# import gradio as gr

# with gr.Blocks() as demo:

#     gr.Textbox(label="Name")

#     gr.Number(label="Age")

#     gr.Button("Predict")

# demo.launch()







# import gradio as gr

# with gr.Blocks() as demo:

#     gr.Markdown("# Hello Gradio Blocks")

# demo.launch()


# with gr.Blocks() as demo:

#     gr.Markdown("# Employee Prediction")

#     gr.Number(label="Age")

#     gr.Number(label="Salary")

# demo.launch()