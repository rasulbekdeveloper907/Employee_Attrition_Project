from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler,
    RobustScaler,
    MaxAbsScaler
)



class Scaler:
    def __init__(self, x_train,x_test):
        self.x_train = x_train.copy()
        self.x_test = x_test.copy()

    def standard_scaler(self):
        scaler = StandardScaler()
        self.x_train = scaler.fit_transform(self.x_train)
        self.x_test = scaler.transform(self.x_test)

        print("Standart Scaler Applied Succesfully")

        return self.x_train, self.x_test
    

    def minmax_scaler(self):
        scaler = MinMaxScaler()
        self.x_train = scaler.fit_transform(self.x_train)
        self.x_test = scaler.transform(self.x_test)

        print("MinMaxScaler Applied Succesfully")

        return self.x_train, self.x_test

    def robust_scaler(self):
        scaler = RobustScaler()
        self.x_train = scaler.fit_transform(self.x_train)
        self.x_test = scaler.transform(self.x_test)

        print("RobustScaler Applied Succesfully")

        return self.x_train, self.x_test
    
    def maxabs_scaler(self):
        scaler = MaxAbsScaler()
        self.x_train = scaler.fit_transform(self.x_train)
        self.x_test = scaler.transform(self.x_test)

        print("MaxAbsScaler Applied Succesfully")

        return self.x_train, self.x_test    