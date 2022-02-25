import janelas
import config.saveload as csave

from time import sleep
from os import system


def mudar_titulo(titulo:str = '') -> None:
    if titulo:
        system(f'TITLE Tamacat - {titulo}')
    else:
        system(f'TITLE Tamacat')


def janela_voltar(salvo, gato, gela, bau) -> bool:

    if salvo:
        resp = janela_simnao(' Deseja voltar ao menu?', 1, 'ljust', 'Sair do jogo')

    else:
        mudar_titulo('Sair do jogo')
        janela = janelas.Janela()
        janela.muda_linha(1, ' Há alterações não salvas. Digite a opção desejada:', 'ljust')
        janela.muda_linha(2, '  (1) - Salvar e voltar ao menu', 'ljust')
        janela.muda_linha(3, '  (2) - Voltar ao menu sem salvar', 'ljust')
        janela.muda_linha(4, '  (3) - Voltar ao jogo', 'ljust')

        print(janela)
        esc = input('>>> ')
        while esc not in ['1', '2', '3']:
            print(janela)
            esc = input('>>>')

        resp = True
        if esc == '1':
            csave.salvar_jogo([gato, gela, bau])
        elif esc == '3':
            resp = False

    return resp


def janela_deletar(gato_nome) -> bool:
    resp = janela_simnao(' Você quer mesmo abandonar o seu gato???', 1, 'ljust', 'Abandonar gato')

    if resp:
        csave.deletar_jogo(gato_nome)
        return True

    return False


def janela_carregar() -> None:
    janela = janela_msg('Jogo carregado! :)', titulo='Carregando jogo')
    print(janela)


def janela_salvar() -> None:
    janela = janela_msg('Jogo salvo! :)', titulo='Salvar jogo')
    print(janela)


def janela_creditos() -> None:
    mudar_titulo('Créditos')
    
    janela = janelas.Janela()
    
    janela.muda_linha(1, 'CRÉDITOS')
    
    textos = ['  Desenvolvido por Érick Ghuron e Raquel durante a pandemia de COVID-19.',
              ' Feito com amor e carinho <3', '',
              '  Pitacos de PedroPedroPedro e TutoColossal.']
    
    for i in range(len(textos)):
        janela.muda_linha(i+4, textos[i], 'ljust')
    
    janela.muda_linha(21, 'Equipe RaGhu ', 'rjust')
    
    print(janela)
    input('(Aperte ENTER para voltar...)')
    

def janela_sair() -> None:
    janela = janela_msg('Tchau!!')
    print(janela)
    sleep(2)
    

def janela_msg(msg:str, lin:int = 11, alin:str = 'center', titulo:str = '') -> janelas.Janela:
    
    mudar_titulo(titulo)
    janela = janelas.Janela()
    janela.muda_linha(lin, msg, alin)
    
    return janela


def janela_simnao(msg:str, lin:int = 11, alin:str = 'center', titulo:str = '') -> bool:
    janela = janela_msg(msg+' (S)im / (N)ão', lin, alin, titulo)
    print(janela)
    
    esc = input('>>>').lower()
    while esc != 's' and esc != 'n' and esc != 'sim' and esc != 'não' and esc != 'nao':
        janela.muda_linha(lin+1, 'Digite uma opção válida!', alin)
        print(janela)
        esc = input('>>>').lower()
    
    return 's' in esc
