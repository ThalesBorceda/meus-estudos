# Escreva uma função que receba três parâmetros obrigatórios e dois opcionais 

def somar(x, y, z, a=2, b=3):
    """
    Retorna x + y + z + a + b.
    :param x: int.
    :param y: int.
    :param z: int.
    :param a: int.
    :param b: int.
    """
    return x + y + z + a + b 

print(somar(4, 5, 6, 7))
