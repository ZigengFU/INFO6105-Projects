import csv
import re

import extract_text_from_pdf as ext
from summa import keywords
from summa import summarizer

# extracting text from PDF and storing them into a string
pdf = "f0_combined_file.pdf"
text = ext.convert_pdf_to_txt(pdf)
# removing special characters from texts
text = re.sub(r"[^a-zA-Z,.\"\']", ' ', text).lower()
text = re.sub(r"[\n\t\s]+", ' ', text)
print(text)
print("\n\n\n")

ansCsvFile = open('m3_top_100_key_words.csv','w')
writer = csv.writer(ansCsvFile)

# # summarizing the texts
# summa_text = summarizer.summarize(text)
# print(summa_text)

# extracting keywords from summarized texts
ans = keywords.keywords(text)
print(ans)

# writing results into csv file
str = ''
wcnt = 0
for s in ans:
	if s != '\n':
		str = str+s
	else:
		writer.writerow([wcnt+1, str])
		str = ''
		wcnt = wcnt + 1
		if wcnt == 400:
			break
