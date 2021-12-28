import brincadeiras.func as bfunc
import random


palavras = {'Frutas': ['Laranja', 'Maçã', 'Banana', 'Abacaxi', 'Acerola', 'Manga', 'Toranja', 'Mamão', 'Limão',
                       'Morango', 'Maçã verde', 'Melancia', 'Kiwi', 'Ameixa', 'Goiaba', 'Pitanga', 'Lichia', 'Pêssego',
                       'Pêra', 'Uva'],

            'Animais': ['Gato', 'Cachorro', 'Vaca', 'Hipopótamo', 'Rinoceronte', 'Avestruz', 'Pato', 'Zebra'],

            'Objetos': ['Mesa', 'Computador', 'Cadeira', 'Quadro negro', 'Armário', 'Micro-ondas', 'Tapete', 'Skate',
                        'Calculadora', 'Ábaco', 'Piano', 'Açucareiro', 'Bola', 'Bigorna', 'Caderno', 'Candelabro',
                        'Despertador', 'Mangueira', 'Microscópio', 'Roteador', 'Binóculo', 'Navio', 'Avião', 'Picareta',
                        'Quadriciclo', 'Quebra-cabeça', 'Revista', 'Relógio', 'Ratoeira', 'Buquê de flores', 'Telefone',
                        'Tambor', 'Telescópio', 'Tobogã', 'Unha postiça', 'Umidificador', 'Vassoura', 'Violão',
                        'Vuvuzela', 'Webcam', 'Walkie-talkie', 'Xadrez', 'Xilofone', 'Xícara', 'Zíper', 'Zinco',
                        'Zarabatana', 'Secador', 'Saxofone', 'Sunga', 'Saca-rolhas', 'Sabonete', 'Ralador', 'Repelente',
                        'Roleta', 'Rotor', 'Reco-reco', 'Paraquedas', 'Parafuso', 'Pêndulo', 'Óculos', 'Olho mágico',
                        'Liquidificador', 'Lapiseira'],

            'Comidas': ['Sorvete', 'Pizza', 'Arroz', 'Feijão', 'Bife', 'Alface', 'Cenoura', 'Batata', 'Chocolate',
                        'Pudim', 'Bolo de morango', 'Couve', 'Cebola', 'Alho', 'Sopa de tomate', 'Chocolate branco',
                        'Purê de batata', 'Rocambole', 'Cookie', 'Lasanha', 'Macarrão', 'Queijo'],

            'Profissões': ['Professor', 'Astrônoma', 'Palhaço', 'Engenheira', 'Médica', 'Fotógrafo', 'Jornalista',
                           'Jornalista esportivo', 'Programadora', 'Psicólogo', 'Porteiro', 'Vendedor', 'Advogada',
                           'Juíza', 'Agricultor', 'Bombeiro', 'Enfermeiro', 'Paramédico', 'Policial', 'Cientista',
                           'Atriz', 'Babá', 'Piloto'],

            'Planetas': ['Plutão', 'Netuno', 'Urano', 'Saturno', 'Júpiter', 'Vênus', 'Terra', 'Marte', 'Mercúrio']}


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
    letras_esp = {'a': ('a', 'ã', 'à', 'á', 'â'), 'c': ('c', 'ç'), 'e': ('e', 'é', 'ê'), 'o': ('o', 'ó', 'ô'),
                  'i': ('i', 'í'), 'u': ('u', 'ú')}

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

        esc = input('Insira uma letra >>> ').lower()
        while len(esc) != 1 or not esc.isalpha() or esc in letras_desc:
            printar_forca(palavra, tema, letras_desc, err)
            esc = input('Ops, insira somente uma letra >>> ').lower()

        entrou = False

        if esc in letras_esp.keys() or esc in result.lower():
            try:
                for letra in letras_esp[esc]:
                    for i, ltr in enumerate(result):
                        if letra == ltr.lower():
                            palavra[i] = ltr
                            entrou = True

            except KeyError:
                for i, ltr in enumerate(result):
                    if esc == ltr.lower():
                        palavra[i] = ltr
                        entrou = True

            if palavra == list(result):
                acabou = True
                ganhou = True

        if not entrou:
            err += 1
            letras_desc.append(esc)

            if err == 6:
                acabou = True

    printar_forca(result, tema, letras_desc, err, not ganhou)

    if ganhou:
        msg = 'Você ganhou, o ratinho está morto hehehe... '
    else:
        msg = 'Você perdeu, o ratinho fugiu. '
    input(msg + '(Aperte ENTER para sair)')

    return ganhou

