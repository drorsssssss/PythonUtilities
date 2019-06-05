import pytest

''' Count digits util '''
def countDigits(num):
    cnt=0
    while num / 10 !=0:
        cnt+=1
        num=int(num/10)
    return cnt

''' Sum digits util '''
def sumDigits(num):
    sum=0
    while num / 10 !=0:
        sum+=num%10
        num=int(num/10)
    return sum

def test_countdigits():
    assert countDigits(35678)==5


def test_sumdigits():
    assert sumDigits(546)==15

pytest.main(['-rA'])
