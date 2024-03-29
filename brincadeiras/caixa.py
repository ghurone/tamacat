import janelas
import config.funcoes as cfunc

import time


def gato(n):
    gatos = [["      ,-.       _,---._ __  / \\  ",
              "     /  )    .-'       `./ /   \\ ",
              "    (  (   ,'            `/    /|",
              '     \  `-"             \\\'\   / |',
              "      `.              ,  \\ \\ /  |",
              "       /`.          ,'-`----Y   |",
              "      (            ;        |   '",
              "      |  ,-.    ,-'         |  / ",
              "      |  | (   |            | /  ",
              "      )  |  \\  `.___________|/   ",
              "      `--'   `--'                "],

             ["  ,-.           _,---._ __  / \\  ",
              "  |  \\       .-'       `./ /   \\ ",
              "   \\  \\    ,'            `/    /|",
              '     \  `-"             \\\'\   / |',
              "      `.              ,  \\ \\ /  |",
              "       /`.          ,'-`----Y   |",
              "      (            ;        |   '",
              "      |  ,-.    ,-'         |  / ",
              "      |  | (   |            | /  ",
              "      )  |  \\  `.___________|/   ",
              "      `--'   `--'                "],

             ["     .-,        _,---._ __  / \\  ",
              "    (  \\     .-'       `./ /   \\ ",
              "     )  )  ,'            `/    /|",
              '     \  `-"             \\\'\   / |',
              "      `.              ,  \\ \\ /  |",
              "       /`.          ,'-`----Y   |",
              "      (            ;        |   '",
              "      |  ,-.    ,-'         |  / ",
              "      |  | (   |            | /  ",
              "      )  |  \\  `.___________|/   ",
              "      `--'   `--'                "],

             ["    .-,         _,---._ __  / \\  ",
              "    \  \     .-'       `./ /   \\ ",
              "     )  )  ,'            `/    /|",
              '     \  `-"             \\\'\   / |',
              "      `.              ,  \\ \\ /  |",
              "       /`.          ,'-`----Y   |",
              "      (            ;        |   '",
              "      |  ,-.    ,-'         |  / ",
              "      |  | (   |            | /  ",
              "      )  |  \\  `.___________|/   ",
              "      `--'   `--'                "]]

    return gatos[n - 1]


def print_anima(gato_frame, total, momento):
    janela = janelas.Janela()
    porc = (momento / total)

    for i in range(23):
        if i in range(3, 3+len(gato_frame)):
            janela.muda_slice(i, 0, gato_frame[i-3].center(80))
        elif i == 6+len(gato_frame):
            janela.muda_slice(i, 0, 'Explorando a caixinha'.rjust(50) + ('.'*(momento % 4)).ljust(30))
        elif i == 8+len(gato_frame):
            janela.muda_slice(i, 0, '['.rjust(6) + ('■'*int(68*porc)).ljust(68) + ']'.ljust(6))
        else:
            janela.muda_slice(i, 0, ' '.center(80))

    print(janela, end='\r')


def caixa_anima():
    animation = [gato(1), gato(4), gato(2), gato(4)]
    cfunc.limpar_tela()
    print()

    for i in range(len(animation) * 4):
        print_anima(animation[i % len(animation)], total=(len(animation) * 4)-1, momento=i)
        time.sleep(0.7)

    input('Você terminou de brincar! (Aperte ENTER para sair...)')