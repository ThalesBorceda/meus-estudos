#Escreva um programa com um loop infinito (com a opção de digitar q para sair)
#e uma lista de números. A cada iteração do loop, peça ao usuário para fornecer
#um número da lista e informe se o palpite estava ou não correto.

lista = [10,20,30,40,50]

while True: 
  print(lista)
  entrada = input('Digite um número ou \"q\" para sair: ')
  if entrada == 'q':
    break
  else: 
    numero = int(entrada)
    if numero in lista:
      print('Palpite correto!')
    else:
      print('Palpite incorreto')
