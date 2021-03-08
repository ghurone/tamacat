class Janela:

    def __init__(self):
        self.linha_top = ['+' + '-'*78 + '+\n']

        self.corpo = []
        for _ in range(21):
            self.corpo.append('|' + ' '*78 + '|\n')

        self.linha_bot = ['+' + '-'*78 + '+']

        self.janela = self.linha_top + self.corpo + self.linha_bot

    def __str__(self):
        s = ''
        for linha in self.janela:
            s += linha

        return s

    def __setitem__(self, linha, conteudo):
        self.janela[linha] = conteudo + '\n' if linha != 22 else conteudo

    def muda_linha(self, i, miolo):
        self.janela[i] = '|' + miolo + '|\n'


class JanelaTable:

    def __init__(self, cabeca: dict = None):
        self.cabeca_v = {'': 78} if not cabeca else cabeca
        self.itens = []

        self.linha_top = ''
        self.cabeca = self.__criar_cabeca()

    def mostrar_janela(self):
        s = self.cabeca

        if len(self.itens) <= 19:
            for i in range(19):
                try:
                    j = 0
                    for v in self.cabeca_v.values():
                        s += '|' + self.itens[i][j].center(v)
                        j += 1
                    s += '|\n'

                except IndexError:
                    for v in self.cabeca_v.values():
                        s += '|' + ''.center(v)
                    s += '|\n'

            print(s + self.linha_top)
            input('Pressione ENTER para sair...')

        else:
            for i in range(len(self.itens) // 19 + 1):
                s = self.cabeca

                for j in range(i * 19, 19 * (i + 1)):
                    try:
                        y = 0
                        for v in self.cabeca_v.values():
                            s += '|' + self.itens[j][y].center(v)
                            y += 1
                        s += '|\n'
                    except IndexError:
                        for v in self.cabeca_v.values():
                            s += '|' + ''.center(v)
                        s += '|\n'

                print(s + self.linha_top)
                input(f'(Pagina {i + 1}/{len(self.itens) // 19 + 1}) Pressione ENTER para continuar...')

    def add_linha(self, lista):
        self.itens.append(lista)

    def __criar_cabeca(self):
        linha_top = '+'
        linha_cabeca = '|'

        for name in self.cabeca_v.keys():
            valor = self.cabeca_v[name]
            linha_top += '-'*valor + '+'
            linha_cabeca += name.center(valor) + '|'

        self.linha_top = linha_top
        return linha_top+'\n' + linha_cabeca+'\n' + linha_top+'\n'
