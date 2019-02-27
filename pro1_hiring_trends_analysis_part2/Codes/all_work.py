from __future__ import division
from sklearn.linear_model import LogisticRegression as LR
import csv
import random
import numpy as np
import pandas as pd

c = open('TeamAllClean.csv','r')

#TeamAllClean.csv 格式：100列*job行，每行为每个关键词在job description里出现的次数

read = csv.reader(c)

c2 = open('cluster.csv','w')
writer = csv.writer(c2,lineterminator='\n')


#cluster.csv 输出八个聚类

data = [[0 for i in range(100)] for i in range(30000)]

ci = 0


K = 10
for line in read:
	for i in range(100):
		data[ci][i] = int(line[i])
	ci = ci + 1
	print(ci)


L = ci

aim_point = [[0 for i in range(100)] for i in range(K)]
tmp_aim_point = [[0 for i in range(100)] for i in range(K)]

for i in range(L):
	x = random.randint(i,L)
	t = data[i]
	data[i] = data[x]
	data[x] = t

for i in range(K):
	aim_point[i] = data[i]



#while True:


for loopTime in range(30):
	data_cala = []
	print(loopTime)
	tmp_aim_point = [[0 for i in range(100)] for i in range(K)]
	num = [0 for i in range(K)]
	for i in range(L):
		data_cala.append(0)
		minf = 2000000000
		color = -1
		for j in range(K):
			dict = 0
			for kk in range(100):
				dict = dict + (data[i][kk] - aim_point[j][kk])*(data[i][kk] - aim_point[j][kk])
			if dict < minf:
				minf = dict
				color = j	
				data_cala[i] = j
		num[color] = num[color] + 1
		for j in range(100):
			tmp_aim_point[color][j] = tmp_aim_point[color][j] + data[i][j]
	if loopTime == 49:
		break
	for i in range(K):
		if num[i] == 0:
			continue
		for j in range(100):
			aim_point[i][j] = int(tmp_aim_point[i][j] / num[i])
	print(aim_point)

tot_no_fintech = 0

for i in range(L):	
	if data[i][31] != 0:
		aim_point[data_cala[i]][31] = aim_point[data_cala[i]][31] + 1
		
for i in range(K):
	if num[i]!=0:
		writer.writerow(aim_point[i])

#getfeature

c_feature_out = open('feature.csv','w')
writerCFO = csv.writer(c_feature_out,lineterminator='\n')

#feature.csv 提取的特征值单词，和在原key_word_list中的位置

c_keywords = open('top_100_key_words_all_teams.csv','r')
readCK = csv.reader(c_keywords)

flag = [0 for i in range(100)]

for i in range(K):
	for j in range(100):
		if aim_point[i][j] > 2: 
			flag[j] = 1

cnt = 0

for line in readCK:
	if flag[cnt] == 1:
		writerCFO.writerow(line)
	cnt = cnt + 1
	

#######################
c3 = open('TeamAllClean.csv','r')
readc3 = csv.reader(c3)

ans1CsvFile = open('fintech_data_used.csv','w')
writerans1 = csv.writer(ans1CsvFile,lineterminator='\n')

labeled_data=[]

for i in range(L):
	linetmp = []
	for j in range(100):
		if flag[j]:
			linetmp.append(data[i][j])
	if aim_point[data_cala[i]][31] > 10:
		linetmp.append(1)
	else:
		linetmp.append(0)
		tot_no_fintech = tot_no_fintech + 1
	labeled_data.append(linetmp)

labeled_data_array = np.array(labeled_data)

#labeled_data_array[np.lexsort(labeled_data_array.T)]

outputCi = 0
for line in labeled_data_array:
	linetmp = []
	linetmp.append(outputCi)
	linetmp.extend(line)
	linetmp.append(data_cala[outputCi])
	writerans1.writerow(linetmp)
	outputCi = outputCi + 1

labeled_data_array = labeled_data_array[np.lexsort(labeled_data_array.T)]

#machine learning

x =labeled_data_array[:,:cnt]
selection = [v for v in range(len(x)) if v % 20 == 0]
selection2 = [v for v in range(len(x)) if v% 20 != 0]
x2 = x[selection,:]
x3 = x[selection2,:]

y = labeled_data_array[:,-1:]
y2 = y[selection,:]
y3 = y[selection2,:]

print(x2)
print(y2)

lr = LR()
lr.fit(x2,y2)

y22 = lr.predict(x2)


print(u'模型的平均准确率（训练集）为：%s'% lr.score(x2, y2));

y23 = lr.predict(x3)

print(y23)

print(u'模型的平均准确率（训练集）为：%s'% lr.score(x3, y3));

print(lr.coef_)

#y = lr.predict(x) y为预测结果
#单组预测数据格式应为csv表，1行*39列

print(tot_no_fintech)