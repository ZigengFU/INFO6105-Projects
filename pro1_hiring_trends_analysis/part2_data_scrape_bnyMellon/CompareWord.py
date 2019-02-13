import csv

data = open('BNYJobdata.csv')
word = open('NewWords.csv')
url = open('URL.csv')
dataReader = csv.reader(data)
wordReader = csv.reader(word)
urlReader = csv.reader(url)

'''
wordDic = {}
for d in dataReader:
    print(d[3])
    

store = ""
for d in dataReader:
    #print(d)
    store += ' '.join(d)

#print(store)
for w in wordReader:
    wordDic[w[1]] =(int)(store.count(w[1])/2)
finalWord = sorted(wordDic.items(),key=lambda item:item[1],reverse=True)
print(finalWord)
'''

JobNumber = 0
JobTitle = []
JobURL = []
count = []
store = ""
text = []
Location = []
words = []
for w in wordReader:
    words.append(w[1])
for dataLine in dataReader:
    JobTitle.append(dataLine[1])
    Location.append(dataLine[2])
    store = ' '.join(dataLine)
    text.append(store)

for i in range(0,1317):
    JobTitle[i] = JobTitle[i].replace(',',' ')

#print(JobTitle)
for dataLine in dataReader:
    JobTitle.append(dataLine[1])
    store = ' '.join(dataLine)
    text.append(store)
for t in text:
    temp = []
    for w in words:
        temp.append(t.count(w))
    count.append(temp)

for urlLine in urlReader:
    JobURL.append(urlLine[1])


BNY = open('BNYData.csv','w')
writer = csv.writer(BNY)
i=0
temp = ""

for i in range(0,1317):
    EveryLine = str(JobNumber) + ',' +JobTitle[i]+ ','+"BNY Mellon" + ',' + JobURL[i]+ ',' + str(count[i])
    print(EveryLine)
    #writer.writerow(JobTitle[i], url[i], count[i])
    JobNumber = JobNumber + 1



'''
i = 0;
for dataTemp in dataReader:
    #store = ' '.join(d)
    print(dataTemp)
    #count.append(store.count(words[i]))
    #i = i+1

print(count)
print(words)
print(JobURL)
print(len(JobTitle))
'''
data.close()
word.close()
url.close()
#count = open('WM3.csv','w')
#writer = csv.writer(count)
#writer.writerow(finalWord)

