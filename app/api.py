from pathlib import Path

import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


# ============================================================
# PATH
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
    MODEL_LOADED = True
    MODEL_ERROR = None

except Exception as e:
    pipeline = None
    MODEL_LOADED = False
    MODEL_ERROR = str(e)


# ============================================================
# FASTAPI
# ============================================================

app = FastAPI(
    title="Employee Attrition Prediction API",
    description="""
Professional Machine Learning API for Employee Attrition Prediction.

This API uses a trained XGBoost pipeline to predict whether
an employee is likely to stay or leave the company.
""",
    version="1.0.0",
)


# ============================================================
# INPUT SCHEMA
# ============================================================

class Employee(BaseModel):

    Age: int = Field(..., ge=18, le=100)

    BusinessTravel: str

    DailyRate: float

    Department: str

    DistanceFromHome: float

    Education: int = Field(..., ge=1, le=5)

    EducationField: str

    EmployeeNumber: int

    EnvironmentSatisfaction: int = Field(..., ge=1, le=4)

    Gender: str

    HourlyRate: float

    JobInvolvement: int = Field(..., ge=1, le=4)

    JobLevel: int = Field(..., ge=1, le=5)

    JobRole: str

    JobSatisfaction: int = Field(..., ge=1, le=4)

    MaritalStatus: str

    MonthlyIncome: float

    MonthlyRate: float

    NumCompaniesWorked: int

    OverTime: str

    PercentSalaryHike: float

    PerformanceRating: int = Field(..., ge=1, le=5)

    RelationshipSatisfaction: int = Field(..., ge=1, le=4)

    StockOptionLevel: int = Field(..., ge=0, le=3)

    TotalWorkingYears: int

    TrainingTimesLastYear: int

    WorkLifeBalance: int = Field(..., ge=1, le=4)

    YearsAtCompany: int

    YearsInCurrentRole: int

    YearsSinceLastPromotion: int

    YearsWithCurrManager: int


# ============================================================
# FEATURE ENGINEERING
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


def create_features(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    # Income per age
    df["Income_Per_Age"] = (
        df["MonthlyIncome"]
        / df["Age"].replace(0, 1)
    )

    # Company experience ratio
    df["Work_Ratio"] = (
        df["YearsAtCompany"]
        / df["TotalWorkingYears"].replace(0, 1)
    )

    # Loyalty ratio
    df["Loyalty_Ratio"] = (
        df["YearsWithCurrManager"]
        / df["YearsAtCompany"].replace(0, 1)
    )

    # Overtime binary
    df["OverTime_Binary"] = (
        df["OverTime"]
        .map({
            "Yes": 1,
            "No": 0
        })
        .fillna(0)
    )

    return df


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get(
    "/",
    tags=["System"]
)
def home():

    return {
        "message": "Employee Attrition Prediction API",
        "status": "running",
        "version": "1.0.0",
        "model_loaded": MODEL_LOADED
    }


@app.get(
    "/health",
    tags=["System"]
)
def health():

    if MODEL_LOADED:

        return {
            "status": "healthy",
            "model": "XGBoost Pipeline",
            "model_loaded": True
        }

    return {
        "status": "unhealthy",
        "model": "XGBoost Pipeline",
        "model_loaded": False,
        "error": MODEL_ERROR
    }


# ============================================================
# MODEL INFO
# ============================================================

@app.get(
    "/model-info",
    tags=["Model"]
)
def model_info():

    return {
        "model_type": "XGBoost",
        "pipeline": True,
        "features": len(PIPELINE_FEATURES),
        "feature_names": PIPELINE_FEATURES,
        "model_path": str(MODEL_PATH),
    }


# ============================================================
# PREDICTION
# ============================================================

@app.post(
    "/predict",
    tags=["Prediction"]
)
def predict(employee: Employee):

    if pipeline is None:

        raise HTTPException(
            status_code=500,
            detail=f"Model could not be loaded: {MODEL_ERROR}"
        )

    try:

        # ----------------------------------------------------
        # Pydantic -> DataFrame
        # ----------------------------------------------------

        data = pd.DataFrame([
            employee.model_dump()
        ])

        # ----------------------------------------------------
        # Feature Engineering
        # ----------------------------------------------------

        data = create_features(data)

        # ----------------------------------------------------
        # Check features
        # ----------------------------------------------------

        missing_features = [
            feature
            for feature in PIPELINE_FEATURES
            if feature not in data.columns
        ]

        if missing_features:

            raise HTTPException(
                status_code=400,
                detail={
                    "message": "Required features are missing.",
                    "missing_features": missing_features
                }
            )

        # ----------------------------------------------------
        # Feature order
        # ----------------------------------------------------

        data = data[PIPELINE_FEATURES]

        # ----------------------------------------------------
        # Prediction
        # ----------------------------------------------------

        prediction = pipeline.predict(data)[0]

        # ----------------------------------------------------
        # Probability
        # ----------------------------------------------------

        probabilities = pipeline.predict_proba(data)[0]

        classes = list(pipeline.classes_)

        probability_map = dict(
            zip(classes, probabilities)
        )

        stay_probability = (
            probability_map.get(0, 0) * 100
        )

        leave_probability = (
            probability_map.get(1, 0) * 100
        )

        # ----------------------------------------------------
        # Label
        # ----------------------------------------------------

        if int(prediction) == 1:

            label = "Leave"

        else:

            label = "Stay"

        # ----------------------------------------------------
        # Response
        # ----------------------------------------------------

        return {

            "success": True,

            "prediction": int(prediction),

            "label": label,

            "probabilities": {

                "stay": round(
                    float(stay_probability),
                    2
                ),

                "leave": round(
                    float(leave_probability),
                    2
                )
            },

            "model": {

                "name": "XGBoost",

                "pipeline": True,

                "features": len(
                    PIPELINE_FEATURES
                )
            }
        }

    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail={
                "message": "Prediction failed.",
                "error": str(e)
            }
        )