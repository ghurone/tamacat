class Comida:

    def __init__(self, nome, saciar, saude, feliz):
        self.nome = nome
        self.saciar = saciar
        self.saude = saude
        self.feliz = feliz

    def __lt__(self, other):
        return self.saciar < other.saciar

    def __gt__(self, other):
        return self.saciar > other.saciar

    def __le__(self, other):
        return self.saciar <= other.saciar

    def __ge__(self, other):
        return self.saciar >= other.saciar

    def __eq__(self, other):
        return self.saciar == other.saciar

    def __ne__(self, other):
        return self.saciar != other.saciar
