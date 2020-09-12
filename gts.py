#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from boilerpy3 import extractors
from googletrans import Translator
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os
import sys
import requests

if len(sys.argv) != 2:
    print ("Usage: Python gts.py <url>")
    print ("e.g: python gts.py http://example.com")
    sys.exit()
else:
    url = sys.argv[1]
    request = requests.get(url)
    if request.status_code != 200:
        print ("This URL did not return a status code of 200. Try a different URL.")
        print ("Status Code:" + str(request.status_code))
        exit()

def printArray(array, array_name):
    print (array_name + ":" + "\n" + "--------------")
    for item in array:
        print (item)
        ar_item = translator.translate(item, src='en', dest='ar')
        print (ar_item.text)

st = StanfordNERTagger(r'stanford-ner-4.0.0/classifiers/english.all.3class.distsim.crf.ser.gz',
					   r'stanford-ner-4.0.0/stanford-ner.jar',
					   encoding='utf-8')

extractor = extractors.ArticleExtractor()

# From a URL
content = extractor.get_content_from_url(url)

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
