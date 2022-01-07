class Gatinho:

    def __init__(self, nome, idade, fome, energia, saude, feliz, gen, vac):
        self.nome = nome
        self.idade = idade
        self.fome = fome
        self.energia = energia
        self.saude = saude
        self.feliz = feliz
        self.vacinado = vac
        self.dormindo = False
        
        self.gen = gen
        
        if gen == 'F':
            self.gens = {'pron': 'a', 'um': 'a', 'letra': 'a'}
        
        elif gen == 'M':            
            self.gens = {'pron': 'e', 'um': '', 'letra': 'o'}

    def comer(self, geladeira, comida):
        """Diminui a fome e altera a saúde dependendo dos níveis de saúde da Comida."""
        geladeira.pegar_comida(comida)

        self.fome = self.atualizar_attr(self.fome, comida.saciar)
        self.saude = self.atualizar_attr(self.saude, comida.saude)

    def brincar(self, bau, brinquedo):
        """Realiza as ações resultantes da brincadeira no objeto gatinho, no baú e no próprio brinquedo."""

        # resultado da brincadeira (se ganhou ou perdeu)
        res = brinquedo.brincadeira(self)

        if res:
            self.feliz = self.atualizar_attr(self.feliz, brinquedo.feliz)

        brinquedo.usar()
        if brinquedo.quebrou():
            bau.remover_brinquedo(brinquedo)

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
    def atualizar_attr(attr, valor, sinal=1, sup=100, inf=0):
        """Atualiza um atributo, não permitindo que ele exceda
        seus limites superior ou inferior ao ser atualizado."""

        attr += valor*sinal

        if attr >= sup:
            return sup
        elif attr <= inf:
            return inf
        else:
            return attr

    def mostrar_idade(self):
        """Firulas para printar a idade bonitinha."""

        mes = self.idade % 12
        ano = self.idade // 12
        
        if ano == 0:
            return f'{mes} meses'
        
        elif mes == 0:
            if ano == 1:
                return '1 ano'
            else:
                return f'{ano} anos'

        elif mes == 1:
            if ano == 1:
                return f'1 ano e 1 mês'
            else:
                return f'{ano} anos e 1 mês'
        
        elif ano == 1:
            return f'1 ano e {mes} meses'

        return f'{ano} anos e {mes} meses'


class Adotado(Gatinho):
    def __init__(self, nome, idade, fome, energia, saude, feliz, gen, vac):
        super().__init__(nome, idade, fome, energia, saude, feliz, gen, vac)


class Comprado(Gatinho):
    def __init__(self, nome, idade, fome, energia, saude, feliz, gen, vac):
        super().__init__(nome, idade, fome, energia, saude, feliz, gen, vac)


class Resgatado(Gatinho):
    def __init__(self, nome, idade, fome, energia, saude, feliz, gen, vac):
        super().__init__(nome, idade, fome, energia, saude, feliz, gen, vac)

    def mostrar_idade(self):
        
        if not self.vacinado:
        
            if self.idade <= 12:
                return 'Filhote'
            
            elif 12 < self.idade < 84:
                return 'Adult' + self.gens['letra']
            
            else:
                return 'Idos' + self.gens['letra']
        
        else:
            pass
            
            