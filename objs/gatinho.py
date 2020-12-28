class Gatinho:

    def __init__(self, nome, idade, fome, energia, saude, feliz, vac=False):
        self.nome = nome
        self.vacinado = vac

        self.dormindo = False
        self.idade = idade
        self.fome = fome
        self.energia = energia
        self.saude = saude
        self.feliz = feliz

    def comer(self, geladeira, comida):
        """Diminui a fome e altera a saúde dependendo dos níveis de saúde da Comida."""
        geladeira.pegar_comida(comida.nome)

        self.fome -= comida.saciar
        self.fome = self.atualizar_attr(self.fome)

        self.saude += comida.saude
        self.saude = self.atualizar_attr(self.saude)

    def brincar(self, bau, brinquedo):
        """?"""
        if not self.dormindo:
            # lista de brincadeiras? classe nova?
            pass
        else:
            print(f'{self.nome} está dormindo, acorde-o para brincar!')

    def dormir(self):
        """Muda o estado do gato para dormindo."""
        if not self.dormindo:
            self.dormindo = True
            print('zzZzZzzzz')
        else:
            print(f'{self.nome} já está dormindo!')

    def acordar(self):
        """Acorda o gato se ele estiver dormindo."""
        if self.dormindo:
            self.dormindo = False
            print(f'{self.nome} acordou!')
        else:
            print(f'{self.nome} já está acordado!')

    def crescer(self):
        """Aumenta a idade."""
        self.idade += 1

    @staticmethod
    def miar():
        print('Miau!')

    @staticmethod
    def lamber():
        # :P
        print(':P')

    @staticmethod
    def ronronar():
        print('rrrRRRRrrrRRr')

    @staticmethod
    def atualizar_attr(attr, sup=100, inf=0):
        if attr >= sup:
            return sup
        elif attr <= inf:
            return inf
        else:
            return attr


class Adotado(Gatinho):
    def __init__(self, nome, idade, fome, energia, saude, feliz, vac):
        super().__init__(nome, idade, fome, energia, saude, feliz, vac)

    def mostrar_idade(self):
        return self.idade


class Comprado(Gatinho):
    def __init__(self, nome, idade, fome, energia, saude, feliz, vac):
        super().__init__(nome, idade, fome, energia, saude, feliz, vac)

    def mostrar_idade(self):
        return self.idade


class Resgatado(Gatinho):
    def __init__(self, nome, idade, fome, energia, saude, feliz, vac):
        super().__init__(nome, idade, fome, energia, saude, feliz, vac)

    @staticmethod
    def mostrar_idade():
        return '?'
