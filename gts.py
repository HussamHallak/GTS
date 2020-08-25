# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:38:06 2020

@author: Hussam Hallak
"""


from boilerpy3 import extractors
from googletrans import Translator
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os

def printArray(array, array_name):
    print (array_name + ":" + "\n" + "--------------")
    for item in array:
        print (item)
        ar_item = translator.translate(item, src='en', dest='ar')
        print (ar_item.text)

java_path = "C:\Program Files (x86)\Java\jre1.8.0_251/java.exe"
os.environ['JAVAHOME'] = java_path

st = StanfordNERTagger(r'stanford-ner-4.0.0/stanford-ner-4.0.0/classifiers/english.all.3class.distsim.crf.ser.gz',
					   r'stanford-ner-4.0.0/stanford-ner-4.0.0/stanford-ner.jar',
					   encoding='utf-8')

extractor = extractors.ArticleExtractor()

# From a URL
content = extractor.get_content_from_url('https://www.alarabiya.net/ar/culture-and-art/2020/08/19/%D9%85%D9%81%D8%A7%D8%AC%D8%A3%D8%A9-%D8%B9%D9%85%D8%B1%D9%88-%D8%AF%D9%8A%D8%A7%D8%A8-%D9%8A%D8%B9%D9%88%D8%AF-%D9%84%D9%84%D8%AA%D9%85%D8%AB%D9%8A%D9%84-%D9%85%D8%B9-%D9%86%D8%AA%D9%81%D9%84%D9%8A%D9%83%D8%B3-%D8%A8%D8%B9%D8%AF-%D8%A7%D9%86%D9%82%D8%B7%D8%A7%D8%B9-27-%D8%B9%D8%A7%D9%85%D8%A7.html')

#print (content)

translator = Translator()

output = translator.translate(content)

translated_content = output.text

#print (translated_content)

tokenized_text = word_tokenize(translated_content)
classified_text = st.tag(tokenized_text)

#print(type(classified_text))

locations = []
persons = []
organizations = []

for word in classified_text:
    if word[1] == "LOCATION":
        locations.append(word[0])
    if word[1] == "PERSON":
        persons.append(word[0])
    if word[1] == "ORGANIZATION":
        organizations.append(word[0])


printArray(locations, "Locations")
printArray(organizations, "Organizations")
printArray(persons, "Persons")