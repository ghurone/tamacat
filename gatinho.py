from random import randint


class Gatinho:
    
    def __init__(self, nome):
        self.nome = nome
        self.dormindo = False
        self.idade = 0
        
        self.humores = ['feliz', 'triste', 'agitado', 'cansado', 'quieto', 'brincalhão', 'assustado']
        
        self.humor = self.humores[randint(0, len(self.humores))]
        
    def comer(self): 
        if not self.dormindo:
            # criar a classe comida sei lá
            pass
        else:
            print(f'{self.nome} está dormindo...')
    
    def brincar(self):
        if not self.dormindo:
            # lista de brincadeiras? classe nova?
            pass
        else:
            print(f'{self.nome} está dormindo, acorde-o para brincar!')
    
    def dormir(self):
        self.dormindo = True
        print('zzZzZzzzz')
        
    def acordar(self):
        self.dormindo = False
        print(f'{self.nome} acordou!')
    
    def miar(self):
        print('Miau!')

    @staticmethod
    def lamber():
        # :P
        print(':P')

    def mostrar_humor(self):
        print(f'{self.nome} está {self.humor}')
        
    def mudar_humor(self, i):
        self.humor = self.humores[i]
