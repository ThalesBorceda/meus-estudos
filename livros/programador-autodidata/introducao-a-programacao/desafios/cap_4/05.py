# Escreva uma função que converta uma string em um float e retorne o resultado. Use a manipulação de exceções para capturar a exceção que pode ocorrer 

def conversor_string_em_float(texto):
    """
    Retorna a string transformada em float
    :param texto: str.
    """
    try:
         texto = float(texto)
    except ValueError:
        print('O valor digitado não é válido')
        return None
    return texto
        
print(conversor_string_em_float('olá'))