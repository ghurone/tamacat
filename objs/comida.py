class Comida:

    def __init__(self, nome, saciar, saude):
        self.nome = nome
        self.saciar = saciar
        self.saude = saude

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


class Bebida(Comida):
    def __init__(self, nome, saciar, saude):
        super().__init__(nome, saciar, saude)


class Salgado(Comida):
    def __init__(self, nome, saciar, saude):
        super().__init__(nome, saciar, saude)


class Doce(Comida):
    def __init__(self, nome, saciar, saude):
        super().__init__(nome, saciar, saude)


class Fruta(Comida):
    def __init__(self, nome, saciar, saude):
        super().__init__(nome, saciar, saude)
