"""
    ESTRUTURA DE DADOS FILA
    
    É uma estrutura de dados linear em que a operação de inserção (enqueue) acontece no final (ou cauda) da estrutura, enquanto a operação de remoção (dequeue) ocorre no início (ou cabeça). Em consequência, o funcionamento da fila pode ser descrito como FIFO (First In, First Out): o primeiro a entrar é o primeiro a sair.
"""
class Queue:

    """ Método construtor """
    def __init__(self):
        self.__data = []    # Lista vazia

    """
        Método de inserção
        Em filas, tem nome padronizado: enqueue
    """
    def enqueue(self, val):
        self.__data.append(val)

    """
        Método que retorna se a fila está vazia (true)
        ou não (false)
    """
    def is_empty(self):
        return len(self.__data) == 0
    
    """
        Método de remoção
        Em filas, tem nome padronizado: dequeue
    """
    def dequeue(self):
        if self.is_empty():
            raise Exception("ERRO: impossível remover de uma fila vazia.")
        return self.__data.pop(0)   # Remove o primeiro item
    
    """
        Método para consultar o primeiro item da fila, sem removê-lo
    """
    def peek(self):
        if self.is_empty():
            raise Exception("ERRO: impossível consultar uma fila vazia")
        return self.__data[0]
    
    """
        Método que retorna uma representação da fila como string
    """
    def __str__(self):
        return str(self.__data)