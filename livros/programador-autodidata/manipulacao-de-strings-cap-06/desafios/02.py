#Escreva um programa que colete duas strings com um usuário, insira-as na string "Yesterday I wrote a 
#[resposta_um]. I sent it to [resposta_dois]! e exiba uma nova string. 

answer_one = str(input('What did you write yesterday? '))
answer_two = str(input('To whom did you send it? '))

print(f'Yesterday I wrote a {answer_one}. I send it to {answer_two}')
