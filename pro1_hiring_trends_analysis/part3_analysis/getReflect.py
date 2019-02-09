from summa import summarizer
from summa import keywords
import csv
import string

text = ''
c1 = open('chartData.csv','r')
read1 = csv.reader(c1)

Chart1CsvFile2 = open('chartData2.csv','r')
read2 = csv.reader(Chart1CsvFile2)


Chart1CsvFile = open('chartReflect.csv','w')
writer = csv.writer(Chart1CsvFile)


dict = {}
dict2 = {}

keyw = []

for line in read1:
	dict[line[0]] = 1
	print(line[0])

for line in read2:
	temps = line[0].split(' ')
	print(temps)
	if temps[0] in dict:
		writer.writerow(line)


