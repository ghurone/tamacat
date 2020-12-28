import mysql.connector as mycon
from pickle import dumps, loads

class SQL:
    def __init__(self):
        config = {
            'user': 'raghu',
            'password': 'P@stel99!',
            'host': 'tamacat-data.mysql.uhserver.com',
            'database': 'tamacat_data'
        }

        self.cnx = mycon.connect(**config)
        self.cursor = self.cnx.cursor(buffered=True)

    def select(self, columns, table, where):
        query = f'SELECT {columns} FROM {table} WHERE {where};'
        self.query(query)

        colunas = tuple(columns.replace(' ', '').split(","))
        dicio = {}

        for row in self.cursor:
            for i in range(len(colunas)):
                dicio[colunas[i]] = row[i]

        return dicio

    def insert_user(self, e, u, s):
        query = f"insert into users (email, usuario, senha) values ('{e}', '{u}', md5('{s}'));"

        try:
            self.query(query)
            self.cnx.commit()

        except mycon.Error as e:
            if "Duplicate" in str(e):
                if "for key 'email'" in str(e):
                    return 'email'
                elif "for key 'usuario'" in str(e):
                    return 'usuario'
            else:
                return 'bobo'

        query = f"insert into saves (user_id) values ((select id from users where usuario = '{u}'));"
        self.query(query)
        self.cnx.commit()

        ide = self.select('id', 'users', f"usuario = '{u}'")
        resp = self.carregar_jogo(ide['id'])

        return resp

    def salvar_jogo(self, i, gato, gela, bau):
        gatinho = dumps(gato)
        geladeira = dumps(gela)
        b = dumps(bau)
        query = f"UPDATE saves SET gato = '{gatinho}', gela = '{geladeira}', bau = '{b}' WHERE user_id = {i};"
        self.query(query)
        self.cnx.commit()

    def carregar_jogo(self, i):
        game = self.select('user_id, gato, gela, bau', 'saves', f"user_id = '{i}'")

        for i, key in enumerate(game):
            if i != 0 and game[key] is not None:
                game[key] = loads(game[key])

        return game

    def deletar_save(self, i):
        query = f"UPDATE saves SET gato = null, gela = null, bau = null WHERE user_id = {i};"
        self.query(query)
        self.cnx.commit()

    def query(self, query):
        self.cursor.execute(query)

    def close(self):
        self.cursor.close()
        self.cnx.close()
