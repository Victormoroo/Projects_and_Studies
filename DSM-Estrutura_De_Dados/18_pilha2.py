"""
programa simples que iverte uma palavra e verifica se ela é um PALÍNDROMO, uma palavra que pode ser lida de trás para a frente, assim como da frente para trás.
Para isso, usaremos uma estrutura de pilha baseada em uma lista do Python.
"""
from lib.stack import Stack

palavra = input('Informe a palavra a ser verificada: ')

pilha = Stack()  # Lista vazia que será usada como pilha

# 1) Pega cada letra da palavra e insere no final (topo) da pilha
for letra in palavra:
    pilha.push(letra)
    print(pilha)

print('*' * 50)

inverso = ''

# 2) Vamos retirar as letras da pilha, uma a uma, DO FIM PARA O INÍCIO.
# A opereção se repete enquanto a pilha não estiver vazia.
# Cada letra retirada é acrescentada à variável inverso.
while not pilha.is_empty():
    letra = pilha.pop()     # Retira o último elemento da pilha
    inverso += letra        # Acrescenta a letra ao inverso
    print(f'Pilha: {pilha}, inverso: {inverso}')

print('*' * 50)

print(f'Palavra original: {palavra}')
print(f'Palavra invertida: {inverso}')

if palavra == inverso:
    print('\n*** É UM PALÍNDROMO***\n')
else:
    print('\n---NÃO É PALÍNDROMO---\n')