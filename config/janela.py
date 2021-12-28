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

    def __getitem__(self, item):
        return self.janela[item]

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

    def limpar_janela(self):
        self.janela = Janela().janela


class JanelaTable:

    def __init__(self, cabeca: dict = None):
        self.cabeca_v = {'': 78} if not cabeca else cabeca
        self.itens = []

        self.linha_top = ''
        self.cabeca = self.__criar_cabeca()

    def mostrar_janela(self, show_input=True):

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
            if show_input:
                input(f'(Página {i + 1}/{len(self.itens) // 19 + 1}) Aperte ENTER para continuar...')

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


class JanelaMenu:

    def __init__(self, gato_img: list, acoes_gato: list, acoes_jogo: list, gato):
        self.gato = gato
        self.gato_img = gato_img
        self.acoes = acoes_gato
        self.acoes_jogo = acoes_jogo

        self.janela = Janela()  # oi érick - oi richard :D
        self.janela.criar_janelinha((0, 0), (22, 30))  # Janela das ações
        self.janela.criar_janelinha((0, 30), (14, 79))  # Janela do gatinho

        self.janela.muda_slice(1, 1, 30,  'TAMACAT'.center(29))

        self.__add_acoes()
        self.__add_gato()
        self.__add_status()

    def __str__(self):
        return str(self.janela)

    def __add_acoes(self):

        i = 1
        for k in range(len(self.acoes)):
            if self.acoes[k] != '':
                self.janela.muda_slice(k+2, 1, 30, f'({i}) - {self.acoes[k]}'.ljust(29))
                i += 1
            else:
                self.janela.muda_slice(k+2, 1, 30, ''.ljust(29))

        self.janela.muda_slice(21-len(self.acoes_jogo), 1, 30, '-' * 29)

        for j in range(len(self.acoes_jogo)):
            self.janela.muda_slice(22-len(self.acoes_jogo)+j, 1, 30, f'({i}) - {self.acoes_jogo[j]}'.ljust(29))
            i += 1

    def __add_gato(self):
        for i in range(len(self.gato_img)):
            self.janela.muda_slice(i+1, 31, 79, self.gato_img[i].center(48))

    def __add_status(self):
        vac = 'Sim' if self.gato.vacinado else 'Não'

        self.janela.muda_slice(15, 31, 79,
                               f'Nome: {self.gato.nome}'.ljust(48))
        self.janela.muda_slice(16, 31, 79,
                               f'Idade: {self.gato.mostrar_idade()}'.ljust(48))
        self.janela.muda_slice(17, 31, 79,
                               ('Vacinado:   ' + vac).ljust(48))
        self.janela.muda_slice(18, 31, 79,
                               ('Fome:       ' + '[' + ('■' * (self.gato.fome // 5)).ljust(20) + ']').ljust(48))
        self.janela.muda_slice(20, 31, 79,
                               ('Saúde:      ' + '[' + ('■' * (self.gato.saude // 5)).ljust(20) + ']').ljust(48))
        self.janela.muda_slice(19, 31, 79,
                               ('Energia:    ' + '[' + ('■' * (self.gato.energia // 5)).ljust(20) + ']').ljust(48))
        self.janela.muda_slice(21, 31, 79,
                               ('Felicidade: ' + '[' + ('■' * (self.gato.feliz // 5)).ljust(20) + ']').ljust(48))
