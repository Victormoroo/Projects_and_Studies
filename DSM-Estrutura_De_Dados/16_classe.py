"""
    Classe é uma estrutura que representa conjuntamente dados e algoritmos. Uma classe pode ser comparada a uma "assadeira" com a qual se pode produzir
"""
from math import pi

# Por convenção, nomes de classe seguem a convenção PascalCase
class FormaGeometrica:
    """
        Uma classe pode ter, dentro de si, tanto dados quanto funções (estas, representando os algoritmos). Uma função especial, chamada __init__, é chamada sempre que um novo objeto é criado a partir de uma classe. Essa função função é chamada de CONSTRUTOR.

        Quando aparecem dentro de uma classe:
        ~> funções passam a ser chamadas de MÉTODOS, e seu primeiro parâmetro é sempre self, que representa o próprio objeto
        ~> Variáveis passam a ser chamadas ATRIBUTOS
    """

    def __init__(self, base, altura, tipo):
        # Armazenando os dados recebidos DENTRO do objeto, com self
        self.set_base(base)
        self.set_altura(altura)
        self.set_tipo(tipo)

    # Métodos setter + validação dos parâmetros recebidos
    def set_base(self, val):
        if type(val) not in [int, float] or val <= 0:
            raise Exception(f'ERRO: a base ({val}) deve ser numérica e maior que zero.')
        self.__base = val

    def set_altura (self, val):
        if type(val) not in [int, float] or val <= 0:
            raise Exception(f'ERRO: a base ({val}) deve ser numérica e maior que zero.')
        self.__altura = val

    def set_tipo (self, val):
        if val not in ['R', 'T', 'E']:
            raise Exception(f"ERRO: o tipo ('{val}') deve ser 'R', 'T' ou 'E'.")
        self.__tipo = val

    # Métodos getter
    def get_base (self):
        return self.__base
    
    def get_altura (self):
        return self.__altura
    
    def get_tipo (self):
        return self.__tipo
    
    # Con o objetivo para uma representação personalizada em string
    def __str__(self):
        return f'< Base: {self.__base}; Altura: {self.__altura}; Tipo: {self.__tipo}>'
    
    def calc_area(self):
        if self.__tipo == 'R':      # Retângulo
            return self.__base * self.__altura
        elif self.__tipo == 'T':    # Triângulo     
            return self.__base * self.__altura / 2
        else:                       # Elipse/circulo
            return (self.__base / 2) * (self.__altura / 2) * pi

################################################################################

# Criando um obejto chamado forma1 a partir da classe FormaGeometrica
forma1 = FormaGeometrica(10, 7.2, 'T')
forma2 = FormaGeometrica(10, 4.5, 'R')
forma3 = FormaGeometrica(12, 12, 'E')

# print(f'Base: {forma1.get_base()}')
# print(f'Altura: {forma1.get_altura()}')
# print(f'Tipo: {forma1.get_tipo()}')

# Formata a área com duas casas decimais
print(forma1, f'Área: {forma1.calc_area():.2f}')
print(forma1, f'Área: {forma2.calc_area():.2f}')
print(forma1, f'Área: {forma3.calc_area():.2f}')