#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sklearn.externals import joblib
from keras.preprocessing.text import Tokenizer
import keras
import pandas as pd
import numpy as np
import csv
	
def predict_work(str):
	keras.backend.clear_session()
	aim_d = {}
	che = open('test.csv','r')
	aim = csv.reader(che)
	for line1 in aim:
		for s1 in line1:
			aim_d[s1] = 1;
	
	loan_data = pd.read_csv('train_lyrics_1000.csv',error_bad_lines=False,encoding = "utf-8")
	data_array = np.array(loan_data)

	x = []
	for line in data_array:
		tmpline = line[0].split(' ');
		tmpline2 = []
		for s in tmpline:
			if s.lower() not in aim_d:
				tmpline2.append(s)
		x.append(tmpline2)
	
	x_pre_work = []	
	tmpline = str.split(' ')
	#tmpline = tmpline[:min(len(tmpline), 20000)]
	tmpline2 = []
	for s in tmpline:
		if s.lower() not in aim_d:
			tmpline2.append(s)
	
	x_pre_work.append(tmpline2)	

	tokenizer = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n',lower=True,split=" ")
	tokenizer.fit_on_texts(x)
	vocab = tokenizer.word_index
	# 将每个词用词典中的数值代替
	X_pre_word_ids = tokenizer.texts_to_sequences(x_pre_work)

	# One-hot
	x_pre = tokenizer.sequences_to_matrix(X_pre_word_ids, mode='binary')
	
	model = joblib.load('train_model.m')

	x_pre = np.array(x_pre)
	y_pre = model.predict(x_pre)
	che.close()

	return y_pre[0][0],y_pre[0][1]