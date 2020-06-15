import nltk
import numpy as np
import random
import string

#read corpus.txt
f = open('chatbot.txt', 'r', errors = 'ignore')

raw = f.read()
#converts to lower case
raw = raw.lower()

#convert entire corpus into list of sentences and words
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

print(sent_tokens[:2])
print(word_tokens[:2])
