def faz_matriz(matriz):
    """Representa uma matriz como string."""

    col = len(matriz[0])
    lin = len(matriz)

    s = ''

    for i in range(lin):
        for j in range(col):
            s += matriz[i][j]

    return s


def como_jogar(titulo, conteudo):
    """Cria a tela de "como jogar" para um jogo, recebendo o título e as instruções daquele jogo."""

    s = '+' + '-'*78 + '+\n'
    s += '|' + f'{titulo.upper()}'.center(78) + '|\n'
    s += '|' + ' ' * 78 + '|\n'
    s += '|' + '  - INSTRUÇÕES:'.ljust(78) + '|\n'
    s += '|' + ' ' * 78 + '|\n'

    for i in range(17):
        try:
            linha = conteudo[i]
            s += '|' + linha.ljust(78) + '|\n'
        except IndexError:
            s += '|' + ' ' * 78 + '|\n'

    s += '+' + '-' * 78 + '+'

    print(s)
    input('Pressione ENTER para jogar!')
