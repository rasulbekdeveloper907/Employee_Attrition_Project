from imblearn.over_sampling import RandomOverSampler, SMOTE, ADASYN
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTETomek, SMOTEENN


class Sampler:
    def __init__(self, x_train, y_train):
        self.x_train = x_train.copy()
        self.y_train = y_train.copy()


    def random_over_sampler(self, random_state = 42):
        ros = RandomOverSampler(random_state=random_state)
        self.x_train, self.y_train = ros.fit_resample(self.x_train, self.y_train)

        print("Random Over Samler Apllied Succesfully")

        return self.x_train, self.y_train
    

    def random_under_sampler(self, random_state = 42):
        
        rus = RandomUnderSampler(random_state=random_state)

        self.x_train, self.y_train = rus.fit_resample(self.x_train, self.y_train)

        print("Random Under Samler Apllied Succesfully")

        return self.x_train, self.y_train
    
    def smote(self, random_state = 42):

        smote = SMOTE(random_state = random_state)

        self.x_train, self.y_train = smote.fit_resample(self.x_train, self.y_train)

        print("SMOTE Apllied Sucessfully")


        return self.x_train, self.y_train
    

    def adasyn(self, random_state = 42):

        ada = ADASYN(random_state = random_state)

        self.x_train, self.y_train = ada.fit_resample(self.x_train, self.y_train)

        print("ADASYN Apllied Sucessfully")

        return self.x_train, self.y_train

    def smote_tomek(self, random_state = 42):

        smt = SMOTETomek(random_state = random_state)

        self.x_train, self.y_train = smt.fit_resample(self.x_train, self.y_train)

        print("SMOTE TOMEK  Apllied Sucessfully")

        return self.x_train, self.y_train

    def smote_enn(self, random_state = 42):

        smenn = SMOTEENN(random_state = random_state)

        self.x_train, self.y_train = smenn.fit_resample(self.x_train, self.y_train)

        print(" SMOTEENN  Apllied Sucessfully")

        return self.x_train, self.y_train
    
    def distribution(self):
        print(self.y_train.value_counts())

    def get_data(self):
        return self.x_train, self.y_train