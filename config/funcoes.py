from os import name, system


def limpar_tela():
    if 'nt' in name:
        system('cls')
    else:
        system('clear')
