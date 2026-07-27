import gradio as gr 





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







# def power(x):

#     return x**2


# demo = gr.Interface(

#     fn = power,

#     inputs=gr.Slider(

#         0,
#         100
#     ),

#     outputs= "number"
# )

# demo.launch()




# def annual(month):

#     return month*12


# demo = gr.Interface(

#     fn = annual,

#     inputs=gr.Number(

#         label="Monthly Salary"
#     ),

#     outputs=gr.Number(

#         label="Annual Salary"
#     )

# )


# demo.launch()




# def square(x):

#     return x*x

# demo = gr.Number(

#     label="Age"
# )

# demo.launch()


# demo = gr.Number(

#     value=25
# )

# demo.launch()


# demo = gr.Number(

#     precision=2
# )

# demo.launch()


# demo = gr.Number(

#     interactive=True
# )


# demo.launch()


# demo = gr.Number(

#     interactive=False,
#     value=100
# )

# demo.launch()


# def word(text):

#     return len(text.split())

# demo = gr.Interface(

#     fn=word,

#     inputs="text",

#     outputs="number"
# )

# demo.launch()



# def length(text):

#     return len(text)

# demo = gr.Interface(
#     fn = length,
#     inputs=gr.Textbox(),
#     outputs="number"
# )

# demo.launch()








# gr.Textbox(
#     type="password"
# )



# gr.Textbox(
#     interactive=True
# )



# gr.Textbox(
#     interactive=False,
#     value="Prediction Result"
# )


# gr.Textbox(
#     scale=2
# )



# gr.Textbox(
#     container=True
# )



# gr.Textbox(
#     info="Enter Your Email"
# )




# def reverse(text):

#     return text[::-1]


# demo = gr.Interface(

#     fn=reverse,

#     inputs=gr.Textbox(

#         lines=3,
#         max_lines=10
#     ),

#     outputs="text"
# )


# demo.launch()










# def reverse(text):

#     return text[::-1]


# demo = gr.Interface(

#     fn=reverse,

#     inputs=gr.Textbox(

#         lines=5
#     ),

#     outputs="text"
# )


# demo.launch()









# def hello(name):

#     return name


# demo = gr.Interface(

#     fn=hello,

#     inputs=gr.Textbox(

#         value="Rasulbek"
#     ),

#     outputs= "text"
# )


# demo.launch()










# def upper(text):

#     return text.upper()


# demo = gr.Interface(

#     fn=upper,

#     inputs=gr.Textbox(

#         placeholder="Enter Text.... "
#     ),

#     outputs="text"
# )


# demo.launch()




# def hello(name):
#     return f"Hello {name}"


# demo = gr.Interface(

#     fn=hello,

#     inputs=gr.Textbox(
#             label="Your Name"
#     ),

#     outputs=gr.Textbox(

#         label="Greeting"

#     )
# )


# demo.launch()







# def echo(text):
#     return text 

# demo = gr.Interface(
#     fn=echo,
#     inputs=gr.Textbox(),
#     outputs=gr.Textbox()
# )

# demo.launch()






# def greet(name):
#     return f"Welcome {name}"


# demo = gr.Interface(
#     fn=greet,
#     inputs=gr.Textbox(
#         "Your Name"
#     ),

#     outputs=gr.Textbox(
#         label="Result"
#     )



# )

# demo.launch()












# def square(x):

#     return x*x

# demo = gr.Interface(
#     fn=square,
#     inputs=gr.Number(
#         label="Enter Number"
#     ),

#     outputs=gr.Number(
#         label="Square"
#     )
    
# )

# demo.launch()












# def statistics(x):
#     return (
#         x,
#         x+10,
#         x*2,
#         x/2
#     )

# demo = gr.Interface(
#     fn = statistics,

#     inputs= "number",

#     outputs=[
#         "number",
#         "number",
#         "number",
#         "number"

#     ]
# )


# demo.launch()


















# def calculate(x):
#     return (
#         x,
#         x**2,
#         x**3,
#         x**4
#     )

# demo = gr.Interface(
#     fn = calculate,

#     inputs= "number",

#     outputs=[
#         "number",
#         "number",
#         "number",
#         "number"

#     ]
# )


# demo.launch()










# outputs = "text"


# outputs = "number"



# outputs = "json"



# outputs = "image"



# outputs = "gallery"



# outputs = "dataframe"



# outputs = "plot"













# def power(x):
#     return x**2

# demo = gr.Interface(
#     fn= power,
#     inputs=gr.Slider(
#         minimum=0,
#         maximum=100,
#         step=1,
#         value=25
#     ),
#     outputs="number"
# )


# demo.launch()



# def choose(value):
#     return value

# demo = gr.Interface(
#     fn= choose,
#     inputs=gr.Radio(
#         [
#             "Male",
#             "Female"            
#         ]
#     ),
#     outputs="text"
# )


# demo.launch()




# def select(lang):
#     return lang

# demo = gr.Interface(
#     fn= select,
#     inputs=gr.Dropdown(
#         [
#             "Python",
#             "Java",
#             "C++"
#         ]
#     ),
#     outputs="text"
# )


# demo.launch()


    






# def hello(name):
#     return name


# demo = gr.Interface(
#     fn =hello,
#     inputs="text",
#     outputs="text",
# )

# demo.launch()




# demo = gr.Interface(
#     fn =hello,
#     inputs="number",
#     outputs="number",
# )









# def add(a,b):
#     return a+b


# demo = gr.Interface(
#     fn=add,
#     inputs=[
#         "number",
#         "number"

#     ],

#     outputs="number"
# )

# demo.launch()














# def bmi(weight, height):
#     return weight/(height**2)


# demo = gr.Interface(
#     fn=bmi,
#     inputs=[
#         "number",
#         "number"

#     ],

#     outputs="number"
# )

# demo.launch()





# def hello(name):
#     return f"Hello {name}"

# demo = gr.Interface(
#     fn = hello,
#     inputs= "text",
#     outputs="text"
# )

# demo.launch()









# def cube(x):
#     return x**3


# demo = gr.Interface(
#     fn = cube,
#     inputs= "number",
#     outputs="number"
# )

# demo.launch()









# def square(x):
#     return x**2


# demo = gr.Interface(
#     fn = square,
#     inputs= "number",
#     outputs="number"
# )

# demo.launch()









# def count(text):
#     return len(text)

# demo = gr.Interface(
#     fn = count,
#     inputs= "text",
#     outputs="number"
# )

# demo.launch()










# def reverse(text):
#     return text[::-1]

# demo = gr.Interface(
#     fn = reverse,
#     inputs = "text",
#     outputs = "text"
# )

# demo.launch()












# def lower(text):
#     return text.lower()

# demo = gr.Interface(
#     fn = lower,
#     inputs="text",
#     outputs="text"
# )

# demo.launch()






# def upper(text):
#     return text.upper()

# demo = gr.Interface(
#     fn = upper,
#     inputs="text",
#     outputs="text"
# )

# demo.launch()






# def greet(name):
#     return "Welcome"  + name 

# app = gr.Interface(
#     fn=greet,
#     inputs="text",
#     outputs="text"
# )

# app.launch()



#
# 
#  def greet(name):
#     return f"Hello {name}"

# demo = gr.Interface(
#     fn=greet,
#     inputs="text",
#     outputs="text"
# )

# demo.launch()