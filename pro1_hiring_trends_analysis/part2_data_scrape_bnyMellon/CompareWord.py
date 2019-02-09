import csv

data = open('WMdata.csv')
word = open('word1.csv')

dataReader = csv.reader(data)
wordReader = csv.reader(word)

wordDic = {}
'''for d in dataReader:
    print(d[3])
    '''

store = ""
for d in dataReader:
    #print(d)
    store += ' '.join(d)

#print(store)
for w in wordReader:
    wordDic[w[0]] =(int)(store.count(w[0])/2)
finalWord = sorted(wordDic.items(),key=lambda item:item[1],reverse=True)
print(finalWord)
data.close()
word.close()

count = open('WM1.csv','w')
writer = csv.writer(count)
writer.writerow(finalWord)

