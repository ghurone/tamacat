from pickle import dump, loads
from os import remove


def salvar_jogo(*objs):
    try:
        for i in range(len(objs)):
            t = 'ab'
            if i == 0:
                t = 'wb'

            with open('../save.file', t) as file:
                dump(objs[i], file)
                file.write(bytes('_pE_dRo_'.encode('utf8')))

        print('Jogo salvo!')

    except Exception as e:
        print(e)


def carregar_jogo():
    try:
        with open('../save.file', 'rb') as file:
            objs = file.read()
            objs = objs.split('_pE_dRo_'.encode('utf8'))

        list_objs = []
        for obj in objs[:-1]:
            list_objs.append(loads(obj))

        return list_objs

    except FileNotFoundError:
        print('Não existe nenhum jogo salvo.')
        return False


def deletar_jogo():
    try:
        remove('../save.file')
    except Exception as e:
        print(e)
