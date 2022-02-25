import janelas

from os import system
from random import randint, choice


def printar_tela(gato_name, tipo, r, m):
    """Printa a tela do jogo."""

    tipos_nave = {'parada': ["                         .-.   ",
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
                             """   ,                         `."""],
                  'voando': ["                         .-.   " + ' ' * (9 + len(gato_name)),
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
                             """   ,                         `.""" + ' ' * (9 + len(gato_name))],
                  'falhou': ["                         .-.                     ",
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
                  }

    g = 'G = 6.674 × 10⁻¹¹ m³•kg⁻¹•s⁻²'
    raio = f'R = {r} × 10⁶ m'.ljust(29)
    massa = f'M = {m} × 10²⁴ kg'.ljust(29)

    nave = tipos_nave[tipo]
    col = len(nave[0])

    janela = janelas.Janela()

    for i in range(21):
        janela.muda_slice(i+1, 1, col+1, nave[i])

    janela.muda_slice(17, 47, 76, g)
    janela.muda_slice(18, 47, 76, raio)
    janela.muda_slice(19, 47, 76, massa)

    # posiciona as estrelinhas aleatórias no miolo
    for _ in range(20):

        xn, yn = randint(1, 15), randint(2, 77)
        while janela[xn][yn] != ' ' or (xn == 1 and yn == 26):
            xn, yn = randint(1, 15), randint(2, 77)

        janela.muda_slice(xn, yn, yn+1, choice(['*', '*', '.']))

    print(janela)


def jogo_nave(gato_name):
    """Faz a mecânica geral do jogo."""

    system('color 0f')  # deixa a cor do jogo preta

    # gera as variáveis e o resultado da conta
    raio = float('6.' + str(randint(0, 999)))
    massa = choice([float('5.' + str(randint(500, 999))), float('6.' + str(randint(0, 499)))])
    result = round((2 * 6.674e-11 * massa * 1e24 / (raio * 1e6)) ** 0.5, 3)

    printar_tela(gato_name, 'parada', raio, massa)

    try:
        resp = float(input('>>> ').replace(',', '.'))
    except ValueError:  # caso não seja possível converter para float
        resp = 0.0

    # o jogador ganha se responder com precisão de 0,001
    if result - 0.001 <= resp <= result + 0.001:
        printar_tela(gato_name, 'voando', raio, massa)
        input('(Aperte ENTER para sair...)')
        system('color f0')  # volta a cor para branco
        return True

    else:
        printar_tela(gato_name, 'falhou', raio, massa)
        input('(Aperte ENTER para sair...)')

    system('color f0')  # volta a cor para branco
    return False
