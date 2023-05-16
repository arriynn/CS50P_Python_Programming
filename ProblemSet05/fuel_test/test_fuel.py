from fuel import convert
from fuel import gauge 
def test_gauge():
    assert gauge(100)== "F"
    assert gauge(0)== "E"
def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4")== 0