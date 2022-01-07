import config.caminhos as cpath

from pickle import dump, loads
from os import remove, path, listdir
    

def salvar_jogo(objs:list):
    try:
        save_file = path.join(cpath.path_save, objs[0].nome + '.tamacat')
        
        for i in range(len(objs)):
            t = 'ab'
            if i == 0:
                t = 'wb'

            with open(save_file, t) as file:
                dump(objs[i], file)
                file.write(bytes('_pE_dRo_'.encode('utf8')))

    except Exception as e:
        print(e)


def carregar_jogo(nome):
    try:
        save_file = path.join(cpath.path_save, nome + '.tamacat')
        
        with open(save_file, 'rb') as file:
            objs = file.read()
            objs = objs.split('_pE_dRo_'.encode('utf8'))

        list_objs = []
        for obj in objs[:-1]:
            list_objs.append(loads(obj))

        return list_objs

    except Exception:
        return False


def deletar_jogo(nome):
    try:
        remove(path.join(cpath.path_save, nome + '.tamacat'))
    except Exception as e:
        print(e)


def listar_saves():
    return [file for file in listdir(cpath.path_save) if file.endswith('.tamacat')]
