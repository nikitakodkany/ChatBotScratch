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

# print(sent_tokens[:2])
# print(word_tokens[:2])


lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a symantically-oriented dictionary of English included in nltk

#input tokens, output normalized tokens
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

#storing all punctions with its unicode in dictionary
remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)

#punctuation removal
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there!", "hello", "I am glad!"]

def greeting(sentence):
    if word.lower() in GREETING_INPUTS:
        return random.choice(GREETING_RESPONSES)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robo_response = input()
    user_response = user_response.lower()
    if(user_response!='bye'):
        if(user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print("PINTO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("PINTO: "+greeting(user_response))
            else:
                print("PINTO: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag = False
        print("PINTO: Bye! take care..")
