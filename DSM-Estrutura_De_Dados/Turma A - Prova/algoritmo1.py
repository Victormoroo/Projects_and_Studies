"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

"""
    1) Merge Sort
    3) O erro esta no if inicial que esta como <= 1, deveria ser > 1, pois teria algo dentro da lista e o algoritmo iria rodar, e caso tivesse apenas um item, ele ja estaria em ordem.
"""

def merge_sort(lista):
    if len(lista) > 1:
        return lista
    meio = len(lista) // 2 # encontra a posicao do meio da lista para dividi-la ao meio
    sublista_esq = lista[:meio] # copia a primeira metade
    sublista_dir = lista[meio:] # copia a segunda metade
    sublista_esq = merge_sort(sublista_esq) # chama recursivamente a funcao para continuar divindo as sublistas ao meio
    sublista_dir = merge_sort(sublista_dir)
    pos_esq = pos_dir = 0 # comeca a ordenacao das duas sublistas
    ordenada = []
    sobra = [] # lista vazia para verificar sobra
    while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir): # compara os elementos das sublistas entre si e insere o menor entre os dois valores na sublista "ordenada"
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]: # menor elemento na sublista da esquerda
            ordenada.append(sublista_esq[pos_esq]) # desce o elemento da esquerda para a lista ordenada
            pos_esq += 1
        else: # menor elemento na sublista da direita
            ordenada.append(sublista_dir[pos_dir]) # desce o da direita para a sublista ordenada
            pos_dir += 1
    if(pos_esq < pos_dir): # sobra a esquerda
        sobra += sublista_esq[pos_esq:]
    else: # sobra a direita
        sobra = sublista_dir[pos_dir:]
    return ordenada + sobra # o resultado final e a juncao da sobra com a lista ordenada
    