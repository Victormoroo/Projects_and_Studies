"""
    ALGORITMO DE BUSCA BINÁRIA
    Dados uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor de busca, divide a lista em duas metades procurando pelo valor de busca apenas na metade onde o valor poderia estar. Novas subdivisões são feitas até que se encontre o valor de busca ou que reste apenas uma sublista vazia, quando então se conclui que o valor de busca não existe na lista.
"""
def busca_binaria(lista, val):
    global count
    count= 0

    ini = 0               # Início da lista
    fim = len(lista) - 1   # Fim da lista

    while ini <=fim:
        meio = (ini + fim) // 2   # // = Divisão inteira

        # O valor de busca foi encontrado.
        # Retorna a posição
        if lista[meio] == val:
            count += 1
            return meio
        elif val < lista[meio]:
            count += 2
            fim = meio - 1
        else:
            count += 2
            ini = meio + 1
    return - 1   # Valor não existe na lista

# TESTES COM NOMES

import sys
sys.dont_write_bytecode = True     # Impede a criação do cache

from time import time

from data.lista_nomes import nomes

# Busca pelo nome VICTOR
hora_ini = time()
resultado = busca_binaria(nomes, 'VICTOR')
hora_fim = time()
print(f'Posição do nome VICTOR na lista: {resultado}')
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {count}')

print('\n', '-'*80, '\n', sep='')

# Busca pelo nome BRUNO
hora_ini = time()
resultado = busca_binaria(nomes, 'BRUNO')
hora_fim = time()
print(f'Posição do nome BRUNO na lista: {resultado}')
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {count}')

print('\n', '-'*80, '\n', sep='')

# Busca pelo nome kELEN
hora_ini = time()
resultado = busca_binaria(nomes, 'KELEN')
hora_fim = time()
print(f'Posição do nome KELEN na lista: {resultado}')
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {count}')

print('\n', '-'*80, '\n', sep='')

# Busca por um nome inxistente
hora_ini = time()
resultado = busca_binaria(nomes, 'WILJISLEN')
hora_fim = time()
print(f'Posição do nome WILJISLEN na lista: {resultado}')
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms, comparações: {count}')

print('\n', '-'*80, '\n', sep='')
