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

csvFile =open("WMJob.csv","r")
reader = csv.reader(csvFile)
url = []
for item in reader:
    if reader.line_num == 1:
        continue
    url.append(item[1])

csvFile.close()
#print(url[0])
# for single page

data = [0,'0','0','0']

csvFile1  = open("WMdata.csv","w")
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
    data[0] = i
    data[1] = title
    data[2] = location
    data[3] = jobDescription
    writer.writerow(data)
    i = i+1
    print("write page")
csvFile1.close()
    #print(jobDescription)
    #print("Next Job")

