from summa import summarizer
from summa import keywords
import csv
import string

text = ''
c = open('BNY Mellon New.csv','r')
read = csv.reader(c)


Chart1CsvFile = open('chartData.csv','w')
writer = csv.writer(Chart1CsvFile)

Chart1CsvFile2 = open('chartData2.csv','w')
writer2 = csv.writer(Chart1CsvFile2)

dict = {}
dict2 = {}
for line in read:
	ci = 0
	for s in line:
		ci = ci + 1;
		if ci == 3:
			careers = s
			print(s)
		
		if s[0] == '(':
			s = s[2:-1]
			temps = s.split(',')
			temps[0] = temps[0][:-1]
			
			print(temps[0] + "    " + temps[1])
			
			if temps[0] in dict:
				dict[temps[0]] = dict[temps[0]] + float(temps[1])
			else:
				dict[temps[0]] = float(temps[1])
			tmpdics =  temps[0] + ' ' + careers 
			print(tmpdics)
			if tmpdics in dict2:
				dict2[tmpdics] = dict2[tmpdics] + float(temps[1])
			else:
				dict2[tmpdics] = float(temps[1])


				
for x in dict2.keys():
	writer2.writerow([x,dict2[x]])
	
for x in dict.keys():
	writer.writerow([x,dict[x]])


