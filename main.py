from gatinho import Gatinho
from bau import Bau
from brinquedo import Brinquedo
from geladeira import Geladeira
from comida import Comida

gato = Gatinho('Pedro', 0, 100, 100, 50)
gela = Geladeira()
pexito = Comida('pexito', 29, 13)
gela.add_comida(pexito, 19)