"""
    1) Identifique o algoritmo abaixo.
    2) Faça o mapeamento das variáveis (registre em comentário o propósito de cada uma delas).
    3) Há um erro no algoritmo. Identifique-o, descreva-o e corrija-o.
"""

"""
    1) Busca Binária
    3) O erro esta no if dentro do while, pois o "fim" nao irá receber "meio", mas sim o "if" irá retornar "meio" (se o valor for encontrado ele retorna a posição)
"""

def busca_binaria(lista, val):
    ini = 0 # inicio da lista
    fim = len(lista) - 1 # fim da lista
    while ini <= fim: 
        meio = (ini + fim) // 2 # faz uma divisao inteira
        if val == lista[meio]: # valor de busca encontrado...
            return meio # retorna a posição
        elif val < lista[meio]:
            fim = meio - 1
        else:
            ini = meio + 1
    return -1 # valor nao existe na lista