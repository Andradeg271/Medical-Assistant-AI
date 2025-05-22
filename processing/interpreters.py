import joblib
import pandas as pd


with open('model/models_pkl/btest_model.pkl', 'rb') as f:
    model1 = joblib.load(f)
    
columns = ['Hemoglobin_Status', 'Hematocrit_Status', 'WBC_Status', 
           'Platelets_Status', 'MCH_Status', 'MCV_Status', 'Condition']

def interpreter_btest(data):
    prediction = model1.predict(data)
    prediction_df = pd.DataFrame(prediction,columns=columns)
    return prediction_df



with open('model/models_pkl/symptoms_model.pkl', 'rb') as f:
    model2 = joblib.load(f)

def interpreter_sympt(data):
    prediction = model2.predict(data)
    return prediction



