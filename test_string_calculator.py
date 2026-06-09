from string_calculator import add

def test_empty_string():
    """Debe retornar 0 si se envía un string vacío"""
    assert add("") == 0

def test_single_number():
    """Debe retornar el mismo número si se envía solo uno"""
    assert add("1") == 1
    assert add("5") == 5

def test_multiple_numbers():
    """Debe sumar múltiples números separados por comas"""
    assert add("1,2,3") == 6
    assert add("1,2,3,4,5") == 15

def test_newlines_as_delimiters():
    """Debe permitir el salto de línea como delimitador además de la coma"""
    assert add("1\n2,3") == 6
    assert add("10\n20\n30") == 60