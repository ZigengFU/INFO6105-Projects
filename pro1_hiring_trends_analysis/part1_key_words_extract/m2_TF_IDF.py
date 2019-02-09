import csv
import math
from decimal import Decimal

dict_list = [{},{},{},{}]#store word in every file

c = open('cleaned_text_combined_file.csv', 'r')
read = csv.reader(c)

ansCsvFile = open('m2_top_100_key_words.csv', 'w')
writer = csv.writer(ansCsvFile)

for i in range(0, 4):
    print(i)
    tmpFile = open('cleaned_text_file_' + str(i + 1) + '.csv', 'r')
    tmpFileRead = csv.reader(tmpFile)
    for line in tmpFileRead:
        for s in line:
            dict_list[i][s] = 1;

d_file = {}  # how many files have some word
aim_d = {}  # skip the stop word
d = {}  # the times a words has appear

for line in read:
    for s in line:
        flag = 0
        if s == '':
            continue
        for ch in s:
            if ch < 'a' or ch > 'z':
                flag = 1
                break
        if flag == 0:
            if s in d:
                d[s] = d[s] + 1
            else:
                d[s] = 1
            if s in d_file:
                continue
            else:
                count_file = 0
                for i in range(0, 4):
                    if s in dict_list[i]:
                        count_file = count_file + 1
                if count_file == 0:
                    print(s)
                d_file[s] = Decimal(math.log(4 / count_file + 1))
tot_words = 0

for key in d.keys():
    tot_words = tot_words + d[key]

work_d = {}

for key in d.keys():
    work_d[key] = (d[key] / tot_words) * d_file[key]

temp = sorted(work_d.items(), key=lambda x: x[1], reverse=True)
i = 0;

writer.writerow(['words', 'counts'])

for key in temp:
    if i == 200:
        break
    writer.writerow([key[0], key[1], d_file[key[0]]])
    i = i + 1
