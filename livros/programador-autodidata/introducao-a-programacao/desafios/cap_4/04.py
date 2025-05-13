# Escreva um programa com duas funções. A primeira função deve receber um inteiro como parâmetro e retornar o resultado do inteiro dividido por 2. 

def divisao_por_2(numero_inteiro_dividir):
    return numero_inteiro_dividir / 2 

# A segunda função deve receber um inteiro como parâmetro e retornar o resultado do inteiro multiplicado por 4

def multiplicar_por_4(numero_inteiro_multiplicar):
    return numero_inteiro_multiplicar * 4

# Chame a primeira função, salve o resultado como uma variável e passe-a como um parâmetro para a segunda função 

resultado = divisao_por_2(10)

print(multiplicar_por_4(resultado))
