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

    def __lt__(self, other):
        return self.dura < other.dura

    def __gt__(self, other):
        return self.dura > other.dura

    def __le__(self, other):
        return self.dura <= other.dura

    def __ge__(self, other):
        return self.dura >= other.dura

    def __eq__(self, other):
        return self.dura == other.dura

    def __ne__(self, other):
        return self.dura != other.dura

    def lt(self, other):
        return self.feliz < other.feliz

    def gt(self, other):
        return self.feliz > other.feliz

    def le(self, other):
        return self.feliz <= other.feliz

    def ge(self, other):
        return self.feliz >= other.feliz

    def eq(self, other):
        return self.feliz == other.feliz

    def ne(self, other):
        return self.feliz != other.feliz
