class Geladeira:

    def __init__(self, alimentos=None):
        """
        Estrutura principal formada por um dicionário self.alimentos em que as chaves são os nomes dos alimentos e os
        valores são listas que contém o objeto Comida e a sua quantidade na geladeira.

        {'nome_alimento': [Comida, quantidade]}
        """
        if alimentos is None:
            alimentos = {}

        self.alimentos = alimentos

    def __str__(self):
        s = ''

        comidas = sorted([valor[0] for valor in self.alimentos.values()], reverse=True)

        for comida in comidas:
            f = self.alimentos[comida.nome]
            s += '|' + f'{f[1]}'.center(6) + '|' + str(f[0]) + '|\n'

        return s

    def __getitem__(self, name):
        return self.alimentos[name]

    def add_comida(self, comida, quantidade=1):
        """Adiciona uma determinada quantidade da Comida."""
        try:
            self.alimentos[comida.nome][1] += quantidade
        except KeyError:
            self.alimentos[comida.nome] = [comida, quantidade]

    def pegar_comida(self, comida):
        """Diminui em 1 a quantidade da Comida ou a remove da geladeira."""
        self.alimentos[comida.nome][1] -= 1

        if self.alimentos[comida.nome][1] == 0:
            del self.alimentos[comida.nome]

    def tem_comida(self, comida):
        """Verifica se a Comida está na geladeira."""
        return comida.nome in self.alimentos.keys()

    def mostrar_comidas(self, comida=None):
        """Imprime uma Comida em específico e sua quantidade, ou todos os alimentos na geladeira."""
        if not comida:
            print(self)
        else:
            f = self.alimentos[comida.nome]
            print(f'{f[1]}x {f[0]}')

    def comida_por_classe(self):

        c = {}
        for val in self.alimentos.values():
            comida = val[0]

            try:
                c[comida.__class__.__name__].append(comida)
            except KeyError:
                c[comida.__class__.__name__] = [comida]

        return c

    def comidasort(self):
        c = self.comida_por_classe()

        aux = []
        for key in sorted(c.keys(), key=len, reverse=True):
            aux += sorted(c[key], reverse=True)

        return aux
