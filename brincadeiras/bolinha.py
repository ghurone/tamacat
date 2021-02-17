from func import faz_matriz

from time import time
from random import randint


def criar_bola(num):
    bola = [' .-. ',
            f'| {num} |',
            " '-' "]

    return bola


def print_tela(n):
    miolo = []

    meio_x = randint(3, 76)
    meio_y = randint(1, 18)
    bolinha = criar_bola(n)

    x = 0
    for i in range(21):
        linha = []

        y = 0
        for j in range(80):
            if j == 0:
                linha.append('|')
            elif j == 79:
                linha.append('|\n')
            elif meio_x - 2 <= j <= meio_x + 2 and meio_y - 1 <= i <= meio_y + 1:
                linha.append(bolinha[x][y])
                if y == 4:
                    x += 1
                y += 1
            else:
                linha.append(' ')

        miolo.append(linha)

    k = 0
    while k != 10:
        if k != n:
            xn, yn = randint(1, 18), randint(3, 76)

            while meio_x - 2 <= xn <= meio_x + 2 and meio_y - 1 <= yn <= meio_y + 1 and miolo[xn][yn] != ' ':
                xn, yn = randint(1, 18), randint(3, 76)

            miolo[xn][yn] = str(k)

        k += 1

    tela = '+' + '-' * 78 + '+\n'
    tela += faz_matriz(miolo)
    tela += '+' + '-' * 78 + '+'

    print(tela)


def jogo_bolinhas():

    # COMO JOGAR

    for i in range(5):

        n = randint(0, 9)
        print_tela(n)
        t0 = time()
        esc = input('>>> ')
        t = time() - t0

        if t > 1.5 or esc != str(n):
            input('Você perdeu, lesminha kk. Pressione ENTER para sair...')
            return False

    input('Vencedor! Você tem bons reflexos! Pressione ENTER para sair...')
    return True
