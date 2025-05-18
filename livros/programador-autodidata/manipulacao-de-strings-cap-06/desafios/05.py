#Pegue a lista ["The", "fox", "jumped", "over", "the", "fence", "."] e transforme-a em uma string
#gramaticalmente correta. É preciso que haja um espaço entre cada palavra, mas nenhum espaço entre
#a palavra fence e o ponto que vem depois dela. (Não se esqueça que você conheceu um método que 
#transforma uma lista de strings em uma única string) 

from posixpath import join
list = ["The ", "fox ", "jumped ", "over ", "the ", "fence", "."] 

list = ''.join(list)

print(list)

#Fiz uma gambiarra, não poderia ter incluído o espaço depois de cada palavra na lista.
#O autor faz o seguinte: 

#fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
#fox = " ".join(fox)
#fox = fox[0: -2] + "."
#print(fox)
