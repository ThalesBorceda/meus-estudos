# As listas, tuplas e os dicionários são apenas alguns dos contêineres internos do Python. Faça uma pesquisa sobre os conjuntos (um tipo de contêiner) do Python. Quando você usaria um conjunto?

# Conjuntos (set) são coleções desordenadas e que não permitem elementos duplicados.
# Eles são úteis quando queremos armazenar itens únicos, verificar rapidamente se um item está presente
# Por exemplo, você usaria um conjunto para guardar nomes sem deixar repetir.

# Guardar nomes sem deixar repetir
nomes = ["Ana", "João", "Ana", "Carlos", "João"]

nomes_unicos = set(nomes)  # transforma a lista em conjunto, removendo repetições

print(nomes_unicos)  

