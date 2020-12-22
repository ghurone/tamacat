from objs.gatinho import Gatinho
from objs.geladeira import Geladeira
from objs.bau import Bau
from client import entrar

from time import sleep
from os import system
from random import randint

# self.humores = ['feliz', 'triste', 'agitado', 'cansado', 'quieto', 'brincalhão', 'assustado', 'irritado']

objetos = entrar()

if not objetos:
    system('cls')

    print('Você está pensando em ter um gato.')
    sleep(2)
    print('\nUm amigo seu conhece alguém que está vendendo um gato bonitininho.')
    sleep(3)
    print('Mas também tem um gato que sempre têm andado pela vizinhança, e ele parece muito simpático.')
    sleep(3.5)
    print('Por outro lado, também existe um abrigo de gatos perto da sua casa.')
    sleep(3)

    escolha = input('\nVocê deseja (C)omprar, (R)esgatar ou (A)dotar o gato?\n>>> ')
    while escolha.lower() != 'c' and escolha.lower() != 'r' and escolha.lower() != 'a':
        escolha = input('Você deve digitar C, R ou A para decidir como conseguirá o seu gatinho:\n>>> ')

    system('cls')

    if escolha in 'Cc':
        print('Você conversou com o conhecido do seu amigo e comprou o gatinho!')
        idade = randint(2, 12)

    elif escolha in 'Rr':
        print('Você resgatou o gatinho. Agora ele tem um dono!')
        idade = randint(0, 180)

    else:
        i = input('Você vai adotar um gato (F)ilhote ou (A)dulto?\n>>> ')

        while i.lower() != 'f' and i.lower() != 'a':
            i = input('Você deve digitar F ou A para decidir a faixa etária do gato:\n>>> ')
        sleep(1)

        if i.lower() == 'f':
            idade = randint(3, 12)
        else:
            idade = randint(13, 84)

        print('Você foi até o abrigo e escolheu o seu gatinho. Ou será que foi ele quem te escolheu?')


    sleep(2)
    nome = input('Hora de uma decisão difícil... Qual vai ser o nome do seu gato?\n>>> ')

else:
    gato, geladeira, bau = objetos


