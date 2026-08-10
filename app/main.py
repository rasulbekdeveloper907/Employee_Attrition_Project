import joblib
import pandas as pd
import gradio as gr

from pathlib import Path



MODEL_PATH = Path("C:\Users\Rasulbekk\Desktop\Employee_Attrition_Project\Notebook\Models\xgboost_pipeline.pkl")

pipeline = joblib.load(MODEL_PATH)


CSS = """

.gradio-container{

    max-width:1400px !important;

    margin:auto;

}

.main-title{

    font-size:38px;

    font-weight:bold;

    text-align:center;

    color:#2563eb;

    margin-bottom:10px;

}

.subtitle{

    text-align:center;

    color:gray;

    margin-bottom:25px;

}

.result-card{

    border-radius:15px;

    padding:18px;

    background:#f4f4f4;

}

.footer{

    text-align:center;

    color:gray;

    margin-top:20px;

}

"""


def predict_employee(

    Age,
    BusinessTravel,
    DailyRate,
    Department,
    DistanceFromHome,
    Education,
    EducationField,
    EmployeeNumber,
    EnvironmentSatisfaction,
    Gender,
    HourlyRate,
    JobInvolvement,
    JobLevel,
    JobRole,
    JobSatisfaction,
    MaritalStatus,
    MonthlyIncome,
    MonthlyRate,
    NumCompaniesWorked,
    OverTime,
    PercentSalaryHike,
    PerformanceRating,
    RelationshipSatisfaction,
    StockOptionLevel,
    TotalWorkingYears,
    TrainingTimesLastYear,
    WorkLifeBalance,
    YearsAtCompany,
    YearsInCurrentRole,
    YearsSinceLastPromotion,
    YearsWithCurrManager

):



    Income_Per_Age = MonthlyIncome / Age

    Work_Ratio = YearsAtCompany / (TotalWorkingYears + 1)

    Loyalty_Ratio = YearsWithCurrManager / (YearsAtCompany + 1)

    OverTime_Binary = 1 if OverTime == "Yes" else 0

  
    df = pd.DataFrame({

        "Age":[Age],

        "BusinessTravel":[BusinessTravel],

        "DailyRate":[DailyRate],

        "Department":[Department],

        "DistanceFromHome":[DistanceFromHome],

        "Education":[Education],

        "EducationField":[EducationField],

        "EmployeeNumber":[EmployeeNumber],

        "EnvironmentSatisfaction":[EnvironmentSatisfaction],

        "Gender":[Gender],

        "HourlyRate":[HourlyRate],

        "JobInvolvement":[JobInvolvement],

        "JobLevel":[JobLevel],

        "JobRole":[JobRole],

        "JobSatisfaction":[JobSatisfaction],

        "MaritalStatus":[MaritalStatus],

        "MonthlyIncome":[MonthlyIncome],

        "MonthlyRate":[MonthlyRate],

        "NumCompaniesWorked":[NumCompaniesWorked],

        "OverTime":[OverTime],

        "PercentSalaryHike":[PercentSalaryHike],

        "PerformanceRating":[PerformanceRating],

        "RelationshipSatisfaction":[RelationshipSatisfaction],

        "StockOptionLevel":[StockOptionLevel],

        "TotalWorkingYears":[TotalWorkingYears],

        "TrainingTimesLastYear":[TrainingTimesLastYear],

        "WorkLifeBalance":[WorkLifeBalance],

        "YearsAtCompany":[YearsAtCompany],

        "YearsInCurrentRole":[YearsInCurrentRole],

        "YearsSinceLastPromotion":[YearsSinceLastPromotion],

        "YearsWithCurrManager":[YearsWithCurrManager],

        "Income_Per_Age":[Income_Per_Age],

        "Work_Ratio":[Work_Ratio],

        "Loyalty_Ratio":[Loyalty_Ratio],

        "OverTime_Binary":[OverTime_Binary]

    })

    prediction = pipeline.predict(df)[0]

    probability = pipeline.predict_proba(df)[0]

    stay = probability[0] * 100

    leave = probability[1] * 100

    if prediction == 0:

        result = "🟢 Employee Will Stay"

    else:

        result = "🔴 Employee Will Leave"

    return (

        result,

        round(stay,2),

        round(leave,2)

    )


with gr.Blocks(
    title="Employee Attrition AI",
    css=CSS,
    theme=gr.themes.Soft()
) as demo:



    gr.Markdown(
        """
        <div class="main-title">
            Employee Attrition Prediction AI
        </div>

        <div class="subtitle">
            XGBoost-powered Machine Learning System
            for Employee Attrition Prediction
        </div>
        """
    )



    gr.Markdown(
        """
        ## 👤 Employee Information

        Enter employee information below and click
        **Predict Attrition** to generate a prediction.
        """
    )



    with gr.Accordion(
        "👤 Basic Information",
        open=True
    ):

        with gr.Row():

            Age = gr.Number(
                label="Age",
                value=35,
                minimum=18,
                maximum=70,
                step=1
            )

            Gender = gr.Dropdown(
                choices=[
                    "Male",
                    "Female"
                ],
                value="Male",
                label="Gender"
            )

            MaritalStatus = gr.Dropdown(
                choices=[
                    "Single",
                    "Married",
                    "Divorced"
                ],
                value="Single",
                label="Marital Status"
            )

            Education = gr.Dropdown(
                choices=[
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                value=3,
                label="Education Level"
            )


    with gr.Accordion(
        "💼 Job Information",
        open=True
    ):

        with gr.Row():

            Department = gr.Dropdown(
                choices=[
                    "Sales",
                    "Research & Development",
                    "Human Resources"
                ],
                value="Sales",
                label="Department"
            )

            JobRole = gr.Dropdown(
                choices=[
                    "Sales Executive",
                    "Research Scientist",
                    "Laboratory Technician",
                    "Manufacturing Director",
                    "Healthcare Representative",
                    "Manager",
                    "Sales Representative",
                    "Research Director",
                    "Human Resources"
                ],
                value="Sales Executive",
                label="Job Role"
            )

            JobLevel = gr.Dropdown(
                choices=[
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                value=2,
                label="Job Level"
            )

        with gr.Row():

            JobInvolvement = gr.Dropdown(
                choices=[
                    1,
                    2,
                    3,
                    4
                ],
                value=3,
                label="Job Involvement"
            )

            JobSatisfaction = gr.Dropdown(
                choices=[
                    1,
                    2,
                    3,
                    4
                ],
                value=3,
                label="Job Satisfaction"
            )

            EnvironmentSatisfaction = gr.Dropdown(
                choices=[
                    1,
                    2,
                    3,
                    4
                ],
                value=3,
                label="Environment Satisfaction"
            )

            RelationshipSatisfaction = gr.Dropdown(
                choices=[
                    1,
                    2,
                    3,
                    4
                ],
                value=3,
                label="Relationship Satisfaction"
            )

 

    with gr.Accordion(
        "🏢 Business & Career Information",
        open=False
    ):

        with gr.Row():

            BusinessTravel = gr.Dropdown(
                choices=[
                    "Travel_Rarely",
                    "Travel_Frequently",
                    "Non-Travel"
                ],
                value="Travel_Rarely",
                label="Business Travel"
            )

            EducationField = gr.Dropdown(
                choices=[
                    "Life Sciences",
                    "Medical",
                    "Marketing",
                    "Technical Degree",
                    "Human Resources",
                    "Other"
                ],
                value="Life Sciences",
                label="Education Field"
            )

            OverTime = gr.Dropdown(
                choices=[
                    "Yes",
                    "No"
                ],
                value="No",
                label="Overtime"
            )

        with gr.Row():

            StockOptionLevel = gr.Dropdown(
                choices=[
                    0,
                    1,
                    2,
                    3
                ],
                value=1,
                label="Stock Option Level"
            )

            PerformanceRating = gr.Dropdown(
                choices=[
                    1,
                    2,
                    3,
                    4
                ],
                value=3,
                label="Performance Rating"
            )

            WorkLifeBalance = gr.Dropdown(
                choices=[
                    1,
                    2,
                    3,
                    4
                ],
                value=3,
                label="Work-Life Balance"
            )


    with gr.Accordion(
        "💰 Financial Information",
        open=False
    ):

        with gr.Row():

            MonthlyIncome = gr.Number(
                label="Monthly Income",
                value=5000,
                minimum=100,
                step=100
            )

            MonthlyRate = gr.Number(
                label="Monthly Rate",
                value=14000,
                minimum=0,
                step=100
            )

            DailyRate = gr.Number(
                label="Daily Rate",
                value=800,
                minimum=0,
                step=10
            )

            HourlyRate = gr.Number(
                label="Hourly Rate",
                value=60,
                minimum=0,
                step=1
            )

        with gr.Row():

            PercentSalaryHike = gr.Number(
                label="Percent Salary Hike",
                value=15,
                minimum=0,
                maximum=100,
                step=1
            )


    with gr.Accordion(
        "📊 Work History",
        open=False
    ):

        with gr.Row():

            DistanceFromHome = gr.Number(
                label="Distance From Home",
                value=5,
                minimum=0,
                step=1
            )

            TotalWorkingYears = gr.Number(
                label="Total Working Years",
                value=10,
                minimum=0,
                step=1
            )

            NumCompaniesWorked = gr.Number(
                label="Number of Companies Worked",
                value=2,
                minimum=0,
                step=1
            )

            TrainingTimesLastYear = gr.Number(
                label="Training Times Last Year",
                value=2,
                minimum=0,
                step=1
            )

        with gr.Row():

            YearsAtCompany = gr.Number(
                label="Years At Company",
                value=5,
                minimum=0,
                step=1
            )

            YearsInCurrentRole = gr.Number(
                label="Years In Current Role",
                value=3,
                minimum=0,
                step=1
            )

            YearsSinceLastPromotion = gr.Number(
                label="Years Since Last Promotion",
                value=1,
                minimum=0,
                step=1
            )

            YearsWithCurrManager = gr.Number(
                label="Years With Current Manager",
                value=3,
                minimum=0,
                step=1
            )

  

    with gr.Accordion(
        "⚙️ System Information",
        open=False
    ):

        with gr.Row():

            EmployeeNumber = gr.Number(
                label="Employee Number",
                value=1001,
                minimum=1,
                step=1
            )




gr.Markdown(
    """
    ## 🤖 AI Prediction

    The trained XGBoost model analyzes the employee profile
    and estimates the probability of employee attrition.
    """
)

with gr.Row():

 

    with gr.Column(scale=1):

        predict_btn = gr.Button(
            "🚀 Predict Attrition",
            variant="primary",
            size="lg"
        )

        clear_btn = gr.Button(
            "🗑️ Clear Form",
            variant="secondary"
        )

        example_btn = gr.Button(
            "📋 Load Example",
            variant="secondary"
        )


 
    with gr.Column(scale=2):

        prediction_output = gr.Markdown(
            """
            ### Prediction

            Enter employee information and click
            **Predict Attrition**.
            """,
            elem_classes=["result-card"]
        )




with gr.Row():

    stay_probability = gr.Number(
        label="🟢 Stay Probability (%)",
        value=0,
        interactive=False
    )

    leave_probability = gr.Number(
        label="🔴 Leave Probability (%)",
        value=0,
        interactive=False
    )



probability_output = gr.Markdown(
    """
    ### 📊 Prediction Probability

    No prediction available yet.
    """,
    elem_classes=["result-card"]
)




inputs = [

    Age,
    BusinessTravel,
    DailyRate,
    Department,
    DistanceFromHome,
    Education,
    EducationField,
    EmployeeNumber,
    EnvironmentSatisfaction,
    Gender,
    HourlyRate,
    JobInvolvement,
    JobLevel,
    JobRole,
    JobSatisfaction,
    MaritalStatus,
    MonthlyIncome,
    MonthlyRate,
    NumCompaniesWorked,
    OverTime,
    PercentSalaryHike,
    PerformanceRating,
    RelationshipSatisfaction,
    StockOptionLevel,
    TotalWorkingYears,
    TrainingTimesLastYear,
    WorkLifeBalance,
    YearsAtCompany,
    YearsInCurrentRole,
    YearsSinceLastPromotion,
    YearsWithCurrManager

]


def prediction_result(
    result,
    stay,
    leave
):

    if "Stay" in result:

        status = "🟢 **Employee is likely to STAY**"

    else:

        status = "🔴 **Employee is likely to LEAVE**"


    probability_html = f"""
    ### 📊 Prediction Probability

    **Stay Probability**

    `{stay:.2f}%`

    **Leave Probability**

    `{leave:.2f}%`

    ---

    {status}
    """

    return probability_html


predict_btn.click(

    fn=prediction_result,

    inputs=[
        prediction_output,
        stay_probability,
        leave_probability
    ],

    outputs=probability_output

)



def clear_form():

    return [

        None,   # Age
        None,   # BusinessTravel
        None,   # DailyRate
        None,   # Department
        None,   # DistanceFromHome
        None,   # Education
        None,   # EducationField
        None,   # EmployeeNumber
        None,   # EnvironmentSatisfaction
        None,   # Gender
        None,   # HourlyRate
        None,   # JobInvolvement
        None,   # JobLevel
        None,   # JobRole
        None,   # JobSatisfaction
        None,   # MaritalStatus
        None,   # MonthlyIncome
        None,   # MonthlyRate
        None,   # NumCompaniesWorked
        None,   # OverTime
        None,   # PercentSalaryHike
        None,   # PerformanceRating
        None,   # RelationshipSatisfaction
        None,   # StockOptionLevel
        None,   # TotalWorkingYears
        None,   # TrainingTimesLastYear
        None,   # WorkLifeBalance
        None,   # YearsAtCompany
        None,   # YearsInCurrentRole
        None,   # YearsSinceLastPromotion
        None,   # YearsWithCurrManager

    ]


clear_btn.click(

    fn=clear_form,

    inputs=[],

    outputs=inputs

)



example_data = [

    35,                     # Age

    "Travel_Rarely",        # BusinessTravel

    800,                    # DailyRate

    "Sales",                # Department

    5,                      # DistanceFromHome

    3,                      # Education

    "Life Sciences",        # EducationField

    1001,                   # EmployeeNumber

    3,                      # EnvironmentSatisfaction

    "Male",                 # Gender

    60,                     # HourlyRate

    3,                      # JobInvolvement

    2,                      # JobLevel

    "Sales Executive",      # JobRole

    3,                      # JobSatisfaction

    "Single",               # MaritalStatus

    5000,                   # MonthlyIncome

    14000,                  # MonthlyRate

    2,                      # NumCompaniesWorked

    "No",                   # OverTime

    15,                     # PercentSalaryHike

    3,                      # PerformanceRating

    3,                      # RelationshipSatisfaction

    1,                      # StockOptionLevel

    10,                     # TotalWorkingYears

    2,                      # TrainingTimesLastYear

    3,                      # WorkLifeBalance

    5,                      # YearsAtCompany

    3,                      # YearsInCurrentRole

    1,                      # YearsSinceLastPromotion

    3                       # YearsWithCurrManager

]


example_btn.click(

    fn=lambda: example_data,

    inputs=[],

    outputs=inputs

)



gr.Markdown("## 📊 Prediction Analytics")

with gr.Row():

    with gr.Column():

        gr.Markdown(
            """
            <div class="result-card">

            ### 🧠 Model Information

            **Algorithm:** XGBoost Classifier

            **Framework:** Scikit-Learn Pipeline

            **Target:** Employee Attrition

            **Version:** 1.0.0

            **Deployment:** Gradio

            </div>
            """
        )

    with gr.Column():

        gr.Markdown(
            """
            <div class="result-card">

            ### 📈 Model Performance

            **Accuracy:** 83.67%

            **Precision:** 86%

            **Recall:** 97%

            **F1 Score:** 91%

            **Status:** Production Ready

            </div>
            """
        )



gr.Markdown("## 📋 About This Project")

gr.Markdown(
    """
    This dashboard predicts whether an employee is likely to **Stay**
    or **Leave** the company using a machine learning model trained on
    the IBM Employee Attrition dataset.

    ### Feature Engineering

    The application automatically creates:

    - Income Per Age
    - Work Ratio
    - Loyalty Ratio
    - Overtime Binary Feature

    ### Technologies Used

    - Python
    - XGBoost
    - Scikit-Learn Pipeline
    - Pandas
    - Gradio
    """
)




gr.Markdown("## 🎯 Input Feature Summary")

with gr.Row():

    gr.Markdown(
        """
        ### 👤 Personal

        - Age
        - Gender
        - Marital Status
        - Education
        - Education Field
        """
    )

    gr.Markdown(
        """
        ### 💼 Job

        - Department
        - Job Role
        - Job Level
        - Business Travel
        - Overtime
        """
    )

    gr.Markdown(
        """
        ### 💰 Financial

        - Monthly Income
        - Daily Rate
        - Hourly Rate
        - Salary Hike
        """
    )




gr.Markdown("## 👨‍💻 Developer")

gr.Markdown(
    """
    <div class="result-card">

    **Rasulbek Ruzmetov**

    Machine Learning Engineer

    Specialization:

    - Machine Learning
    - Deep Learning
    - Computer Vision
    - MLOps
    - FastAPI & Gradio

    </div>
    """
)




gr.Markdown(
    """
    <div class="footer">

    Employee Attrition Prediction Dashboard

    Built with ❤️ using Gradio + XGBoost

    © 2026 Rasulbek Ruzmetov

    </div>
    """
)



if __name__ == "__main__":

    demo.launch(

        server_name="127.0.0.1",

        server_port=7860,

        share=False,

        favicon_path=None,

        show_error=True

    )



