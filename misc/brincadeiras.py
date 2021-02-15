from time import time
from random import randint


def BOLA(num):
    bola = [' .-. ',
            f'| {num} |',
            " '-' "]

    for i in bola:
        print(i)


def print_tela():

    miolo = []

    for i in range(20):
        linha = []

        for j in range(80):
            if j == 0:
                linha.append('|')
            elif j == 79:
                linha.append('|\n')
            else:
                linha.append('0')

        miolo.append(linha)

    tela = '+' + '-' * 78 + '+\n'

    for i in range(20):
        for j in range(80):
            tela += miolo[i][j]

    tela += '+' + '-' * 78 + '+'

    print(tela)


def bolinhas():
    print_tela()
    esc = input('>>> ')


bolinhas()
