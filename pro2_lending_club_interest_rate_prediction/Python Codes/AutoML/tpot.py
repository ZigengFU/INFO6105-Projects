import numpy as np
import pandas as pd
from tpot import TPOTRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

# from sklearn.cross_validation import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.preprocessing import PolynomialFeatures


loan_data = pd.read_csv('hashFinishData(1).csv',error_bad_lines=False,encoding = "utf-8")

data_array = np.array(loan_data)

x = data_array[:, 1:data_array.shape[1]]
selection = [v for v in range(len(x)) if v % 5 == 0]
selection2 = [v for v in range(len(x)) if v % 5 != 0]
x2 = x[selection, :]
x3 = x[selection2, :]
y = data_array[:, -1:]
y2 = y[selection, :]
y3 = y[selection2, :]


tpot = TPOTRegressor(generations=10, population_size=100, verbosity=2)
tpot.fit(x2, y2)
print(tpot.score(x3, y3))
tpot.export('test_pipeline_1.py')