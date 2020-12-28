from objs.gatinho import Adotado, Comprado, Resgatado
from objs.geladeira import Geladeira
from objs.bau import Bau
from objs.brinquedo import Brinquedo
from objs.comida import Comida
from save.client import entrar
from save.sql import SQL

from time import sleep
from os import system, name as osname
from random import randint, choice

humores = ['feliz', 'triste', 'quieto', 'brincalhão', 'carinhoso', 'assustado', 'irritado']


def limpar_tela():
    if 'nt' in osname:
        system('cls')
    else:
        system('clear')


def salvar_jogo(ide, gato, geladeira, bau):
    banco = SQL()
    banco.salvar_jogo(ide, gato, geladeira, bau)
    banco.close()


def novo_gato():
    """Retorna um Gatinho, Geladeira e Bau para um gato inicial."""
    #limpar_tela()

    print('Você está pensando em ter um gato.')
    #sleep(2)
    print('\nUm amigo seu conhece alguém que está vendendo um gato bonitininho.')
    #sleep(3)
    print('Mas também tem um gato que sempre têm andado pela vizinhança, e ele parece muito simpático.')
    #sleep(3.5)
    print('Por outro lado, também existe um abrigo de gatos perto da sua casa.')
    #sleep(3)

    escolha = input('\nVocê deseja (C)omprar, (R)esgatar ou (A)dotar o gato?\n>>> ')
    while escolha.lower() != 'c' and escolha.lower() != 'r' and escolha.lower() != 'a'\
            and escolha.lower() != 'comprar' and escolha.lower() != 'resgatar' and escolha.lower() != 'adotar':
        escolha = input('Você deseja (C)omprar, (R)esgatar ou (A)dotar o gato?\n>>> ')

    #limpar_tela()

    if escolha[0] in 'Cc':
        print('Você conversou com o conhecido do seu amigo e comprou o gatinho!')

        idade = randint(2, 12)
        fome = 0
        energia = randint(75, 100)
        saude = 100
        humor = choice(humores)
        vac = True

        ga = Comprado('', idade, fome, energia, saude, humor, vac)

    elif escolha[0] in 'Rr':
        print('Você resgatou o gatinho. Agora ele tem um dono!')

        idade = randint(0, 180)
        fome = randint(0, 90)
        energia = randint(10, 90)
        saude = randint(10, 50)
        humor = 'assustado'
        vac = choice([True, False])

        ga = Resgatado('', idade, fome, energia, saude, humor, vac)

    else:
        i = input('Você vai adotar um gato (F)ilhote ou (A)dulto?\n>>> ')

        while i.lower() != 'f' and i.lower() != 'a' and i.lower() != 'filhote' and i.lower() != 'adulto':
            i = input('Você vai adotar um gato (F)ilhote ou (A)dulto?\n>>> ')
        #sleep(1)

        print('Você foi até o abrigo e escolheu o seu gatinho. Ou será que foi ele quem te escolheu?')

        if i[0].lower() == 'f':
            idade = randint(3, 12)
        else:
            idade = randint(13, 84)

        fome = randint(0, 40)
        energia = randint(70, 100)
        saude = randint(70, 90)
        humor = choice(humores)
        vac = choice([True, True, True, False, False])  # True: 60%, False: 40%

        ga = Adotado('', idade, fome, energia, saude, humor, vac)

    #sleep(2)
    nome = input('Hora de uma decisão difícil... Qual vai ser o nome do seu gato?\n>>> ')

    ga.nome = nome
    ge = Geladeira()
    ba = Bau()

    return ga, ge, ba


def mostrar_gato(cat):
    """Imprime as características do gato."""
    print('Nome:', cat.nome)
    print('Idade:', cat.mostrar_idade())
    print('Fome:', cat.fome)
    print('Energia:', cat.energia)
    print('Saude:', cat.saude)
    print('Humor:', cat.humor)
    print('Vac:', cat.vacinado)


if __name__ == '__main__':
    objetos = entrar()
    user_id = objetos['user_id']

    if objetos['gato'] is not None:
        gato = objetos['gato']
        gela = objetos['gela']
        bau = objetos['bau']

    else:
        gato, gela, bau = novo_gato()
        salvar_jogo(user_id, gato, gela, bau)

    mostrar_gato(gato)
