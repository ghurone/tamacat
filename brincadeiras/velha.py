import brincadeiras.func as bfunc

import random

def quadrado(coisa):
    if coisa == 'g':
        s = ["           ",
             "    , / ,  ",
             "   / / /   ",
             "  ´ / ´    ",
             "           "]
    elif coisa == 'b':
        s = ["           ",
             "    .-.    ",
             "   |   |   ",
             "    '-'    ",
             "           "]
    else:
        s = []
        for i in range(5):
            s.append(' '.center(11) if i != 2 else f'{coisa}'.center(11))

    return s


def print_tabuleiro(lista):
    janela = bfunc.cjane.Janela()

    k, c = 0, 0
    for i in range(3, 20):
        if i == 8 or i == 14:
            janela.muda_slice(i, 23, 58, '-'*11 + '+' + '-'*11 + '+' + '-'*11)

            k = 0
            c += 3
        else:
            janela.muda_slice(i, 23, 58, lista[c][k] + '|' + lista[c+1][k] + '|' + lista[c+2][k])

            k += 1

    print(janela)


def jogar_velha():
    pos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    pos_print = [quadrado(i) for i in pos]
    pos_ocup = []

    player_venceu = False
    comput_venceu = False
    quem_comeca = random.choice([True, False])

    while not player_venceu and not comput_venceu:
        print_tabuleiro(pos_print)

        esc = input('Selecione uma posição para jogar >>> ').lower()
        while len(esc) != 1 or not esc.isnumeric() or int(esc) not in range(1, 10) or esc in pos_ocup:
            print_tabuleiro(pos_print)
            esc = input('Selecione uma posição para jogar >>> ').lower()

        pos_ocup.append(esc)


jogar_velha()