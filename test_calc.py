from calculator import convert

def test_convert_lowercase():
    assert convert("HELLO") == "hello"

def test_convert_spaces():
    assert convert("hello world") == "hello...world"

def test_convert_mixed():
    assert convert("This Is Python") == "this...is...python"
