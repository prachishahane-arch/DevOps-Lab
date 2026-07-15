from calc import *

def test_add():
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(4, 5) == 20

def test_divide():
    assert divide(20, 4) == 5

def test_divide_zero():
    try:
        divide(10, 0)
    except ValueError:
        assert True