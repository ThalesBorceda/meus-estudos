import csv

resposta = input("Qual é a sua série favorita?")
with open('serie.csv', 'w') as f:
    f.write(resposta + '\n')   