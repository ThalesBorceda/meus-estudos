def f(x):
    return x * 4 

# def informa ao python que estamos definindo uma função 
# return define o valor que uma função exibe quando chamada (valor que a função retorna)

resultado = f(4)
print(resultado)

# exemplo mais prático
#cálculo de adicional de periculosidade (30% sobre o salário da pessoa)

salario = float(input('Digite seu salário: '))

def calcular_adicional_de_periculosidade(salario):
    return salario * 0.3

resultado = calcular_adicional_de_periculosidade(salario)
print(resultado)

#função com mais de um parâmetro 

def f(x, y, z): 
    return x + y +z  

resultado = f(1,3,4)
print(resultado)

# reutilizando funções 
def par_impar(x):
    if x % 2 == 0:
        print("par")
    else:
        print ("ímpar")

par_impar(4)

#exemplo com adicional de periculosidade de diferentes salários calculado internamente 
def adicional_de_periculosidade(x): 
    return(x * 0.3)

print(adicional_de_periculosidade(4000))