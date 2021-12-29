import config.saveload as csave
import config.janela as cjane
from os import name, system
from time import sleep


def limpar_tela():
    if 'nt' in name:
        system('cls')
    else:
        system('clear')


def ajustes_iniciais():
    if 'nt' in name:
        system('color f0')  # define a cor do terminal (branco)
        system('mode con: cols=81 lines=24')  # ajuda o tamanho do terminal
        system('TITLE Tamacat')  # define o título do terminal como Tamacat
    else: # Fazer para os outros SOs
        pass


def mudar_titulo(titulo):
    system(f'TITLE Tamacat - {titulo}')


def verificar_nome(nome):
    if len(nome) > 32 or nome == '_pE_dRo_' or nome.isspace() or nome == '':
        return False

    return True


def janela_sair(salvo, gato, gela, bau):

    mudar_titulo('Sair do jogo')

    janela = cjane.Janela()

    if salvo:
        janela.muda_linha(1, ' Deseja sair? (S)im / (N)ão', 'ljust')

        print(janela)
        esc = input('>>> ').lower()
        while esc != 's' and esc != 'n' and esc != 'sim' and esc != 'não' and esc != 'nao':
            print(janela)
            esc = input('>>>').lower()

    else:
        janela.muda_linha(1, ' Há alterações não salvas. Digite a opção desejada:', 'ljust')
        janela.muda_linha(2, '  (1) - Salvar e sair', 'ljust')
        janela.muda_linha(3, '  (2) - Sair sem salvar', 'ljust')
        janela.muda_linha(4, '  (3) - Voltar ao menu', 'ljust')

        print(janela)
        esc = input('>>> ')
        while esc not in ['1', '2', '3']:
            print(janela)
            esc = input('>>>')

        if int(esc) in range(1, 3):
            esc = 's'
            if esc == '1':
                csave.salvar_jogo(gato, gela, bau)

    if 's' in esc:
        janela.limpar_janela()
        janela.muda_linha(11, 'Tchau!!')
        print(janela)
        sleep(2)

        return True

    return False


def janela_deletar():

    mudar_titulo('Abandonar gato')

    janela = cjane.Janela()
    janela.muda_linha(1, ' Você quer mesmo abandonar o seu gato??? (S)im / (N)ão', 'ljust')

    print(janela)
    esc = input('>>>').lower()
    while esc != 's' and esc != 'n' and esc != 'sim' and esc != 'não' and esc != 'nao':
        print(janela)
        esc = input('>>>').lower()

    if 's' in esc:
        csave.deletar_jogo()

        return True

    return False


def janela_carregar():

    mudar_titulo('Carregando jogo')

    janela = cjane.Janela()
    janela.muda_linha(11, 'Jogo carregado! :)')
    print(janela)


def janela_salvar():

    mudar_titulo('Salvar jogo')

    janela = cjane.Janela()
    janela.muda_linha(11, 'Jogo salvo! :)')
    print(janela)
