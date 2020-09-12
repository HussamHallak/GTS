#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from boilerpy3 import extractors
from googletrans import Translator
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from collections import Counter
import os
import sys

st = StanfordNERTagger(r'stanford-ner-4.0.0/classifiers/english.all.3class.distsim.crf.ser.gz', r'stanford-ner-4.0.0/stanford-ner.jar', encoding='utf-8')
translator = Translator()
extractor = extractors.ArticleExtractor()

TRACKED_CLASSES = ["LOCATION", "PERSON", "ORGANIZATION"]

def extract(url):

	try:
		content = extractor.get_content_from_url(url)
	except:
		print ("This URL did not return a status code of 200. Try a different URL.")
		return

	output = translator.translate(content)

	translated_content = output.text

	tokenized_text = word_tokenize(translated_content)

	tagged_text = st.tag(tokenized_text)

	dedup_tags = Counter(tagged_text)

	res = {k: [] for k in TRACKED_CLASSES}
	for item, count in dedup_tags.items():
		if item[1] in TRACKED_CLASSES:
			ar_item = translator.translate(item[0], src='en', dest='ar')
			res[item[1]].append((item[0], ar_item.text, count))
	return res

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print ("Usage: Python gts.py <url>")
		print ("e.g: python gts.py http://example.com")
		sys.exit()
	else:
		ext_entities = extract(sys.argv[1])
		if not ext_entities:
			sys.exit()
		for cat in TRACKED_CLASSES:
			print("----------- " + cat + " -------------")
			for e in ext_entities[cat]:
				print(e[0], e[1], e[2])

