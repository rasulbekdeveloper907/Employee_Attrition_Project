import pandas as pd 

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

class TrainModel:
    def __init__(self, x_train, x_test, y_train, y_test):
        self.x_train = x_train.copy()
        self.x_test = x_test.copy()

        if isinstance(y_train, pd.DataFrame):
            self.y_train = y_train.iloc[:, 0]
        else:
            self.y_train = y_train

        if isinstance(y_test, pd.DataFrame):
            self.y_test = y_test.iloc[:, 0]
        else:
            self.y_test = y_test

        
    def logistic_regression(self):
        model = LogisticRegression()

        model.fit(self.x_train, self.y_train)
        prediction = model.predict(self.x_test)

        accuracy = accuracy_score(self.y_test, prediction)

        print("Logistic Regression")
        print(f"Accuracy Score: {accuracy:.4f}")

        return model 
    
        
    def decision_tree(self):
        model = DecisionTreeClassifier(random_state=42)

        model.fit(self.x_train, self.y_train)

        prediction = model.predict(self.x_test)

        accuracy = accuracy_score(self.y_test, prediction)

        print("Decision Tree Classifier")
        print(f"Accuracy Score: {accuracy:.4f}")

        return model     
    
    def random_forest(self):
        model = RandomForestClassifier(random_state=42)

        model.fit(self.x_train, self.y_train)

        prediction = model.predict(self.x_test)

        accuracy = accuracy_score(self.y_test, prediction)

        print("Random Forest Classifier")
        print(f"Accuracy Score: {accuracy:.4f}")

        return model      

    def knn(self, n_neighbors=5):
        model = KNeighborsClassifier(n_neighbors=n_neighbors)

        model.fit(self.x_train, self.y_train)

        prediction = model.predict(self.x_test)

        accuracy = accuracy_score(self.y_test, prediction)

        print(" KNN Classifier")
        print(f"Accuracy Score: {accuracy:.4f}")

        return model       

    def svc(self):
        model = SVC(random_state=42)

        model.fit(self.x_train, self.y_train)

        prediction = model.predict(self.x_test)

        accuracy = accuracy_score(self.y_test, prediction)

        print(" SVM  Classifier")
        print(f"Accuracy Score: {accuracy:.4f}")

        return model     
    
    def naive_bayes(self):

        model = GaussianNB()

        model.fit(self.x_train, self.y_train)

        prediction = model.predict(self.x_test)

        accuracy = accuracy_score(self.y_test, prediction)

        print(" Naive Bayes  Classifier")
        print(f"Accuracy Score: {accuracy:.4f}")

        return model       