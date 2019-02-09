import csv

dict = {}

for i in range(1,4):
	print(i)
	c = open('m'+str(i)+'_top_100_key_words.csv','r')
	read = csv.reader(c)
	for line in read:
		#print(line[0]+'    ' +line[1])
		if line[1] in dict:
			dict[line[1]] = dict[line[1]] + int(line[0])
		else:
			dict[line[1]] = int(line[0])

temp = sorted(dict.items(), key=lambda x: x[1], reverse=False)

w = open("word_show.csv",'w')
writer = csv.writer(w)

ci = 0
for x in temp:
	for i in range(temp[60 - ci][1]):
		writer.writerow([x[0]])
	ci = ci + 1
	if ci == 60:
		break
	

