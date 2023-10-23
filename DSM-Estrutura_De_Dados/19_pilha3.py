from lib.stack import Stack

#expr = "2 + (( 5 * ( 3 / 2 + 1) / 4 ))"
#expr = "(2 + (( 5 * ( 3 / (2 + 1) / 4 ))"
expr = "2 + (( 5 * ( 3 / 2 ) + 1)) / 4 ))"

print(f"EXPRESSÃO ANALISADA: {expr}")

pilha = Stack()

# Percorre a expressão em busca de parênteses
for pos in range(len(expr)):
    # Empilha a posição quando é encontrado um abre parênteses
    if expr[pos] == "(":
        pilha.push(pos)
        # print(pilha)

    # Desempilha a posição do último abre parêntese empilhado
    # quando um fecha parêntese é encontrado
    elif expr[pos] == ")":
        if pilha.is_empty():
            print(f"ERRO: parêntese fechado na posição {pos} não tem o abre correspondente")
        else:
            pos_abre = pilha.pop()
            print(f"Parêntese aberto na posição {pos_abre} foi fechado na posição {pos}")
            # print(pilha)

# Verifica sobras na pilha
while not pilha.is_empty():
    pos_abre = pilha.pop()
    print(f"ERRO: parêntese aberto na posição {pos_abre} não possui o fecha correspondente")