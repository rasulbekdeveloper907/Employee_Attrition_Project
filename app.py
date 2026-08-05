import gradio as gr 
import librosa
import pandas as pd 
from PIL import Image
import time
import matplotlib.pyplot as plt




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


# import gradio as gr

# code="""

# def predict(x):

#     return model.predict(x)

# """

# gr.Interface(

#     lambda:code,

#     outputs=gr.Code()

# ).launch()

# def info():

#     return {

#         "Accuracy":0.96,

#         "Model":"XGBoost",

#         "Version":"1.0"

#     }

# gr.Interface(

#     info,

#     outputs=gr.JSON()

# ).launch()


# import pandas as pd

# df=pd.DataFrame({

#     "Prediction":[

#         "Stay",

#         "Leave"

#     ]

# })

# df.to_csv(

#     "prediction.csv",

#     index=False

# )


# import numpy as np
# import matplotlib.pyplot as plt
# import gradio as gr

# def hist():

#     fig=plt.figure()

#     plt.hist(

#         np.random.randn(1000)

#     )

#     return fig

# gr.Interface(

#     hist,

#     outputs=gr.Plot()

# ).launch()

# import matplotlib.pyplot as plt
# import gradio as gr

# def bar():

#     fig=plt.figure()

#     plt.bar(

#         ["A","B","C"],

#         [5,8,4]

#     )

#     return fig

# gr.Interface(

#     bar,

#     outputs=gr.Plot()

# ).launch()

# import matplotlib.pyplot as plt
# import gradio as gr

# def chart():

#     fig=plt.figure()

#     plt.plot(

#         [1,2,3,4],

#         [5,7,3,8]

#     )

#     return fig

# gr.Interface(

#     chart,

#     outputs=gr.Plot()

# ).launch()


# df = pd.DataFrame({

#     "Age":[23,35,40],

#     "Salary":[2500,7000,9000]

# })

# gr.Interface(

#     lambda:df,

#     outputs=gr.Dataframe()

# ).launch()



# import pandas as pd
# import gradio as gr

# df = pd.DataFrame({

#     "Age":[23,35,40],

#     "Salary":[2500,7000,9000]

# })

# gr.Interface(

#     lambda:df,

#     outputs=gr.Dataframe()

# ).launch()



# import pandas as pd
# import gradio as gr

# def stats(df):

#     return df.describe()

# gr.Interface(

#     stats,

#     gr.Dataframe(),

#     gr.Dataframe()

# ).launch()


# gr.Interface(

#     fn=predict,

#     inputs="number",

#     outputs="text",

#     examples=[

#         [20],

#         [35],

#         [50]

#     ],

#     cache_examples=True

# ).launch()



# import gradio as gr

# def employee(age,salary):

#     if salary>6000:

#         return "Senior Employee"

#     return "Junior Employee"

# gr.Interface(

#     employee,

#     [

#         gr.Number(),

#         gr.Number()

#     ],

#     "text",

#     examples=[

#         [24,3000],

#         [35,7000],

#         [42,12000]

#     ]

# ).launch()

# import gradio as gr

# def predict(age):

#     if age > 30:
#         return "Stay"

#     return "Leave"

# demo = gr.Interface(

#     fn=predict,

#     inputs=gr.Number(),

#     outputs="text",

#     examples=[

#         [22],

#         [35],

#         [48],

#         [27]

#     ]

# )

# demo.launch()










# def predict(age,progress=gr.Progress()):

#     for i in range(100):

#         progress(

#             i/100,

#             desc="Predicting..."

#         )

#         time.sleep(0.02)

#     if age>30:

#         return "Stay"

#     return "Leave"

# with gr.Blocks() as demo:

#     age=gr.Number()

#     result=gr.Textbox()

#     btn=gr.Button(

#         "Predict",

#         variant="primary"

#     )

#     btn.click(

#         predict,

#         age,

#         result

#     )

# demo.queue()

# demo.launch()


# def batch(numbers):

#     return [x*2 for x in numbers]

# gr.Interface(

#     batch,

#     inputs=gr.Dataframe(),

#     outputs=gr.Dataframe()

# ).launch()


# def bmi(weight,height):

#     return weight/(height**2)

# with gr.Blocks() as demo:

#     w=gr.Slider(

#         40,

#         120,

#         value=70

#     )

#     h=gr.Slider(

#         1.4,

#         2.2,

#         value=1.70

#     )

#     out=gr.Number()

#     w.change(

#         bmi,

#         [w,h],

#         out

#     )

#     h.change(

#         bmi,

#         [w,h],

#         out

#     )

# demo.launch()


# def streaming():

#     yield "Loading"

#     yield "Processing"

#     yield "Predicting"

#     yield "Finished"



# def stream():

#     text="Hello Gradio!"

#     output=""

#     for ch in text:

#         output+=ch

#         time.sleep(0.1)

#         yield output

# gr.Interface(

#     stream,

#     outputs="text"

# ).launch()


# import gradio as gr
# import time

# def loading(progress=gr.Progress()):

#     tasks=[

#         "Loading Model",

#         "Reading Data",

#         "Prediction",

#         "Saving"

#     ]

#     for task in tasks:

#         progress(

#             0,

#             desc=task

#         )

#         time.sleep(1)

#     return "Done"

# gr.Interface(

#     loading,

#     outputs="text"


# demo.launch()

# demo.queue(

#     max_size=30,

#     default_concurrency_limit=3

# )


# def train(progress=gr.Progress()):

#     for i in range(100):

#         progress(

#             i/100,

#             desc=f"Training {i}%"

#         )

#         time.sleep(0.03)

#     return "Training Finished"

# with gr.Blocks() as demo:

#     out=gr.Textbox()

#     btn=gr.Button("Train")

#     btn.click(

#         train,

#         outputs=out

#     )

# demo.launch()


# demo.queue(

#     max_size=30,

#     default_concurrency_limit=3

# )




# def slow_prediction(x):

#     time.sleep(5)

#     return x * 2

# with gr.Blocks() as demo:

#     number = gr.Number()

#     output = gr.Number()

#     button = gr.Button("Predict")

#     button.click(

#         slow_prediction,

#         number,

#         output

#     )

# demo.queue()

# demo.launch()

# def preprocess(age):

#     return age + 5

# def predict(age):

#     if age > 35:

#         return "Stay"

#     return "Leave"

# with gr.Blocks() as demo:

#     age = gr.Number()

#     result = gr.Textbox()

#     button = gr.Button(

#         "Predict",

#         variant="primary"

#     )

#     button.click(

#         preprocess,

#         age,

#         age

#     ).then(

#         predict,

#         age,

#         result

#     )

# demo.launch()


# def preprocess(x):

#     return x*2

# def predict(x):

#     return x+5

# def postprocess(x):

#     return f"Result : {x}"

# with gr.Blocks() as demo:

#     inp = gr.Number()

#     out = gr.Textbox()

#     btn = gr.Button("Predict")

#     btn.click(

#         preprocess,

#         inp,

#         inp

#     ).then(

#         predict,

#         inp,

#         inp

#     ).then(

#         postprocess,

#         inp,

#         out

#     )

# demo.launch()


# def first(x):

#     return x*2

# def second(y):

#     return y+10

# with gr.Blocks() as demo:

#     num = gr.Number()

#     out = gr.Number()

#     btn = gr.Button("Run")

#     event = btn.click(

#         first,

#         num,

#         out

#     )

#     event.then(

#         second,

#         out,

#         out

#     )

# demo.launch()




# def chat(message,history):

#     history.append(message)

#     return history,history

# with gr.Blocks() as demo:

#     state = gr.State([])

#     inp = gr.Textbox()

#     out = gr.JSON()

#     inp.submit(

#         chat,

#         [inp,state],

#         [out,state]

#     )

# demo.launch()



# def add(state):

#     state += 1

#     return state,state

# with gr.Blocks() as demo:

#     counter = gr.State(0)

#     value = gr.Number()

#     button = gr.Button("Increase")

#     button.click(

#         add,

#         counter,

#         [value,counter]

#     )

# demo.launch()

# def counter(x,state):

#     state += 1

#     return state,state

# with gr.Blocks() as demo:

#     state = gr.State(0)

#     out = gr.Number()

#     btn = gr.Button("Click")

#     btn.click(

#         counter,

#         [btn,state],

#         [out,state]

#     )

# demo.launch()


# def cleared():

#     return "Textbox Cleared"

# with gr.Blocks() as demo:

#     txt = gr.Textbox()

#     out = gr.Textbox()

#     txt.clear(

#         cleared,

#         outputs=out

#     )

# demo.launch()



# def image_loaded(img):

#     return img

# with gr.Blocks() as demo:

#     image = gr.Image()

#     output = gr.Image()

#     image.upload(

#         image_loaded,

#         image,

#         output

#     )

# demo.launch()


# def uploaded(file):

#     return "Upload Success"

# with gr.Blocks() as demo:

#     file = gr.File()

#     out = gr.Textbox()

#     file.upload(

#         uploaded,

#         file,

#         out

#     )

# demo.launch()

# import gradio as gr

# def tab(name):

#     return f"Current Tab : {name}"

# with gr.Blocks() as demo:

#     tabs = gr.Radio(

#         ["Home","Charts","Prediction"]

#     )

#     out = gr.Textbox()

#     tabs.select(

#         tab,

#         tabs,

#         out

#     )

# demo.launch()


# def language(lang):

#     return f"You selected : {lang}"

# with gr.Blocks() as demo:

#     radio = gr.Radio(

#         ["Python","Java","C++"]

#     )

#     out = gr.Textbox()

#     radio.select(

#         language,

#         radio,

#         out

#     )

# demo.launch()


# def predict(name, age):

#     if age >= 30:

#         return f"{name} : Stay"

#     return f"{name} : Leave"

# with gr.Blocks() as demo:

#     gr.Markdown("# Employee Prediction")

#     name = gr.Textbox(label="Name")

#     age = gr.Slider(18,60)

#     result = gr.Textbox()

#     button = gr.Button(

#         "Predict",

#         variant="primary"

#     )

#     button.click(

#         predict,

#         [name, age],

#         result

#     )

# demo.launch()



# import gradio as gr

# def login(user):

#     return f"Welcome {user}"

# with gr.Blocks() as demo:

#     username=gr.Textbox()

#     result=gr.Textbox()

#     username.submit(

#         login,

#         username,

#         result

#     )

# demo.launch()


# def hello(name):

#     return f"Hello {name}"

# with gr.Blocks() as demo:

#     txt=gr.Textbox()

#     out=gr.Textbox()

#     txt.submit(

#         hello,

#         txt,

#         out

#     )

# demo.launch()