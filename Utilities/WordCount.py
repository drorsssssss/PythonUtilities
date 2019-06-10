import string
import re
import pytest

def countWords(words):
    temp_words = str(words).strip()
    temp_words = temp_words.translate(temp_words.maketrans("","",string.punctuation))
    temp_lst_words_ln = temp_words.split()
    return len(temp_lst_words_ln)



def countWordsEff(words):
    if words:

        temp_words = words.translate(words.maketrans("","",string.punctuation))
        temp_words = temp_words.strip()
        temp_words=re.sub(' +',' ',temp_words)
        cnt=0
        for i in range(len(temp_words)):
            if temp_words[i]==' ':
                cnt+=1

        return cnt+1 if cnt != 0 else 0
    else:
        return 0


def test_simple():
    x='dror sivan test'
    assert countWordsEff(x)==3


def test_none():
    x=None
    assert countWordsEff(x)==0

def test_empty():
    x=''
    assert countWordsEff(x)==0

def test_n_empty():
    x='    '
    assert countWordsEff(x)==0

def test_punctuation():
    x='dror sivan !'
    assert countWordsEff(x)==2

def test_n_punctuation():
    x=' !dror s dd!d @ '
    assert countWordsEff(x)==3

pytest.main(['-rA'])    