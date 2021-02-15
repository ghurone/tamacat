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

    coord = []
    i = 0
    while i != 9:
        xn, yn = randint(3, 76), randint(1, 18)
        if not (meio_x-2 <= xn <= meio_x+2 and meio_y-1 <= yn <= meio_y+1):
            coord.append((xn, yn))
            i += 1

    for i in range(20):
        linha = []
        y = 0

        for j in range(80):
            if j == 0:
                linha.append('|')
            elif j == 79:
                linha.append('|\n')
            elif meio_x-2 <= j <= meio_x+2 and meio_y-1 <= i <= meio_y+1:
                linha.append(bolinha[x][y])
                if y == 4:
                    x += 1
                y += 1
            else:
                linha.append(' ')

        miolo.append(linha)

    c = 0
    k = 0
    while k != 10:
        if k != n:
            b, a = coord[c]
            miolo[a][b] = str(k)
            c += 1
        k += 1

    tela = '+' + '-' * 78 + '+\n'

    for i in range(20):
        for j in range(80):
            tela += miolo[i][j]

    tela += '+' + '-' * 78 + '+'

    print(tela)


def bolinhas():

    for i in range(5):

        n = randint(0, 9)
        print_tela(n)
        t0 = time()
        esc = input('>>> ')
        t = time() - t0

        if t > 1 or esc != str(n):
            print('perdeu otario')
            return False

    print('uhu ganhou')
    return True


bolinhas()
