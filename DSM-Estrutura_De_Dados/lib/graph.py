"""
    ESTRUTURA DE DADOS GRAFO
    É uma estrutura de dados não-linear, formada por vértices (ou nodos) e arestas (ou arcos). Sua principal finalidade é representar as relações entre diferentes objetos. Tais relações podem ser bidirecionais, resultando em grafos não direcionados, ou unidirecionais, constituindo grafos direcionados (digrafos). Tem várias aplicações, como a  representação de redes de computadores, mapas e caminhos e redes sociais.
"""
class Graph:

    """
        Método construtor
    """
    def __init__(self, is_directed = False):
        self.__is_directed = is_directed

        # __data armazenará o grafo no formato de
        # LISTA DE ADJACÊNCIA
        self.__data = {}        # Dicionário vazio

    """
        Método que adiciona um vértice ao grafo
    """
    def add_vertex(self, val):
        # Verifica se o vértice já existe no dicionário.
        # Só cria se o vértice não existir ainda
        if not val in self.__data:
            self.__data[val] = set()    # Conjunto vazio

    """
        Método que adiciona uma aresta entre dois vértices
        origin: vértice de origem
        dest: vértice de destino
        rel: nome do relacionamento (opcional)
    """
    def add_edge(self, origin, dest, rel = None):
        # Cria os vértices de origem e destino, caso não
        # existam ainda
        if not origin in self.__data: self.add_vertex(origin)
        if not dest in self.__data: self.add_vertex(dest)

        # Monta a aresta
        edge1 = (dest, rel)     # Isto é uma tupla ("lista imutável")

        # Adiciona a relação origem->destino
        self.__data[origin].add(edge1)

        # Se o grafo não for direcionado, adicionamos também a 
        # relação no sentido oposto, isto é, destino->origem
        if not self.__is_directed:
            edge2 = (origin, rel)   # Tupla
            self.__data[dest].add(edge2)

    """
        Método que retorna o grau (número de vértices adjacentes) de um vértice
    """
    def degree(self, vertex):
        result = 0
        # GRAU DE SAÍDA (OUT-DEGREE)
        # É determinado contando-se o número de arestas associadas
        # à entrada de dicionário correspondente ao vértice
        if vertex in self.__data: result = len(self.__data[vertex])

        # GRAU DE ENTRADA (IN-DEGREE)
        # É determinado procurando-se referências ao vértice nas
        # arestas associadas a todos os vértices do dicionário
        for v in self.__data.keys():    # Percorre o dicionário (vértices)
            for e in self.__data[v]:    # Percorre os conjuntos (arestas)
                if vertex == e[0]: result += 1

        # O grau final é a soma dos graus de entrada e de saída
        return result
    
    """
        Método que exclui um vértice do grafo (Para que um vértice possa ser excluído, ele não pode ter arestas incidentes, ou seja, seu grau deve ser 0, nem ser referenciado por outros vértices)
    """
    def remove_vertex(self, vertex):
        if self.degree(vertex) != 0:
            raise Exception("ERRO: impossível remover um vértice com arestas incidentes a ele.")
        # Vértice de grau 0, podemos excluir, caso exista no dicionário
        elif vertex in self.__data: del self.__data[vertex]

    
    """
        Método que remove uma aresta do grafo
    """
    def remove_edge(self, origin, dest, rel = None):
        edge1 = (dest, rel)
        # Retira a tupla edge1 do conjunto de arestas do vértice de origem
        self.__data[origin].discard(edge1)

        # Se o grafo não for direcionado, precisamos remover também a aresta
        # em sentido contrário
        if not self.__is_directed:
            edge2 = (origin, rel)
            self.__data[dest].discard(edge2)

    """
        Método que representa o grafo como uma string
    """
    def __str__(self):
        output = str(self.__data)
        output += f"\nis_directed: {self.__is_directed}\n\n"
        return output
    