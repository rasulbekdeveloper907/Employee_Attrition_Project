import pandas as pd 
from sklearn.preprocessing import LabelEncoder


class Encoder:
    def __init__(self, df):
        self.df = df.copy()
        self.label_encoders = {}


    def label_encode_binary(self):
        binary_cols = []

        for col in self.df.select_dtypes(include=["object"]).columns:
            if self.df[col].nunique() == 2:
                binary_cols.append(col)

        for col in binary_cols:
            le = LabelEncoder()
            self.df[col] = le.fit_transform(self.df[col])
            self.label_encoders[col] = le

        print(f"Label Encoded Columns: {binary_cols}")

        return self.df

    def one_hot_encode(self):
        categorical_cols = []

        for col in self.df.select_dtypes(include=["object", "category"]).columns:
            if self.df[col].nunique() > 2:
                categorical_cols.append(col)
        self.df = pd.get_dummies(
            self.df,
            columns=categorical_cols,
            drop_first=True,
            dtype=int
        )

        print(f"One Hot Encoded Columns: {categorical_cols}")

        return self.df
    
    def get_data(self):
        return self.df