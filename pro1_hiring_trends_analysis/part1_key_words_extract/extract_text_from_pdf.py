# -*- coding: utf-8 -*-
# pip install pdfminer.six
# import pdfminer to extract text from PDF files
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# import regular expression
import re
# import csv tools
import csv

"""
Three steps for extracting the texts from PDF files
Step1: extract texts from a PDF file
Step2: clean the extracted texts, including remove tne stop words and signs, etc.
Step3: save the cleaned texts into a csv file
"""

def textExtract(pdf, output):
    """Step1: extract texts from PDF file"""
    # getting the extracted text and storing them into a string
    extract_txt = convert_pdf_to_txt(pdf)

    """Step2: clean the extracted texts, including remove tne stop words and signs, etc."""
    # removing all non-alphabet words, line breaks, tabs and lower the words
    extract_txt = re.sub(r"[^a-zA-Z]", ' ', extract_txt).lower()
    extract_txt = re.sub(r"[\n\t\s]+", ' ', extract_txt)
    # removing stop words with given stop words list, return a list of String
    #   ref: long stop words list from https://www.ranks.nl/stopwords
    stop_words = read_from_text("stop_words.txt")
    extract_txt = remove_stop_words(extract_txt, stop_words)
    # sorting list of String in alphabet order
    extract_txt.sort()

    """Step3: save the cleaned texts into a csv file"""
    write_to_csv(extract_txt, output)

    print('Extracted texts from ' + pdf + ':\n')
    print(extract_txt)

# extract texts from PDF file, return a String
#   ref: https://www.programcreek.com/python/example/107202/pdfminer.pdfpage.PDFPage.get_pages
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()
    retstr.close()
    return str

# remove stop words in a string, return a list of String
#   ref: https://www.geeksforgeeks.org/removing-stop-words-nltk-python/
def remove_stop_words(string, stop_words):
    word_tokens = word_tokenize(string)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence

# write to csv file using csv writer
def write_to_csv(list, file):
    with open(file, 'wb') as targetFile:
        wr = csv.writer(targetFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        wr.writerow(list)

# read from text file, return a list
def read_from_text(file):
    text_file = open(file, "r")
    lines = text_file.read().split('\n')
    text_file.close()
    return lines