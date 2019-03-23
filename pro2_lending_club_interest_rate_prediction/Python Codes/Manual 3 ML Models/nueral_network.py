import numpy as np
from sklearn.neural_network import MLPRegressor  # 多层线性回归
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_predict
import pandas as pd

loan_data = pd.read_csv('loadHashFinishData.csv',error_bad_lines=False,encoding = "utf-8")

dataMat = np.array(loan_data)
X=dataMat[:,1:dataMat.shape[1]]
selection = [v for v in range(len(X)) if v % 5 != 0]
selection2 = [v for v in range(len(X)) if v % 5 == 0]
selectionAll = [v for v in range(len(X))]
x2 = X[selection, :]
x3 = X[selection2, :]
y = dataMat[:,-1]
y2 = y[selection]
y3 = y[selection2]

scaler = StandardScaler() # 标准化转换
scaler.fit(x2)  # 训练标准化对象
x2 = scaler.transform(x2)   # 转换数据集

# solver='lbfgs',  MLP的求解方法：L-BFGS 在小数据上表现较好，Adam 较为鲁棒，SGD在参数调整较优时会有最佳表现（分类效果与迭代次数）；SGD标识随机梯度下降。
# alpha:L2的参数：MLP是可以支持正则化的，默认为L2，具体参数需要调整
# hidden_layer_sizes=(5, 2) hidden层2层,第一层5个神经元，第二层2个神经元)，2层隐藏层，也就有3层神经网络
clf = MLPRegressor(learning_rate='constant',learning_rate_init=0.001, solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(x2, y2)

y_predprob_test = clf.predict(x3)
mape = sum(np.abs((y_predprob_test-y3)/y3))/len(y3)*100
print('the forest test mape is',mape)

y_predprob_training = clf.predict(x2)
mape = sum(np.abs((y_predprob_training-y2)/y2))/len(y2)*100
print('the forest training mape is',mape)

y = y[selectionAll]
y6_cross = cross_val_predict(clf, X, y, cv = 5)
y6_cross = y6_cross[selection2]
mape = sum(np.abs((y6_cross-y3)/y3))/len(y3)*100
print(mape)

#cengindex = 0
#for wi in clf.coefs_:
    #cengindex += 1  # 表示底第几层神经网络。
    #print('第%d层网络层:' % cengindex)
    #print('权重矩阵维度:',wi.shape)
    #print('系数矩阵：\n',wi)
	
clf = MLPRegressor()
clf.fit(x2, y2)

y_predprob_test = clf.predict(x3)
mape = sum(np.abs((y_predprob_test-y3)/y3))/len(y3)*100
print('the forest test mape is',mape)

y_predprob_training = clf.predict(x2)
mape = sum(np.abs((y_predprob_training-y2)/y2))/len(y2)*100
print('the forest training mape is',mape)

y = y[selectionAll]
y6_cross = cross_val_predict(clf, X, y, cv = 5)
y6_cross = y6_cross[selection2]
mape = sum(np.abs((y6_cross-y3)/y3))/len(y3)*100
print(mape)