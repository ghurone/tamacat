from pickle import dump, loads
from os import remove, path

path_save = path.join(path.expanduser('~'), 'tamacat.save')


def salvar_jogo(*objs):
    try:
        for i in range(len(objs)):
            t = 'ab'
            if i == 0:
                t = 'wb'

            with open(path_save, t) as file:
                dump(objs[i], file)
                file.write(bytes('_pE_dRo_'.encode('utf8')))

    except Exception as e:
        print(e)


def carregar_jogo():
    try:
        with open(path_save, 'rb') as file:
            objs = file.read()
            objs = objs.split('_pE_dRo_'.encode('utf8'))

        list_objs = []
        for obj in objs[:-1]:
            list_objs.append(loads(obj))

        return list_objs

    except FileNotFoundError:
        return False


def deletar_jogo():
    try:
        remove(path_save)
    except Exception as e:
        print(e)
