# Lista
frutas = ['laranja', 'maçã', 'uva', 'pera', 'mamão', 'abacate', 'amora']

# Para percorrer uma lista e exibir apenas seus elementos, usamos for...in, como já vimos no arquivo 02
for f in frutas:
    print(f)

print('-'*80)

# Se quisermos percorrer a lista em ordem inversa para exibir apenas seus elementos, podemos usar for...in combinado com reversed()
for f in reversed(frutas):
    print(f)

print('-'*80)

# Agora, se precisamos exibir, além do elemento, tambem sua POSIÇÃO, devemos usar range()
for pos in range(len(frutas)):
    print(f'A fruta {frutas[pos]} está na posição {pos}.')

print('-'*80)

# Percurso em ordem inversa usando range() com 3 parâmetros
for i in range(len(frutas) -1, -1, -1):
    print(f'A fruta {frutas[i]} está na posição {i}.')

print('-'*80)
