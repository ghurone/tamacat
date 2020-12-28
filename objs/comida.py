class Comida:

    def __init__(self, nome, saciar, saude, feliz):
        self.nome = nome
        self.saciar = saciar
        self.saude = saude
        self.feliz = feliz

    def __str__(self):
        return f'{self.nome} - Saciar: {self.saciar} - Saude: {self.saude}'
