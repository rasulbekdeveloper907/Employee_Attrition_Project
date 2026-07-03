import numpy as np
import pandas as pd

from sklearn.feature_selection import (
    VarianceThreshold,
    SelectKBest,
    mutual_info_classif,
    RFE
)

from sklearn.ensemble import RandomForestClassifier


class FeatureSelector:

    def __init__(self, x_train, x_test, y_train):

        self.x_train = x_train.copy()
        self.x_test = x_test.copy()

        if isinstance(y_train, pd.DataFrame):
            self.y_train = y_train.iloc[:, 0]
        else:
            self.y_train = y_train



    def variance_threshold(self, threshold=0.0):

        selector = VarianceThreshold(threshold=threshold)

        selector.fit(self.x_train)

        selected_columns = self.x_train.columns[selector.get_support()]

        self.x_train = pd.DataFrame(
            selector.transform(self.x_train),
            columns=selected_columns
        )

        self.x_test = pd.DataFrame(
            selector.transform(self.x_test),
            columns=selected_columns
        )

        print(" Variance Threshold Applied")
        print(f"Remaining Features: {self.x_train.shape[1]}")

        return self.x_train, self.x_test



    def correlation(self, threshold=0.90):

        corr_matrix = self.x_train.corr().abs()

        upper = corr_matrix.where(
            np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
        )

        drop_columns = [
            column
            for column in upper.columns
            if any(upper[column] > threshold)
        ]

        if drop_columns:
            self.x_train.drop(columns=drop_columns, inplace=True)
            self.x_test.drop(columns=drop_columns, inplace=True)

        print(f" Dropped {len(drop_columns)} Columns")
        print(drop_columns)
        print(f"Remaining Features: {self.x_train.shape[1]}")

        return self.x_train, self.x_test



    def select_k_best(self, k=20):

        selector = SelectKBest(
            score_func=mutual_info_classif,
            k=k
        )

        selector.fit(self.x_train, self.y_train)

        selected_columns = self.x_train.columns[
            selector.get_support()
        ]

        self.x_train = pd.DataFrame(
            selector.transform(self.x_train),
            columns=selected_columns
        )

        self.x_test = pd.DataFrame(
            selector.transform(self.x_test),
            columns=selected_columns
        )

        print(f" Top {k} Features Selected")

        return self.x_train, self.x_test



    def rfe(self, n_features=20):

        model = RandomForestClassifier(random_state=42)

        selector = RFE(
            estimator=model,
            n_features_to_select=n_features
        )

        selector.fit(self.x_train, self.y_train)

        selected_columns = self.x_train.columns[
            selector.support_
        ]

        self.x_train = pd.DataFrame(
            selector.transform(self.x_train),
            columns=selected_columns
        )

        self.x_test = pd.DataFrame(
            selector.transform(self.x_test),
            columns=selected_columns
        )

        print(f" RFE Applied ({n_features} Features Selected)")

        return self.x_train, self.x_test



    def feature_importance(self):

        model = RandomForestClassifier(
            random_state=42
        )

        model.fit(
            self.x_train,
            self.y_train
        )

        importance = pd.DataFrame({

            "Feature": self.x_train.columns,
            "Importance": model.feature_importances_

        })

        importance = importance.sort_values(
            by="Importance",
            ascending=False
        ).reset_index(drop=True)

        return importance



    def get_data(self):

        return self.x_train, self.x_test