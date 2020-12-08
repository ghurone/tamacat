from gatinho import Gatinho
from bau import Bau
from brinquedo import Brinquedo
from geladeira import Geladeira
from comida import Comida
from saveload import salvar_jogo, carregar_jogo

gato = Gatinho('Pedro', 0, 100, 100, 50)
gela = Geladeira()
pexito = Comida('pexito', 29, 13)
gela.add_comida(pexito, 19)

salvar_jogo(gato, gela)
gato_salvo, gela_salvo = carregar_jogo()

print(gato.nome, gato_salvo.nome)
print(gela.alimentos, gela_salvo.alimentos)
print(gela.alimentos['pexito'], gela_salvo.alimentos['pexito'])
print(gela.alimentos['pexito'][0].nome, gela_salvo.alimentos['pexito'][0].nome)