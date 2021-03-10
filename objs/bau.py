class Bau:

    def __init__(self, brinquedos=None):
        """
        Estrutura principal formada por um dicionário self.brinquedos em que as chaves são os nomes de cada tipo de
        brinquedo (ex. bola azul) e os valores são listas com objetos Brinquedo do mesmo tipo, mas de durabilidades
        diferentes.

        {'nome_brinquedo': [Brinquedo1, Brinquedo2, Brinquedo3]}
        """
        if brinquedos is None:
            brinquedos = {}

        self.brinquedos = brinquedos

    def __str__(self):
        s = ''

        for brinquedo in self.brinquedosort():
            for brinqs in sorted(self.brinquedos[brinquedo.nome]):
                s += '|' + str(brinqs) + '|\n'

        return s

    def __getitem__(self, name):
        return self.brinquedos[name]

    def add_brinquedo(self, brinquedo):
        """Insere um Brinquedo na lista de brinquedos de seu tipo ou adiciona um tipo de Brinquedo novo."""
        try:
            self.brinquedos[brinquedo.nome].append(brinquedo)

        except KeyError:
            self.brinquedos[brinquedo.nome] = [brinquedo]

    def remover_brinquedo(self, brinquedo):
        """Remove um Brinquedo da lista de brinquedos do seu tipo ou remove um tipo de Brinquedo."""
        if len(self.brinquedos[brinquedo.nome]) <= 1:
            del self.brinquedos[brinquedo.nome]

        else:
            self.brinquedos[brinquedo.nome].remove(brinquedo)

    def tem_brinquedo(self, brinquedo):
        """Verifica se o Brinquedo está no baú."""
        return brinquedo.nome in self.brinquedos.keys()

    def numero_de_brinquedos(self):
        n = 0

        for i, k in enumerate(self.brinquedos):
            for j in self.brinquedos[k]:
                n += 1

        return n

    def brinquedosort(self):
        """Retorna uma lista de brinquedos ordenados por felicidade."""

        brinquedos = [valor[0] for valor in self.brinquedos.values()]

        for brinquedo in range(len(brinquedos) - 1, 0, -1):
            for i in range(brinquedo):
                if brinquedos[i].lt(brinquedos[i + 1]):
                    brinquedos[i], brinquedos[i + 1] = brinquedos[i + 1], brinquedos[i]

        return brinquedos
