import config.funcoes as cfunc
import config.saveload as csave
import config.janela as cjane
import config.gatos_ascii as cga
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
        janela.muda_linha(i + 1, fonte[i])
        try:
            janela.muda_linha(i + 16, botao[i])
        except IndexError:
            pass

    janela.muda_linha(11, 'O MELHOR JOGO DO MUNDO!')
    janela.muda_linha(20, '© RaGhu 2021 ', alin='rjust')

    print(janela)
    input(wait('enter'))  # para não dar para digitar nada no input além de enter


def novo_gato():
    """Retorna um Gatinho, Geladeira e Bau para um gato inicial."""

    textos1 = ['Você está pensando em ter um gato.',
               'Um amigo seu conhece alguém que está vendendo um gato bonitinho.',
               'Mas também tem um gato que sempre têm andado pela vizinhança,',
               'e ele parece muito simpático.',
               'Por outro lado, também existe um abrigo de gatos perto da sua casa.']

    cfunc.limpar_tela()
    janela = cjane.Janela()

    j = 1
    for i in range(len(textos1)):
        janela.muda_linha(j, textos1[i], 'ljust')
        print(janela)
        input('(pressione ENTER para continuar...)')

        j += 2 if i != 2 else 1

    janela.muda_linha(10, 'Você deseja (C)omprar, (R)esgatar ou (A)dotar o gato?', 'ljust')
    print(janela)

    escolha = input('>>> ')
    while escolha.lower() != 'c' and escolha.lower() != 'r' and escolha.lower() != 'a' \
            and escolha.lower() != 'comprar' and escolha.lower() != 'resgatar' and escolha.lower() != 'adotar':
        print(janela)
        escolha = input('>>> ')

    janela.limpar_janela()

    v = 0
    if escolha[0] in 'Cc':
        janela.muda_linha(1, 'Você conversou com o conhecido do seu amigo e comprou o gatinho!', 'ljust')

        idade = randint(2, 12)
        fome = 100
        energia = randint(75, 100)
        saude = 100
        feliz = randint(80, 100)
        vac = True

        ga = ogato.Comprado('', idade, fome, energia, saude, feliz, vac)

    elif escolha[0] in 'Rr':
        janela.muda_linha(1, 'Você resgatou o gatinho. Agora ele tem um dono!', 'ljust')

        idade = randint(0, 180)
        fome = randint(10, 100)
        energia = randint(10, 90)
        saude = randint(10, 50)
        feliz = randint(10, 90)
        vac = choice([True, False])

        ga = ogato.Resgatado('', idade, fome, energia, saude, feliz, vac)

    else:
        v = 1
        janela.muda_linha(1, 'Você vai adotar um gato (F)ilhote ou (A)dulto?', 'ljust')
        print(janela)
        i = input('>>> ')

        while i.lower() != 'f' and i.lower() != 'a' and i.lower() != 'filhote' and i.lower() != 'adulto':
            print(janela)
            i = input('>>>')

        janela.muda_linha(1, 'Você foi até o abrigo e escolheu o seu gatinho.', 'ljust')
        janela.muda_linha(2, 'Ou será que foi ele quem te escolheu?', 'ljust')

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

    print(janela)
    input('(pressione ENTER para continuar...)')

    janela.muda_linha(3+v, 'Hora de uma decisão difícil... Qual vai ser o nome do seu gato?', 'ljust')
    print(janela)
    nome = input('>>> ')

    while not cfunc.verificar_nome(nome):
        janela.muda_linha(4+v, 'Insira um nome válido (e com tamanho menor que 32)!', 'ljust')
        print(janela)
        nome = input('>>> ')

    ga.nome = nome
    ge = ogela.Geladeira()
    ba = obau.Bau()

    return ga, ge, ba


def menu(cat, gato_img):
    """Imprime as características do gato."""

    acoes = ['Ver geladeira',
             'Comer', '',
             'Ver bau',
             'Brincar'
             ]

    acoes_jogo = ['Salvar o jogo',
                  'Abandonar o gato :(',
                  'Sair'
                  ]

    janela = cjane.JanelaMenu(gato_img, acoes, acoes_jogo, cat)

    print(janela)


def mostra_gela(geladita):
    """Mostra todos os alimentos da geladeira, em ordem decrescente de magnitude do saciamento."""

    janela = cjane.JanelaTable({'QTE.': 6, 'Nome': 29, 'Fome': 13, 'Saúde': 13, 'Felicidade': 13})

    for name in geladita.alimentos.keys():
        comida = [geladita[name][1], name, geladita[name][0].saciar, geladita[name][0].saude, geladita[name][0].feliz]
        janela.add_linha(comida)

    janela.mostrar_janela()


def mostrar_bau(bauzito):
    """Mostra todos os brinquedos do baú.
    Tipos diferentes: ordem decrescente, por felicidade.
    Mesmo tipo: ordem crescente, por durabilidade."""

    janela = cjane.JanelaTable({'Nome': 32, 'Felicidade': 22, 'Usos restantes': 22})

    for brinquedo in bauzito.brinquedosort():
        for brinqs in sorted(bauzito[brinquedo.nome]):
            brinq = [brinqs.nome, brinqs.feliz, brinqs.dura]
            janela.add_linha(brinq)

    janela.mostrar_janela()


def brincar(cat, bauzito):
    """Ações principais da ação brincar no menu."""

    janela = cjane.JanelaTable({'##': 4, 'Nome': 58, 'Felicidade': 14})

    # imprime os brinquedos disponíveis para brincar em ordem de felicidade
    brinqs = bauzito.brinquedosort()
    for i in range(len(brinqs)):
        janela.add_linha([i + 1, brinqs[i].nome, brinqs[i].feliz])

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
        menor_dura = min(bauzito[brinqs[int(brinq) - 1].nome])

        cat.brincar(bauzito, menor_dura)


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
        menu(gato, gato_img=cga.gatitos['Padrão'])

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
            salvo = False

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
