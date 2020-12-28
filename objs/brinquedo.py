class Brinquedo:

    def __init__(self, nome, feliz, dura):
        self.nome = nome
        self.feliz = feliz
        self.dura = dura

    @property
    def __str__(self):
        return f'{self.nome} - Durabilidade: {self.dura} - Alegria: {self.alegria}'

    def usar(self):
        """ Diminui a durabilidade do brinquedo."""
        self.dura -= 1
