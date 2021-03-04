from objs.gatinho import Adotado, Resgatado, Comprado
from objs.bau import Bau
from objs.geladeira import Geladeira
from objs.comida import Comida

from tamaedit.abaGatinho import AbaGatinho
from tamaedit.abaGeladeira import AbaGeladeira
from tamaedit.abaBau import AbaBau

import tkinter as tk

from pickle import loads, dump
from tkinter import ttk
from tkinter import filedialog


class AppWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.save_path = ''

        # Configuração da janela

        self.window.title('Tamacat Edit')
        self.window.geometry('600x500')
        self.window.iconbitmap('icone.ico')
        self.window.resizable(0, 0)
        self.window.configure(background="#68BCED")

        # Widgets

        self.Titulo = tk.Label(self.window)
        self.Titulo.configure(background="#68bced")
        self.Titulo.configure(disabledforeground="#a3a3a3")
        self.Titulo.configure(font="-family {Small Fonts} -size 23 -weight bold")
        self.Titulo.configure(foreground="#ffffff")
        self.Titulo.configure(text='''TAMACAT SAVE EDIT''')

        self.EscolherSave = tk.Button(self.window)
        self.EscolherSave.configure(activebackground="#68BCED")
        self.EscolherSave.configure(activeforeground="#60F7DD")
        self.EscolherSave.configure(background="#60F7DD")
        self.EscolherSave.configure(borderwidth="0")
        self.EscolherSave.configure(disabledforeground="#a3a3a3")
        self.EscolherSave.configure(font="-family {Small Fonts} -size 8 -weight bold")
        self.EscolherSave.configure(foreground="#5484d6")
        self.EscolherSave.configure(highlightbackground="#d9d9d9")
        self.EscolherSave.configure(highlightcolor="black")
        self.EscolherSave.configure(pady="0")
        self.EscolherSave.configure(relief="flat")
        self.EscolherSave.configure(text='''Abrir save''')
        self.EscolherSave.configure(command=self.abrir_save)

        self.SalvarSave = tk.Button(self.window)
        self.SalvarSave.configure(activebackground="#68BCED")
        self.SalvarSave.configure(activeforeground="#60F7DD")
        self.SalvarSave.configure(background="#60F7DD")
        self.SalvarSave.configure(borderwidth="0")
        self.SalvarSave.configure(disabledforeground="#a3a3a3")
        self.SalvarSave.configure(font="-family {Small Fonts} -size 8 -weight bold")
        self.SalvarSave.configure(foreground="#5484d6")
        self.SalvarSave.configure(highlightbackground="#d9d9d9")
        self.SalvarSave.configure(highlightcolor="black")
        self.SalvarSave.configure(pady="0")
        self.SalvarSave.configure(relief="flat")
        self.SalvarSave.configure(state='disabled')
        self.SalvarSave.configure(text='''Salvar save''')
        self.SalvarSave.configure(command=self.salvar)

        self.Frame = tk.Frame(self.window)
        self.Frame.configure(background="#68BCED")

        # Abas

        self.Abas = ttk.Notebook(self.Frame)

        self.gato_aba = AbaGatinho(self)
        self.Abas.add(self.gato_aba.frame, text='Gatinho')

        self.gela_aba = AbaGeladeira(self)
        self.Abas.add(self.gela_aba.frame, text='Geladeira')

        self.bau_aba = AbaBau(self)
        self.Abas.add(self.bau_aba.frame, text='Baú')

        # Packing Widgets

        self.Titulo.place(x=20, y=20, height=41, width=324)
        self.EscolherSave.place(x=360, y=20, height=44, width=107)
        self.SalvarSave.place(x=480, y=20, height=44, width=107)

        self.Frame.place(relx=0.0, rely=0.16, relheight=0.85, relwidth=1.008)
        self.Abas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.window.mainloop()

    def abrir_save(self):
        save_path = filedialog.askopenfilename(defaultextension='.save', filetypes=[('Tamacat Save File', '*.save')])

        if save_path and save_path.endswith('tamacat.save'):

            with open(save_path, 'rb') as file:
                objs = file.read()
                objs = objs.split('_pE_dRo_'.encode('utf8'))

            list_objs = [loads(obj) for obj in objs[:-1]]

            self.set_gatinho(list_objs[0])
            self.set_gela(list_objs[1])
            self.set_bau(list_objs[2])

            self.save_path = save_path
            self.SalvarSave.configure(state='normal')

    def set_gatinho(self, gato):

        # Deletando as coisas:

        self.gato_aba.del_inputs()

        # Inserindo as coisas:

        self.gato_aba.NameInput.insert(tk.INSERT, gato.nome)
        self.gato_aba.IdadeInput.insert(tk.INSERT, gato.idade)
        self.gato_aba.FomeScale.set(gato.fome)
        self.gato_aba.EnergiaScale.set(gato.energia)
        self.gato_aba.SaudeScale.set(gato.saude)
        self.gato_aba.FelizScale.set(gato.feliz)

        if gato.vacinado:
            self.gato_aba.VacCheck.select()
        else:
            self.gato_aba.VacCheck.deselect()

        if gato.dormindo:
            self.gato_aba.SonoCheck.select()
        else:
            self.gato_aba.SonoCheck.deselect()

        if isinstance(gato, Resgatado):
            self.gato_aba.Tipo.current(2)
        elif isinstance(gato, Comprado):
            self.gato_aba.Tipo.current(1)
        elif isinstance(gato, Adotado):
            self.gato_aba.Tipo.current(0)

    def set_gela(self, gela):
        comidas = [(i[1], i[0].nome, i[0].saciar, i[0].saude, i[0].feliz) for i in gela.alimentos.values()]

        # Deletando as coisas

        self.gela_aba.Table.delete(*self.gela_aba.Table.get_children())
        self.gela_aba.del_inputs()

        self.gela_aba.EditarComida['state'] = 'disable'
        self.gela_aba.DelComida['state'] = 'disable'

        # Inserindo as coisas

        for comida in comidas:
            self.gela_aba.Table.insert('', tk.END, values=comida)

        self.gela_aba.AddComida['state'] = 'normal'

    def set_bau(self, bau):
        # Deletando as coisas

        self.bau_aba.Table.delete(*self.bau_aba.Table.get_children())
        self.bau_aba.del_inputs()

        self.bau_aba.EditarBrinq['state'] = 'disable'
        self.bau_aba.DelBrinq['state'] = 'disable'

        # Inserindo as coisas

        for i in bau.brinquedos.values():
            for brinq in i:
                tipo = self.bau_aba.tipo_brinq(brinq)
                self.bau_aba.Table.insert('', tk.END, values=(brinq.nome, brinq.feliz, brinq.dura, tipo))

        self.bau_aba.AddBrinq['state'] = 'normal'

    def salvar(self):
        gela = Geladeira()
        bau = Bau()

        # Criando o objeto Gato

        nome = self.gato_aba.NameInput.get()
        idade = int(self.gato_aba.IdadeInput.get())
        fome = int(self.gato_aba.FomeScale.get())
        energ = int(self.gato_aba.EnergiaScale.get())
        saude = int(self.gato_aba.SaudeScale.get())
        feliz = int(self.gato_aba.FelizScale.get())
        vac = True if self.gato_aba.Vac.get() == 1 else False

        gato = eval(self.gato_aba.Tipo.get())(nome, idade, fome, energ, saude, feliz, vac)

        if self.gato_aba.Sono.get() == 1:
            gato.dormindo = True

        # Criando o objeto da geladeira

        for i in self.gela_aba.Table.get_children():
            valores = self.gela_aba.Table.item(i)["values"]
            comida = Comida(valores[1], int(valores[2]), int(valores[3]), int(valores[4]))
            gela.add_comida(comida, int(valores[0]))

        # Criando o objeto do baú

        for i in self.bau_aba.Table.get_children():
            valores = self.bau_aba.Table.item(i)["values"]
            brinq = eval(valores[3])(valores[0], int(valores[1]), int(valores[2]))
            bau.add_brinquedo(brinq)

        objs = [gato, gela, bau]
        for i in range(len(objs)):
            t = 'ab'
            if i == 0:
                t = 'wb'

            with open(self.save_path, t) as file:
                dump(objs[i], file)
                file.write(bytes('_pE_dRo_'.encode('utf8')))


if __name__ == '__main__':
    AppWindow()
