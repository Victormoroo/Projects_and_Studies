"""
LISTAS EM PYTHON
Listas são uma forma de armazenar mais de um valor
em uma única variável. Os valores podem ser de tipos
diferentes.

1) PERCURSO: significa percorrer a lista do primeiro até o último elemento, fazendo
algo com cada um deles. No caso a seguir, vamos exibir cada um em uma linha usando print().
"""
lista = [2, 3, 4, 5, 7, 9, 11, 'batata', 'tomate', True]

for val in lista:
    print(val)

print('*' *50)

# 2) INSERÇÃO de um novo elemento no *fim* da lista usando append().
lista.append("cebola")
print(lista)

lista.append(29)
print(lista)

print('*' *50)
"""
3) INSERINDO UM NOVO ELEMENTO EMUMA POSIÇÃO ESPECIFICICADA usando insert().
Parâmetros:
1°: Posição para inserir (contagem inicia em 0)
2°: valor a ser inserido
"""
lista.insert(4, 'chuchu') # Insere 'chuchu' na 5° posição
print(lista)

lista.insert(0, False) # Insere 'False' na 1° posição
print(lista)

print('*' *50)

# 4) ACESSANDO um valor na posição específica:
print(f'Elemento na SÉTIMA posição: {lista[6]}')
print(f'Elemento na PRIMEIRA posição: {lista[0]}')
print(f'Elemento na ÚLTIMA posição: {lista[-1]}')
print(f'Elemento na PENÚLTIMA posição: {lista[-2]}')

print('*' *50)

# 5) SUBSTITUINDO valores existentes:
print(f'ANTES: {lista}')

# Substituindo o valor da posição 10
lista[10] = 'cenoura'
# Substituindo o valor da posição 0
lista[0] = 'beterraba'
# Substituindo o valor da última posição
lista[-1] = 'alho'
print(f'DEPOIS: {lista}')

print('*' *50)

# 6) DETERMINANDO QUANTOS ELEMENTOS HÁ NA LISTA: len()
print(f'Número de elementos na lista: {len(lista)}')

# Imprimindo o último elemento da lista com a ajuda de len()
print(f'Último valor da lista: {lista[len(lista) -1]}')
print(lista)

print("*" * 80)

# 7) REMOVENDO O ÚLTIMO ELEMENTO DA LISTA: pop()
print(f'ANTES: {lista}')
ultimo = lista.pop()
print(f'Valor removido da lista: {ultimo}')
print(f'DEPOIS: {lista}')

print("*" * 80)

# 8) REMOVENDO UM ELEMENTO POR SUA POSIÇÃO: pop() com parâmetro
print(f'ANTES: {lista}')
pos9 = lista.pop(9)   # Remove o elemento da posição 9
print(f'Valor removido da posição 9: {pos9}')
pos0 = lista.pop(0)   # Remove o primeiro elemento da lista
print(f'Valor removido da posição 0: {pos0}')
print(f'DEPOIS: {lista}')

print("*" * 80)

# 9) REMOVENDO UM ELEMENTO PELO SEU VALOR: remove()
print(f'ANTES: {lista}')
lista.remove('chuchu')   # Remove o valor 'batata'
lista.remove(5)          # Remove o valor 5
print(f'DEPOIS: {lista}')

print("*" * 80)

# Acrescentando mais alguns elementos na lista
lista.append(13)
lista.append(15)
lista.append("milho")
lista.append(17)
lista.append("mandioca")
lista.append(19)

print("*" * 80)

# 10) FATIANDO UMA LISTA
print(lista)

# Cria uma sublista que contém os elementos de 2 até a posição 7 (posição 8 não entra)
sublista2_7 = lista[2:8]
print(f'Sublista de 2 a 7: {sublista2_7}')

# Cria uma sublista que contém os elementos do início até a posição 5 (posição 6 não entra)
sublista0_5 = lista[:6]
print(f'Sublista de 0 a 5 {sublista0_5}')

# Cria uma sublista que contém os elementos da posição 10 até o fim da lista
sublista10_fim = lista[10:]
print(f'Sublista de 10 até o final: {sublista10_fim}')
