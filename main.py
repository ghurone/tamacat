import config.funcoes as cfunc
import config.saveload as csave
import config.janela as cjane
import objs.gatinho as ogato
import objs.geladeira as ogela
import objs.bau as obau

from random import randint, choice
from time import sleep

from keyboard import wait

humores = ['feliz', 'triste', 'quieto', 'brincalhão', 'carinhoso', 'assustado', 'irritado']


def tela_inicial():
    """`Printa a tela inicial do jogo."""

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

    janela = cjane.Janela()

    for i in range(len(fonte)):
        janela.muda_linha(i+1, fonte[i])
        try:
            janela.muda_linha(i+16, botao[i])
        except IndexError:
            pass

    janela.muda_linha(11, 'O MELHOR JOGO DO MUNDO!')
    janela.muda_linha(20, '© RaGhu 2021 ', alin='rjust')

    print(janela)
    input(wait('enter'))  # para não dar para digitar nada no input além de enter


def novo_gato():
    """Retorna um Gatinho, Geladeira e Bau para um gato inicial."""

    cfunc.limpar_tela()

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

    cfunc.limpar_tela()

    if escolha[0] in 'Cc':
        print('Você conversou com o conhecido do seu amigo e comprou o gatinho!')

        idade = randint(2, 12)
        fome = 100
        energia = randint(75, 100)
        saude = 100
        feliz = randint(80, 100)
        vac = True

        ga = ogato.Comprado('', idade, fome, energia, saude, feliz, vac)

    elif escolha[0] in 'Rr':
        print('Você resgatou o gatinho. Agora ele tem um dono!')

        idade = randint(0, 180)
        fome = randint(10, 100)
        energia = randint(10, 90)
        saude = randint(10, 50)
        feliz = randint(10, 90)
        vac = choice([True, False])

        ga = ogato.Resgatado('', idade, fome, energia, saude, feliz, vac)

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

        fome = randint(60, 100)
        energia = randint(70, 100)
        saude = randint(70, 90)
        feliz = randint(80, 100)
        vac = choice([True, True, True, False, False])  # True: 60%, False: 40%

        ga = ogato.Adotado('', idade, fome, energia, saude, feliz, vac)

    sleep(2)
    nome = input('Hora de uma decisão difícil... Qual vai ser o nome do seu gato?\n>>> ')

    while not cfunc.verificar_nome(nome):
        nome = input('Insira um nome com um tamanho menor que 43:\n>>> ')

    ga.nome = nome
    ge = ogela.Geladeira()
    ba = obau.Bau()

    return ga, ge, ba


def menu(cat):
    """Imprime as características do gato."""

    vac = 'Sim' if cat.vacinado else 'Não'

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
    s += '|' + acoes[-3].ljust(29) + '|' + ('Energia:    ' + '[' + ('■' * (cat.energia // 5)).ljust(20) + ']').ljust(
        48) + '|\n'
    s += '|' + acoes[-2].ljust(29) + '|' + ('Saude:      ' + '[' + ('■' * (cat.saude // 5)).ljust(20) + ']').ljust(
        48) + '|\n'
    s += '|' + acoes[-1].ljust(29) + '|' + ('Felicidade: ' + '[' + ('■' * (cat.feliz // 5)).ljust(20) + ']').ljust(
        48) + '|\n'

    s += '+' + '-' * 29 + '+' + '-' * 48 + '+'

    print(s)


def mostra_gela(gela):
    """Mostra todos os alimentos da geladeira, em ordem decrescente de magnitude do saciamento."""

    janela = cjane.JanelaTable({'QTE.': 6, 'Nome': 29, 'Fome': 13, 'Saúde': 13, 'Felicidade': 13})

    for name in gela.alimentos.keys():
        comida = [gela[name][1], name, gela[name][0].saciar, gela[name][0].saude, gela[name][0].feliz]
        janela.add_linha(comida)

    janela.mostrar_janela()


def mostrar_bau(bau):
    """Mostra todos os brinquedos do baú.
    Tipos diferentes: ordem decrescente, por felicidade.
    Mesmo tipo: ordem crescente, por durabilidade."""

    janela = cjane.JanelaTable({'Nome': 32,'Felicidade': 22, 'Usos restaante': 22})

    for brinquedo in bau.brinquedosort():
        for brinqs in sorted(bau[brinquedo.nome]):
            brinq = [brinqs.nome, brinqs.feliz, brinqs.dura]
            janela.add_linha(brinq)

    janela.mostrar_janela()


def brincar(cat, bau):
    """Ações principais da ação brincar no menu."""

    janela = cjane.JanelaTable({'##': 4, 'Nome': 58, 'Felicidade': 14})

    # imprime os brinquedos disponíveis para brincar em ordem de felicidade
    brinqs = bau.brinquedosort()
    for i in range(len(brinqs)):
        janela.add_linha([i+1, brinqs[i].nome, brinqs[i].feliz])

    janela.mostrar_janela(show_input=False)

    brinq = input('Digite o número do brinquedo para jogar (ENTER para voltar): ')
    while brinq != '' and (not brinq.isnumeric() or int(brinq) > len(brinqs)):
        janela.mostrar_janela(show_input=False)

        if not brinq.isnumeric():
            brinq = input('Digite um valor numérico (ENTER para voltar): ')
        else:
            brinq = input('Digite um número válido (ENTER para voltar): ')

    if brinq != '':
        # seleciona o brinquedo com menor durabilidade dentre os do tipo escolhido para brincar
        menor_dura = min(bau[brinqs[int(brinq) - 1].nome])

        cat.brincar(bau, menor_dura)


if __name__ == '__main__':

    cfunc.ajustes_iniciais()
    tela_inicial()
    cfunc.limpar_tela()

    if csave.carregar_jogo():
        gato, gela, bau = csave.carregar_jogo()
        print('Jogo carregado! :)'.center(81))
        sleep(1)

    else:
        gato, gela, bau = novo_gato()
        csave.salvar_jogo(gato, gela, bau)

    salvo = True

    while True:
        cfunc.limpar_tela()
        menu(gato)

        esc = input('>>> ')

        if esc in ['2']:  # comer
            salvo = False

        if esc == '1':
            # Ver geladeira
            cfunc.limpar_tela()
            mostra_gela(gela)

        elif esc == '3':
            # Ver bau
            cfunc.limpar_tela()
            mostrar_bau(bau)

        elif esc == '4':
            cfunc.limpar_tela()
            brincar(gato, bau)

        elif esc == '5':
            # Salvar jogo
            salvo = True
            cfunc.limpar_tela()
            csave.salvar_jogo(gato, gela, bau)
            sleep(1)

        elif esc == '6':
            # Deletar jogo (abandonar gato)
            cfunc.limpar_tela()
            if cfunc.deletar():
                break

        elif esc == '7':
            # Sair do jogo
            cfunc.limpar_tela()
            if cfunc.sair(salvo):
                break

        else:
            continue

    print('Tchau!!')
