import string
from collections import defaultdict
import pytest

''' Print highest member in sentence '''

x="dror sivan were here last summer, dror shalom were".strip()

def getHighestOccur(str):
    res=defaultdict(int)

    clean_str = str.translate(x.maketrans("","",string.punctuation))
    lst = clean_str.split(" ")
    for i in lst:
        res[i]+=1


    max_member = max(res.items(),key=lambda x:x[1])
    return max_member



def test_getHighestOccur():
    test_str = "dror dror sivan"

    assert getHighestOccur(test_str) == ('dror',2)


def test_getHighestOccur_none():
    test_str = ""

    assert getHighestOccur(test_str) == ('',1)

def test_getHighestOccur_diff():
    test_str = "aaa bb cc !! dd rrrrrrr rrrrrrr rrrrrrr rrrrrrr h h h"

    assert getHighestOccur(test_str) == ('rrrrrrr',4)



pytest.main(['-rA'])


    