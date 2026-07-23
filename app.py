import streamlit as st 
import pandas as pd 
import datetime
from PIL import Image


import streamlit as st
import pandas as pd

st.set_page_config(

    page_title="ML Dashboard",

    layout="wide"

)

st.sidebar.title("Settings")

algorithm=st.sidebar.selectbox(

    "Model",

    [

        "Random Forest",

        "XGBoost",

        "CatBoost"

    ]

)

st.title("Machine Learning Dashboard")

col1,col2=st.columns(2)

df=pd.DataFrame({

    "A":[5,10,15],

    "B":[8,12,20]

})

with col1:

    st.subheader("Dataset")

    st.dataframe(df)

with col2:

    st.subheader("Visualization")

    st.bar_chart(df)

st.divider()

if st.button("Predict"):

    st.success(f"{algorithm} Prediction Completed")











st.sidebar.title("Menu")


st.sidebar.header("Settings")




st.sidebar.write("Welcome")

algorithm = st.sidebar.selectbox(

    "Algorithm",

    [

        "Random Forest",

        "XGBoost",

        "CatBoost"

    ]

)

st.write(algorithm)


epochs = st.sidebar.slider(

    "Epochs",

    1,

    100,

    20

)

st.write(epochs)



lr = st.sidebar.number_input(

    "Learning Rate",

    value=0.001

)

st.write(lr)

gpu = st.sidebar.checkbox(

    "Use GPU"

)

st.write(gpu)



st.sidebar.button("Start")



st.sidebar.success("Ready")




st.sidebar.info("Version 1.0")


col1,col2=st.columns(2)




col1,col2=st.columns(2)

with col1:

    st.write("Left")

with col2:

    st.write("Right")




col1,col2,col3=st.columns(3)

with col1:

    st.metric("Accuracy","97%")

with col2:

    st.metric("Loss","0.05")

with col3:

    st.metric("Epoch","25")


col1,col2=st.columns([3,1])

with col1:

    st.write("Main Content")

with col2:

    st.button("Predict")


import pandas as pd

df=pd.DataFrame({

    "A":[1,2,3],

    "B":[4,5,6]

})

import pandas as pd

df=pd.DataFrame({

    "A":[1,2,3],

    "B":[4,5,6]

})

col1,col2=st.columns(2)

with col1:

    st.dataframe(df)

with col2:

    st.bar_chart(df)


# st.title("Registration Form")

# name = st.text_input("Name")
# age = st.number_input("Age", 1, 100)

# gender = st.radio(

#     "Gender",

#     ["Male", "Female"]
# )

# skills = st.multiselect(

#     "Skills",
#     ["Python", "SQL", "Docker", "FastAPI", "Tensorflow"]
# )

# birthday = st.date_input("Birthday")
# resume = st.file_uploader(
#     "Resume",
#     type=["pdf"]
# )
















# if st.button("Submit"):
#     st.success("Registration Completed")

#     st.write("Name: ", name)

#     st.write("Age: ", age)

#     st.write("Gender: ", gender)

#     st.write("Skills: ", skills)

#     st.write("Birthday: ", birthday)










# picture = st.camera_input(

#     "Camera"

# )

# if picture:
#     st.image(picture)

















# uploaded_files = st.file_uploader(

#     "IMAGE",
#     type=["png", "jpg"]

# )

# if uploaded_files:
#     image = Image.open(uploaded_files)
#     st.image(image)



# uploaded_files = st.file_uploader(
#     "CSV",
#     type="csv"
# )

# if uploaded_files:
#     df = pd.read_csv(uploaded_files)
#     st.dataframe(df)



# uploaded_files = st.file_uploader(

#     "Upload Excel",

#     type=["xlsx"]
# )


# uploaded_files = st.file_uploader(

#     "Upload IMAGE",

#     type=["jpg", "png", "jpeg", "dvv"]
# )


# uploaded_files = st.file_uploader(

#     "Upload CSV"
# )

# st.write(uploaded_files)





# text_color = st.color_picker(

#     "Text Color",

#     "#B02121"

# )


# bacground = st.color_picker(
#     "Bacground"
# )



# color = st.color_picker("Choose Color")

# st.write(color)





# time = st.time_input(
#     "Curent Time",
#     datetime.datetime.now().time()
# )




# time = st.time_input("Meeting Time")

# st.write()



# date = st.date_input(
#     "Select Date"
# )





# today = st.date_input(

#     "Today",

#     datetime.date.today()
# )



# date = st.date_input("Birthday")

# st.write(date)









# df = pd.DataFrame({
#     "A":[1,2,3], 
#     "B":[4,5,6]
# })


# csv = df.to_csv(index=False)

# st.download_button(
#     "Download.csv",
#     csv,
#     file_name="data.csv",
#     mime="text/.csv"
# )


# text = "Hello Streamlit"

# st.download_button(
#     "Download",
#     text,
#     file_name="hello.txt"
# )



#  
# st.button(
#     "Save",
#     type="primary"
# )



# st.button(
#     "Cancel",
#     type="secondary"
# )

# st.button(
#     "uchunchi",
#     type="tertiary"
# )

# if st.button("Start Training"):
#     st.success("Training Started")

# if st.button("Start Training"):
#     st.line_chart([5, 10, 15, 20])




# skills = st.multiselect(
#     "Skills",
#     [
#         "Python",
#         "SQL",
#         "Docker",
#         "FastApi",
#         "PyTorch"
#     ]
# )

# st.write(skills)





# country = st.selectbox(
#     "Country",
#     [
#         "Uzb",
#         "Kor",
#         "Japan"
#     ]
# )




# gender = st.radio(
#     "Gender",
#     [
#         "Male",
#         "Female"
#     ]
# )

# st.write(gender)











# dark = st.toggle("Dark Mode")

# st.write(dark)

# agree = st.checkbox(
#     "I Agree"
# )

# st.write(agree)


# volume = st.slider(
#     "Volume",
#     0,
#     100,
#     50
# )

# st.write(volume)



# age = st.slider(
#     "Age",
#     1,
#     100
# )

# st.write(age)

# height = st.number_input(
#     "Height",
#     min_value=100,
#     max_value=500
# )

# st.write(height)


# age = st.number_input(
#     "Age"
# )

# st.write(age)

# about = st.text_area(
#     "About Yourself"
# )

# st.write(about)

# name = st.text_input(
#     "Username",
#     label_visibility = "Collapsed"
#     )
# st.write(name)


# st.balloons()
# st.snow()

# df = pd.DataFrame({
#     "Name": ["Ali", "Vali"],
#     "Age" : [20, 18]
# })

# st.write(df)


# st.markdown('## Subtitle')
# st.markdown('### Small')
# st.markdown('# Hello')
# st.markdown("**Bold**")
# st.markdown("*Italic*")
# st.markdown("---")

# st.caption("Created by Rasulbek")

# st.write("Python")
# st.write(100)
# st.write([1, 2, 3, 4, 5])
# st.write({"A":1, "B":2})



# st.set_page_config(
#     page_title="Employee Dashboard",
#     page_icon="👉",
#     layout="wide"
# )

# st.title("Employee Attrition Dashboard")

# uploaded_file = st.file_uploader(
#     "CSV faylni yuklang",
#     type=["csv"]
# )

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)

#     st.subheader("Malumotlar")
#     st.dataframe(df)

#     st.metric(
#         label="Rows",
#         value=len(df)
#     )

#     st.metric(
#         label="Columns",
#         value=len(df.columns)        
#     )





#mini loyiha 

# st.title("My first App")

# name = st.text_input("Enter name")

# if st.button("Submit"):
#     st.success(f"Welcome {name}")


# st.title("Machine Learning App")

# st.write("Welcome!")

# st.header("Prediction")

# st.subheader("House Price ")

# st.text("Python + Streamlit")

# st.markdown("""
# #Machine Learning
 
            
# ## Regression 

            
# ###CLassification



# **Bold**

# *Italic*


# - Apple
# - Banana
# - Orange                                                              
# # """)


# st.latex(r'''
# E=mc^2
# ''')


# code = '''
# for i in range(5):
#     print(i)

# '''

# st.code(code)

# st.metric("Accuracy", "97.3")

# st.success("Model Loaded")

# st.error("File not found")

# st.warning("GPU not available")

# st.info("Training...")

# st.balloons()

# st.snow()