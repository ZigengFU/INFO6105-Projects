import csv
from collections import Counter
import wordcount

# use Counter of collections to get the words and their frequencies
with open('cleaned_text_combined_file.csv', 'r') as f:
    wordcount = Counter(f.read().split(','))

# sort the items in the dictionary by reverse order of the values
# return a list of tuples
sorted_by_value = sorted(wordcount.items(), key=lambda kv: kv[1])
sorted_by_value.reverse()

# write the sorted data into csv file
with open('m1_sorted_text.csv','wb') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['WORD','FREQ'])
    for row in sorted_by_value:
        csv_out.writerow(row)