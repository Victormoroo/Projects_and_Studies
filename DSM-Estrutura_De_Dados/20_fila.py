from lib.queue import Queue

fila = Queue()      # Cria uma fila vazia

# Insere algumas pessoas na fila
fila.enqueue('Leotildes')
fila.enqueue('Orozimbo')
fila.enqueue('Valdisney')
fila.enqueue('Adamastor')

print(fila)

atendido = fila.dequeue()
print(f"Atendido: {atendido}")
print(fila)

fila.enqueue('Marcinéia')
print(fila)

proximo = fila.peek()
print(f"Próximo a ser atendido: {proximo}")
print(fila)