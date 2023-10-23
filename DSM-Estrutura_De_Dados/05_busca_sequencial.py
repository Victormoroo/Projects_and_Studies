# Lista de números
nums = [9, 21, 33, 12, 0, 18, 24, 30, 15, 6, 3, 27]

"""
    Função que realiza uma busca sequencial em uma lista procurando por val.
    Se val for encontrado, retorna a posição de val.
    Caso contrário, retorna o valor -1.
"""
def busca_sequencial(lista, val):
    for pos in range(len(lista)):
        # Encontrou val; retorna a posição onde foi encontrado
        if val == lista[pos]: return pos
    # Percorreu toda a lista e não encontrou val: retorna -1
    return -1

################################################################################

# TESTES

# Procurando o valor 15
resultado = busca_sequencial(nums, 15)
print(f'Posição do valor 15 na lista: {resultado}')

# Procurando o valor 20
resultado = busca_sequencial(nums, 20)
print(f'Posição do valor 20 na lista: {resultado}')

# Procurando o valor 33
resultado = busca_sequencial(nums, 33)
print(f'Posição do valor 33 na lista: {resultado}')

# TESTES COM NOMES

import sys
sys.dont_write_bytecode = True     # Impede a criação do cache

from time import time

from data.lista_nomes import nomes

# Busca pelo nome VICTOR
hora_ini = time()
resultado = busca_sequencial(nomes, 'VICTOR')
hora_fim = time()
print(f'Posição do nome VICTOR na lista: {resultado}')
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms')

print('\n', '-'*80, '\n', sep='')

# Busca pelo nome BRUNO
hora_ini = time()
resultado = busca_sequencial(nomes, 'BRUNO')
hora_fim = time()
print(f'Posição do nome BRUNO na lista: {resultado}')
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms')

print('\n', '-'*80, '\n', sep='')

# Busca por um nome inexistente
hora_ini = time()
resultado = busca_sequencial(nomes, 'BIN LADEN')
hora_fim = time()
print(f'Posição do nome BIN LADEN na lista: {resultado}')
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms')

print('\n', '-'*80, '\n', sep='')
