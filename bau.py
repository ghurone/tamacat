class Bau:

    def __init__(self, brinquedos=None):
        if brinquedos is None:
            brinquedos = {}

        self.brinquedos = brinquedos

    def add_brinquedo(self, brinquedo):
        self.brinquedos[brinquedo.nome] = brinquedo
        # se tiver o brinquedo não precisa adicionar (?)

    def pegar_brinquedo(self, nome):
        return self.brinquedos[nome]
