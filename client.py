from save.cadastro import login, registrar
from save.sql import SQL


def entrar():
    esc = input('(L)ogin ou (R)egistrar?\n>>> ')
    while esc.lower() != 'l' and esc.lower() != 'r':
        esc = input('(L)ogin ou (R)egistrar?\n>>> ')

    if esc in 'lL':
        log = login()
        while len(log) != 1:

            esc = input('O usuario e senha não conferem, deseja tentar novamente? (S)im / (N)ão\n>>> ')
            while esc.lower() != 's' and esc.lower() != 'n':
                esc = input('Por favor digite S ou N\n>>> ')

            if esc in 'sS':
                log = login()
            else:
                break

        if len(log) == 1:
            i = log['id']

            banco = SQL()
            resp = banco.q_select('gatinho, geladeira, bau', 'saves', f"user_id = '{i}'")
            banco.close()

            return resp

        return None

    else:
        reg = registrar()

        while reg != 'ok':
            if reg == 'email':
                print('Email já cadastrado!')
            elif reg == 'usuario':
                print('Usuario já cadastrado!')
            elif reg == 'bobo':
                print('Erro inesperado!!')

            esc = input('Deseja tentar se cadastrar novamente? (S)im / (N)ão\n>>> ')
            while esc.lower() != 's' and esc.lower() != 'n':
                esc = input('Por favor digite S ou N\n>>> ')

            if esc in 'sS':
                reg = registrar()
            else:
                break

        return None
