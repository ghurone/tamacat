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

    def muda_topo(self, conteudo):
        self.janela[0] = '+' + conteudo + '+\n'

    def muda_base(self, conteudo):
        self.janela[-1] = '+' + conteudo + '+'

    def muda_linha(self, i, miolo, alin='center'):

        if alin == 'center':
            miolo = miolo.center(78)
        elif alin == 'rjust':
            miolo = miolo.rjust(78)
        elif alin == 'ljust':
            miolo = miolo.ljust(78)

        self.janela[i] = '|' + miolo + '|\n'

    def muda_slice(self, linha, ini, fim, conteudo):
        string = self[linha]
        my_string = ''

        for i in range(len(string)):
            if ini <= i < fim:
                my_string += conteudo[i-ini]
            else:
                my_string += string[i]

        self.janela[linha] = my_string

    def criar_janelinha(self, ponto_init, ponto_fim):
        x0, y0 = ponto_init
        x, y = ponto_fim

        for i in range(x0, x+1):

            if i == x0 or i == x:
                string = '+' + '-'*(y-y0-1) + '+'
                self.muda_slice(i, y0, y+1, string)
            else:
                string = '|' + ' '*(y-y0-1) + '|'
                self.muda_slice(i, y0, y+1, string)


class JanelaTable:

    def __init__(self, cabeca: dict = None):
        self.cabeca_v = {'': 78} if not cabeca else cabeca
        self.itens = []

        self.linha_top = ''
        self.cabeca = self.__criar_cabeca()

    def mostrar_janela(self, show_input=True):
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

            if show_input:
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
        lista = [str(i) for i in lista]
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
