from plates import is_valid

def test_valid():
    assert is_valid("ABC123")== True
    assert is_valid("abc123")== True
def test_invalid():
    assert is_valid("ABC123A")== False
    assert is_valid("abc123a")== False
def test_zeroFirst():
    assert is_valid("abc01")==False
    assert is_valid("abc101")== False
def test_specialChars():
    assert is_valid("ABC!,.")==False