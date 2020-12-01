class Geladeira:

    def __init__(self, alimentos=None):
        if alimentos is None:
            alimentos = {}

        self.alimentos = alimentos

    def add_comida(self, comida, quantidade):
        try:
            self.alimentos[comida] += quantidade
        except KeyError:
            self.alimentos = quantidade

    def pegar_comida(self, comida, quantidade):
        self.alimentos[comida] -= quantidade

        if self.alimentos[comida] == 0:
            del self.alimentos[comida]
