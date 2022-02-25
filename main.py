import config.funcoes as cfunc
import config.saveload as csave
import config.janela as cjane
import config.gatos_ascii as cga
import objs.gatinho as ogato
import objs.geladeira as ogela
import objs.bau as obau

from random import randint, choice
from time import sleep


def janela_titulo() -> cjane.Janela:
    janela = cjane.Janela()
    
    fonte = ['                                    /)                              ',
             '                            |\\---/|((                              ',
             "                            | ° ° | ))                              ",
             '                             \\_T_/_//                               ',
             ' ________  _______  _____ _{_}_  {_}____  ______  _______  ________ ',
             '|_      _||   _   ||    | |    ||   _   ||   ___||   _   ||_      _|',
             '  |    |  |  |_|  ||     -     ||  |_|  ||  |    |  |_|  |  |    |  ',
             '  |    |  |   _   ||   _   _   ||   _   ||  |___ |   _   |  |    |  ',
             '  |____|  |__| |__||__| |_| |__||__| |__||______||__| |__|  |____|  ']
    
    for i in range(len(fonte)):
        janela.muda_linha(i + 1, fonte[i])

    janela.muda_linha(11, 'O MELHOR JOGO DO MUNDO!')
    janela.muda_linha(21, '© RaGhu 2021 ', alin='rjust')
    
    return janela


def tela_inicial() -> None:
    """
    Printa a tela inicial do jogo. 
    """
    janela = janela_titulo()

    janela.muda_linha(15, '.-----------------------------.')
    janela.muda_linha(16, '|   Aperte ENTER para jogar!  |')
    janela.muda_linha(17, "'-----------------------------'")
    
    print(janela)
    input()
    
    
def menu_principal() -> str:
    cfunc.mudar_titulo('Menu principal')
    janela = janela_titulo()
    
    janela.muda_linha(15, '(1) Novo Jogo         ')
    janela.muda_linha(16, '(2) Carregar Jogo     ')
    janela.muda_linha(17, '(3) Deletar Jogo      ')
    janela.muda_linha(18, '(4) Sair              ')
    
    print(janela)
    op = input('Digite a opção desejada: ')
    
    while op not in ['1', '2', '3', '4']:
        print(janela)
        op = input('Digite uma opção válida: ')
    
    return op


def novo_gato() -> tuple:
    """
    Printa uma janela para criar um novo jogo.
    
    Retorna uma tupla (Gatinho, Geladeira, Baú) de um novo gato.
    """
    cfunc.mudar_titulo('Novo jogo')
    
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

    esc = input('>>> ').lower()
    while esc != 'c' and esc != 'r' and esc != 'a' and esc != 'comprar' and esc != 'resgatar' and esc != 'adotar':
        
        janela.muda_linha(11, '   Digite uma opção válida!', 'ljust')     
        print(janela)
        esc = input('>>> ').lower()

    janela.limpar_janela()

    v = 0
    if esc[0] in 'c':
        janela.muda_linha(1, f'  Você conversou com o conhecido do seu amigo e comprou {letra_c} gatinh{letra_c}!',
                          'ljust')

        idade = randint(2, 12)
        fome = 100
        energia = randint(75, 100)
        saude = 100
        feliz = randint(80, 100)
        vac = True

        ga = ogato.Comprado('', idade, fome, energia, saude, feliz, gen_c, vac)

    elif esc[0] in 'r':
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
        i = input('>>> ').lower()
        
        while i != 'o' and i != 'a' and i != 'gatinho' and i != 'gatinha':
            janela.muda_linha(2, '   Digite uma opção válida!', 'ljust')                
            print(janela)
            i = input('>>> ').lower()
        
        if i[-1] == 'a':
            gen_a = 'F'
            um_a = 'a'
            letra_a = um_a
            pron_a = um_a
        elif i[-1] == 'o':
            gen_a = 'M'
            um_a = ''
            letra_a = 'o'
            pron_a = 'e'
        
        janela.muda_linha(2, f'   - Gatinh{letra_a}', 'ljust')
        print(janela)
        
        sleep(1)
        
        janela.muda_linha(4, f'  Você vai adotar um{um_a} gat{letra_a} (F)ilhote, (A)dult{letra_a} ou (I)dos{letra_a}?',
                          'ljust')
        print(janela)
        i = input('>>> ').lower()

        while i != 'f' and i != 'a' and i != 'i' and i != 'filhote' and i != 'adulto' and i != 'idoso':
            janela.muda_linha(5, '   Digite uma opção válida!', 'ljust')
            print(janela)
            i = input('>>>').lower()
            
        if i[0] == 'f':
            idade = randint(3, 12)
            janela.muda_linha(5, '   - Filhote', 'ljust')
            
        elif i[0] == 'a':
            idade = randint(13, 84)
            janela.muda_linha(5, f'   - Adult{letra_a}', 'ljust')
            
        elif i[0] == 'i':
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
    
    p = ga.gens['pron']
    janela.muda_linha(3+v, f'  Hora de uma decisão difícil... Qual vai ser o nome del{p}?', 'ljust')
    print(janela)
    nome = input('>>> ')

    while not cfunc.verificar_nome(nome):
        
        if cfunc.existe_save(nome):
            gatolino = csave.carregar_jogo(nome)[0]
            l_existe = gatolino.gens['letra']
            p_existe = gatolino.gens['pron']
            janela.muda_linha(4+v, f'   Ess{p_existe} gatinh{l_existe} já existe! Escolha outro nome.', 'ljust')
        else:
            janela.muda_linha(4+v, '   Digite um nome válido (e com tamanho menor que 32)!', 'ljust')
            
        print(janela)
        nome = input('>>> ')
    
    ga.nome = nome  # cria o nome do gato
    ge = ogela.Geladeira()
    ba = obau.Bau()

    return ga, ge, ba


def tela_carregar_gato() -> tuple:
    cfunc.mudar_titulo('Carregar jogo')
    gatos = csave.listar_saves()
    
    if len(gatos) == 0:
        janela = cjane.Janela()
        janela.muda_linha(11, 'Você não possui nenhum gato, deseja criar um? (S)im ou (N)ão')
        
        print(janela)
        
        esc = input('>>> ').lower()
        while esc != 's' and esc != 'n' and esc != 'sim' and esc != 'não' and esc != 'nao':
            janela.muda_linha(12, 'Digite uma opção válida!')
            print(janela)
            esc = input('>>> ').lower()    
        
        if 's' in esc:
            return novo_gato()
        elif 'n' in esc:
            return ()
        
    elif len(gatos) == 1:
        save = csave.carregar_jogo(gatos[0].split(".")[0])
        if save:
            return save

        janela = cjane.Janela()
        janela.muda_linha(11, 'Jogo corrompido!!')
        print(janela)
        input('(Aperte ENTER para voltar...)')
        
    elif len(gatos) > 1:
        janela = cjane.JanelaTable({'##': 4, 'Gato': 52, 'Idade': 20})
        gatitos = []
        pos = []
        
        v = 1
        for gato in gatos:
            nome = gato.split(".")[0]
            save = csave.carregar_jogo(nome)
            
            if save:
                ga, ge, ba = save
                gatitos.append((ga, ge, ba))
                janela.add_linha([v, ga.nome, ga.mostrar_idade()])
                pos.append(v)
                v += 1
            else:
                janela.add_linha(['X', f'{nome} (CORROMPIDO)', 'X'])
        
        janela.mostrar_janela(False)
        esc = input('Digite o número do gato para carregar (ENTER para voltar): ').lower()
        
        while esc != '' and (not esc.isnumeric() or int(esc) not in pos):
            janela.mostrar_janela(False)
            esc = input('Digite uma opção válida (ENTER para voltar): ').lower()
        
        if esc != '':
            return gatitos[int(esc)-1]
        else:
            return ()
    

def tela_deletar_gato() -> None:
    cfunc.mudar_titulo('Deletar jogo')
    gatos = csave.listar_saves()
    
    if len(gatos) == 0:
        janela = cjane.Janela()
        janela.muda_linha(11, 'Você não possui nenhum gato para deletar!!')
        
        print(janela)
        input('(Aperte ENTER para voltar...)')
        
    elif len(gatos) == 1:
        nome = gatos[0].split(".")[0]

        janela = cjane.Janela()
        janela.muda_linha(11, f'Deseja deletar o jogo ({nome})? (S)im ou (N)ão')
        
        print(janela)
        
        esc = input('>>> ').lower()
        while esc != 's' and esc != 'n' and esc != 'sim' and esc != 'não' and esc != 'nao':
            janela.muda_linha(12, 'Digite uma opção válida!')
            print(janela)
            esc = input('>>> ').lower()    
        
        if 's' in esc:
            csave.deletar_jogo(nome)
        
    elif len(gatos) > 1:
        janela = cjane.JanelaTable({'##': 4, 'Gato': 52, 'Idade': 20})
        nomes = []
        
        for i in range(len(gatos)):
            nome = gatos[i].split(".")[0]
            nomes.append(nome)
            save = csave.carregar_jogo(nome)
            
            if save:
                ga = save[0]
                janela.add_linha([i+1, ga.nome, ga.mostrar_idade()])
            else:
                janela.add_linha([str(i+1), f'{nome} (CORROMPIDO)', 'X'])
        
        janela.mostrar_janela(False)
        esc = input('Digite o número do gato para DELETAR (ENTER para voltar): ').lower()
        
        while esc != '' and (not esc.isnumeric() or int(esc) not in range(1, len(gatos)+1)):
            janela.mostrar_janela(False)
            esc = input('Digite uma opção válida (ENTER para voltar): ').lower()
        
        if esc != '':
            nome = nomes[int(esc)-1]
            janela = cjane.Janela()
            janela.muda_linha(11, f'Deseja deletar o jogo ({nome})? (S)im ou (N)ão')
            
            print(janela)
            
            esc = input('>>> ').lower()
            while esc != 's' and esc != 'n' and esc != 'sim' and esc != 'não' and esc != 'nao':
                janela.muda_linha(12, 'Digite uma opção válida!')
                print(janela)
                esc = input('>>> ').lower()    
            
            if 's' in esc:
                csave.deletar_jogo(nome)
 
        
def menu_jogo(gato:ogato.Gatinho, gato_img:list) -> None:
    """
    Imprime as características do gato.
    """

    acoes = ['',
             'Ver geladeira',
             'Comer',
             '',
             'Ver baú',
             'Brincar']

    acoes_jogo = ['Salvar o jogo',
                  f'Abandonar {gato.gens["letra"]} gat{gato.gens["letra"]} :(',
                  'Voltar ao menu']

    janela = cjane.JanelaMenu(gato_img, acoes, acoes_jogo, gato)

    print(janela)


def mostrar_geladeira(gela:ogela.Geladeira) -> None:
    """
    Mostra todos os alimentos da geladeira, em ordem decrescente de magnitude do saciamento.
    """

    cfunc.mudar_titulo('Geladeira')

    janela = cjane.JanelaTable({'QTE.': 6, 'Nome': 36, 'Tipo': 15, 'Fome': 8, 'Saúde': 9})

    for comida in gela.comidasort():
        linha = [gela[comida.nome][1], comida.nome, comida.__class__.__name__, comida.saciar, comida.saude]
        janela.add_linha(linha)

    janela.mostrar_janela()
    
    
def mostrar_bau(bau:obau.Bau) -> None:
    """
    Mostra todos os brinquedos do baú.
    Tipos diferentes: ordem decrescente, por felicidade.
    Mesmo tipo: ordem crescente, por durabilidade.
    """

    cfunc.mudar_titulo('Baú')

    janela = cjane.JanelaTable({'Nome': 32, 'Felicidade': 22, 'Usos restantes': 22})

    for brinquedo in bau.brinquedosort():
        for brinqs in sorted(bau[brinquedo.nome]):
            brinq = [brinqs.nome, brinqs.feliz, brinqs.dura]
            janela.add_linha(brinq)

    janela.mostrar_janela()


def brincar(gato:ogato.Gatinho, bau:obau.Bau) -> bool:
    """
    Ações principais da ação brincar no menu.
    """

    cfunc.mudar_titulo('Escolher brinquedo')
    janela = cjane.JanelaTable({'##': 4, 'Nome': 58, 'Felicidade': 14})

    # imprime os brinquedos disponíveis para brincar em ordem de felicidade
    brinqs = bau.brinquedosort()
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
        menor_dura = min(bau[brinq_nome])

        cfunc.mudar_titulo(f'Brincando com {brinq_nome}')

        gato.brincar(bau, menor_dura)
        return True
    
    else:
        return False


def comer(gato:ogato.Gatinho, gela:ogela.Geladeira) -> bool:
    cfunc.mudar_titulo('Escolher comida')
    
    comidas_tipos = gela.comida_por_classe()
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
            
            gato.comer(gela, comida)
            
            return True
            
        else:
            return False
        
    else:
        return False


def run_game(gato:ogato.Gatinho, gela:ogela.Geladeira, bau:obau.Bau) -> None:
    
    salvo = True
    running = True
    
    while running:
        cfunc.mudar_titulo('Menu')
        cfunc.limpar_tela()
        menu_jogo(gato, gato_img=cga.gatitos['Padrão'])

        esc = input('>>> ').lower()

        if esc == '1':
            # Ver geladeira
            cfunc.limpar_tela()
            mostrar_geladeira(gela)

        elif esc == '2':
            cfunc.limpar_tela()
            if comer(gato, gela):
                salvo = False

        elif esc == '3':
            # Ver bau
            cfunc.limpar_tela()
            mostrar_bau(bau)

        elif esc == '4':
            cfunc.limpar_tela()
            if brincar(gato, bau):
                salvo = False

        elif esc == '5':
            # Salvar jogo
            cfunc.limpar_tela()
            csave.salvar_jogo((gato, gela, bau))

            salvo = True
            cfunc.janela_salvar()
            sleep(1)

        elif esc == '6':
            # Deletar jogo (abandonar gato)
            cfunc.limpar_tela()
            if cfunc.janela_deletar(gato.nome):
                running = False

        elif esc == '7':
            # Sair do jogo
            cfunc.limpar_tela()
            if cfunc.janela_voltar(salvo, gato, gela, bau):
                running = False
        
        elif esc == 'creditos' or esc == 'créditos':
            cfunc.limpar_tela()
            cfunc.janela_creditos()
        
        else:
            continue


if __name__ == '__main__':
    cfunc.ajustes_iniciais()
    tela_inicial()
    
    running = True
    while running:
        
        op = menu_principal()
        if op == '1':
            objs = novo_gato()
        elif op == '2':
            objs = tela_carregar_gato()
        elif op == '3':
            tela_deletar_gato()
            objs = ()
        elif op == '4':
            objs = ()
            running = False
        
        if objs:
            gato, gela, bau = objs
            csave.salvar_jogo((gato, gela, bau))
            run_game(gato, gela, bau)

    cfunc.janela_sair()
