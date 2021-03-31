import brincadeiras.func as bfunc

import random
from time import sleep
from math import inf


ganhantes = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 4, 8), (6, 4, 2),
             (0, 3, 6), (1, 4, 7), (2, 5, 8)]


def check_vitoria(pos, figura):
    for p in ganhantes:
        if pos[p[0]] == figura and pos[p[1]] == figura and pos[p[2]] == figura:
            return True
    return False


def check_vazios(pos):
    for i in pos:
        if i.isnumeric():
            return True
    return False


def fim_jogo(pos):
    return check_vitoria(pos, 'b') or check_vitoria(pos, 'g')


def minmax(pos, depth, player):
    max_player = 'b'
    other_player = 'b' if player == 'g' else 'g'
    novo_pos = pos[:]

    if check_vitoria(novo_pos, other_player):
        return {'pos': None, 'score': depth if other_player == max_player else -depth}
    elif not check_vazios(novo_pos) or depth == 0:
        return {'pos': None, 'score': 0}

    melhor = {'position': None, 'score': -inf} if player == max_player else {'pos': None, 'score': inf}

    for i in novo_pos:
        if i.isnumeric():
            novo_pos[int(i)] = player
            score = minmax(novo_pos, depth - 1, 'b' if player == 'g' else 'g')

            novo_pos[int(i)] = str(i)
            score['pos'] = i

            if player == max_player:
                if score['score'] > melhor['score']:
                    melhor = score
            else:
                if score['score'] < melhor['score']:
                    melhor = score

    return melhor


def bot_mov(pos, pos_ocup):
    if 9 - len(pos_ocup) >= 3:
        depth = 3

    else:
        depth = 9 - len(pos_ocup)

    print(depth)
    if depth == 0 or fim_jogo(pos):
        return

    move = minmax(pos, depth, 'b')
    return move['pos']


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
    pos = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
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
            while len(esc) != 1 or not esc.isnumeric() or int(esc) not in range(9) or esc in pos_ocup:
                print_tabuleiro(pos_print, msg)
                esc = input('Selecione uma posição para jogar >>> ').lower()

            figura = 'g'

        else:
            if len(pos_ocup) == 0:
                esc = str(random.randint(0, 8))
                while esc in pos_ocup:
                    esc = str(random.randint(0, 8))
            else:
                esc = bot_mov(pos, pos_ocup)

            figura = 'b'
            sleep(2)

        if esc is not None:
            pos_print[int(esc)] = quadrado(figura)
            pos[int(esc)] = figura

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
