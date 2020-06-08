#import libraries
import numpy as np
import pandas as pd
import joblib

#import dataset
dataset = pd.read_csv('AhmDataSet_new_test.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 5].values

#Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_x_1 = LabelEncoder()
labelencoder_x_3 = LabelEncoder()

x[:, 1] = labelencoder_x_1.fit_transform(x[:, 1])
x[:, 3] = labelencoder_x_3.fit_transform(x[:, 3])
filename = 'LE_1.sav'
joblib.dump(labelencoder_x_1, filename)
filename = 'LE_3.sav'
joblib.dump(labelencoder_x_3, filename)
# onehotencoder = OneHotEncoder(categorical_features = [1,3])
# x = onehotencoder.fit_transform(x).toarray()
ct = ColumnTransformer([("Appartment_size", OneHotEncoder(), [1])], remainder = 'passthrough')
x = ct.fit_transform(x).toarray()
filename = 'OHE.sav'

joblib.dump(ct, filename)

#split dataset into training and test sets
#from sklearn.model_selection import train_test_split
#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
x_train = x
y_train = y

# =============================================================================
# #Decision Tree
# =============================================================================
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(x_train,y_train)

regressor_score_dt = regressor.score(x_train,y_train)

#y_pred_dt = regressor.predict(x_test)
#y_pred_list = y_pred.tolist()

#Save model
filename = '../predict_decision_tree.sav'
joblib.dump(regressor, filename)

# =============================================================================
# #Random Forest
# =============================================================================
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=300, random_state=0)
regressor.fit(x_train,y_train)

regressor_score_rf = regressor.score(x_train,y_train)
#y_pred_rf = regressor.predict(x_test)

#Save model
filename = '../predict_random_forest.sav'
joblib.dump(regressor, filename)

# =============================================================================
# #Gradient Boosting model
# =============================================================================
from sklearn import ensemble
params = {'n_estimators': 500, 'max_depth': 4, 'min_samples_split': 2,
          'learning_rate': 0.01, 'loss': 'ls'}
model = ensemble.GradientBoostingRegressor(**params)

model.fit(x_train, y_train)

model_score_gb = model.score(x_train,y_train)
#y_pred_gb = model.predict(x_test)

#Save model
filename = '../predict_gradient_boosting.sav'
joblib.dump(regressor, filename)

