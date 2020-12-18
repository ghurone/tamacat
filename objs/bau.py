class Bau:

    def __init__(self, brinquedos=None):
        if brinquedos is None:
            brinquedos = {}

        self.brinquedos = brinquedos

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
