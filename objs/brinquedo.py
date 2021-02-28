from objs.brincadeiras.bolinha import jogo_bolinhas
from objs.brincadeiras.navezinha import jogo_nave
from objs.brincadeiras.func import como_jogar


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
        cont = ['  A tela será preenchida com todos os algarismos de 0 a 9, e um deles',
                ' estará dentro da bolinha.', '',
                '  Pegue a bolinha ao teclar o algarismo contido nela, o mais',
                ' rápido que puder! Isso acontecerá repetidas vezes, dependendo do',
                ' tipo de bolinha escolhida.', '',
                '  Caso digite o algarismo errado ou seja muito lento, perderá o jogo.']
        como_jogar('Jogo da Bolinha', cont)
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
        cont = ['  Você é um gatinho astronauta!', '',
                '  Para viajar à Lua, calcule corretamente a velocidade de escape necessária',
                ' para a nave decolar, usando os seguintes dados fornecidos:', '',
                '   Constante Gravitacional Universal (G)',
                '   Massa da Terra (M)',
                '   Raio da Terra (R)', '',
                '  Os aparelhos de medida usados para medir M e R nem sempre estão calibrados,',
                ' então podem haver divergências desses valores com os valores do Google.', '',
                '  - Note e adote:'.center(78),
                '          _______'.center(78),
                '         / 2 G M |'.center(78),
                ' v = _  / ―――――――'.center(78),
                '                                    \\/     R',
                ]
        como_jogar('Jogo da Nave', cont)
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

