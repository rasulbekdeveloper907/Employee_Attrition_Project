import pandas as pd 
import numpy as np 

class MissingValueHandler:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def missing_report(self):
        report = pd.DataFrame({
            "missing_count":self.df.isnull().sum(),
            "missing_percent": (self.df.isnull().sum() / len(self.df)) * 100 
        })
        return report.sort_values(by="missing_percent", ascending=False)
    
    def fill_numerical(self, strategy="median"):
        num_cols = self.df.select_dtypes(include=["int64", "float64"]).columns

        for col in num_cols:
            if self.df[col].isnull().sum() > 0:
                if strategy== "mean":
                    self.df[col].fillna(self.df[col].mean(), inplace=True)
                elif strategy=="median":
                    self.df[col].fillna(self.df[col].median(), inplace=True)
                elif strategy == "zero":
                    self.df[col].fillna(0, inplace=True)

        return self.df
    
    def fill_categorical(self, strategy="mode"):
        cat_cols = self.df.select_dtypes(include=["object"]).columns

        for col in cat_cols:
            if self.df[col].isnull().sum() > 0:
                if strategy== "mode":
                    self.df[col].fillna(self.df[col].mode()[0], inplace=True)
                elif strategy=="unknown":
                    self.df[col].fillna("Unknown", inplace=True)
                
        return self.df

    def drop_high_missing(self, threshold=50):
        missing_percent = (self.df.isnull().sum() / len(self.df)) * 100 
        drop_cols = missing_percent[missing_percent > threshold].index
        self.df.drop(columns=drop_cols, inplace=True)
        return self.df
    
    def get_data(self):
        return self.df
