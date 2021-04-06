import config.janela as cjane


def gerador(num):
    num = '0' + str(num) if len(str(num)) == 1 else str(num)

    result = []
    for i in range(7):
        if i == 3:
            result.append(f'{num}'.center(8))
        else:
            result.append(' '*8)

    return result


def printar_jogo(lista):
    janela = cjane.Janela()

    k = 0
    lin = 0
    for i in range(2, 21):
        if i == 2 or i == 10 or i == 12 or i == 20:
            janela.muda_slice(i, 2, 79, ('+' + '-' * 8 + '+ ') * 7)
        elif i == 11:
            k = 7
            lin = 0
        else:
            conteudo = ''
            for j in range(7):
                conteudo += '|' + lista[k+j][lin] + '| '

            janela.muda_slice(i, 2, 79, conteudo)
            lin += 1

    print(janela)


def jogar_memoria():
    lista = [gerador(i) for i in range(1,15)]
    printar_jogo(lista)
    input('>>>')


if __name__ == '__main__':
    printar_jogo()
