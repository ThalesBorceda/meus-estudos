# Escreva um programa com uma variável age que receba um inteiro e exiba strings diferentes dependendo de que inteiro age receber 

# Decidi aplicar o conceito de capacidade do Código Civil 


print('Informe sua idade e descubra sua condição para entrar em juízo')

age = int(input('Digite sua idade em anos: '))

if (age < 16):
    print('Você é absolutamente incapaz e deve ser representando')
elif (age < 18):
    print('Você é relativamente capaz e deve ser assistido')
else:
    print('Você é absolutamente capaz e não precisa de representação nem de assistência')