from functions import add, convert_to_integer, divide, get_element


def test_add_numbers():
    assert add(2, 3) == 5  # Ahora add retorna un numero, no 5


def test_divide_numbers():
    assert divide(10, 2) == 5  # 10 / 2 ahora da 5 correctamente


def test_get_valid_element():
    list_ = [1, 2, 3]
    assert get_element(list_, 1) == 2  # El índice 1 de (1, 2, 3) es efectivamente 2


def test_convert_valid_integer():
    # Esta prueba busca que "5.5" se convierta en el entero 5
    assert convert_to_integer("5.5") == 5
