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
from sklearn.preprocessing import Normalizer
from sklearn.model_selection import cross_val_predict

loan_data = pd.read_csv('loadHashFinishData.csv',error_bad_lines=False,encoding = "utf-8")

data_array = np.array(loan_data)

#print(data_array[1])

x = data_array[:, 1:data_array.shape[1]]
selection = [v for v in range(len(x)) if v % 5 != 0]
selection2 = [v for v in range(len(x)) if v % 5 == 0]
x2 = x[selection, :]
x3 = x[selection2, :]
y = data_array[:, -1:]
y2 = y[selection, :]
y3 = y[selection2, :]



#print(x2)
#print(y2)

lr = LR.LinearRegression()
lr.normalize = True
lr.fit(x2, y2)

y4 = lr.predict(x3)
#print(y4)
y5 = lr.predict(x2)
#print(u'模型的平均准确率（训练集）为：%s' % lr.score(x2, y2));
#print(u'模型的平均准确率（测试集）为：%s' % lr.score(x3, y3));
#print(lr.coef_)
#print(lr.intercept_)
#print(lr.get_params(deep=True))

n= len(y3)
n2= len(y2)
mape = sum(np.abs((y4-y3)/y3))/n*100
print(mape)
mape = sum(np.abs((y5-y2)/y2))/n2*100
print(mape)
y6_cross = cross_val_predict(lr, x, y, cv = 5)
y6_cross = y6_cross[selection2, :]
mape = sum(np.abs((y6_cross-y3)/y3))/len(y3)*100
print(mape)



#l1 normalize
norm1 = Normalizer(norm = 'l1')
data_array = norm1.fit_transform(data_array)

x = data_array[:, 1:data_array.shape[1]]
selection = [v for v in range(len(x)) if v % 5 != 0]
selection2 = [v for v in range(len(x)) if v % 5 == 0]
x2 = x[selection, :]
x3 = x[selection2, :]
y = data_array[:, -1:]
y2 = y[selection, :]
y3 = y[selection2, :]

lr2 = LR.LinearRegression()
lr.fit(x2, y2)
y4 = lr.predict(x3)
#print(y4)
y5 = lr.predict(x2)
#print(u'模型的平均准确率（训练集）为：%s' % lr.score(x2, y2));
#print(u'模型的平均准确率（测试集）为：%s' % lr.score(x3, y3));
#print(lr.coef_)
#print(lr.intercept_)
#print(lr.get_params(deep=True))

n= len(y3)
n2= len(y2)
mape = sum(np.abs((y4-y3)/y3))/n*100
print(mape)
mape = sum(np.abs((y5-y2)/y2))/n2*100
print(mape)
y6_cross = cross_val_predict(lr, x, y, cv = 5)
y6_cross = y6_cross[selection2, :]
mape = sum(np.abs((y6_cross-y3)/y3))/len(y3)*100
print(mape)


#l2 normalize
norm1 = Normalizer(norm = 'l2')
data_array = norm1.fit_transform(data_array)

x = data_array[:, 1:data_array.shape[1]]
selection = [v for v in range(len(x)) if v % 5 != 0]
selection2 = [v for v in range(len(x)) if v % 5 == 0]
selectionAll = [v for v in range(len(x))]
x2 = x[selection, :]
x3 = x[selection2, :]
y = data_array[:, -1:]
y2 = y[selection, :]
y3 = y[selection2, :]

lr2 = LR.LinearRegression()
lr2.fit(x2, y2)
y4 = lr2.predict(x3)
#print(y4)
y5 = lr2.predict(x2)
#print(u'模型的平均准确率（训练集）为：%s' % lr.score(x2, y2));
#print(u'模型的平均准确率（测试集）为：%s' % lr.score(x3, y3));
#print(lr.coef_)
#print(lr.intercept_)
#print(lr.get_params(deep=True))

n= len(y3)
n2= len(y2)
mape = sum(np.abs((y4-y3)/y3))/n*100
print(mape)
mape = sum(np.abs((y5-y2)/y2))/n2*100
print(mape)
y6_cross = cross_val_predict(lr2, x, y, cv = 5)
y6_cross = y6_cross[selection2, :]
mape = sum(np.abs((y6_cross-y3)/y3))/len(y3)*100
print(mape)
