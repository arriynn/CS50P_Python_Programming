from bank import value

def test_hello():
    assert value("hello")== "$0"
def test_hey():
    assert value("h")=="$20"
def test_else():
    assert value("Whats up")== "$100"