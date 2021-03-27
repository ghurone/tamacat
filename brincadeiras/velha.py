import brincadeiras.func as bfunc

import random
import time

ganhantes = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 4, 8), (6, 4, 2),
             (0, 3, 6), (1, 4, 7), (2, 5, 8)]


def check_vitoria(pos, figura):
    for p in ganhantes:
        if pos[p[0]] == figura and pos[p[1]] == figura and pos[p[2]] == figura:
            return True
    return False


def fscore(pos):

    if check_vitoria(pos, 'b'):
        s = 1
    elif check_vitoria(pos, 'g'):
        s = -1
    else:
        s = 0

    return s


def fim_jogo(pos):
    return check_vitoria(pos, 'b') or check_vitoria(pos, 'g')


def minmax(pos, depth, player):
    melhor = [-1, -100000] if player == 'b' else [-1, 100000]

    if depth == 0 or fim_jogo(pos):
        score = fscore(pos)
        return [-1, score]

    for i in pos:
        if i.isnumeric():
            pos_agora = pos[int(i)-1]
            pos[int(i)-1] = player
            score = minmax(pos, depth - 1, 'b' if player == 'g' else 'g')
            pos[int(i)-1] = pos_agora
            score[0] = i

            if player == 'b':
                if score[1] > melhor[1]:
                    melhor = score
            else:
                if score[1] < melhor[1]:
                    melhor = score

    return melhor


def bot_mov(pos, pos_ocup):
    depth = 8 if 9 - len(pos_ocup) < 8 else 9 - len(pos_ocup)

    if depth == 0 or fim_jogo(pos):
        return

    move = minmax(pos, depth, 'b')
    return move[0]


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


def print_tabuleiro(lista, msg=''):
    janela = bfunc.cjane.Janela()

    k, c = 0, 0
    for i in range(3, 20):
        if i == 3:
            janela.muda_linha(1, msg, 'ljust')
        elif i == 8 or i == 14:
            janela.muda_slice(i, 23, 58, '-' * 11 + '+' + '-' * 11 + '+' + '-' * 11)

            k = 0
            c += 3
        else:
            janela.muda_slice(i, 23, 58, lista[c][k] + '|' + lista[c + 1][k] + '|' + lista[c + 2][k])

            k += 1

    print(janela)


def jogar_velha():
    pos = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    pos_print = [quadrado(i) for i in pos]
    pos_ocup = []

    player_venceu = False
    comput_venceu = False
    velha = False
    player_turno = random.choice([True, False])

    while not player_venceu and not comput_venceu and not velha:
        msg = ' Sua vez!' if player_turno else ' Vez do dono'
        print_tabuleiro(pos_print, msg)

        if player_turno:

            esc = input('Selecione uma posição para jogar >>> ').lower()
            while len(esc) != 1 or not esc.isnumeric() or int(esc) not in range(1, 10) or esc in pos_ocup:
                print_tabuleiro(pos_print, msg)
                esc = input('Selecione uma posição para jogar >>> ').lower()

            figura = 'g'

        else:
            if len(pos_ocup) == 0:
                esc = str(random.randint(1, 9))
                while esc in pos_ocup:
                    esc = str(random.randint(1, 9))
            else:
                esc = bot_mov(pos, pos_ocup)

            figura = 'b'
            time.sleep(2)

        if str(esc) != '-1':
            pos_print[int(esc) - 1] = quadrado(figura)
            pos[int(esc) - 1] = figura

            pos_ocup.append(esc)

        # Checar vitoria
        if check_vitoria(pos, figura):
            if player_turno:
                player_venceu = True
            else:
                comput_venceu = True

        if len(pos_ocup) == 9 and not player_venceu and not comput_venceu:
            velha = True

        player_turno = False if player_turno else True

    print_tabuleiro(pos_print)

    if player_venceu:
        input('Você venceu seu dono! [Pressione ENTER para voltar...]')
        return True

    elif comput_venceu:
        input('O seu dono venceu... [Pressione ENTER para voltar...]')
    else:
        input('Deu velha :/ [Pressione ENTER para voltar...]')
    return False
