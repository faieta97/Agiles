from string_calculator import add

def test_multiple_numbers():


    assert add("1,2,3") == 6
    assert add("1,2,3,4,5") == 15

def test_newlines_as_delimiters():
    assert add("1\n2,3") == 6
    assert add("10\n20\n30") == 60