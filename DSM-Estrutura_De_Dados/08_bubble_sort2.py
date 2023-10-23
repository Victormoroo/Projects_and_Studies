"""
  ALGORITMO DE ORDENAÇÃO BUBBLE SORT percorre a lista a ser ordenada em sucessivas passadas, trocando dois elementos adjacentes sempre que o segundo for MENOR que o primeiro. Efetua tantas passadas quanto necessárias, até que, na última passada, nenhuma troca seja efetuada.
  VERSÃO OTIMIZADA COM ENCOLHIMENTO DO PERCURSO A CADA PASSADA
"""

# Variáveis de estastísticas
comps = trocas = passadas = 0

def bubble_sort(lista):
    global comps, trocas, passadas
    comps = trocas = passadas = 0

    desloc = 1

    # Loop eterno, não sabemos quantas passads serão necessárias
    while True:
        trocou = False
        passadas += 1

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento, com acesso a cada posição
        for pos in range(len(lista) - desloc):

            comps += 1

            # Se o número que está à frente na lista for MENOR do que o que está atrás, TROCA
            if lista[pos + 1] < lista[pos]:
                lista[pos +1], lista[pos] = lista[pos], lista[pos + 1]
                trocou = True
                trocas += 1

        if not trocou: # Não houve troca na passada
            break      # Interrompe o loop eterno; acabou

        # Aumenta o deslocamento para diminuir o tamanho da próxima passada
        desloc += 1

################################################################################

# Teste com um vetor de 10 números
nums = [6, 4, 2, 0, 9, 5, 1, 8, 3, 7]

bubble_sort(nums)
print(f'Lista ordenada {nums}')
print(f'Comparações: {comps}, trocas: {trocas}, passadas: {passadas}')

print('\n', '-'*80, '\n', sep='')

pior_caso = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
bubble_sort(pior_caso)
print(f'Lista ordenada (pior caso): {nums}')
print(f'Comparações: {comps}, trocas: {trocas}, passadas: {passadas}')

print('\n', '-'*80, '\n', sep='')

melhor_caso = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
bubble_sort(melhor_caso)
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
bubble_sort(nomes)
hora_fim = time()

print(f'Nomes ordenados: {nomes}')
print(f'Tempo gasto: {(hora_fim - hora_ini) * 1000}ms')
print(f'Comparações: {comps}, trocas: {trocas}, passadas: {passadas}')