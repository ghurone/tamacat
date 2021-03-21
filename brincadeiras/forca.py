import brincadeiras.func as bfunc
import random


palavras = {'Frutas': ['Laranja', 'Maça', 'Banana', 'Abacaxi', 'Acerola', 'Manga', 'Toranja', 'Mamão'],
            'Animais': ['Gato', 'Cachorro', 'Vaca', 'Hipopótamo', 'Rinoceronte', 'Avestruz']}


def ratinho(err, vivo=True):
    cabeca = [' _ │ _ ',
              '(q\┴/p)',
              ' |. .| ' if vivo else ' |x x| ',
              ' =\,/= ']

    corpo = ['   |   ',
             '  /|\  ',
             '   |   ',
             '   |   ',
             '  / \  ']

    if err == 0:
        return cabeca + corpo

    elif err == 1:
        corpo[4] = '  /    '
        return cabeca + corpo

    elif err == 2:
        corpo[4] = '       '
        return cabeca + corpo

    elif err == 3:
        corpo[4] = '       '
        corpo[1] = '   |\  '
        return cabeca + corpo

    elif err == 4:
        corpo[4] = '       '
        corpo[1] = '   |   '
        return cabeca + corpo

    elif err == 5:
        return cabeca

    elif err == 6:
        return []

def printar_forca(lista_char, tema, letras_desc, err=0, vivo=True):

    # Janela
    janela = bfunc.cjane.Janela()
    janela.muda_slice(1,10,40, f'TEMA: {tema}'.ljust(30))

    # Letras descartadas
    janela.criar_janelinha((0,40), (5,79))
    janela.muda_slice(1, 41, 79, 'LETRAS DESCARTADAS'.center(38))
    janela.muda_slice(3, 41, 79, ' '.join(letras_desc).center(38))

    # Forca
    janela.muda_slice(5, 10, 24, '┌'+ '─'*12 +'┐')
    janela.muda_slice(6, 10, 24, '│            │')
    for i in range(7,19):
        janela.muda_slice(i, 10, 11, '│')
    janela.muda_slice(19, 5, 16, '─────┴─────')

    # Palavra
    k = 0
    for i in range(len(lista_char)):
        janela.muda_slice(16, i + k + 40, i + k + 42, f'{lista_char[i]} ')
        k += 1

    # Ratinho
    rato = ratinho(err, vivo)
    for i in range(len(rato)):
        janela.muda_slice(7+i, 20, 27, rato[i])

    print(janela)


def jogar_forca():
    tema = random.choice(list(palavras.keys()))
    result = random.choice(palavras[tema])
    err = 0
    letras_desc = []

    palavra = []
    for letra in result:
        if letra.isalpha():
            palavra.append('_')
        else:
            palavra.append(letra)

    acabou = False
    ganhou = False
    while not acabou:
        printar_forca(palavra, tema, letras_desc, err, not ganhou)

        esc = input('Insira uma letra >>> ')
        while len(esc) != 1 or not esc.isalpha():
            printar_forca(palavra, tema, letras_desc, err)
            esc = input('Ops, insira somente uma letra >>> ')

        if esc.lower() in result.lower():
            for i, letra in enumerate(result):
                if esc.lower() == letra.lower():
                    palavra[i] = letra

            if palavra == list(result):
                acabou = True
                ganhou = True

        else:
            err += 1
            letras_desc.append(esc)

            if err == 6:
                acabou = True

    printar_forca(palavra, tema, letras_desc, err, not ganhou)

    msg = 'Você ganhou, o ratinho está morto hehehe... ' if ganhou else 'Você perdeu, o ratinho fugiu. '
    input(msg + '(Pressione ENTER para sair)')

    return ganhou