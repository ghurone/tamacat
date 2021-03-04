import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class AbaBau:

    def __init__(self, app):
        self.list_tipos = sorted(['Bola', 'Caixa', 'Varinha', 'Arranhador', 'Torre', 'Nave', 'Ioio', 'Ratinho'])

        self.frame = tk.Frame(app.window, background="#68BCED")

        self.BrinqFrame = tk.Frame(self.frame)
        self.BrinqFrame.place(relx=0.033, rely=0.05, relheight=0.738, relwidth=0.476)
        self.BrinqFrame.configure(background="#60F7DD")
        self.BrinqFrame.configure(highlightbackground="#d9d9d9")
        self.BrinqFrame.configure(highlightcolor="black")

        self.Table = ttk.Treeview(self.BrinqFrame, show='headings')
        self.Table.configure(column=('c1', 'c2', 'c3', 'c4'), select='browse')

        self.Table.column('#1', anchor=tk.CENTER, width=130)
        self.Table.heading('#1', text='Nome')
        self.Table.column('#2', anchor=tk.CENTER, width=50)
        self.Table.heading('#2', text='Feliz')
        self.Table.column('#3', anchor=tk.CENTER, width=50)
        self.Table.heading('#3', text='Dura')
        self.Table.column('#4', anchor=tk.CENTER, width=80)
        self.Table.heading('#4', text='Tipo')

        self.Table.bind('<<TreeviewSelect>>', self.row_select)

        self.ScrollY = tk.Scrollbar(self.BrinqFrame)
        self.ScrollY.pack(side=tk.RIGHT, fill=tk.Y)
        self.ScrollY.configure(command=self.Table.yview)
        self.Table.configure(yscrollcommand=self.ScrollY.set)

        self.ScrollX = tk.Scrollbar(self.BrinqFrame, orient='horizontal')
        self.ScrollX.pack(side=tk.BOTTOM, fill=tk.X)
        self.ScrollX.configure(command=self.Table.xview)
        self.Table.configure(xscrollcommand=self.ScrollX.set)

        self.Table.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)

        self.BrinqEditFrame = tk.Frame(self.frame)
        self.BrinqEditFrame.place(relx=0.534, rely=0.05, relheight=0.738, relwidth=0.442)
        self.BrinqEditFrame.configure(background="#60F7DD")
        self.BrinqEditFrame.configure(highlightbackground="#d9d9d9")
        self.BrinqEditFrame.configure(highlightcolor="black")

        self.BrinqTitulo = tk.Label(self.BrinqEditFrame)
        self.BrinqTitulo.place(relx=0.302, rely=0.034, height=22, width=94)
        self.BrinqTitulo.configure(activebackground="#f9f9f9")
        self.BrinqTitulo.configure(activeforeground="black")
        self.BrinqTitulo.configure(anchor='w')
        self.BrinqTitulo.configure(background="#60F7DD")
        self.BrinqTitulo.configure(cursor="fleur")
        self.BrinqTitulo.configure(disabledforeground="#a3a3a3")
        self.BrinqTitulo.configure(font="-family {Small Fonts} -size 14")
        self.BrinqTitulo.configure(foreground="#5484d6")
        self.BrinqTitulo.configure(highlightbackground="#d9d9d9")
        self.BrinqTitulo.configure(highlightcolor="black")
        self.BrinqTitulo.configure(text='''Brinquedo''')

        self.NameLabel = tk.Label(self.BrinqEditFrame)
        self.NameLabel.place(x=10, y=50, height=22, width=64)
        self.NameLabel.configure(activebackground="#f9f9f9")
        self.NameLabel.configure(activeforeground="black")
        self.NameLabel.configure(anchor='w')
        self.NameLabel.configure(background="#60F7DD")
        self.NameLabel.configure(disabledforeground="#a3a3a3")
        self.NameLabel.configure(font="-family {Small Fonts} -size 14")
        self.NameLabel.configure(foreground="#5484d6")
        self.NameLabel.configure(highlightbackground="#d9d9d9")
        self.NameLabel.configure(highlightcolor="black")
        self.NameLabel.configure(text='''Nome:''')

        self.FelizLabel = tk.Label(self.BrinqEditFrame)
        self.FelizLabel.place(x=10, y=90, height=22, width=64)
        self.FelizLabel.configure(activebackground="#f9f9f9")
        self.FelizLabel.configure(activeforeground="black")
        self.FelizLabel.configure(anchor='w')
        self.FelizLabel.configure(background="#60F7DD")
        self.FelizLabel.configure(disabledforeground="#a3a3a3")
        self.FelizLabel.configure(font="-family {Small Fonts} -size 14")
        self.FelizLabel.configure(foreground="#5484d6")
        self.FelizLabel.configure(highlightbackground="#d9d9d9")
        self.FelizLabel.configure(highlightcolor="black")
        self.FelizLabel.configure(text='''Feliz:''')

        self.NameInput = tk.Entry(self.BrinqEditFrame)
        self.NameInput.place(x=80, y=50, height=20, width=164)
        self.NameInput.configure(background="white")
        self.NameInput.configure(disabledforeground="#a3a3a3")
        self.NameInput.configure(font="-family {Small Fonts} -size 8")
        self.NameInput.configure(foreground="#000000")
        self.NameInput.configure(highlightbackground="#d9d9d9")
        self.NameInput.configure(highlightcolor="black")
        self.NameInput.configure(insertbackground="black")
        self.NameInput.configure(readonlybackground="#f0f0f0f0f0f0")
        self.NameInput.configure(relief="flat")
        self.NameInput.configure(selectbackground="blue")
        self.NameInput.configure(selectforeground="white")

        self.FelizInput = tk.Entry(self.BrinqEditFrame)
        self.FelizInput.place(x=80, y=90, height=20, relwidth=0.242)
        self.FelizInput.configure(background="white")
        self.FelizInput.configure(disabledforeground="#a3a3a3")
        self.FelizInput.configure(font="-family {Small Fonts} -size 8")
        self.FelizInput.configure(foreground="#000000")
        self.FelizInput.configure(highlightbackground="#d9d9d9")
        self.FelizInput.configure(highlightcolor="black")
        self.FelizInput.configure(insertbackground="black")
        self.FelizInput.configure(readonlybackground="#f0f0f0f0f0f0")
        self.FelizInput.configure(relief="flat")
        self.FelizInput.configure(selectbackground="blue")
        self.FelizInput.configure(selectforeground="white")

        self.DuraLabel = tk.Label(self.BrinqEditFrame)
        self.DuraLabel.place(x=10, y=130, height=22, width=64)
        self.DuraLabel.configure(activebackground="#f9f9f9")
        self.DuraLabel.configure(activeforeground="black")
        self.DuraLabel.configure(anchor='w')
        self.DuraLabel.configure(background="#60F7DD")
        self.DuraLabel.configure(disabledforeground="#a3a3a3")
        self.DuraLabel.configure(font="-family {Small Fonts} -size 14")
        self.DuraLabel.configure(foreground="#5484d6")
        self.DuraLabel.configure(highlightbackground="#d9d9d9")
        self.DuraLabel.configure(highlightcolor="black")
        self.DuraLabel.configure(text='''Dura:''')

        self.DuraInput = tk.Entry(self.BrinqEditFrame)
        self.DuraInput.place(x=80, y=130, height=20, relwidth=0.242)
        self.DuraInput.configure(background="white")
        self.DuraInput.configure(disabledforeground="#a3a3a3")
        self.DuraInput.configure(font="-family {Small Fonts} -size 8")
        self.DuraInput.configure(foreground="#000000")
        self.DuraInput.configure(highlightbackground="#d9d9d9")
        self.DuraInput.configure(highlightcolor="black")
        self.DuraInput.configure(insertbackground="black")
        self.DuraInput.configure(readonlybackground="#f0f0f0f0f0f0")
        self.DuraInput.configure(relief="flat")
        self.DuraInput.configure(selectbackground="blue")
        self.DuraInput.configure(selectforeground="white")

        self.TipoLabel = tk.Label(self.BrinqEditFrame)
        self.TipoLabel.place(x=10, y=170, height=22, width=64)
        self.TipoLabel.configure(activebackground="#f9f9f9")
        self.TipoLabel.configure(activeforeground="black")
        self.TipoLabel.configure(anchor='w')
        self.TipoLabel.configure(background="#60F7DD")
        self.TipoLabel.configure(disabledforeground="#a3a3a3")
        self.TipoLabel.configure(font="-family {Small Fonts} -size 14")
        self.TipoLabel.configure(foreground="#5484d6")
        self.TipoLabel.configure(highlightbackground="#d9d9d9")
        self.TipoLabel.configure(highlightcolor="black")
        self.TipoLabel.configure(text='''Tipo:''')

        self.Tipo = ttk.Combobox(self.BrinqEditFrame)
        self.Tipo.place(x=80, y=170, height=21, width=143)
        self.Tipo.configure(font="-family {Small Fonts} -size 10")
        self.Tipo.configure(takefocus="")
        self.Tipo.configure(values=self.list_tipos)
        self.Tipo.configure(state='readonly')

        self.AddBrinq = tk.Button(self.frame)
        self.AddBrinq.place(relx=0.684, rely=0.825, height=54, width=177)
        self.AddBrinq.configure(activebackground="#68BCED")
        self.AddBrinq.configure(activeforeground="#60F7DD")
        self.AddBrinq.configure(background="#60F7DD")
        self.AddBrinq.configure(borderwidth="0")
        self.AddBrinq.configure(disabledforeground="#a3a3a3")
        self.AddBrinq.configure(font="-family {Small Fonts} -size 23 -weight bold")
        self.AddBrinq.configure(foreground="#5484d6")
        self.AddBrinq.configure(highlightbackground="#d9d9d9")
        self.AddBrinq.configure(highlightcolor="black")
        self.AddBrinq.configure(pady="0")
        self.AddBrinq.configure(relief="flat")
        self.AddBrinq.configure(text='''Adicionar!''')
        self.AddBrinq.configure(state='disabled')
        self.AddBrinq.configure(command=self.button_row_add)

        self.EditarBrinq = tk.Button(self.frame)
        self.EditarBrinq.place(relx=0.033, rely=0.825, height=54, width=177)
        self.EditarBrinq.configure(activebackground="#68BCED")
        self.EditarBrinq.configure(activeforeground="#60F7DD")
        self.EditarBrinq.configure(background="#60F7DD")
        self.EditarBrinq.configure(borderwidth="0")
        self.EditarBrinq.configure(disabledforeground="#a3a3a3")
        self.EditarBrinq.configure(font="-family {Small Fonts} -size 23 -weight bold")
        self.EditarBrinq.configure(foreground="#5484d6")
        self.EditarBrinq.configure(highlightbackground="#d9d9d9")
        self.EditarBrinq.configure(highlightcolor="black")
        self.EditarBrinq.configure(pady="0")
        self.EditarBrinq.configure(relief="flat")
        self.EditarBrinq.configure(state='disabled')
        self.EditarBrinq.configure(text='''Editar!''')
        self.EditarBrinq.configure(command=self.button_row_edit)

        self.DelBrinq = tk.Button(self.frame)
        self.DelBrinq.place(relx=0.367, rely=0.825, height=54, width=177)
        self.DelBrinq.configure(activebackground="#68BCED")
        self.DelBrinq.configure(activeforeground="#60F7DD")
        self.DelBrinq.configure(background="#60F7DD")
        self.DelBrinq.configure(borderwidth="0")
        self.DelBrinq.configure(disabledforeground="#a3a3a3")
        self.DelBrinq.configure(font="-family {Small Fonts} -size 23 -weight bold")
        self.DelBrinq.configure(foreground="#5484d6")
        self.DelBrinq.configure(highlightbackground="#d9d9d9")
        self.DelBrinq.configure(highlightcolor="black")
        self.DelBrinq.configure(pady="0")
        self.DelBrinq.configure(relief="flat")
        self.DelBrinq.configure(state='disabled')
        self.DelBrinq.configure(text='''Deletar''')
        self.DelBrinq.configure(command=self.button_row_del)

    def row_select(self, e):
        item = self.Table.item(self.Table.focus())['values']

        self.del_inputs()

        self.NameInput.insert(tk.INSERT, item[0])
        self.FelizInput.insert(tk.INSERT, item[1])
        self.DuraInput.insert(tk.INSERT, item[2])
        self.Tipo.current(self.list_tipos.index(item[3]))

        self.EditarBrinq['state'] = 'normal'
        self.DelBrinq['state'] = 'normal'

    def button_row_edit(self):
        item = self.Table.selection()[0]

        new_values = [self.NameInput.get(), self.FelizInput.get(), self.DuraInput.get(), self.Tipo.get()]
        self.Table.item(item, text='', values=new_values)

    def button_row_del(self):
        item = self.Table.selection()[0]

        self.Table.delete(item)
        self.del_inputs()

        self.EditarBrinq['state'] = 'disable'
        self.DelBrinq['state'] = 'disable'

    def button_row_add(self):
        values = [self.NameInput.get(), self.FelizInput.get(), self.DuraInput.get(), self.Tipo.get()]

        podeadd = True
        for i in values:
            if i == '':
                podeadd = False

        if podeadd:
            self.Table.insert('', tk.END, values=values)
        else:
            messagebox.showerror('Erro!!', 'Ops, você deixou algum campo vazio.')

    @staticmethod
    def tipo_brinq(brinq):
        return str(type(brinq)).replace("'", '').replace('>', '').split('.')[-1]

    def del_inputs(self):
        self.NameInput.delete(0, tk.END)
        self.FelizInput.delete(0, tk.END)
        self.DuraInput.delete(0, tk.END)