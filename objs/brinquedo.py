import brincadeiras.func as bfunc
import brincadeiras.forca as bforca
import brincadeiras.bolinha as bbola
import brincadeiras.navezinha as bnave
import brincadeiras.caixa as bcaixa
import brincadeiras.velha as bvelha
import brincadeiras.memoria as bmoria


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
        cont = ['  É hora de brincar com a bolinha!',
                '  A tela será preenchida com todos os algarismos de 0 a 9, e um deles',
                ' estará dentro da bolinha.', '',
                '  Pegue a bolinha ao teclar o algarismo contido nela, o mais',
                ' rápido que puder! Isso acontecerá repetidas vezes, dependendo do',
                ' tipo de bolinha escolhida.', '',
                f'  Caso digite o algarismo errado ou seja muito lent{gato.gens["letra"]}, perderá o jogo.']
        bfunc.como_jogar('Jogo da Bolinha', cont)

        return bbola.jogo_bolinhas(self.feliz)


class Caixa(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    @staticmethod
    def brincadeira(gato):
        bcaixa.caixa_anima()
        return True


class Varinha(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    def brincadeira(self, gato):
        # como jogar
        pass


class Arranhador(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    @staticmethod
    def brincadeira(gato):
        cont = ['  Enquanto você brincava no seu arranhador, o seu dono quis jogar uma',
                ' partida de jogo da velha.', '',
                '  Você vai arranhar e o seu dono irá colocar as bolinhas no tabuleiro.',
                '  É só teclar o número desejado!']
        bfunc.como_jogar('Jogo da Velha', cont)
        return bvelha.jogar_velha()


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
        cont = [f'  Você é um{gato.gens["um"]} gatinh{gato.gens["letra"]} astronauta!', '',
                '  Para viajar à Lua, calcule corretamente a velocidade de escape necessária',
                ' para a nave decolar, usando os seguintes dados fornecidos:', '',
                '    Constante Gravitacional Universal (G)',
                '    Massa da Terra (M)',
                '    Raio da Terra (R)', '',
                '  Os aparelhos de medida usados para medir M e R nem sempre estão calibrados,',
                ' então podem haver divergências desses valores com os valores do Google.', '',
                '  - Note e adote:'.center(78),
                '         _______ '.center(78),
                '        / 2 G M |'.center(78),
                'v = _  / ――――――― '.center(78),
                '     \\/     R    '.center(78),
                ]
        bfunc.como_jogar('Jogo da Nave', cont)

        return bnave.jogo_nave(gato.nome)


class Memoria(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    def brincadeira(self, gato):
        cont = ['  Você estava xeretando um armário e encontrou um jogo da memória!', '',
                '  Há 7 pares de cartas no jogo, e elas serão embaralhadas e viradas para',
                ' baixo. O seu objetivo é memorizar a localização das cartas e virar para',
                ' cima todos os pares.',
                '', '  A cada rodada, você terá que virar duas cartas. Se elas não formarem',
                ' um par, você perde uma vida.', '',
                '  Você tem apenas 4 vidas, então é melhor memorizar corretamente!'
                ]
        bfunc.como_jogar('Jogo da Memória', cont)
        return bmoria.jogar_memoria()


class Ratinho(Brinquedo):
    def __init__(self, nome, feliz, dura):
        super().__init__(nome, feliz, dura)

    def brincadeira(self, gato):
        cont = ['  Você capturou um rato e o seu objetivo é destruí-lo!',
                '', '  Para isso, jogue o clássico jogo da forca.', '',
                '  A diferença é: a cada erro, o ratinho estará mais perto de fugir,',
                ' então não deixe que ele escape!'
                ]
        bfunc.como_jogar('Jogo da Forca', cont)
        return bforca.jogar_forca()

