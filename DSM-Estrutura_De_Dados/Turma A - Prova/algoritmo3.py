"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

"""
    1) Bubble Sort
    3) O erro esta no if entro do for, caso "lista[pos - 1] < lista[pos], o algortmo deve trocar as posições de [pos + 1] com [pos] e nao com a variavel "trocou", exemplo:
    
    ERRADO -> lista[pos + 1], lista[trocou] = lista[trocou], lista[pos + 1]
    CORRETO -> lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
"""

def bubble_sort(lista):
    while True: # loop eterno, pois nao se sabe quantas passadas serao necessarias
        trocou = False
        for pos in range(len(lista) - 1): # corre a lista toda do primeiro ao ultimo elemento, com acesso a cada posição
            if lista[pos + 1] < lista[pos]: # Se o numero que esta à frente na lista for menor do que o que esta atras, ele troca
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocou = True
        if not trocou: # se nao houver troca na passada
            break # interrompe o loop eterno, o algoritmo para