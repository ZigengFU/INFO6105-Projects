import requests,re
import pandas as pd
import time
import urllib
from bs4 import BeautifulSoup
import csv
import os
import numpy as np

def getIndexPageLinks(page):
    try:
        # kv = {'user-agent': 'Mozilla/5.0'}
        kv = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        url = 'https://www.capitalonecareers.com/search-jobs/results?'
        data = {
            'ActiveFacetID': 0,
            'CurrentPage': page,
            'RecordsPerPage': 15,
            'Distance': 50,
            'RadiusUnitType': 0,
            'Keywords': '',
            'Location': '',
            'Latitude': '',
            'Longitude': '',
            'ShowRadius': False,
            'CustomFacetName': '',
            'FacetTerm': '',
            'FacetType': 0,
            'SearchResultsModuleName': 'Search+Results',
            'SearchFiltersModuleName': 'Search+Filters',
            'SortCriteria': 0,
            'SortDirection': 1,
            'SearchType': 5,
            'CategoryFacetTerm': '',
            'CategoryFacetType': '',
            'LocationFacetTerm': '',
            'LocationFacetType': '',
            'KeywordType': '',
            'LocationType': '',
            'LocationPath': '',
            'OrganizationIds': '',
            'PostalCode': '',
            'fc': '',
            'fl': '',
            'fcf': '',
            'afc': '',
            'afl': '',
            'afcf': ''
        }
        url_data = urllib.parse.urlencode(data)
        url_data = urllib.parse.unquote(url_data)
        r = requests.get(url, headers=kv, params=url_data)


        r.raise_for_status()
        return r.text.encode('utf-8').decode('unicode-escape')
    except:
        print('404 error!')
        return(' ')

def getPerJobHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,'lxml')
        tag = soup.findAll('section')[0]
        return tag.text

    except:
        print('404 error!')
        return(' ')

def getPerJobHTMLTitle(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,'lxml')
        tag = soup.findAll('h1')[0]
        return tag.text
    except:
        print('404 error!')
        return(' ')

# def getPerJobHTMLLocation(url):
#     try:
#         kv = {'user-agent': 'Mozilla/5.0'}
#         r = requests.get(url, headers=kv)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         soup = BeautifulSoup(r.text,'lxml')
#         tag = soup.findAll("span", class_="job-info")[2]
#
#         location=re.split('\s',tag.text)
#         location.remove('Location')
#         return "".join(location)
#     except:
#         print('404 error!')
#         return(' ')



def getUrlsFromIndexPage(html):
    time.sleep(2)
    pattern = re.compile(r'/job\S*')
    p = re.findall(pattern, html)
    # if p:
    #     return p
    # return 'N'
    joblinks=[]
    for jobLink in p:
        joblinks.append('https://www.capitalonecareers.com'+jobLink[0:-1])
    return joblinks


def readFromCSV(csvFile):
    obj = []
    csv_reader = csv.reader(open(csvFile))
    for row in csv_reader:
        if(len(row)!=0):
            obj.append(row[1])
    return obj[0:100]


def countWordsFreq(content,csvFile):
    # a specific job position's page
    count = []
    # keywords = readFromCSV('/Users/ziyanzhu/PycharmProjects/Top Key Words Lists/m3_top_100_key_words.csv')
    keywords = readFromCSV(csvFile)
    for keyword in keywords:
        num = len(re.findall(keyword, content, re.IGNORECASE))
        if(num==0):
            count.append(0)
        else:
            count.append(num)
    return count

def grabAllJobTxt(page):
    file1 = open('/Users/ziyanzhu/PycharmProjects/capitalOneJobInfo.txt','w')
    file2 = open('/Users/ziyanzhu/PycharmProjects/capitalOneJobTitle.txt','w')
    file3 = open('/Users/ziyanzhu/PycharmProjects/capitalOneJobUrls.txt','w')

    for page in range(page):
        pageContent=getIndexPageLinks(page + 1)
        joblinksPerPage = getUrlsFromIndexPage(pageContent)
        if ((page + 1) % 5 == 0):
            print(page + 1)
        for joblink in joblinksPerPage:
            jobInfo=getPerJobHTMLText(joblink)
            jobTitle=getPerJobHTMLTitle(joblink)
            file1.write(jobInfo)
            file1.write('*****')
            file2.writelines(jobTitle)
            file2.write('*****')
            file3.writelines(joblink)
            file3.write('*****')
    file1.close()
    file2.close()
    file3.close()

    # printCsv(sinfo)



def readTxt(txt):
    file=open(txt)
    content = re.split(r'\*{5}',file.read())
    content.remove('')
    return content

def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            yield  file

def combineInfoToCsv():
    writePath ="/Users/ziyanzhu/PycharmProjects/capitalOne.csv"
    path = "/Users/ziyanzhu/PycharmProjects/Top Key Words Lists"
    out = open(writePath,'a', newline='')
    csv_write = csv.writer(out,dialect='excel')
    jobContent = readTxt('/Users/ziyanzhu/PycharmProjects/capitalOneJobInfo.txt')
    jobTitle = readTxt('/Users/ziyanzhu/PycharmProjects/capitalOneJobTitle.txt')
    jobUrl = readTxt('/Users/ziyanzhu/PycharmProjects/capitalOneJobUrls.txt')
    # jobLocation = readTxt('/Users/ziyanzhu/PycharmProjects/capitalOneJobLocation.txt')
    totalNumber = len(jobTitle)
    key=[]
    key.append('job no')
    key.append('job title')
    # key.append('job location')
    key.append('institution')
    key.append('URL')
    # key.append('list id')
    # key.append('extraction method')
    for j in range(100):
        key.append(j+1)
    csv_write.writerow(key)

    for i in range(totalNumber):
            # for fileName in file_name(path):
                    l = []
                    # listNumber = re.split('_', fileName)[0][-1]
                    # if listNumber == '1':
                    #     countmethod = 'wordcount'
                    # elif listNumber == '2':
                    #     countmethod = 'TF/IDF'
                    # else:
                    #     countmethod = 'TextRank'
                    fileName = 'overall_top_100_key_words.csv'
                    l.append(i)
                    count=countWordsFreq(jobContent[i],path+'/'+fileName)
                    l.append(jobTitle[i])
                    # l.append(jobLocation[i])
                    l.append('capitalOne')
                    l.append(jobUrl[i])
                    # l.append(listNumber)
                    # l.append(countmethod)
                    for keywordId in range(100):
                        l.append(count[keywordId])
                    csv_write.writerow(l)





def main():
    # 1.uncomment grabAllJobTxt and comment combineInfoToCsv to get two texts. One contains job description details, the other contains job titles
    #2.comment grabAllJobTxt and uncomment combineInfoToCsv, the purpose is to transform all information into a csv file.
    # grab 50 page of jobs
    # grabAllJobTxt(155)
    # make csv
    combineInfoToCsv()




main()