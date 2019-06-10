import pytest

def subStrCount(input_str,sub_str):
    cnt=0
    if input_str:
        for i in range(len(input_str)):

            if input_str[i]!=sub_str[0]: #Edge case for sub_str
                continue

            if i+len(sub_str)-1>len(input_str):
                continue

            if input_str[i:i+len(sub_str)]==sub_str:
                cnt+=1
        return cnt

    else:
        return 0


def test_simple():
    input_str='abcdcfcdc'
    sub_str='cdc'
    assert subStrCount(input_str,sub_str) == 2



def test_none():
    input_str=''
    sub_str='cdc'
    assert subStrCount(input_str,sub_str) == 0

def test_empty_inputs():
    input_str=''
    sub_str=''
    assert subStrCount(input_str,sub_str) == 0

def test_simple():
    input_str=None
    sub_str=None
    assert subStrCount(input_str,sub_str) == 0


def test_n_times():
    input_str='aaaaaaa'
    sub_str='aaaaaaa'
    assert subStrCount(input_str,sub_str) == 1


pytest.main(['-rA'])
