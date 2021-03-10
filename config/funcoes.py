import config.saveload as csave
from os import name, system


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


def verificar_nome(nome):
    if len(nome) > 32 or nome == '_pE_dRo_':
        return False

    return True


def sair(salvo):
    if salvo:
        esc = input('Deseja sair? (S)im / (N)ão\n>>> ')

        while esc.lower() != 's' and esc.lower() != 'n':
            esc = input('Deseja sair? (S)im / (N)ão\n>>> ')

    else:
        esc = input('Há alterações não salvas. Deseja sair sem salvar? (S)im / (N)ão\n>>> ')

        while esc.lower() != 's' and esc.lower() != 'n':
            esc = input('Há alterações não salvas. Deseja sair sem salvar? (S)im / (N)ão\n>>> ')

    if esc.lower() == 's':
        return True

    return False


def deletar():
    isc = input('Você quer mesmo abandonar o seu gato??? (S)im / (N)ão\n>>> ')
    while isc.lower() != 's' and isc.lower() != 'n':
        isc = input('Você quer mesmo abandonar o seu gato??? (S)im / (N)ão\n>>> ')

    if isc.lower() == 's':
        csave.deletar_jogo()

        return True

    return False
