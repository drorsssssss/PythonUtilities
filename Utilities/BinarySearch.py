import pytest
''' Binary Search Implementation '''

def BS(lst,num):
    try:
        middle=int(len(lst)/2)

        if len(lst) == 0:
            return False

        if lst[middle]==num:
            return True

        if num<=middle:
            return BS(lst[:middle],num)
        else:
            return BS(lst[middle+1:],num)
    except:
        print('An error occurred!')




def test_regular():
    x=[1,2,3,4,5,6,7]
    num=7
    assert BS(x,num)==True

def test_identical():
    x=[1,1,1,1]
    num=1
    assert BS(x,num)==True

def test_not_exist():
    x=[1,2,7,8]
    num=0
    assert BS(x,num)==False

def test_not_valid_lst():
    x=[]
    num=0
    assert BS(x,num)==False

def test_not_valid_input():
    x=[]
    num='a'
    assert BS(x,num)==False

def test_chars():
    x=['a']
    num='a'
    assert BS(x,num)==True

def test_not_valid_lst_type():
    x=['a']
    num=8
    assert BS(x,num)==False

pytest.main(['-rA'])