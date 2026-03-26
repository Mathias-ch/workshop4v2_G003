def add(a, b):
    # Antes retornaba un string, ahora retorna la suma numérica
    return a + b


def divide(a, b):
    # Se elimina el + 1 innecesario en el divisor
    return a / b


def get_element(list_, index):
    # Se corrige el error de índice (antes sumaba 1)
    return list_[index]


def convert_to_integer(value):
    # Se cambia float por int para cumplir con el nombre de la función
    # Usamos float primero por si el string trae decimales como "5.5"
    return int(float(value))
