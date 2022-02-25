import janelas
import random

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


def printar_jogo(lista, vidas=''):
    janela = janelas.Janela()

    if vidas != '':
        janela.muda_linha(1, f'vidas: {vidas} ', 'rjust')
    
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
    cartas = [gerador(i) for i in range(1, 15)]
    mov_poss = list(range(1, 15))
    animais_duplos = animais + animais
    
    printar_jogo(animais_duplos)
    input('(Aperte ENTER para embaralhar)')
    random.shuffle(animais_duplos)
    
    vidas = 4
    while cartas != animais_duplos and vidas != 0:
        printar_jogo(cartas, vidas)
        
        pos_1 = input('Digite a primeira carta para virar: ')
        while not pos_1.isnumeric() or int(pos_1) not in mov_poss:
            printar_jogo(cartas, vidas)
            pos_1 = input('Digite a primeira carta para virar: ')
        
        temp = cartas.copy()
        temp[int(pos_1)-1] = animais_duplos[int(pos_1)-1]
        printar_jogo(temp, vidas)
        
        pos_2 = input('Digite a segunda carta para virar: ')
        while not pos_2.isnumeric() or int(pos_2) not in mov_poss or pos_2 == pos_1:
            printar_jogo(temp, vidas)
            pos_2 = input('Digite a segunda carta para virar: ')
        
        temp[int(pos_2)-1] = animais_duplos[int(pos_2)-1]
        printar_jogo(temp, vidas)
        
        if animais_duplos[int(pos_1)-1] == animais_duplos[int(pos_2)-1]:
            cartas[int(pos_1)-1] = animais_duplos[int(pos_1)-1]
            cartas[int(pos_2)-1] = animais_duplos[int(pos_2)-1]
            mov_poss[int(pos_1)-1] = ''
            mov_poss[int(pos_2)-1] = ''
            input('Parabéns! (Aperte ENTER para continuar...)')
        else:
            vidas -= 1
            input('Que pena, você errou :( (Aperte ENTER para continuar...)')
    
    printar_jogo(animais_duplos)
    
    if vidas == 0:
        input('Você perdeu :( (Aperte ENTER para voltar...)')
        return False
    else:
        input('Você ganhou!! (Aperte ENTER para voltar...)')
        return True
