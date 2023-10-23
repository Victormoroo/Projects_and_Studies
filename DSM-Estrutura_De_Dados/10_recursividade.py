"""
RECURSIVIDADE

Trata-se de uma técnica de programação pela qual uma função chama a si mesma, em um condição diferente da inicial. O principal objetivo do uso da recursividade é diminuir a complexidade de algoritmos.
"""

# Cálculo do fatorial, versão iterativa (não recursiva)
def fatorial_iter(num):
    if num < 0:
        raise Exception('ERRO: número negativo, cálculo impossível')
    
    res = 1

    # Loop descendente de num até 1
    for x in range(num, 0, -1): res *= x

    return res         # res = res * x

################################################################################

# Cálculo do fatorial de forma recursiva
def fatorial_rec(num):
    # Não é possível calcular o fatorial de números negativos
    if num < 0:
        raise Exception('ERRO: número negativo, cálculo impossível')
    
    if num <= 1:
        return 1   # O fatorial de 0 e 1 é 1
    
    else:
        return num * fatorial_rec(num - 1)   # Chamada recursiva à função
    
################################################################################

# print('7! = ', fatorial_iter(7))
# print('0! = ', fatorial_iter(0))
# print('-6! = ', fatorial_iter(-6))

print('7! = ', fatorial_rec(7))
print('0! = ', fatorial_rec(0))
print('-6! = ', fatorial_rec(-6))
