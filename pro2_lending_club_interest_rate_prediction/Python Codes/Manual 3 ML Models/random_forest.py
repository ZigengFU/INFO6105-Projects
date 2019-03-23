from __future__ import division
from sklearn import linear_model as LR
from sklearn.ensemble import RandomForestClassifier
import random
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_predict

loan_data = pd.read_csv('autoFeatureloadHashFinishData.csv',error_bad_lines=False,encoding = "utf-8")

data_array = np.array(loan_data)

print(data_array[1])

x = data_array[:, 1:data_array.shape[1]-1]
selection = [v for v in range(len(x)) if v % 5 != 0]
selection2 = [v for v in range(len(x)) if v % 5 == 0]
selectionAll = [v for v in range(len(x))]
x2 = x[selection, :]
x3 = x[selection2, :]
y = data_array[:, -1]
y2 = y[selection]
y3 = y[selection2]

dtr = GradientBoostingRegressor()
dtr.fit(x2,y2)

y_predprob_test = dtr.predict(x3)
#y_result = []
#for x in y_predprob_test:
	#y_result.append([x])
#y_result_random_forest = np.array(y_result)
#print(y_result_random_forest)
mape = sum(np.abs((y_predprob_test-y3)/y3))/len(y3)*100
print('the forest test mape is',mape)

y_predprob_training = dtr.predict(x2)
#y_result = []
#for x in y_predprob_training:
	#y_result.append([x])
#y_result_random_forest = np.array(y_result)
#print(y_result_random_forest)
mape = sum(np.abs((y_predprob_training-y2)/y2))/len(y2)*100
print('the forest training mape is',mape)

y = y[selectionAll]
y6_cross = cross_val_predict(dtr, x, y, cv = 5)
y6_cross = y6_cross[selection2]
mape = sum(np.abs((y6_cross-y3)/y3))/len(y3)*100
print(mape)

"""
x = data_array[:, 1:data_array.shape[1]-1]
selection = [v for v in range(len(x)) if v % 5 != 0]
selection2 = [v for v in range(len(x)) if v % 5 == 0]
x2 = x[selection, :]
x3 = x[selection2, :]
y = data_array[:, -1]
y2 = y[selection]
y3 = y[selection2]


dtr = GradientBoostingRegressor(n_estimators = 200, max_depth = 15)
#n_estimators default 100
#max_depth default 3
dtr.fit(x2,y2)
print(lr.coef_)
print(lr.intercept_)
y_predprob_test = dtr.predict(x3)
#y_result = []
#for x in y_predprob_test:
	#y_result.append([x])
#y_result_random_forest = np.array(y_result)
#print(y_result_random_forest)
mape = sum(np.abs((y_predprob_test-y3)/y3))/len(y3)*100
print('the forest test mape is',mape)


y_predprob_training = dtr.predict(x2)
#y_result = []
#for x in y_predprob_training:
	#y_result.append([x])
#y_result_random_forest = np.array(y_result)
#print(y_result_random_forest)
mape = sum(np.abs((y_predprob_training-y2)/y2))/len(y2)*100
print('the forest training mape is',mape)

y = y[selectionAll]
y6_cross = cross_val_predict(dtr, x, y, cv = 5)
y6_cross = y6_cross[selection2]
mape = sum(np.abs((y6_cross-y3)/y3))/len(y3)*100
print(mape)
"""