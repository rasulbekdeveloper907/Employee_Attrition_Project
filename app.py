import streamlit as st 
import pandas as pd 














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