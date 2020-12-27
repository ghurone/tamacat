class Brinquedo:

    def __init__(self, nome, alegria, dura=100):
        self.nome = nome
        self.dura = dura
        self.alegria = alegria

    def __str__(self):
        return f'{self.nome} - Durabilidade: {self.dura} - Alegria: {self.alegria}'

    def usar(self, valor):
        self.dura -= valor
