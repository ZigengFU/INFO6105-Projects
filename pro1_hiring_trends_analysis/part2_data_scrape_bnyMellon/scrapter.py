from bs4 import BeautifulSoup
import requests
import csv
'''
sourceContainer = requests.get('https://jobs.bnymellon.com/jobs?page=1').text
soupSource = BeautifulSoup(sourceContainer,'lxml')

jobResults = soupSource.find('div',class_= "snap-content")
jobList = jobResults.findAll('a')
print(jobList)
'''

csvFile =open("URL.csv","r")
reader = csv.reader(csvFile)
url = 
for item in reader:
    if reader.line_num == 1:
        continue
    url.append(item1)

csvFile.close()
#print(url0)
# for single page

data = 0,'0','0','0'

csvFile1  = open("BNYJobData.csv","w")
writer = csv.writer(csvFile1)
i=0
for page in url:
    source = requests.get(page).text

    soup = BeautifulSoup(source,'lxml')

#print(soup.prettify())

    jobInfoContainer = soup.find('div',class_="jibe-job-info-container")
#print(jobInfoContainer.prettify())
    title = jobInfoContainer.find('h1',class_="job-title").text
    location = jobInfoContainer.find('div',class_="job-location job-categories").text
    jobDescription = jobInfoContainer.find('div',class_="jibe-job-description job-description").text
    data0 = i
    data1 = title
    data2 = location
    data3 = jobDescription
    writer.writerow(data)
    i = i+1
    print("write page",i)
csvFile1.close()
    #print(jobDescription)
    #print("Next Job")

