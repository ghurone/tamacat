from objs.brincadeiras.func import faz_matriz

from os import system
from random import randint, choice
from time import time


def tipos_nave(gato_name, tipo=None):
    nave_parada = ["                         .-.   ",
                   "                        ( (    ",
                   "                         `-'   ",
                   "                               ",
                   "                               ",
                   "                               ",
                   "                               ",
                   "                               ",
                   "                               ",
                   "                               ",
                   "                               ",
                   "                               ",
                   "                    .          ",
                   "                   .'.         ",
                   "                   |o|         ",
                   "                  .'o'.        ",
                   "               ___|.-.|        ",
                   """          .-'""    ""`-.       """,
                   "       .-'              `-.    ",
                   "     ,'                   '`.  ",
                   """   ,                         `."""]

    nave_voando = ["                         .-.   " + ' ' * (9 + len(gato_name)),
                   "                        ( (    " + ' ' * (9 + len(gato_name)),
                   "                         `-'   " + ' ' * (9 + len(gato_name)),
                   "                               " + ' ' * (9 + len(gato_name)),
                   "                               " + ' ' * (9 + len(gato_name)),
                   "                               " + ' ' * (9 + len(gato_name)),
                   "                               " + ' ' * (9 + len(gato_name)),
                   f"                    .   ,- Rumo à Lua, {gato_name}!",
                   "                   .'.         " + ' ' * (9 + len(gato_name)),
                   "                   |o|         " + ' ' * (9 + len(gato_name)),
                   "                  .'o'.        " + ' ' * (9 + len(gato_name)),
                   "                  |.-.|        " + ' ' * (9 + len(gato_name)),
                   "                  '   '        " + ' ' * (9 + len(gato_name)),
                   "                   ( )         " + ' ' * (9 + len(gato_name)),
                   "                    )          " + ' ' * (9 + len(gato_name)),
                   "                   ( )         " + ' ' * (9 + len(gato_name)),
                   "               ____            " + ' ' * (9 + len(gato_name)),
                   """          .-'""    ""`-.       """ + ' ' * (9 + len(gato_name)),
                   "       .-'              `-.    " + ' ' * (9 + len(gato_name)),
                   "     ,'                   '`.  " + ' ' * (9 + len(gato_name)),
                   """   ,                         `.""" + ' ' * (9 + len(gato_name))]

    nave_falhou = ["                         .-.                     ",
                   "                        ( (                      ",
                   "                         `-'                     ",
                   "                                                 ",
                   "                                                 ",
                   "                                                 ",
                   "                                                 ",
                   "                                                 ",
                   "                                                 ",
                   "                  ,   ,                          ",
                   "                  |'-'|                          ",
                   "                  ',o,'                          ",
                   "                   |o|                           ",
                   "                   '.' ‛- Oh no, errei o cálculo!",
                   "                    ˙                            ",
                   "                                                 ",
                   "               ____                              ",
                   """          .-'""    ""`-.                         """,
                   "       .-'              `-.                      ",
                   "     ,'                   '`.                    ",
                   """   ,                         `.                  """]

    if tipo == 0:
        return nave_parada
    elif tipo == 1:
        return nave_voando
    elif tipo == 2:
        return nave_falhou

    return False


def printar_tela(gato_name, tipo, r, m):
    G = 'G = 6.674 × 10⁻¹¹ m³•kg⁻¹•s⁻²'
    raio = f'R = {r} × 10⁶ m'.ljust(29)
    massa = f'M = {m} × 10²⁴ kg'.ljust(29)

    nave = tipos_nave(gato_name, tipo)
    col = len(nave[0])

    miolo = []

    for i in range(21):
        linha = []

        for j in range(80):
            if j == 0:
                linha.append('|')
            elif j == 79:
                linha.append('|\n')
            elif i == 17 and 46 < j < 76:
                linha.append(G[j-47])
            elif i == 18 and 46 < j < 76:
                linha.append(raio[j-47])
            elif i == 19 and 46 < j < 76:
                linha.append(massa[j-47])
            elif j <= col:
                linha.append(nave[i][j-1])
            else:
                linha.append(' ')

        miolo.append(linha)

    for _ in range(20):

        xn, yn = randint(1, 15), randint(2, 77)
        while miolo[xn][yn] != ' ' or (xn == 1 and yn == 26):
            xn, yn = randint(1, 15), randint(2, 77)

        miolo[xn][yn] = choice(['*', '*', '.'])

    tela = '+' + '-' * 78 + '+\n'
    tela += faz_matriz(miolo)
    tela += '+' + '-' * 78 + '+'

    print(tela)


def jogo_nave(gato_name):

    # COMO JOGAR
    system('color 0f')

    raio = float('6.' + str(randint(0, 999)))
    massa = choice([float('5.' + str(randint(500, 999))), float('6.' + str(randint(0, 499)))])
    result = round((2 * 6.674e-11 * massa * 1e24 / (raio * 1e6)) ** 0.5, 3)

    printar_tela(gato_name, 0, raio, massa)

    t0 = time()

    try:
        resp = float(input('>>> '))
    except ValueError:
        resp = 0.0

    t = time() - t0

    if t <= 60 and (result - 0.001 <= resp <= result + 0.001):
        printar_tela(gato_name, 1, raio, massa)
        input('Pressione ENTER para sair...')
        system('color f0')
        return True

    elif t <= 60 and not (result - 0.001 <= resp <= result + 0.001):
        printar_tela(gato_name, 2, raio, massa)
        input('Pressione ENTER para sair...')

    else:
        printar_tela(gato_name, 0, raio, massa)
        input('Tempo esgotado! Pressione ENTER para sair...')

    system('color f0')
    return False
