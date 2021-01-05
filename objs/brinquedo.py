class Brinquedo:

    def __init__(self, nome, feliz, dura):
        self.nome = nome
        self.feliz = feliz
        self.dura = dura

    def __str__(self):
        return self.nome.center(32) + '|' + f'{self.feliz}'.center(22) + '|' + f'{self.dura}'.center(22)

    def usar(self):
        """ Diminui a durabilidade do brinquedo."""
        self.dura -= 1
