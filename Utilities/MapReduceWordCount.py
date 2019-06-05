''' MapReduce program for counting words '''
import string
from collections import defaultdict

def _reducer(series):
    res=defaultdict(int)
    for i in series:
        res[i[0]]+=1
    return res

def wordCount(sen):

    sen=sen.strip()
    sen=sen.translate(sen.maketrans("","",string.punctuation))

    word_list = sen.split(" ")
    word_list_map = list(map(lambda x:(x,1),word_list))
    return _reducer(word_list_map)




