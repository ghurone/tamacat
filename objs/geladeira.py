class Geladeira:

    def __init__(self, alimentos=None):
        if alimentos is None:
            alimentos = {}

        self.alimentos = alimentos

    def __str__(self):
        s = ''

        for i, nome in enumerate(self.alimentos):
            f = self.alimentos[nome]
            s += f'{f[1]}x {f[0]}\n'

        return s

    def add_comida(self, comida, quantidade):
        try:
            self.alimentos[comida.nome][1] += quantidade
        except KeyError:
            self.alimentos[comida.nome] = [comida, quantidade]

    def pegar_comida(self, comida):
        self.alimentos[comida.nome][1] -= 1

        if self.alimentos[comida.nome][1] == 0:
            del self.alimentos[comida.nome]

    def tem_comida(self, comida):
        return comida.nome in self.alimentos.keys()

    def mostrar_comidas(self, comida=None):
        if not comida:
            print(self)
        else:
            f = self.alimentos[comida.nome]
            print(f'{f[1]}x {f[0]}')
