import joblib
import pandas as pd


class GuassianNBClassifier:
    def __init__(self):
        path_to_artifacts="/notebook/"
        self.model = joblib.load(path_to_artifacts + "GuassianNB.joblib")

    def preprocessing(self,input_data):

        return input_data

    def predict(self,input_data):
        return self.model.predict(input_data)

    def computeprediction(self,input_data):

        try:
            input_data=self.preprocessing(input_data)
            prediction=self.predict(input_data)[0]
        
        except Exception as e:
            return "something went Wrong"

        return prediction

    