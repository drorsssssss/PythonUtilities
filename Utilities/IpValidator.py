import pytest

def isValidIp(ip):
    ip_lst=str(ip).split(".")
    if len(ip_lst) != 4:
        return False
    for dig in ip_lst:
        if dig.isalpha() or (int(dig) <0 or int(dig) >255):
            return False
    return True


def test_ip():
    print("Test valid ip: 100.0.5.198")
    assert isValidIp('100.0.5.198') == True

def test_invalid_ip():
    print("Test invalid ip: a.0.5.198")
    assert isValidIp('a.0.5.198') == False

def test_invalid_ip_out_range():
    print("Test invalid ip (out range): 0.0.5.256")
    assert isValidIp('a.0.5.198') == False

def test_invalid_ip_none():
    print("Test None ip")
    assert isValidIp('') == False

def test_invalid_ip_int():
    print("Test Int input")
    assert isValidIp(100) == False

pytest.main(['-rA'])    