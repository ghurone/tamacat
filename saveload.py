import pickle


# noinspection PyTypeChecker
def salvar_jogo(*objs):
    try:
        for i in range(len(objs)):
            t = 'ab'
            if i == 0:
                t = 'wb'

            with open('save.file', t) as file:
                pickle.dump(objs[i], file)
                file.write(bytes('\n'.encode('utf8')))

    except Exception as e:
        print(e)


def carregar_jogo():
    try:
        with open('save.file', 'rb') as file:
            objs = file.readlines()

        list_objs = []
        for obj in objs:
            list_objs.append(pickle.loads(obj[:-1]))

        return list_objs
    except Exception as e:
        print(e)


def deletar_save():
    try:
        with open('save.file', 'wb') as file:
            file.write(bytes(''.encode('utf8')))
    except Exception as e:
        print(e)
