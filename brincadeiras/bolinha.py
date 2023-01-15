import janelas

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
    meio_x = randint(2, 20)
    meio_y = randint(3, 76)

    bolinha = criar_bola(n)

    janela = janelas.Janela()

    janela.muda_slice(meio_x-1, meio_y - 2, bolinha[0])
    janela.muda_slice(meio_x, meio_y - 2,  bolinha[1])
    janela.muda_slice(meio_x + 1, meio_y - 2, bolinha[2])

    # coloca os algarismos de 0 a 9 no miolo, diferentes do algarismo dentro da bolinha
    k = 0
    while k != 10:
        if k != n:

            # coordenadas do algarismo
            xn, yn = randint(2, 20), randint(3, 76)

            # não deixa o algarismo aparecer dentro da bolinha ou em um caractere que não esteja em branco
            while (meio_x - 1 <= xn <= meio_x + 1 and meio_y - 2 <= yn <= meio_y + 2) or janela[xn][yn] != ' ':
                xn, yn = randint(2, 20), randint(3, 76)

            janela.muda_slice(xn, yn, yn+1, str(k))

        k += 1

    print(janela)


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
            input('Você perdeu, lesminha kkkkk (Aperte ENTER para sair...)')
            return False

    input('Vencedor! Você tem bons reflexos! (Aperte ENTER para sair...)')
    return True
