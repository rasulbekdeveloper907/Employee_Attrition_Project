from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="Employee Attrition Prediction API",
    description="Machine Learning API using FastAPI",
    version="1.0.0"
)

model = joblib.load("Models/xgboost_model.pkl")


class Employee(BaseModel):
    Age: int
    DailyRate: int
    DistanceFromHome: int
    Education: int
    EnvironmentSatisfaction: int
    JobInvolvement: int
    JobLevel: int
    JobSatisfaction: int
    MonthlyIncome: int
    MonthlyRate: int
    NumCompaniesWorked: int
    PercentSalaryHike: int
    PerformanceRating: int
    RelationshipSatisfaction: int
    StockOptionLevel: int
    TotalWorkingYears: int
    TrainingTimesLastYear: int
    WorkLifeBalance: int
    YearsAtCompany: int
    YearsInCurrentRole: int
    YearsSinceLastPromotion: int
    YearsWithCurrManager: int



@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Attrition Prediction API"
    }



@app.get("/about")
def about():
    return {
        "Project": "Employee Attrition Prediction",
        "Framework": "FastAPI",
        "Model": "XGBoost"
    }



@app.post("/predict")
def predict(employee: Employee):

    # Convert input to DataFrame
    data = pd.DataFrame([employee.model_dump()])

    # Prediction
    prediction = model.predict(data)[0]

    # Probability (agar model qo'llab-quvvatlasa)
    probability = model.predict_proba(data)[0].max()

    return {
        "Prediction": int(prediction),
        "Probability": round(float(probability), 4)
    }