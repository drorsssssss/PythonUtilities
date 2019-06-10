import string
import pytest

def countUnique(sentence):
    if sentence:
        sentence=str(sentence)
        temp_lst = sentence.translate(sentence.maketrans("","",string.punctuation)).strip()
        res_unique_set=set(temp_lst.split())
        return len(res_unique_set)
    else:
        return 0



def test_simple():
    sentence='dror sivan shalom sivan'
    assert countUnique(sentence) == 3

def test_none():
    sentence=None
    assert countUnique(sentence) == 0

def test_empty():
    sentence=''
    assert countUnique(sentence) == 0

def test_same_char():
    sentence='aaaa'
    assert countUnique(sentence) == 1

def test_same_word():
    sentence='aaaa aaaa aaaa'
    assert countUnique(sentence) == 1

def test_resemble_word():
    sentence='aaaa aaaa aaa'
    assert countUnique(sentence) == 2

def test_numeric_input():
    sentence=5
    assert countUnique(sentence) == 1


pytest.main(['-rA'])