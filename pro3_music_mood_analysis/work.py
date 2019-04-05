#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.externals import joblib
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.layers.merge import concatenate
from keras.models import Sequential, Model
from keras.layers import Dense, Embedding, Activation, merge, Input, Lambda, Reshape
from keras.layers import Convolution1D, Flatten, Dropout, MaxPool1D, GlobalAveragePooling1D
from keras.layers import LSTM, GRU, TimeDistributed, Bidirectional
from keras.utils.np_utils import to_categorical
from keras import initializers
from keras import backend as K
from keras.engine.topology import Layer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import csv

aim_d = {}
che = open('test.csv','r')
aim = csv.reader(che)
for line1 in aim:
	for s1 in line1:
		aim_d[s1] = 1;


loan_data = pd.read_csv('train_lyrics_1000.csv',error_bad_lines=False,encoding = "utf-8")

data_array = np.array(loan_data)

x = []
y = []
for line in data_array:
	tmpline = line[0].split(' ');
	tmpline2 = []
	for s in tmpline:
		if s.lower() not in aim_d:
			tmpline2.append(s)
	x.append(tmpline2)
	
	tmpline = []
	if line[1] == 'happy':
		tmpline.append(1);
		tmpline.append(0);
	else:
		tmpline.append(0);
		tmpline.append(1);
	y.append(tmpline)

# 划分训练/测试集

# X: 歌词 Y：结果（Happy/Sad）
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

tokenizer = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',lower=True,split=" ")
tokenizer.fit_on_texts(x)
vocab = tokenizer.word_index

# 将每个词用词典中的数值代替
X_train_word_ids = tokenizer.texts_to_sequences(X_train)
X_test_word_ids = tokenizer.texts_to_sequences(X_test)

# One-hot
x_train = tokenizer.sequences_to_matrix(X_train_word_ids, mode='binary')
x_test = tokenizer.sequences_to_matrix(X_test_word_ids, mode='binary')

model = Sequential()
# 全连接层
model.add(Dense(512, input_shape=(len(vocab)+1,), activation='relu'))
# DropOut层
model.add(Dropout(0.5))
# 全连接层+分类器
print(y_train)
model.add(Dense(2,activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
			  
x_train = np.array(x_train)
y_train = np.array(y_train)			  
x_test = np.array(x_test)
y_test = np.array(y_test)	
# 训练集实际结果
print(y_train)
# 测试集实际结果
print(y_test)
model.fit(x_train, y_train,
          batch_size=32,
          epochs=3,
          validation_data=(x_test, y_test))
# 训练集预测结果
print(model.predict(x_train)) 
# 测试集预测结果
print(model.predict(x_test))  
joblib.dump(model, 'train_model.m')