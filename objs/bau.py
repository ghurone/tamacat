class Bau:

    def __init__(self, brinquedos=None):
        if brinquedos is None:
            brinquedos = {}

        self.brinquedos = brinquedos

    def __str__(self):
        s = ''

        for i, nome in enumerate(self.brinquedos):
            for brinqs in self.brinquedos[nome]:
                s += str(brinqs)

        return s

    def add_brinquedo(self, brinquedo):
        try:
            self.brinquedos[brinquedo.nome].append(brinquedo)

        except KeyError:
            self.brinquedos[brinquedo.nome] = [brinquedo]

    def remover_brinquedo(self, brinquedo):
        if len(self.brinquedos[brinquedo.nome]) <= 1:
            del self.brinquedos[brinquedo.nome]

        else:
            self.brinquedos[brinquedo.nome].remove(brinquedo)

    def tem_brinquedo(self, brinquedo):
        return brinquedo.nome in self.brinquedos.keys()

    def mostrar_brinquedos(self, brinq=None):
        if not brinq:
            print(self)
        else:
            for brinqs in self.brinquedos[brinq.nome]:
                print(brinqs)
