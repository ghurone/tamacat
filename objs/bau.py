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

    @property
    def __str__(self):
        s = ''

        for i, nome in enumerate(self.brinquedos):
            for brinqs in self.brinquedos[nome]:
                s += str(brinqs)

        return s

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

    def mostrar_brinquedos(self, brinq=None):
        """Imprime Brinquedos de um determinado tipo, ou todos os Brinquedos do baú."""
        if not brinq:
            print(self)
        else:
            for brinqs in self.brinquedos[brinq.nome]:
                print(brinqs)
