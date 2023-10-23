"""
    ESTRUTURA DE DADOS LISTA DUPLAMENTE ENCADEADA

    Trata-se de uma lista linear, em que seus elementos (chamados nodos ou nós) não estão fisicamente adjacentes uns dos outros, mas ligados logicamente por ponteiros que indicam o nodo anterior e o próximo nodo da sequência. Não possui restrição de acesso - inserções, exclusões e consultas podem ser realizadas em qualquer posição da lista.
"""

class DoublyLinkedList:

    """
        Classe que representa a unidade de informação
        armazenada pela lista duplamente encadeada
    """
    class Node:
        def __init__(self, data):
            self.prev = None    # Ponteiro para o nodo anterior
            self.data = data    # Dado útil para o usuário
            self.next = None    # Ponteiro para o nodo posterior
    
    """ Construtor da classe DoublyLinkedList """
    def __init__(self):
        self.__head = None      # Ponteiro para o primeiro nodo da lista
        self.__tail = None      # Ponteiro para o último nodo da lista
        self.__count = 0        # Quantidade de nodos da lista

    """ Método que retorna a quantidade de itens da lista """
    def get_count(self):
        return self.__count
    
    """ Método PRIVADO que encontra um nodo na posição especificada """
    def __find_node(self, pos):
        # 1º caso: posição 0, retorna self.__head
        if pos == 0: return self.__head

        # 2º caso: posição final (self.get_count() - 1)
        if pos == self.get_count() - 1: return self.__tail

        # 3º caso: posição intermediária

        # Se a posição estiver na primeira metade da lista, faz o
        # percurso a partir de self.__head, seguindo next
        if pos < self.get_count() // 2:
            # Percorre a lista quantas vezes for necessário para encontrar
            # o nodo
            node = self.__head
            for i in range(1, pos + 1): node = node.next
            return node
        
        # Senão, a posição estando na segunda metade da lista, faz o
        # percurso reverso a partir de self.__tail, seguindo prev
        else:
            node = self.__tail      # Começa pelo último nodo
            for i in range(self.get_count() - 2, pos - 1, -1):
                node = node.prev
            return node
    
    """ Método que insere um novo valor à lista """
    def insert(self, pos, val):

        # Criamos um nodo para armazenar a informação do usuário e
        # também os ponteiros prev e next, ambos apontando para None
        inserted = self.Node(val)

        # 1º caso: a lista está vazia, e este é o primeiro nodo a
        # ser inserido
        if self.get_count() == 0:
            self.__head = inserted
            self.__tail = inserted

        # 2º caso: inserção no início da lista (posição 0)
        elif pos == 0:
            inserted.next = self.__head
            self.__head.prev = inserted
            self.__head = inserted

        # 3º caso: inserção no final da lista
        # Obs.: consideramos como posição final qualquer posição
        # que seja >= self.get_count()
        elif pos >= self.get_count():
            inserted.prev = self.__tail
            self.__tail.next = inserted
            self.__tail = inserted

        # 4º caso: inserção em posição intermediária
        elif pos > 0:   # Descarta posições negativas
            # Encontra o nodo que atualmente ocupa a posição de inserção
            current = self.__find_node(pos)

            # Determina o nodo anterior à posição de inserção
            before = current.prev

            before.next = inserted
            inserted.prev = before
            inserted.next = current
            current.prev = inserted

        # Incrementa a quantidade de nodos da lista
        self.__count += 1

    """ Método de atalho para inserção no início da lista """
    def insert_front(self, val):
        self.insert(0, val)

    """ Método de atalho para inserção no final da lista """
    def insert_back(self, val):
        self.insert(self.get_count(), val)

    """ Método que remove o nodo da posição especificada """
    def remove(self, pos):

        # 1º caso: lista vazia ou posição fora dos limites
        if self.get_count() == 0 or pos < 0 or pos > self.get_count() - 1:
            raise Exception("ERRO: posição inválida para remoção.")
        
        # 2º caso: remoção do início da lista
        if pos == 0:
            # Será removido o primeiro nodo da lista
            removed = self.__head
            # O novo __head passa a ser o sucessor do nodo removido
            self.__head = removed.next
            # Se o novo __head for um nodo válido, ele não pode ter um
            # antecessor
            if self.__head is not None: self.__head.prev = None
            # Em caso de remoção do único nodo restante da lista, __tail
            # precisa passar a valer None também
            if self.get_count() == 1: self.__tail = None

        # 3º caso: remoção do final da lista
        elif pos == self.get_count() - 1:
            # Será removido o último nodo da lista
            removed = self.__tail
            # O novo __tail passa a ser o antecessor do nodo removido
            self.__tail = removed.prev
            # Se o novo __tail for um nodo válido, ele não pode ter um
            # sucessor
            if self.__tail is not None: self.__tail.next = None
            # Em caso de remoção do único nodo restante da lista, __head
            # precisa passar a valer None também
            if self.get_count() == 1: self.__head = None

        # 4º caso: remoção em posição intermediária
        else:
            removed = self.__find_node(pos)
            before = removed.prev   # Nodo anterior ao que está sendo removido
            after = removed.next    # Nodo posterior ao que está sendo removido
            # O nodo anterior passa a apontar, à frente, para o nodo posterior
            before.next = after
            # O nodo posterior passa a apontar, para trás, para o nodo anterior
            after.prev = before

        # Decrementa a quantidade de itens da lista
        self.__count -= 1

        # Retorna a informação do usuário armazenada no nodo removido
        return removed.data

    """ Método de atalho para remoção do primeiro nodo """
    def remove_front(self):
        return self.remove(0)
    
    """ Método de atalho para remoção do último nodo """
    def remove_back(self):
        return self.remove(self.get_count() - 1)
    
    """
        Método que retorna o valor armazenado na posição especificada,
        sem removê-lo
    """
    def peek(self, pos):
        # 1º caso: lista vazia ou posição fora dos limites
        if self.get_count() == 0 or pos < 0 or pos >= self.get_count():
            raise Exception("ERRO: posição inválida para consulta")
        
        node = self.__find_node(pos)
        return node.data
    
    """ Método de atalho para consultar o primeiro nodo """
    def peek_front(self):
        return self.peek(0)
    
    """ Método de atalho para consultar o último nodo """
    def peek_back(self):
        return self.peek(self.get_count() - 1)
    
    """ 
        Método que procura um nodo por seu valor
        Retorna a posição do nodo, se o encontrar, ou -1, caso contrário
    """
    def find(self, val):
        node = self.__head
        for pos in range(0, self.get_count()):
            if node.data == val: return pos     # Encontrou o valor
            node = node.next
        return -1       # Valor não encontrado

    """
        Método que exibe uma representação da lista como string
    """
    def __str__(self):
        if self.get_count() == 0: return "*** [ LISTA VAZIA ] ***\n\n"
        else:
            repr = f"LISTING {self.get_count()} ITEM(S)\n"
            repr += ('=' * 50) + "\n"
            node = self.__head
            for pos in range(self.get_count()):
                repr += f"NODE #{pos}, address: {hex(id(node))}\n"
                repr += f"prev: {hex(id(node.prev))}\n"
                repr += f"DATA: {node.data}\n"
                repr += f"next: {hex(id(node.next))}\n"
                repr += ('-' * 50) + "\n"
                node = node.next
            repr += "\n\n"
            return repr
