from save.sql import SQL
from hashlib import md5


def login():
    user = input('Digite o seu usuário:\n>>> ')
    senha = input('Digite a sua senha:\n>>> ')
    senha_md5 = md5(senha.encode('utf8')).hexdigest()

    banco = SQL()
    resp = banco.select('id', 'users', f"usuario = '{user}' and senha = '{senha_md5}'")
    banco.close()

    return resp


def registrar():
    user = input('Digite um nome de usuario com no maximo 15 caracteres:\n>>> ')
    email = input('Digite o seu email:\n>>> ')
    senha = input('Digite a sua senha:\n>>> ')

    banco = SQL()
    resp = banco.insert_user(email, user, senha)
    banco.close()

    return resp


