from pathlib import Path
import joblib
import pandas as pd
import gradio as gr


# ============================================================
# CONFIG
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = (
    BASE_DIR
    / "Notebook"
    / "Models"
    / "xgboost_pipeline.pkl"
)



# ============================================================
# LOAD MODEL
# ============================================================

try:
    pipeline = joblib.load(MODEL_PATH)
    MODEL_STATUS = "🟢 Model loaded successfully"
except Exception as e:
    pipeline = None
    MODEL_STATUS = f"🔴 Model loading error: {e}"


# ============================================================
# PIPELINE FEATURES
# ============================================================

PIPELINE_FEATURES = [
    "Age",
    "BusinessTravel",
    "DailyRate",
    "Department",
    "DistanceFromHome",
    "Education",
    "EducationField",
    "EmployeeNumber",
    "EnvironmentSatisfaction",
    "Gender",
    "HourlyRate",
    "JobInvolvement",
    "JobLevel",
    "JobRole",
    "JobSatisfaction",
    "MaritalStatus",
    "MonthlyIncome",
    "MonthlyRate",
    "NumCompaniesWorked",
    "OverTime",
    "PercentSalaryHike",
    "PerformanceRating",
    "RelationshipSatisfaction",
    "StockOptionLevel",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "WorkLifeBalance",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager",
    "Income_Per_Age",
    "Work_Ratio",
    "Loyalty_Ratio",
    "OverTime_Binary",
]


# ============================================================
# CSS
# ============================================================

CSS = """
.gradio-container {
    max-width: 1400px !important;
    margin: auto;
}

.hero {
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 25px;
    background: linear-gradient(135deg, #111827, #1e3a8a);
    color: white;
}

.hero h1 {
    font-size: 38px;
    margin-bottom: 8px;
}

.hero p {
    font-size: 17px;
    opacity: .9;
}

.result-card {
    border-radius: 18px;
    padding: 22px;
    border: 1px solid #e5e7eb;
    min-height: 150px;
}

.footer {
    text-align: center;
    padding: 25px;
    margin-top: 30px;
    color: #6b7280;
}
"""


# ============================================================
# FEATURE ENGINEERING
# ============================================================

def create_features(df):
    df = df.copy()

    df["Income_Per_Age"] = (
        df["MonthlyIncome"] / df["Age"].replace(0, 1)
    )

    df["Work_Ratio"] = (
        df["YearsAtCompany"] /
        df["TotalWorkingYears"].replace(0, 1)
    )

    df["Loyalty_Ratio"] = (
        df["YearsWithCurrManager"] /
        df["YearsAtCompany"].replace(0, 1)
    )

    df["OverTime_Binary"] = (
        df["OverTime"]
        .map({"Yes": 1, "No": 0})
        .fillna(0)
    )

    return df


# ============================================================
# PREPARE EMPLOYEE
# ============================================================

def prepare_employee(
    Age, BusinessTravel, DailyRate, Department, DistanceFromHome,
    Education, EducationField, EmployeeNumber,
    EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement,
    JobLevel, JobRole, JobSatisfaction, MaritalStatus,
    MonthlyIncome, MonthlyRate, NumCompaniesWorked, OverTime,
    PercentSalaryHike, PerformanceRating, RelationshipSatisfaction,
    StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear,
    WorkLifeBalance, YearsAtCompany, YearsInCurrentRole,
    YearsSinceLastPromotion, YearsWithCurrManager
):
    return pd.DataFrame([{
        "Age": Age,
        "BusinessTravel": BusinessTravel,
        "DailyRate": DailyRate,
        "Department": Department,
        "DistanceFromHome": DistanceFromHome,
        "Education": Education,
        "EducationField": EducationField,
        "EmployeeNumber": EmployeeNumber,
        "EnvironmentSatisfaction": EnvironmentSatisfaction,
        "Gender": Gender,
        "HourlyRate": HourlyRate,
        "JobInvolvement": JobInvolvement,
        "JobLevel": JobLevel,
        "JobRole": JobRole,
        "JobSatisfaction": JobSatisfaction,
        "MaritalStatus": MaritalStatus,
        "MonthlyIncome": MonthlyIncome,
        "MonthlyRate": MonthlyRate,
        "NumCompaniesWorked": NumCompaniesWorked,
        "OverTime": OverTime,
        "PercentSalaryHike": PercentSalaryHike,
        "PerformanceRating": PerformanceRating,
        "RelationshipSatisfaction": RelationshipSatisfaction,
        "StockOptionLevel": StockOptionLevel,
        "TotalWorkingYears": TotalWorkingYears,
        "TrainingTimesLastYear": TrainingTimesLastYear,
        "WorkLifeBalance": WorkLifeBalance,
        "YearsAtCompany": YearsAtCompany,
        "YearsInCurrentRole": YearsInCurrentRole,
        "YearsSinceLastPromotion": YearsSinceLastPromotion,
        "YearsWithCurrManager": YearsWithCurrManager,
    }])


# ============================================================
# PREDICTION
# ============================================================

def predict_employee(*args):

    if pipeline is None:
        return (
            f"## 🔴 Model Error\n\n`{MODEL_STATUS}`",
            "### 🟢 Stay Probability\n\n**N/A**",
            "### 🔴 Leave Probability\n\n**N/A**"
        )

    try:
        df = prepare_employee(*args)
        df = create_features(df)

        missing = [
            col for col in PIPELINE_FEATURES
            if col not in df.columns
        ]

        if missing:
            return (
                "## 🔴 Feature Error\n\n"
                f"Missing features:\n`{missing}`",
                "### 🟢 Stay Probability\n\n**N/A**",
                "### 🔴 Leave Probability\n\n**N/A**"
            )

        df = df[PIPELINE_FEATURES]

        prediction = int(pipeline.predict(df)[0])
        probabilities = pipeline.predict_proba(df)[0]

        classes = list(pipeline.classes_)
        probability_map = dict(zip(classes, probabilities))

        stay = probability_map.get(0, 0) * 100
        leave = probability_map.get(1, 0) * 100

        if prediction == 1:
            result = f"""
## 🔴 Attrition Risk Detected

The model predicts that this employee is likely to **LEAVE**.

**Leave Probability:** `{leave:.2f}%`

**Stay Probability:** `{stay:.2f}%`
"""
        else:
            result = f"""
## 🟢 Employee Likely to Stay

The model predicts that this employee is likely to **STAY**.

**Stay Probability:** `{stay:.2f}%`

**Leave Probability:** `{leave:.2f}%`
"""

        return (
            result,
            f"### 🟢 Stay Probability\n\n# {stay:.2f}%",
            f"### 🔴 Leave Probability\n\n# {leave:.2f}%"
        )

    except Exception as e:
        return (
            f"## 🔴 Prediction Error\n\n```text\n{type(e).__name__}: {e}\n```",
            "### 🟢 Stay Probability\n\n**N/A**",
            "### 🔴 Leave Probability\n\n**N/A**"
        )


# ============================================================
# EXAMPLE
# ============================================================

EXAMPLE_DATA = [
    35,
    "Travel_Rarely",
    800,
    "Sales",
    5,
    3,
    "Life Sciences",
    1001,
    3,
    "Male",
    60,
    3,
    2,
    "Sales Executive",
    3,
    "Single",
    5000,
    14000,
    2,
    "No",
    15,
    3,
    3,
    1,
    10,
    2,
    3,
    5,
    3,
    1,
    3,
]


# ============================================================
# GRADIO UI
# ============================================================

with gr.Blocks(title="Employee Attrition AI") as demo:

    gr.HTML("""
    <div class="hero">
        <h1>🤖 Employee Attrition AI</h1>
        <p>
            Professional Employee Attrition Prediction
            powered by XGBoost Machine Learning.
        </p>
    </div>
    """)

    gr.Markdown(f"### System Status\n\n{MODEL_STATUS}")

    gr.Markdown("# 👤 Employee Information")

    with gr.Row():
        with gr.Column():
            Age = gr.Number(label="Age", value=35)
            Gender = gr.Dropdown(
                ["Male", "Female"],
                label="Gender"
            )
            MaritalStatus = gr.Dropdown(
                ["Single", "Married", "Divorced"],
                label="Marital Status"
            )

        with gr.Column():
            Education = gr.Number(
                label="Education",
                minimum=1,
                maximum=5,
                value=3
            )
            EducationField = gr.Dropdown(
                [
                    "Life Sciences",
                    "Medical",
                    "Marketing",
                    "Technical Degree",
                    "Human Resources",
                    "Other"
                ],
                label="Education Field"
            )
            EmployeeNumber = gr.Number(
                label="Employee Number",
                value=1001
            )

    gr.Markdown("## 💼 Job Information")

    with gr.Row():
        with gr.Column():
            Department = gr.Dropdown(
                [
                    "Sales",
                    "Research & Development",
                    "Human Resources"
                ],
                label="Department"
            )

            JobRole = gr.Dropdown(
                [
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
                label="Job Role"
            )

            JobLevel = gr.Number(
                label="Job Level",
                minimum=1,
                maximum=5,
                value=2
            )

        with gr.Column():
            BusinessTravel = gr.Dropdown(
                [
                    "Travel_Rarely",
                    "Travel_Frequently",
                    "Non-Travel"
                ],
                label="Business Travel"
            )

            OverTime = gr.Dropdown(
                ["Yes", "No"],
                label="OverTime"
            )

            JobInvolvement = gr.Number(
                label="Job Involvement",
                minimum=1,
                maximum=4,
                value=3
            )

    gr.Markdown("## 😊 Satisfaction")

    with gr.Row():
        EnvironmentSatisfaction = gr.Number(
            label="Environment Satisfaction",
            minimum=1,
            maximum=4,
            value=3
        )

        JobSatisfaction = gr.Number(
            label="Job Satisfaction",
            minimum=1,
            maximum=4,
            value=3
        )

        RelationshipSatisfaction = gr.Number(
            label="Relationship Satisfaction",
            minimum=1,
            maximum=4,
            value=3
        )

        WorkLifeBalance = gr.Number(
            label="Work-Life Balance",
            minimum=1,
            maximum=4,
            value=3
        )

    gr.Markdown("## 💰 Financial Information")

    with gr.Row():
        DailyRate = gr.Number(label="Daily Rate", value=800)
        HourlyRate = gr.Number(label="Hourly Rate", value=60)
        MonthlyIncome = gr.Number(
            label="Monthly Income",
            value=5000
        )
        MonthlyRate = gr.Number(
            label="Monthly Rate",
            value=14000
        )

    gr.Markdown("## 📈 Career Information")

    with gr.Row():
        DistanceFromHome = gr.Number(
            label="Distance From Home",
            value=5
        )
        NumCompaniesWorked = gr.Number(
            label="Number of Companies Worked",
            value=2
        )
        TotalWorkingYears = gr.Number(
            label="Total Working Years",
            value=10
        )
        YearsAtCompany = gr.Number(
            label="Years At Company",
            value=5
        )

    with gr.Row():
        YearsInCurrentRole = gr.Number(
            label="Years In Current Role",
            value=3
        )
        YearsSinceLastPromotion = gr.Number(
            label="Years Since Last Promotion",
            value=1
        )
        YearsWithCurrManager = gr.Number(
            label="Years With Current Manager",
            value=3
        )
        TrainingTimesLastYear = gr.Number(
            label="Training Times Last Year",
            value=2
        )

    gr.Markdown("## 🎯 Performance & Compensation")

    with gr.Row():
        PercentSalaryHike = gr.Number(
            label="Percent Salary Hike",
            value=15
        )
        PerformanceRating = gr.Number(
            label="Performance Rating",
            minimum=1,
            maximum=5,
            value=3
        )
        StockOptionLevel = gr.Number(
            label="Stock Option Level",
            minimum=0,
            maximum=3,
            value=1
        )

    # ========================================================
    # INPUT LIST
    # ========================================================

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
        YearsWithCurrManager,
    ]

    # ========================================================
    # BUTTONS
    # ========================================================

    with gr.Row():
        predict_btn = gr.Button(
            "🚀 Predict Attrition",
            variant="primary"
        )

        example_btn = gr.Button(
            "📋 Load Example"
        )

        clear_btn = gr.Button(
            "🗑️ Clear"
        )

    # ========================================================
    # OUTPUTS
    # ========================================================

    with gr.Row():

        prediction_output = gr.Markdown(
            """
## 🔮 Prediction

Enter employee information and click
**Predict Attrition**.
""",
            elem_classes=["result-card"]
        )

        probability_output = gr.Markdown(
            """
## 📊 Probability

No prediction available.
""",
            elem_classes=["result-card"]
        )

    with gr.Row():

        stay_probability = gr.Markdown(
            """
### 🟢 Stay Probability

# 0.00%
""",
            elem_classes=["result-card"]
        )

        leave_probability = gr.Markdown(
            """
### 🔴 Leave Probability

# 0.00%
""",
            elem_classes=["result-card"]
        )

    # ========================================================
    # EVENTS
    # ========================================================

    predict_btn.click(
        fn=predict_employee,
        inputs=inputs,
        outputs=[
            prediction_output,
            stay_probability,
            leave_probability
        ]
    )

    example_btn.click(
        fn=lambda: EXAMPLE_DATA,
        inputs=[],
        outputs=inputs
    )

    clear_btn.click(
        fn=lambda: [None] * len(inputs),
        inputs=[],
        outputs=inputs
    )

    # ========================================================
    # INFORMATION
    # ========================================================

    gr.Markdown("""
## 🧠 Model Information

**Algorithm:** XGBoost Classifier

**Framework:** Scikit-Learn Pipeline

**Target:** Employee Attrition

**Accuracy:** 83.67%

**Deployment:** Gradio 6.20.0
""")

    gr.Markdown("""
## ⚙️ Automatic Feature Engineering

The application automatically creates:

- `Income_Per_Age`
- `Work_Ratio`
- `Loyalty_Ratio`
- `OverTime_Binary`

The final input is reordered according to the trained
pipeline feature schema.
""")

    gr.HTML("""
    <div class="footer">
        <h3>Employee Attrition AI</h3>
        <p>Python • Pandas • XGBoost • Scikit-Learn • Gradio</p>
        <p>© 2026</p>
    </div>
    """)


# ============================================================
# LAUNCH
# ============================================================

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=False,
        show_error=True,
        css=CSS,
        theme=gr.themes.Soft()
    )


    