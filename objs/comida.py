class Comida:

    def __init__(self, nome, saciar, saude):
        self.nome = nome
        self.saciar = saciar
        self.saude = saude

    def __str__(self):
        return f'{self.nome} - Saciar: {self.saciar} - Saude: {self.saude}'
