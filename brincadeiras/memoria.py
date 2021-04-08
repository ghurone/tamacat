import config.janela as cjane

animais = [['         ',
            '  _   _  ',
            ' (q\\_/p) ',
            '  |. .|  ',
            '  =\\,/=  ',
            '         ',
            '         '],

           ['         ',
            '    _\\_  ',
            ' |\/  o\\ ',
            ' |/\\___< ',
            "    ''   ",
            '         ',
            '         '],

           ['         ',
            ' |\\---/| ',
            ' | ° ° | ',
            '  \\_T_/  ',
            '         ',
            '         ',
            '         '],

           ['         ',
            ' /^---^\\ ',
            ' V o o V ',
            '  | Y |  ',
            '   -.-   ',
            '         ',
            '         '],

           ['         ',
            '  ()-()  ',
            "  (':')  ",
            '  d . b  ',
            '  ()_()  ',
            '         ',
            '         '],

           ['         ',
            '   ,_,   ',
            '  (O,O)  ',
            '  (   )  ',
            '   " "   ',
            '         ',
            '         '],

           [' .-",    ',
            " `~||    ",
            "   ||___ ",
            "   (':.)`",
            "   || || ",
            "   || || ",
            "   ^^ ^^ "]]


def gerador(num):
    result = []
    for i in range(7):
        if i == 3:
            result.append(f'{num}'.center(9))
        else:
            result.append(' ' * 9)

    return result


def printar_jogo(lista):
    janela = cjane.Janela()

    k = 0
    lin = 0
    for i in range(2, 21):
        if i == 2 or i == 10 or i == 12 or i == 20:
            janela.muda_slice(i, 4, 75, ('+' + '-' * 9) * 7 + '+')
        elif i == 11:
            k = 7
            lin = 0
        else:
            conteudo = ''
            for j in range(7):
                conteudo += '|' + lista[k + j][lin]
            conteudo += '|'
            janela.muda_slice(i, 4, 75, conteudo)
            lin += 1

    print(janela)


def jogar_memoria():
    lista = [gerador(i) for i in range(1, 15)]
    #lista = animais + animais
    printar_jogo(lista)
    input('>>>')

jogar_memoria()
