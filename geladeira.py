class Geladeira:

    def __init__(self, alimentos=None):
        if alimentos is None:
            alimentos = {}

        self.alimentos = alimentos

    def add_comida(self, comida, quantidade):
        try:
            self.alimentos[comida.nome][1] += quantidade
        except KeyError:
            self.alimentos[comida.nome] = [comida, quantidade]

    def pegar_comida(self, nome, quantidade):
        self.alimentos[nome][1] -= quantidade

        if self.alimentos[nome][1] == 0:
            del self.alimentos[nome]
