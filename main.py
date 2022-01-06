import config.funcoes as cfunc
import config.saveload as csave
import config.janela as cjane
import config.gatos_ascii as cga
import objs.gatinho as ogato
import objs.geladeira as ogela
import objs.bau as obau

from random import randint, choice
from time import sleep

humores = ['feliz', 'triste', 'quieto', 'brincalhão', 'carinhoso', 'assustado', 'irritado']


class Main:
    def __init__(self):
        cfunc.ajustes_iniciais()
        self.tela_inicial()

        if csave.carregar_jogo():
            self.gato, self.gela, self.bau = csave.carregar_jogo()
            cfunc.janela_carregar()
            sleep(1)

        else:
            self.gato, self.gela, self.bau = self.novo_gato()
            csave.salvar_jogo(self.gato, self.gela, self.bau)

        self.salvo = True

    @staticmethod
    def tela_inicial():
        """`Printa a tela inicial do jogo."""

        fonte = ['                                    /)                              ',
                 '                            |\\---/|((                              ',
                 "                            | ° ° | ))                              ",
                 '                             \\_T_/_//                               ',
                 ' ________  _______  _____ _{_}_  {_}____  ______  _______  ________ ',
                 '|_      _||   _   ||    | |    ||   _   ||   ___||   _   ||_      _|',
                 '  |    |  |  |_|  ||     -     ||  |_|  ||  |    |  |_|  |  |    |  ',
                 '  |    |  |   _   ||   _   _   ||   _   ||  |___ |   _   |  |    |  ',
                 '  |____|  |__| |__||__| |_| |__||__| |__||______||__| |__|  |____|  ']

        botao = ['.-----------------------------.',
                 '|   Aperte ENTER para jogar!  |',
                 "'-----------------------------'"]

        janela = cjane.Janela()

        for i in range(len(fonte)):
            janela.muda_linha(i + 1, fonte[i])
            try:
                janela.muda_linha(i + 15, botao[i])
            except IndexError:
                pass

        janela.muda_linha(11, 'O MELHOR JOGO DO MUNDO!')
        janela.muda_linha(20, '© RaGhu 2021 ', alin='rjust')

        print(janela)
        input()  # para não dar para digitar nada no input além de enter

    @staticmethod
    def novo_gato():
        """Retorna um Gatinho, Geladeira e Bau para um gato inicial."""
        
        gen_c = choice(['F', 'M'])
        gen_r = choice(['F', 'M'])
        
        if gen_c == 'F':
            um_c = 'a'
            letra_c = um_c
            pron_c = um_c
        else:
            um_c = ''
            letra_c = 'o'
            pron_c = 'e'
        
        if gen_r == 'F':
            um_r = 'a'
            letra_r = um_r
            pron_r = um_r
        else:
            um_r = ''
            letra_r = 'o'
            pron_r = 'e'

        textos1 = ['  Você está pensando em ter um gato.',
                   f'  Um amigo seu conhece alguém que está vendendo um{um_c} gat{letra_c} bonitinh{letra_c}.',
                   f'  Mas também tem um{um_r} gat{letra_r} que sempre têm andado pela vizinhança,',
                   f' e el{pron_r} parece muito simpátic{letra_r}.',
                   '  Por outro lado, também existe um abrigo de gatos perto da sua casa.']

        cfunc.limpar_tela()
        janela = cjane.Janela()

        j = 1
        i = 0
        while i < len(textos1):
            janela.muda_linha(j, textos1[i], 'ljust')
            if i == 2:
                j += 1
                janela.muda_linha(j, textos1[i+1], 'ljust')

            print(janela)
            input('(Aperte ENTER para continuar...)')

            j += 2
            i += 1 if i != 2 else 2

        janela.muda_linha(10, '  Você deseja (C)omprar, (R)esgatar ou (A)dotar o gato?', 'ljust')
        print(janela)

        escolha = input('>>> ')
        while escolha.lower() != 'c' and escolha.lower() != 'r' and escolha.lower() != 'a' \
                and escolha.lower() != 'comprar' and escolha.lower() != 'resgatar' and escolha.lower() != 'adotar':
            
            janela.muda_linha(11, '   Digite uma opção válida!', 'ljust')     
            print(janela)
            escolha = input('>>> ')

        janela.limpar_janela()

        v = 0
        if escolha[0] in 'Cc':
            janela.muda_linha(1, f'  Você conversou com o conhecido do seu amigo e comprou {letra_c} gatinh{letra_c}!', 'ljust')

            idade = randint(2, 12)
            fome = 100
            energia = randint(75, 100)
            saude = 100
            feliz = randint(80, 100)
            vac = True

            ga = ogato.Comprado('', idade, fome, energia, saude, feliz, gen_c, vac)

        elif escolha[0] in 'Rr':
            janela.muda_linha(1, f'  Você resgatou {letra_r} gatinh{letra_r}. Agora el{pron_r} tem um dono!', 'ljust')

            idade = randint(0, 180)
            fome = randint(10, 100)
            energia = randint(10, 90)
            saude = randint(10, 50)
            feliz = randint(10, 90)
            vac = False

            ga = ogato.Resgatado('', idade, fome, energia, saude, feliz, gen_r, vac)

        else:
            v = 1
            janela.muda_linha(1, '  Você quer adotar um gatinh(o) ou uma gatinh(a)?', 'ljust')
            print(janela)
            i = input('>>> ')
            
            while i.lower() != 'o' and i.lower() != 'a' and i.lower() != 'gatinho' and i.lower() != 'gatinha':
                janela.muda_linha(2, '   Digite uma opção válida!', 'ljust')                
                print(janela)
                i = input('>>> ')
            
            if i[-1].lower() == 'a':
                gen_a = 'F'
                um_a = 'a'
                letra_a = um_a
                pron_a = um_a
            elif i[-1].lower() == 'o':
                gen_a = 'M'
                um_a = ''
                letra_a = 'o'
                pron_a = 'e'
            
            janela.muda_linha(2, f'   - Gatinh{letra_a}', 'ljust')
            print(janela)
            
            sleep(1)
            
            janela.muda_linha(4, f'  Você vai adotar um{um_a} gat{letra_a} (F)ilhote, (A)dult{letra_a} ou (I)dos{letra_a}?', 'ljust')
            print(janela)
            i = input('>>> ')

            while i.lower() != 'f' and i.lower() != 'a' and i.lower() != 'i' \
                and i.lower() != 'filhote' and i.lower() != 'adulto' and i.lower() != 'idoso':
                janela.muda_linha(5, '   Digite uma opção válida!', 'ljust')
                print(janela)
                i = input('>>>')
                
            if i[0].lower() == 'f':
                idade = randint(3, 12)
                janela.muda_linha(5, '   - Filhote', 'ljust')
                
            elif i[0].lower() == 'a':
                idade = randint(13, 84)
                janela.muda_linha(5, f'   - Adult{letra_a}', 'ljust')
                
            elif i[0].lower() == 'i':
                idade = randint(85, 180)
                janela.muda_linha(5, f'   - Idos{letra_a}', 'ljust')
                
            print(janela)
            sleep(2)
            
            janela.limpar_janela()
            janela.muda_linha(1, f'  Você foi até o abrigo e escolheu um{um_a} gatinh{letra_a}.', 'ljust')
            janela.muda_linha(2, f' Ou será que foi el{pron_a} quem te escolheu?', 'ljust')

            fome = randint(60, 100)
            energia = randint(70, 100)
            saude = randint(70, 90)
            feliz = randint(80, 100)
            vac = choice([True, True, True, False, False])  # True: 60%, False: 40%

            ga = ogato.Adotado('', idade, fome, energia, saude, feliz, gen_a, vac)

        print(janela)
        input('(Aperte ENTER para continuar...)')
        
        l = ga.gens['letra']
        janela.muda_linha(3+v, f'  Hora de uma decisão difícil... Qual vai ser o nome d{l} gat{l}?', 'ljust')
        print(janela)
        nome = input('>>> ')

        while not cfunc.verificar_nome(nome):
            janela.muda_linha(4+v, '   Digite um nome válido (e com tamanho menor que 32)!', 'ljust')
            print(janela)
            nome = input('>>> ')

        ga.nome = nome
        ge = ogela.Geladeira()
        ba = obau.Bau()

        return ga, ge, ba

    def menu(self, gato_img):
        """Imprime as características do gato."""

        acoes = ['', 'Ver geladeira',
                 'Comer', '',
                 'Ver baú',
                 'Brincar'
                 ]

        acoes_jogo = ['Salvar o jogo',
                      f'Abandonar {self.gato.gens["letra"]} gat{self.gato.gens["letra"]} :(',
                      'Sair'
                      ]

        janela = cjane.JanelaMenu(gato_img, acoes, acoes_jogo, self.gato)

        print(janela)

    def mostra_gela(self):
        """Mostra todos os alimentos da geladeira, em ordem decrescente de magnitude do saciamento."""

        cfunc.mudar_titulo('Geladeira')

        janela = cjane.JanelaTable({'QTE.': 6, 'Nome': 36, 'Tipo': 15, 'Fome': 8, 'Saúde': 9})

        for comida in self.gela.comidasort():
            linha = [self.gela[comida.nome][1], comida.nome, comida.__class__.__name__,
                     comida.saciar, comida.saude]
            janela.add_linha(linha)

        janela.mostrar_janela()

    def mostrar_bau(self):
        """Mostra todos os brinquedos do baú.
        Tipos diferentes: ordem decrescente, por felicidade.
        Mesmo tipo: ordem crescente, por durabilidade."""

        cfunc.mudar_titulo('Baú')

        janela = cjane.JanelaTable({'Nome': 32, 'Felicidade': 22, 'Usos restantes': 22})

        for brinquedo in self.bau.brinquedosort():
            for brinqs in sorted(self.bau[brinquedo.nome]):
                brinq = [brinqs.nome, brinqs.feliz, brinqs.dura]
                janela.add_linha(brinq)

        janela.mostrar_janela()

    def brincar(self):
        """Ações principais da ação brincar no menu."""

        cfunc.mudar_titulo('Escolher brinquedo')

        janela = cjane.JanelaTable({'##': 4, 'Nome': 58, 'Felicidade': 14})

        # imprime os brinquedos disponíveis para brincar em ordem de felicidade
        brinqs = self.bau.brinquedosort()
        for i in range(len(brinqs)):
            janela.add_linha([i+1, brinqs[i].nome, brinqs[i].feliz])

        janela.mostrar_janela(show_input=False)

        brinq = input('Digite o número do brinquedo para jogar (ENTER para voltar): ')
        while brinq != '' and (not brinq.isnumeric() or int(brinq) not in range(1, len(brinqs)+1)):
            janela.mostrar_janela(show_input=False)

            if not brinq.isnumeric():
                brinq = input('Digite um valor numérico (ENTER para voltar): ')
            else:
                brinq = input('Digite um número válido (ENTER para voltar): ')

        if brinq != '':
            # seleciona o brinquedo com menor durabilidade dentre os do tipo escolhido para brincar
            brinq_nome = brinqs[int(brinq) - 1].nome
            menor_dura = min(self.bau[brinq_nome])

            cfunc.mudar_titulo(f'Brincando com {brinq_nome}')

            self.gato.brincar(self.bau, menor_dura)
            return True
        
        else:
            return False

    def comer(self):
        cfunc.mudar_titulo('Escolher comida')
        
        comidas_tipos = self.gela.comida_por_classe()
        tipos = list(comidas_tipos.keys())
        
        janela_tipos = cjane.JanelaTable({'##': 4, 'Tipo': 73})
        
        for i in range(len(tipos)):
            janela_tipos.add_linha([i+1, tipos[i]])
        
        janela_tipos.mostrar_janela(show_input=False)
        
        tipo_index = input('Digite o número do tipo de comida para comer (ENTER para voltar): ')
        while tipo_index != '' and (not tipo_index.isnumeric() or int(tipo_index) not in range(1, len(tipos)+1)):
            janela_tipos.mostrar_janela(show_input=False)
            
            if not tipo_index.isnumeric():
                tipo_index = input('Digite um valor numérico (ENTER para voltar): ')
            else:
                tipo_index = input('Digite um número válido (ENTER para voltar): ')
        
        if tipo_index != '':
            tipo = tipos[int(tipo_index)-1]
            comidas = comidas_tipos[tipo]
            
            janela = cjane.JanelaTable({'##': 4, 'Nome': 50, 'Fome': 10, 'Saúde': 11})
            
            for i in range(len(comidas)):
                janela.add_linha([i+1, comidas[i].nome, comidas[i].saciar, comidas[i].saude])
                
            janela.mostrar_janela(show_input=False)
            
            comida_index = input('Digite o número da comida para comer (ENTER para voltar ao menu): ')
            while comida_index != '' and (not comida_index.isnumeric() or int(comida_index) not in range(1, len(comidas)+1)):
                janela_tipos.mostrar_janela(show_input=False)
                
                if not comida_index.isnumeric():
                    comida_index = input('Digite um valor numérico (ENTER para voltar ao menu): ')
                else:
                    comida_index = input('Digite um número válido (ENTER para voltar ao menu): ')
            
            if comida_index != '':
                comida = comidas[int(comida_index)-1]
                cfunc.mudar_titulo(f'Comendo {comida.nome}')
                
                self.gato.comer(self.gela, comida)
                
                return True
                
            else:
                return False
            
        else:
            return False
        
        
    def run_game(self):

        while True:
            cfunc.mudar_titulo('Menu')
            cfunc.limpar_tela()
            self.menu(gato_img=cga.gatitos['Padrão'])

            esc = input('>>> ')

            if esc == '1':
                # Ver geladeira
                cfunc.limpar_tela()
                self.mostra_gela()

            elif esc == '2':
                cfunc.limpar_tela()
                if self.comer():
                    self.salvo = False

            elif esc == '3':
                # Ver bau
                cfunc.limpar_tela()
                self.mostrar_bau()

            elif esc == '4':
                cfunc.limpar_tela()
                if self.brincar():
                    self.salvo = False

            elif esc == '5':
                # Salvar jogo
                cfunc.limpar_tela()
                csave.salvar_jogo(self.gato, self.gela, self.bau)

                self.salvo = True
                cfunc.janela_salvar()
                sleep(1)

            elif esc == '6':
                # Deletar jogo (abandonar gato)
                cfunc.limpar_tela()
                if cfunc.janela_deletar():
                    break

            elif esc == '7':
                # Sair do jogo
                cfunc.limpar_tela()
                if cfunc.janela_sair(self.salvo, self.gato, self.gela, self.bau):
                    break
            
            elif esc.lower() == 'creditos' or esc.lower() == 'créditos':
                cfunc.limpar_tela()
                cfunc.janela_creditos()
            
            else:
                continue


if __name__ == '__main__':

    game = Main()
    game.run_game()
