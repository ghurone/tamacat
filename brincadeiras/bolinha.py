import brincadeiras.func as bfunc

from time import time
from random import randint


def criar_bola(num):
    bola = [' .-. ',
            f'| {num} |',
            " '-' "]

    return bola


def print_tela(n):
    """Printa a tela do jogo."""

    # coordenadas centrais da bolinha
    meio_x = randint(3, 76)
    meio_y = randint(1, 18)

    bolinha = criar_bola(n)

    # faz o "grosso" do miolo + a bolinha
    # i e j percorrem o miolo, x e y percorrem a string da bolinha
    miolo = []
    x = 0
    for i in range(21):
        linha = []

        y = 0
        for j in range(80):
            if j == 0:
                linha.append('|')
            elif j == 79:
                linha.append('|\n')

            # não deixa a bolinha ser posicionada em um lugar estranho do miolo
            elif meio_x - 2 <= j <= meio_x + 2 and meio_y - 1 <= i <= meio_y + 1:
                linha.append(bolinha[x][y])
                if y == 4:
                    x += 1
                y += 1

            else:
                linha.append(' ')

        miolo.append(linha)

    # coloca os algarismos de 0 a 9 no miolo, diferentes do algarismo dentro da bolinha
    k = 0
    while k != 10:
        if k != n:

            # coordenadas do algarismo
            xn, yn = randint(1, 18), randint(3, 76)

            # não deixa o algarismo aparecer dentro da bolinha ou em um caractere que não esteja em branco
            while (meio_x - 2 <= xn <= meio_x + 2 and meio_y - 1 <= yn <= meio_y + 1) or miolo[xn][yn] != ' ':
                xn, yn = randint(1, 18), randint(3, 76)

            miolo[xn][yn] = str(k)

        k += 1

    tela = '+' + '-' * 78 + '+\n'
    tela += faz_matriz(miolo)
    tela += '+' + '-' * 78 + '+'

    print(tela)


def jogo_bolinhas(feli):
    """Faz a mecânica geral do jogo."""

    # define quantas "rodadas" o jogo vai ter, baseado na felicidade do brinquedo
    dif = feli//4

    for i in range(dif):

        n = randint(0, 9)  # gera o algarismo na bolinha
        print_tela(n)
        t0 = time()
        esc = input('>>> ')
        t = time() - t0

        if t > 1.5 or esc != str(n):
            input('Você perdeu, lesminha kk. Pressione ENTER para sair...')
            return False

    input('Vencedor! Você tem bons reflexos! Pressione ENTER para sair...')
    return True
