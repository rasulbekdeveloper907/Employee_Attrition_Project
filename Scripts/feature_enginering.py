import pandas as pd 

class FeatureEngineer:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    
    def create_age_features(self):
        if "Age" in self.df.columns:
            self.df["Age_Group"] = pd.cut(self.df["Age"], bins=[18, 30, 40, 50, 60, 100], labels=["Young", "Mid", "Senior", "Old", "Very_Old"])
            return self.df
        
    def create_income_features(self):
        if "MonthlyIncome" in self.df.columns and "Age" in self.df.columns:
            self.df["Income_Per_Age"] = self.df["MonthlyIncome"] / (self.df["Age"] + 1)

        if "MonthlyIncome" in self.df.columns:
            self.df["Income_Level"] = pd.qcut(self.df["MonthlyIncome"], q = 4, labels=["Low", "Medium", "High", "Very_High"])
        return self.df 