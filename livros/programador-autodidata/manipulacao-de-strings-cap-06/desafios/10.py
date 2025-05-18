#Fatia a string "It was a brigth cold day in April, and the clocks were striking thirteen." para que só inclua
#os caracteres existentes em antes da vírgula

#solução mais simples (a que eu fiz)
sentence = "It was a brigth cold day in April, and the clocks were striking thirteen"

sentence = sentence[0:33]

print(sentence)

#joguei minha solução no CharGPT e ele retornou a seguinte alternativa usando o método index 
sentence = "It was a brigth cold day in April, and the clocks were striking thirteen."

indice_virgula = sentence.index(',')

sentence = sentence[:indice_virgula]

print(sentence)
