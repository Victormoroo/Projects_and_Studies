"""
    ESTRUTURA DE DADOS ÁRVORE BINÁRIA DE BUSCA
    * Árvore ~> é uma estrutura de dados não linear, considerada
      uma especialização do grafo, formada recursivamente por
      outras árvores (subárvores)
    * Árvore binária ~> uma árvore na qual cada nodo tem grau
      máximo igual a 2. Em outras palavras, cada nodo pode ter
      até dois descendentes diretos
    * Árvore binária de busca ~> é uma árvore binária em que as
      inserções são feitas de forma ordenada, de modo a otimizar a
      operação de busca binária
"""
class BinarySearchTree:

    """
        Classe que representa cada unidade de informação (nodo)
        da árvore binária de busca
        Possui três atributos:
        1) Informação relevante para o usuário (data)
        2) Ponteiro para o nodo descendente à esquerda (left)
        3) Ponteiro para o nodo descendente à direita (right)
    """
    class Node:
        def __init__(self, val):
            self.data = val
            self.left = None
            self.right = None

    """
        Método construtor da classe BinarySearchTree
    """
    def __init__(self):
        self.__root = None      # Raiz da árvore

    """
        Método PÚBLICO para a inserção de um VALOR na árvore
    """
    def insert(self, val):
        # Cria um novo nodo para armazenar o valor
        new = self.Node(val)

        # 1º caso: a árvore está vazia.
        # O primeiro nodo inserido será a raiz
        if self.__root is None: self.__root = new

        # 2º caso: a raiz já existe. É necessário procurar pela
        # posição de inserção do novo nodo, o que é feito por
        # um método privado
        else: self.__insert_node(self.__root, new)

    """
        Método PRIVADO para inserção de um NODO na árvore
    """
    def __insert_node(self, root, new):
        # 1º caso: o valor do novo nodo é MENOR que o valor na raiz
        if new.data < root.data:
            # Se a esquerda da raiz estiver desocupada, insere aí
            if root.left is None: root.left = new
            # Senão, passa a considerar o nodo da esquerda como raiz
            else: self.__insert_node(root.left, new)

        # 2º caso: o valor do novo nodo é MAIOR que o valor na raiz
        elif new.data > root.data:
            # Se a direita da raiz estiver desocupada, insere aí
            if root.right is None: root.right = new
            # Senão, passa a considerar o nodo da direita como raiz
            else: self.__insert_node(root.right, new)

    """
        Método que percorre a árvore em-ordem
        1º: percorre recursivamente a subárvore esquerda em-ordem
        2º: visita a raiz
        3º: percorre recursivamente a subárvore direta em-ordem
    """
    def in_order_traversal(self, action, root = False):
        # Se root for False, começamos pela raiz da árvore
        if root is False: root = self.__root

        if root is not None:
            self.in_order_traversal(action, root.left)  # 1º
            action(root.data)    # 2º
            self.in_order_traversal(action, root.right) # 3º

    """
        Método que percorre a árvore pré-ordem
        1º: visita a raiz
        2º: percorre recursivamente a subárvore esquerda pré-ordem
        3º: percorre recursivamente a subárvore direita pré-ordem
    """
    def pre_order_traversal(self, action, root = False):
        if root is False: root = self.__root

        if root is not None:
            action(root.data)                               # 1º
            self.pre_order_traversal(action, root.left)     # 2º
            self.pre_order_traversal(action, root.right)    # 3º
    
    """
        Método que percorre a árvore pós-ordem
        1º: percorre recursivamente a subárvore esquerda pós-ordem
        2º: percorre recursivamente a subárvore direita pós-ordem
        3º: visita a raiz
    """
    def post_order_traversal(self, action, root = False):
        if root is False: root = self.__root

        if root is not None:
            self.post_order_traversal(action, root.left)    # 1º
            self.post_order_traversal(action, root.right)   # 2º
            action(root.data)                               # 3º
    
    """
        Método PÚBLICO que verifica se um valor existe na ABB
    """
    def exists(self, key):
        node = self.__search_node(self.__root, key)
        return (node is not None)
    
    """
        Método PRIVADO que procura por um nodo que contém um valor
        fornecido (key) e retorna esse nodo, se ele existir, ou None,
        caso contrário
    """
    def __search_node(self, root, key):
        # 1º caso: árvore vazia
        if root is None: return None
        
        # 2º caso: o valor de key é MENOR que o valor na raiz
        # Continua a buscar recursivamente pela subárvore ESQUERDA
        if key < root.data: return self.__search_node(root.left, key)

        # 3º caso: o valor de key é MAIOR que o valor na raiz
        # Continua a buscar recursivamente pela subárvore DIREITA
        if key > root.data: return self.__search_node(root.right, key)

        # 4º caso: o valor de key é IGUAL ao valor na raiz
        # ENCONTROU O NODO; retorna o nodo root
        return root

    """
        Método PRIVADO que retorna o maior nodo de uma subárvore
    """
    def __max_node(self, root = None):
        if root is None: root = self.__root
        node = root
        # A partir da raiz, desce pela direita até onde der
        while node is not None and node.right is not None:
            node = node.right
        return node
    
    """
        Método PRIVADO que retorna o menor nodo de uma subárvore
    """
    def __min_node(self, root = None):
        if root is None: root = self.__root
        node = root
        # A partir da raiz, desce pela esquerda até onde der
        while node is not None and node.left is not None:
            node = node.left
        return node
    
    """
        Método público para a remoção de um valor da árvore
    """
    def remove(self, val):
        self.__root = self.__remove_node(self.__root, val)

    """
        Método PRIVADO para a remoção de um nodo da árvore
    """
    def __remove_node(self, root, val):

        # 1º caso: árvore vazia
        if root is None: return None

        # 2º caso: o valor a ser removido é MENOR que o valor da raiz
        # Continua procurando pelo nodo a ser removido pelo lado ESQUERDO
        if val < root.data:
            root.left = self.__remove_node(root.left, val)
            return root
        
        # 3º caso: o valor a ser removido é MAIOR que o valor da raiz
        # Continua procurando pelo nodo a ser removido pelo lado DIREITO
        if val > root.data:
            root.right = self.__remove_node(root.right, val)
            return root
        
        # 4º caso: o valor a ser removido é IGUAL ao valor da raiz
        # O NODO A SER REMOVIDO FOI ENCONTRADO
        # Agora, é necessário determinar o grau do nodo para aplicar
        # o algoritmo de remoção correto para cada caso

        # 4.1: remoção de nodo de grau 0
        if root.left is None and root.right is None:
            # Sobrescreve o nodo (root) com None
            root = None
            return root
        
        # 4.2: remoção de nodo de grau 1 com subárvore à ESQUERDA
        if root.left is not None and root.right is None:
            root = root.left
            return root
        
        # 4.3: remoção de nodo de grau 1 com subárvore à DIREITA
        if root.left is None and root.right is not None:
            root = root.right
            return root
        
        # 4.4: remoção de nodo de grau 2

        # É necessário encontrar:
        # a) o MAIOR nodo da subárvore ESQUERDA; *OU*
        # b) o MENOR nodo da subárvore DIREITA

        # Opção escolhida: usar o maior nodo da subárvore esquerda
        new_root = self.__max_node(root.left)

        # Copia o valor do nodo encontrado e sobrescreve o valor do
        # nodo que está sendo "removido"
        root.data = new_root.data

        # Exclui o valor duplicado que está na subárvore esquerda
        # (de onde veio o valor de new_root)
        root.left = self.__remove_node(root.left, new_root.data)

        return root

#############################################################################