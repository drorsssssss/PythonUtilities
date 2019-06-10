''' O(N),  '''

import pytest

from collections import defaultdict

def getFriendsNumDict(friendList):
    if friendList:
        result = defaultdict(lambda: 0)
        for relation in friendList:
            if len(relation)==1:
                result[relation[0]]+=0

            elif relation[0]==relation[1]:
                result[relation[0]]+=0


            else:
                result[relation[0]]+=1
                result[relation[1]]+=1
        return result
    else:
        return None



def test_regular_input():
    input=[['A','B'],['A','C'],['B','D'],['B','C'],['R','M'],['S'],['P'],['A']]
    result={'A': 2, 'B': 3, 'C': 2, 'D': 1, 'R': 1, 'M': 1, 'S': 0, 'P': 0}
    assert getFriendsNumDict(input)==result


def test_none_input():
    input=None
    result=None
    assert getFriendsNumDict(input)==result

def test_singles():
    input=[['A'],['B'],['C']]
    result={'A':0,'B':0,'C':0}
    assert getFriendsNumDict(input)==result


def test_same_friend():
    input=[['A','A'],['B','B']]
    result={'A':0,'B':0}
    assert getFriendsNumDict(input)==result


pytest.main(['-rA'])






        