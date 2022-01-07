from os import mkdir, path

# Diretório principal
path_dir = path.join(path.expanduser('~'), '.tamacat')

# Diretório dos saves
path_save = path.join(path_dir,'saves')


# Criando as pastas caso elas não existam 
if not path.isdir(path_dir):
    mkdir(path_dir)
    mkdir(path_save)
    
else:
    if not path.isdir(path_save):
        mkdir(path_save)