"""
ALGORITMO DE ORDENAÇÃO SELECTION SORT

Isola (seleciona) o primeiro elemento da lista e, em seguida, encontra o menor valor no restate da lista. Se o valor encontrado for menor que o valor previamente selecionado, efetua a troca entre eles. Continuando, seleciona o segundo elemento da lista, buscando pelo menor valor das posições subsequentes. Faz a troca entre os dois valores, se necessário. O processo se repete até que o penúltimo elemento da lista seja isolado, comparado com o último e feita a troca entre eles, se for o caso.
"""
comps = trocas = passadas = 0

def selection_sort(lista):

    global comps, trocas, passadas
    comps = trocas = passadas = 0
    
    # Loop que vai da primeira até a penúltima posição
    for pos_sel in range(len(lista) - 1):

        passadas += 1

        # Encontra o menor valor na sublista à frente de pos_sel
        pos_menor = pos_sel + 1
        for pos in range(pos_sel + 2, len(lista)):

            # Se o valor encontrado na posição for MENOR que o valor da posição pos_menor, então pos_menor passa a ser pos
            comps +=1
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        # Compara os elementos das posições pos_menor e pos_sel. Se o valor do primeiro for MENOR que o valor do segundo, efetua a troca
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

################################################################################

# Teste com um vetor de 10 números
nums = [6, 4, 2, 0, 9, 5, 1, 8, 3, 7]

selection_sort(nums)
print(f'Lista ordenada {nums}')
print(f'Comparações: {comps}, trocas: {trocas}, passadas: {passadas}')

print('\n', '-'*80, '\n', sep='')

# pior_caso = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
pior_caso = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
selection_sort(pior_caso)
print(f'Lista ordenada (pior caso): {nums}')
print(f'Comparações: {comps}, trocas: {trocas}, passadas: {passadas}')

print('\n', '-'*80, '\n', sep='')

melhor_caso = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
selection_sort(melhor_caso)
print(f'Lista ordenada (melhor caso): {nums}')
print(f'Comparações: {comps}, trocas: {trocas}, passadas: {passadas}')

################################################################################

from time import time
import sys
sys.dont_write_bytecode = True # Impede a criação do cache

from data.nomes_desord import nomes

# Pega apenas os 25k primeiros nomes
nomes = nomes[:25000]

hora_ini = time()
selection_sort(nomes)
hora_fim = time()

print(f'Nomes ordenados: {nomes}')
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms')
print(f'Comparações: {comps}, trocas: {trocas}, passadas: {passadas}')
