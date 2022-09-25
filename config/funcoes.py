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
    elif 'posix' in name: # Fazer para os outros SOs
        system('resize -s 24 81')
        

def verificar_nome(nome):
    
    if len(nome) > 32 or nome == '_pE_dRo_' or nome.isspace() or nome == '' or csave.existe_save(nome):
        return False

    return True
    