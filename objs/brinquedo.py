from objs.brincadeiras.bolinha import jogo_bolinhas
from objs.brincadeiras.navezinha import jogo_nave


class Brinquedo:

    def __init__(self, nome, feliz, dura):
        self.nome = nome
        self.feliz = feliz
        self.dura = dura

    def __str__(self):
        return self.nome.center(32) + '|' + f'{self.feliz}'.center(22) + '|' + f'{self.dura}'.center(22)

    def usar(self, valor=1):
        """ Diminui a durabilidade do brinquedo."""
        self.dura -= valor

    def quebrou(self):
        return self.dura == 0

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


class Bola(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    def brincadeira(self, gato):
        # como jogar
        return jogo_bolinhas(self.feliz)


class Caixa(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    def brincadeira(self, gato):
        # animação
        pass


class Varinha(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    def brincadeira(self, gato):
        # como jogar
        pass


class Arranhador(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    def brincadeira(self, gato):
        # como jogar
        pass


class Torre(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    def brincadeira(self, gato):
        # como jogar
        pass


class Nave(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    @staticmethod
    def brincadeira(gato):
        # como jogar
        return jogo_nave(gato.nome)


class Ioio(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    def brincadeira(self, gato):
        # animação
        pass


class Ratinho(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    def brincadeira(self, gato):
        # como jogar
        pass

