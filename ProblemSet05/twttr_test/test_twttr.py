from twttr import shorten

def test_shorten():
    assert shorten("twitter")== "twttr"
    assert shorten("aeiou")==""
    assert shorten("AEIOU")==""