from objs.gatinho import Adotado, Comprado, Resgatado
from objs.geladeira import Geladeira
from objs.bau import Bau
from objs.brinquedo import Bola, Nave
from objs.comida import Comida
from config.saveload import salvar_jogo, carregar_jogo
from config.funcoes import limpar_tela, sair, deletar, verificar_nome, ajustes_iniciais

from random import randint, choice
from time import sleep

from keyboard import wait

humores = ['feliz', 'triste', 'quieto', 'brincalhão', 'carinhoso', 'assustado', 'irritado']


def tela_inicial():
    fonte = ['                                    /)                              ',
             '                            |\\---/|((                              ',
             "                            | ° ° | ))                              ",
             '                             \\_T_/_//                               ',
             ' ________  _______  _____ _{_}_  {_}____  ______  _______  ________ ',
             '|_      _||   _   ||    | |    ||   _   ||   ___||   _   ||_      _|',
             '  |    |  |  |_|  ||     -     ||  |_|  ||  |    |  |_|  |  |    |  ',
             '  |    |  |   _   ||   _   _   ||   _   ||  |___ |   _   |  |    |  ',
             '  |____|  |__| |__||__| |_| |__||__| |__||______||__| |__|  |____|  ']

    botao = ['.-----------------------------.',
             '| Pressione ENTER para jogar! |',
             "'-----------------------------'"]

    s = '+' + '-'*78 + '+\n'

    for i in range(21):
        if 1 <= i <= 9:
            s += '|' + fonte[i-1].center(78) + '|\n'
        elif i == 11:
            s += '|' + 'O MELHOR JOGO DO MUNDO!'.center(78) + '|\n'
        elif 16 <= i <= 18:
            s += '|' + botao[i-16].center(78) + '|\n'
        elif i == 20:
            s += '|' + '© RaGhu 2021 '.rjust(78) + '|\n'
        else:
            s += '|' + ' '*78 + '|\n'

    s += '+' + '-' * 78 + '+'
    print(s)
    input(wait('enter'))


def novo_gato():
    """Retorna um Gatinho, Geladeira e Bau para um gato inicial."""
    limpar_tela()

    print('Você está pensando em ter um gato.')
    sleep(2)
    print('\nUm amigo seu conhece alguém que está vendendo um gato bonitininho.')
    sleep(3)
    print('Mas também tem um gato que sempre têm andado pela vizinhança, e ele parece muito simpático.')
    sleep(3.5)
    print('Por outro lado, também existe um abrigo de gatos perto da sua casa.')
    sleep(3)

    escolha = input('\nVocê deseja (C)omprar, (R)esgatar ou (A)dotar o gato?\n>>> ')
    while escolha.lower() != 'c' and escolha.lower() != 'r' and escolha.lower() != 'a' \
            and escolha.lower() != 'comprar' and escolha.lower() != 'resgatar' and escolha.lower() != 'adotar':
        escolha = input('Você deseja (C)omprar, (R)esgatar ou (A)dotar o gato?\n>>> ')

    limpar_tela()

    if escolha[0] in 'Cc':
        print('Você conversou com o conhecido do seu amigo e comprou o gatinho!')

        idade = randint(2, 12)
        fome = 0
        energia = randint(75, 100)
        saude = 100
        feliz = randint(80, 100)
        vac = True

        ga = Comprado('', idade, fome, energia, saude, feliz, vac)

    elif escolha[0] in 'Rr':
        print('Você resgatou o gatinho. Agora ele tem um dono!')

        idade = randint(0, 180)
        fome = randint(0, 90)
        energia = randint(10, 90)
        saude = randint(10, 50)
        feliz = randint(10, 90)
        vac = choice([True, False])

        ga = Resgatado('', idade, fome, energia, saude, feliz, vac)

    else:
        i = input('Você vai adotar um gato (F)ilhote ou (A)dulto?\n>>> ')

        while i.lower() != 'f' and i.lower() != 'a' and i.lower() != 'filhote' and i.lower() != 'adulto':
            i = input('Você vai adotar um gato (F)ilhote ou (A)dulto?\n>>> ')
        sleep(1)

        print('Você foi até o abrigo e escolheu o seu gatinho. Ou será que foi ele quem te escolheu?')

        if i[0].lower() == 'f':
            idade = randint(3, 12)
        else:
            idade = randint(13, 84)

        fome = randint(0, 40)
        energia = randint(70, 100)
        saude = randint(70, 90)
        feliz = randint(80, 100)
        vac = choice([True, True, True, False, False])  # True: 60%, False: 40%

        ga = Adotado('', idade, fome, energia, saude, feliz, vac)

    sleep(2)
    nome = input('Hora de uma decisão difícil... Qual vai ser o nome do seu gato?\n>>> ')

    while not verificar_nome(nome):
        nome = input('Insira um nome com um tamanho menor que 43:\n>>> ')

    ga.nome = nome
    ge = Geladeira()
    ba = Bau()

    return ga, ge, ba


def menu(cat):
    """Imprime as características do gato."""
    if cat.vacinado:
        vac = 'Sim'
    else:
        vac = 'Não'

    gato = [' ,_     _        ',
            ' |\\\\_,-//        ',
            ' / _  _ |    ,--. ',
            '(  @  @ )   / ,-\'',
            ' \  _T_/-._( (    ',
            ' /         `. \\  ',
            '|         _  \\ | ',
            ' \ \ ,  /      |  ',
            '  || |-_\__   /   ',
            ' ((_/`(____,-\'   '
            ]

    acoes = ['(1) - Ver geladeira',
             '(2) - Comer', '',
             '(3) - Ver bau',
             '(4) - Brincar', '',
             '', '', '', '',
             '(5) - Salvar o jogo',
             '(6) - Abandonar o gato :(',
             '(7) - Sair'
             ]

    s = '+' + '-' * 29 + '+' + '-' * 48 + '+\n'
    s += '|' + 'TAMACAT'.center(29) + '|' + ' ' * 48 + '|\n'

    for i in range(10):
        s += '|' + acoes[i].ljust(29) + '|' + gato[i].center(48) + '|\n'  # geral

    s += '|' + ' ' * 29 + '|' + ' ' * 48 + '|\n'
    s += '|' + ' ' * 29 + '|' + ' ' * 48 + '|\n'
    s += '|' + ' ' * 29 + '+' + '-' * 48 + '+\n'
    s += '|' + ' ' * 29 + '|' + f'Nome: {cat.nome}'.ljust(48) + '|\n'
    s += '|' + ' ' * 29 + '|' + f'Idade: {cat.mostrar_idade()}'.ljust(48) + '|\n'
    s += '|' + ' ' * 29 + '|' + f'Vacinado: {vac}'.ljust(48) + '|\n'
    s += '|' + '-' * 29 + '|' + ('Fome:       ' + '[' + ('■' * (cat.fome // 5)).ljust(20) + ']').ljust(48) + '|\n'
    s += '|' + acoes[-3].ljust(29) + '|' + ('Energia:    ' + '[' + ('■' * (cat.energia // 5)).ljust(20) + ']').ljust(48) + '|\n'
    s += '|' + acoes[-2].ljust(29) + '|' + ('Saude:      ' + '[' + ('■' * (cat.saude // 5)).ljust(20) + ']').ljust(48) + '|\n'
    s += '|' + acoes[-1].ljust(29) + '|' + ('Felicidade: ' + '[' + ('■' * (cat.feliz // 5)).ljust(20) + ']').ljust(48) + '|\n'

    s += '+' + '-' * 29 + '+' + '-' * 48 + '+'

    print(s)


def mostra_gela(gela):
    """Mostra todos os alimentos da geladeira, em ordem decrescente de magnitude do saciamento."""

    tam_gela = len(gela.alimentos)

    s = '+' + '-'*6 + '+' +'-'*29 + '+' + '-'*13 + '+' + '-'*13 + '+' + '-'*13 + '+\n'
    s += '|' + 'QTE.'.center(6) + '|' + 'Nome'.center(29) + '|' + 'Fome'.center(13) + '|' + 'Saude'.center(13) + '|' + 'Felicidade'.center(13) + '|\n'
    s += '+' + '-' * 6 + '+' + '-' * 29 + '+' + '-' * 13 + '+' + '-' * 13 + '+' + '-' * 13 + '+\n'

    cabeca = s

    if tam_gela <= 19:  # verificar se vai precisar de mais de uma página
        s += str(gela)

        for i in range(19 - tam_gela):
            s += '|' + ' ' * 6 + '|' + ' ' * 29 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|\n'

        s += '+' + '-'*6 + '+' + '-'*29 + '+' + '-'*13 + '+' + '-'*13 + '+' + '-'*13 + '+'
        print(s)
        input('Pressione ENTER para continuar...')

    else:
        gela_str = str(gela).split('\n')[:-1]

        for i in range(tam_gela // 19 + 1):
            s = cabeca
            for j in range(i*19, 19*(i+1)):
                try:
                    s += gela_str[j]
                except IndexError:
                    s += '|' + ' ' * 6 + '|' + ' ' * 29 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|' + ' ' * 13 + '|\n'
            s += '+' + '-' * 6 + '+' + '-' * 29 + '+' + '-' * 13 + '+' + '-' * 13 + '+' + '-' * 13 + '+'
            print(s)
            input(f'(Pagina {i+1}/{tam_gela// 19 + 1}) Pressione ENTER para continuar...')
            limpar_tela()


def mostrar_bau(bau):
    """Mostra todos os brinquedos do baú.
    Tipos diferentes: ordem decrescente, por felicidade.
    Mesmo tipo: ordem crescente, por durabilidade."""

    tam_bau = bau.numero_de_brinquedos()

    s = '+' + '-' * 32 + '+' + '-' * 22 + '+' + '-' * 22 + '+\n'
    s += '|' + 'Nome'.center(32) + '|' + 'Felicidade'.center(22) + '|' + 'Usos restantes'.center(22) + '|\n'
    s += '+' + '-' * 32 + '+' + '-' * 22 + '+' + '-' * 22 + '+\n'

    cabeca = s

    if tam_bau <= 19:  # verificar se vai precisar de mais de uma página

        s += str(bau)

        for i in range(19 - tam_bau):
            s += '|' + ' '*32 + '|' + ' '*22 + '|' + ' '*22 + '|\n'

        s += '+' + '-' * 32 + '+' + '-' * 22 + '+' + '-' * 22 + '+'
        print(s)
        input('Pressione ENTER para sair...')

    else:
        bau_str = str(bau).split('\n')[:-1]

        for i in range(tam_bau // 19 + 1):
            s = cabeca
            for j in range(i*19, 19*(i+1)):
                try:
                    s += bau_str[j] + '\n'
                except IndexError:
                    s += '|' + ' ' * 32 + '|' + ' ' * 22 + '|' + ' ' * 22 + '|\n'

            s += '+' + '-' * 32 + '+' + '-' * 22 + '+' + '-' * 22 + '+'

            print(s)
            input(f'(Pagina {i+1}/{tam_bau//19 + 1}) Pressione ENTER para continuar...')

            limpar_tela()


def brincar(cat, bau):

    s = '+' + '-' * 4 + '+' + '-' * 58 + '+' + '-' * 14 + '+\n'
    s += '|' + '##'.center(4) + '|' + 'Nome'.center(58) + '|' + 'Felicidade'.center(14) + '|\n'
    s += '+' + '-' * 4 + '+' + '-' * 58 + '+' + '-' * 14 + '+\n'

    brinqs = bau.brinquedosort()

    for i in range(19):

        try:
            s += '|' + f'{i+1}'.center(4) + '|' + f'{brinqs[i].nome}'.center(58) + '|' + f'{brinqs[i].feliz}'.center(14) + '|\n'
        except IndexError:
            s += '|' + ' '*4 + '|' + ' '*58 + '|' + ' '*14 + '|\n'

    s += '+' + '-' * 4 + '+' + '-' * 58 + '+' + '-' * 14 + '+'

    print(s)

    brinq = input('Digite o número do brinquedo para jogar (ENTER para sair): ')
    while brinq != '' and (not brinq.isnumeric() or int(brinq) > len(brinqs)):
        limpar_tela()
        print(s)
        if not brinq.isnumeric():
            brinq = input('Digite um valor numérico (ENTER para sair): ')
        else:
            brinq = input('Digite um número válido (ENTER para sair): ')

    if brinq != '':

        limpar_tela()

        menor_dura = min(bau.brinquedos[brinqs[int(brinq)-1].nome])
        cat.brincar(bau, menor_dura)


if __name__ == '__main__':

    ajustes_iniciais()
    tela_inicial()
    limpar_tela()

    if carregar_jogo():
        gato, gela, bau = carregar_jogo()
        print('Jogo carregado! :)'.center(81))
        sleep(1)

    else:
        gato, gela, bau = novo_gato()
        salvar_jogo(gato, gela, bau)

    salvo = True


    while True:
        limpar_tela()
        menu(gato)

        esc = input('>>> ')

        if esc in ['2']:  # comer
            salvo = False

        if esc == '1':
            # Ver geladeira
            limpar_tela()
            mostra_gela(gela)

        elif esc == '3':
            # Ver bau
            limpar_tela()
            mostrar_bau(bau)

        elif esc == '4':
            limpar_tela()
            brincar(gato, bau)

        elif esc == '5':
            # Salvar jogo
            salvo = True
            limpar_tela()
            salvar_jogo(gato, gela, bau)
            sleep(1)

        elif esc == '6':
            # Deletar jogo (abandonar gato)
            limpar_tela()
            if deletar():
                break

        elif esc == '7':
            # Sair do jogo
            limpar_tela()
            if sair(salvo):
                break

        else:
            continue

    print('Tchau!!')
