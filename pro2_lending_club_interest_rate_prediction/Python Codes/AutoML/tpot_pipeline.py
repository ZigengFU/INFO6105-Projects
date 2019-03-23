import numpy as np
import pandas as pd
from sklearn.feature_selection import VarianceThreshold
from sklearn.linear_model import LassoLarsCV
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('hashFinishData(1).csv', sep=',', dtype=np.float64)
features = tpot_data.drop('int_rate', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['int_rate'].values, random_state=None)

# Average CV score on the training set was:-5.976467281491371e-20
exported_pipeline = make_pipeline(
    VarianceThreshold(threshold=0.1),
    LassoLarsCV(normalize=False)
)

# exported_pipeline.fit(training_features, training_target)
# results = exported_pipeline.predict(testing_features)
exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
print("score:")
print(exported_pipeline.score(testing_features,testing_target))
# print(results)
# # print(testing_target[400:600])
print("plot column 0-400 results:")
plt.plot(testing_target[0:400])
plt.plot(results[0:400])
plt.show()