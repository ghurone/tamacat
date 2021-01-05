class Comida:

    def __init__(self, nome, saciar, saude, feliz):
        self.nome = nome
        self.saciar = saciar
        self.saude = saude
        self.feliz = feliz

    def __str__(self):
        return self.nome.center(29) + '|' + f'{self.saciar}'.center(13) + '|' + f'{self.saude}'.center(13) + '|' + f'{self.feliz}'.center(13)
