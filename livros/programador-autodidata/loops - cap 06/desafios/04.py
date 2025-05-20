# Multiplique todos os números da lista [8, 19, 148, 4] por todos os números da 
# lista [9, 1, 33, 83] e acrescente cada resultado a uma terceira lista

lista01 = [8, 19, 148, 4]

lista02 = [9, 1, 33, 83]

resultado = []

for i in lista01:
  for j in lista02:
    resultado.append(i * j)
  
print(resultado)
