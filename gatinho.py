from random import randint


class Gatinho:
    
    def __init__(self, nome):
        self.nome = nome
        self.dormindo = False
        self.idade = 0
        self.fome = 0

        self.humores = ['feliz', 'triste', 'agitado', 'cansado', 'quieto', 'brincalhão', 'assustado', 'irritado']
        
        self.humor = self.humores[randint(0, len(self.humores))]
        
    def comer(self, geladeira, comida):
        if not self.dormindo:
            # criar a classe comida sei
            pass
        else:
            print(f'{self.nome} está dormindo...')
    
    def brincar(self, bau, brinquedo):
        if not self.dormindo:
            # lista de brincadeiras? classe nova?
            pass
        else:
            print(f'{self.nome} está dormindo, acorde-o para brincar!')
    
    def dormir(self):
        if not self.dormindo:
            self.dormindo = True
            print('zzZzZzzzz')
        else:
            print(f'{self.nome} já está dormindo!')
        
    def acordar(self):
        if self.dormindo:
            self.dormindo = False
            print(f'{self.nome} acordou!')
        else:
            print(f'{self.nome} já está acordado!')
    
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

    def mostrar_humor(self):
        print(f'{self.nome} está {self.humor}')
        
    def mudar_humor(self, i):
        self.humor = self.humores[i]

    def crescer(self):
        self.idade += 1
