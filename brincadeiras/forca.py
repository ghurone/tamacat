import brincadeiras.func as bfunc


def ratinho(err):
    cabeca = [' _ │ _ ',
              '(q\┴/p)',
              ' |. .| ',
              ' =\,/= ']

    corpo = ['   |   ' for _ in range(4)]

    if err == 0:
        return []

    elif err == 1:
        return cabeca

    elif err == 3:
        corpo[1] = '   |\  '
    if err >= 4:
        corpo[1] = '  /|\  '
        if err == 5:
            corpo += ['  /    ']
        elif err == 6:
            corpo += ['  / \  ']
    return cabeca + corpo


def printar_forca(lista_char, err=0):
    rato = ratinho(err)
    janela = bfunc.cjane.Janela()

    janela.muda_slice(5, 3, 17, '-'*16)
    janela.muda_slice(6, 3, 17, '|            |')
    for i in range(7,19):
        janela.muda_slice(i, 3, 4, '|')

    k = 0
    for i in range(len(lista_char)):
        janela.muda_slice(16, i+k+28, i+k+30, f'{lista_char[i]} ' if lista_char[i].isalpha() else '_ ' )
        k += 1

    print(janela)

printar_forca(['', '', '', ''])