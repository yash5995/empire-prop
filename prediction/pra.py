# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:00:29 2020

@author: Darshan
"""

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import joblib

#import dataset
#dataset = pd.read_csv('AhmDataSet_new_test.csv')
#x = dataset.iloc[:, :-1].values
#y = dataset.iloc[:, 5].values

x_dummy = [2,'Satellite',1400,'Ready to move',3]
x_dummy_df = pd.DataFrame([x_dummy])
x_dummy_test = np.array(x_dummy_df)

x_test = x_dummy_test

#Load and perform encoding
labelencoder_x_1 = joblib.load('../LE_1.sav')
labelencoder_x_3 = joblib.load('../LE_3.sav')
onehotencoder = joblib.load('../OHE.sav')

x_test[:, 1] = labelencoder_x_1.transform(x_test[:, 1])
x_test[:, 3] = labelencoder_x_3.transform(x_test[:, 3])

x_test = onehotencoder.transform(x_test).toarray()

#Decison Tree
regressor_dt = joblib.load('../predict_decision_tree.sav')
y_pred_dt = regressor_dt.predict(x_test)

#Random Forest
regressor_rf = joblib.load('../predict_random_forest.sav')
y_pred_rf = regressor_rf.predict(x_test)

#Gradient Boosting
regressor_gb = joblib.load('../predict_gradient_boosting.sav')
y_pred_gb = regressor_gb.predict(x_test)

