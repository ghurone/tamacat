class Brinquedo:

    def __init__(self, nome, alegria, dura=100):
        self.nome = nome
        self.dura = dura
        self.alegria = alegria

    def usar(self, valor):
        self.dura -= valor
