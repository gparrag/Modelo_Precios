import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn import ensemble
dataTraining = pd.read_csv('https://raw.githubusercontent.com/albahnsen/MIAD_ML_and_NLP/main/datasets/dataTrain_carListings.zip')
dataTesting = pd.read_csv('https://raw.githubusercontent.com/albahnsen/MIAD_ML_and_NLP/main/datasets/dataTest_carListings.zip', index_col=0)
y = dataTraining["Price"]
x = dataTraining.drop(['Price'],axis=1)
dataTraining_2 = pd.get_dummies(x, columns=["State","Make","Model"],  drop_first=True )
dataTraining_4 = dataTraining_2.drop(['Make_Freightliner'],axis=1)
XTrain, XTest, yTrain, yTest = train_test_split(dataTraining_4, y, test_size=0.33, random_state=0)

best_params = dict(
    learning_rate=0.2,
    n_estimators=450,
    max_depth=10,
    min_samples_leaf=5,
    min_samples_split=10,
)
gbr_ls = ensemble.GradientBoostingRegressor(**best_params)
gbr_ls.fit(XTrain, yTrain)
joblib.dump(gbr_ls, os.path.dirname(__file__) + '/car_pricing.pkl', compress=3)