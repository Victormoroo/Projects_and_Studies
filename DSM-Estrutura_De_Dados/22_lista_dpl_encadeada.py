from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()
print(lista)

# Insere o primeiro elemento
lista.insert(0, "Macarrão")
print(lista)

# Insere no fim
lista.insert(1, "Molho de tomate")
print(lista)

# Insere em uma posição intermediária
lista.insert(1, "Óleo de soja")
print(lista)

# Insere no final usando método de atalho
lista.insert_back("Queijo ralado")

# Insere no início usando método de atalho
lista.insert_front("Carne moída")

# Mais uma inserção em posição intermediária
lista.insert(3, "Sal")
print(lista)

# Busca pelo valor "Queijo ralado" na lista
pos1 = lista.find("Queijo ralado")
print(f"'Queijo ralado' está na posição {pos1}")

# Busca pelo valor "Manjericão" na lista
pos2 = lista.find("Manjericão")
print(f"'Manjericão' está na posição {pos2}")

# Consulta alguns itens da lista
primeiro = lista.peek_front()
ultimo = lista.peek_back()
quarto = lista.peek(3)
print(f"PRIMEIRO: {primeiro}, ÚLTIMO: {ultimo}, QUARTO: {quarto}\n")

# Remove o primeiro item da lista
primeiro = lista.remove_front()
print(f"PRIMEIRO ITEM REMOVIDO: {primeiro}")
print(lista)

# Remove o último item da lista
ultimo = lista.remove_back()
print(f"ÚLTIMO ITEM, REMOVIDO: {ultimo}")
print(lista)

# Remove o item da posição 2
pos2 = lista.remove(2)
print(f"ITEM DA POSIÇÃO 2, REMOVIDO: {pos2}")
print(lista)
