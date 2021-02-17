from os import name, system
from config.saveload import deletar_jogo


def limpar_tela():
    if 'nt' in name:
        system('cls')
    else:
        system('clear')


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
        deletar_jogo()

        return True

    return False
