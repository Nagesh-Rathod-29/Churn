import numpy as np
import pickle
import json

class Model():

    def __init__(self):

        self.model = pickle.load(open(r"artifacts//model.pkl",'rb'))
        self.scaler = pickle.load(open(r"artifacts//scaler.pkl",'rb'))
        self.data = json.load(open(r"artifacts//model_data.json",'r'))


    def result(self,SeniorCitizen,
                Partner,Dependents,tenure,
                InternetService,OnlineSecurity,
                OnlineBackup,DeviceProtection,
                TechSupport,StreamingTV,StreamingMovies,
                Contract,PaperlessBilling,MonthlyCharges,
                TotalCharges,PaymentMethod):

        test_array = np.zeros(self.model.n_features_in_)

        test_array[0] = SeniorCitizen
        test_array[1] = self.data['Partner'][Partner]
        test_array[2] = self.data['Dependents'][Dependents]
        test_array[3] = tenure
        test_array[4] = self.data['InternetService'][InternetService]
        test_array[5] = self.data['OnlineSecurity'][OnlineSecurity]
        test_array[6] = self.data['OnlineBackup'][OnlineBackup]
        test_array[7] = self.data['DeviceProtection'][DeviceProtection]
        test_array[8] = self.data['TechSupport'][TechSupport]
        test_array[9] = self.data['StreamingTV'][StreamingTV]
        test_array[10] = self.data['StreamingMovies'][StreamingMovies]
        test_array[11] = self.data['Contract'][Contract]
        test_array[12] = self.data['PaperlessBilling'][PaperlessBilling]
        test_array[13] = MonthlyCharges
        test_array[14] = TotalCharges

        ind = self.data['features'].index('PaymentMethod_'+PaymentMethod)

        test_array[ind] = 1


        scaled_array = self.scaler.transform([test_array])

        pred = self.model.predict(scaled_array)
        print("Predicted class: ",pred)
        if pred[0] == 0:
            print("Customer will stay with company")
        else:
            print("Churn detected")

        return pred[0]
