"""
ESTRUTURA DE DADOS PILHA
É uma estrutura de dados linear de acesso restrito na qual tanto a operação de inserção (tradicinalmente chamada de "push"), quanto a operação de remoção ("pop") acontecem no final (ou topo). Em consequência, o funcionamento da pilha obedece ao princípio LIFO (Last In, First Out): o último elemento a entrar deve ser o primeiro a sair.
"""
class Stack:

    """Método construtor"""
    def __init__(self):
        # Cria uma lista privada e vazia para armazenar os dados da pilha
        self.__data = []

    """
    Método para inserção
    Em pilhas, tem nome padronizado: push
    """
    def push(self, val):
        self.__data.append(val)

    """
    Método que verifica se a pilha está ou não vazia
    """

    def is_empty(self):
        return len(self.__data) == 0
    
    """
    Método para remoção
    Em pilhas, tem nome padronizado: pop
    """

    def pop(self):
        if self.is_empty():
            raise Exception('ERRO: impossível remover de uma pilha vazia')
        
        # Se chegou até aqui, a pilha NÃO está vazia e a remoção pode ser feita
        return self.__data.pop()
    
    """
    Método que permite consultar o valor que está no topo da pilha, sem removê-lo
    Em pilhas, tem nome padronizado: peek
    ("Peek" significa "dar uma espiadinha" em inglês)
    """

    def peek(self):
        if self.is_empty():
            raise Exception('ERRO: impossível consultar uma lista vazia')
        
        return self.__data[-1]  # Último elemento da lista
    
    """
    Método que permite imprimir a lista como string
    """

    def __str__(self):
        return str(self.__data)
    
################################################################################

"""
pilha = Stack()

pilha.push('Pimeiro')
pilha.push('Segundo')
pilha.push('Terceiro')

print(pilha)

removido = pilha.pop()
print(f'Removido: {removido}')

print(pilha)
"""