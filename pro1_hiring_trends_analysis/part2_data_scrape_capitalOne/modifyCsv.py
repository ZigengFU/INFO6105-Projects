# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:09:17 2019

@author: 96984
"""

import csv
import re
import os

def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:
            yield  file
            
            
if __name__ == '__main__':
    path = "/Users/ziyanzhu/PycharmProjects/capitalOne"
    writePath ="/Users/ziyanzhu/PycharmProjects/capitalOne.csv"
    out = open(writePath,'a', newline='')
    csv_write = csv.writer(out,dialect='excel')
    # csv_write = csv.writer(out)
    for fileName in file_name(path):
        with open(path + "/" +  fileName) as file :
            next(file)
            l = []
            # l.append(0)
            l.append("capitalOne")
            #f1=re.split('/',fileName)[-1]
            f2 = re.split('_', fileName)[0]
            listNumber = re.split('_', fileName)[1][-1]
            if listNumber=='1':
                countmethod = 'wordcount'
            elif listNumber=='2':
                countmethod='TF/IDF'
            else:
                countmethod='TextRank'



            l.append(f2)
            l.append(75)
            l.append(listNumber)
            l.append(countmethod)
            l.append("https://www.capitalonecareers.com/search-jobs")
            for line in file:
                keyWord = line.split(",")[1]
                num = line.split(",")[2].replace("\n", "")
                l.append("(" + "\'" + keyWord + "\'" + ":" + num + ")")
            csv_write.writerow(l)

            
                
               
                