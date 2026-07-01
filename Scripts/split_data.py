from sklearn.model_selection import train_test_split


class DataSplitter:
    def __init__(self, df, target):
        self.df = df.copy()
        self.target = target


        self.x_train = None 
        self.x_test = None
        self.y_train = None
        self.y_test = None

    def split(
            self,
            test_size = 0.2, 
            random_state=42,
            shuffle=True,
            stratify=True
    ):
        x = self.df.drop(columns=[self.target])
        y = self.df[self.target]


        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=test_size, random_state=random_state, shuffle=shuffle, stratify=y if stratify else None)

        print("=" * 45 )
        print("Train/Test Split Copleted Sucessfully")
        print("=" * 45) 

        print(f"Train Shape : {self.x_train.shape}")
        print(f"Train Shape : {self.x_test.shape}")

        return (
            self.x_train,
            self.x_test,
            self.y_train,
            self.y_test
        )
    

    def train_target_distribution(self):
        print("\n Train Target Distribution")
        print(self.y_train.value_counts())

    def test_target_distribution(self):
        print("\nTest Target Distribution")
        print(self.y_test.value_counts())

    def get_data(self):
        
        return (
            self.x_train,
            self.x_test,
            self.y_train,
            self.y_test
        )