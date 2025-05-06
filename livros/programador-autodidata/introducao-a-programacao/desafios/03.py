# Escreva um programa que exiba uma mensagem se uma variável foi menor ou igual a 10, outra mensagem se a variável for maior do que 10, mas menor ou igual a 25, e outra mensagem se a variável for maior do que 25

variavel = int(input('Digite um número: '))

if (variavel < 10) or (variavel == 10):
    print('O número informado é menor ou igual a 10')
elif (variavel > 10) and (variavel < 25) or (variavel == 25):
    print('O número informado é maior do que 10, mas menor ou igual a 25')
else:
    print('O número informado é maior do que 25')