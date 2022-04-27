#!/usr/bin/python

import pandas as pd
import joblib
import sys
import os

def predict_price=(Year,Mileage,State,Make,Model):
    reg = joblib.load(os.path.dirname(__file__) + '/car_pricing.pkl') 
    df_dum=pd.read_csv(os.path.dirname(__file__) + '/df_dum.csv')
    data=[[Year,Mileage,State,Make,Model]]
    df = pd.DataFrame(data, columns=['Year','Mileage','State','Make','Model'])
    newpredict = df.reindex(labels = df_dum['Columns'], axis = 1, fill_value = 0)
    prediction = reg.predict(newpredict)
    
    return prediction
    
if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Please enter a car description')
        
    else:

        Year = sys.argv[1]
        Mileage = sys.argv[2]
        State = sys.argv[3]
        Make = sys.argv[4]
        Model = sys.argv[5]

        prediction = predict_price(Year,Mileage,State,Make,Model)
        
        print(url)
        print('Car Price: ', prediction1)    
        