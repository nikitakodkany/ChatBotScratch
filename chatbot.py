#libraries
import io
import nltk
import random
import string
import warnings
import numpy as np
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

warnings.filterwarnings('ignore')


#read corpus.txt
with open('chatbot.txt', 'r', encoding='utf8', errors = 'ignore') as fin:
    raw = fin.read().lower()



#Tokenization
#convert entire corpus into list of sentences and words
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)


# print(sent_tokens[:2])
# print(word_tokens[:2])



#Prepocessing
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



#keyword matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there!", "hello", "I am glad!"]

def greeting(sentence):
    if word.lower() in GREETING_INPUTS:
        return random.choice(GREETING_RESPONSES)



#generating response
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

flag=True
print("PINTO: My name is Pinto. I will answer your queries about Chatbots. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("PINTO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("PINTO: "+greeting(user_response))
            else:
                print("PINTO: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("PINTO: Bye! take care..")    
