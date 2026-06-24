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

    def create_work_features(self):
        if "TotalWorkingYears" in self.df.columns and "Age" in self.df.columns:
            self.df["Work_Ratio"] = self.df["TotalWorkingYears"] / (self.df["Age"] + 1)

        if "YearsAtCompany" in self.df.columns and "TotalWorkingYears" in self.df.columns:
            self.df["Loyalty_Ratio"] = self.df["YearsAtCompany"] / (self.df["TotalWorkingYears"] +1 )

        return self.df
    
    def create_over_time_feature(self):
        if "OverTime" in self.df.columns:
            self.df["OverTime_Binary"] = self.df["OverTime"].map({"Yes": 1, "No":0})
        return self.df
    
    def drop_originals(self):
        cols_to_drop = []
        for col in  ["OverTime"]:
            if col in self.df.columns:
                cols_to_drop.append(col)
        
        self.df.drop(columns=cols_to_drop, inplace=True, errors='ignore')
        return self.df

    def get_data(self):
        return self.df
    