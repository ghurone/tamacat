import config.janela as cjane


def como_jogar(titulo, conteudo):
    """Cria a tela de "como jogar" para um jogo, recebendo o título e as instruções daquele jogo."""

    janela = cjane.Janela()
    janela.muda_linha(1, titulo.upper())
    janela.muda_linha(3, '  - INSTRUÇÕES:', alin='ljust')

    for i in range(5, 22):
        try:
            linha = conteudo[i - 5]
            janela.muda_linha(i, linha, alin='ljust')
        except IndexError:
            pass

    print(janela)
    input('Pressione ENTER para jogar!')
