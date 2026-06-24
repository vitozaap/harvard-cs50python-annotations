from numb3rs import validate


def test_range():
    assert validate("255.255.255.255") == True
    assert validate("256.0.0.0") == False



def test_dots():
    assert validate("255..255.255.255") == False
    assert validate("255255.255.255") == False


def test_format():
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.1") == False


def test_common_ips():
    assert validate("127.0.0.1") == True
    assert validate("192.168.0.1") == True
    assert validate("10.0.0.1") == True

def test_bytes_validation():
    assert validate("192.256.256.256") == False
