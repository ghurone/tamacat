import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class AbaGeladeira:

    def __init__(self, app):
        self.frame = tk.Frame(app.window, background="#68BCED")

        self.ComidaFrame = tk.Frame(self.frame)
        self.ComidaFrame.place(relx=0.033, rely=0.05, relheight=0.738, relwidth=0.476)
        self.ComidaFrame.configure(background="#60F7DD")
        self.ComidaFrame.configure(highlightbackground="#d9d9d9")
        self.ComidaFrame.configure(highlightcolor="black")

        self.Table = ttk.Treeview(self.ComidaFrame, show='headings')
        self.Table.configure(column=('c1', 'c2', 'c3', 'c4', 'c5'), select='browse')

        self.Table.column('#1', anchor=tk.CENTER, width=50)
        self.Table.heading('#1', text='Quant')
        self.Table.column('#2', anchor=tk.CENTER, width=130)
        self.Table.heading('#2', text='Nome')
        self.Table.column('#3', anchor=tk.CENTER, width=50)
        self.Table.heading('#3', text='Saciar')
        self.Table.column('#4', anchor=tk.CENTER, width=50)
        self.Table.heading('#4', text='Saúde')
        self.Table.column('#5', anchor=tk.CENTER, width=50)
        self.Table.heading('#5', text='Feliz')

        self.Table.bind('<<TreeviewSelect>>', self.row_select)

        self.ScrollY = tk.Scrollbar(self.ComidaFrame)
        self.ScrollY.pack(side=tk.RIGHT, fill=tk.Y)
        self.ScrollY.configure(command=self.Table.yview)
        self.Table.configure(yscrollcommand=self.ScrollY.set)

        self.ScrollX = tk.Scrollbar(self.ComidaFrame, orient='horizontal')
        self.ScrollX.pack(side=tk.BOTTOM, fill=tk.X)
        self.ScrollX.configure(command=self.Table.xview)
        self.Table.configure(xscrollcommand=self.ScrollX.set)

        self.Table.pack(expand=True, side=tk.LEFT, fill=tk.BOTH)

        self.ComidaEditFrame = tk.Frame(self.frame)
        self.ComidaEditFrame.place(relx=0.534, rely=0.05, relheight=0.738, relwidth=0.442)
        self.ComidaEditFrame.configure(background="#60F7DD")
        self.ComidaEditFrame.configure(highlightbackground="#d9d9d9")
        self.ComidaEditFrame.configure(highlightcolor="black")

        self.ComidaTitulo = tk.Label(self.ComidaEditFrame)
        self.ComidaTitulo.place(x=90, y=10, height=22, width=74)
        self.ComidaTitulo.configure(activebackground="#f9f9f9")
        self.ComidaTitulo.configure(activeforeground="black")
        self.ComidaTitulo.configure(anchor='w')
        self.ComidaTitulo.configure(background="#60F7DD")
        self.ComidaTitulo.configure(disabledforeground="#a3a3a3")
        self.ComidaTitulo.configure(font="-family {Small Fonts} -size 14")
        self.ComidaTitulo.configure(foreground="#5484d6")
        self.ComidaTitulo.configure(highlightbackground="#d9d9d9")
        self.ComidaTitulo.configure(highlightcolor="black")
        self.ComidaTitulo.configure(text='''Comida''')

        self.NameLabel = tk.Label(self.ComidaEditFrame)
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

        self.SaciarLabel = tk.Label(self.ComidaEditFrame)
        self.SaciarLabel.place(x=10, y=90, height=22, width=64)
        self.SaciarLabel.configure(activebackground="#f9f9f9")
        self.SaciarLabel.configure(activeforeground="black")
        self.SaciarLabel.configure(anchor='w')
        self.SaciarLabel.configure(background="#60F7DD")
        self.SaciarLabel.configure(disabledforeground="#a3a3a3")
        self.SaciarLabel.configure(font="-family {Small Fonts} -size 14")
        self.SaciarLabel.configure(foreground="#5484d6")
        self.SaciarLabel.configure(highlightbackground="#d9d9d9")
        self.SaciarLabel.configure(highlightcolor="black")
        self.SaciarLabel.configure(text='''Saciar:''')

        self.SaudeLabel = tk.Label(self.ComidaEditFrame)
        self.SaudeLabel.place(x=10, y=130, height=22, width=64)
        self.SaudeLabel.configure(activebackground="#f9f9f9")
        self.SaudeLabel.configure(activeforeground="black")
        self.SaudeLabel.configure(anchor='w')
        self.SaudeLabel.configure(background="#60F7DD")
        self.SaudeLabel.configure(disabledforeground="#a3a3a3")
        self.SaudeLabel.configure(font="-family {Small Fonts} -size 14")
        self.SaudeLabel.configure(foreground="#5484d6")
        self.SaudeLabel.configure(highlightbackground="#d9d9d9")
        self.SaudeLabel.configure(highlightcolor="black")
        self.SaudeLabel.configure(text='''Saúde:''')

        self.FelizLabel = tk.Label(self.ComidaEditFrame)
        self.FelizLabel.place(x=10, y=170, height=22, width=64)
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

        self.NameInput = tk.Entry(self.ComidaEditFrame)
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

        self.SaciarInput = tk.Entry(self.ComidaEditFrame)
        self.SaciarInput.place(x=80, y=90, height=20, width=64)
        self.SaciarInput.configure(background="white")
        self.SaciarInput.configure(disabledforeground="#a3a3a3")
        self.SaciarInput.configure(font="-family {Small Fonts} -size 8")
        self.SaciarInput.configure(foreground="#000000")
        self.SaciarInput.configure(highlightbackground="#d9d9d9")
        self.SaciarInput.configure(highlightcolor="black")
        self.SaciarInput.configure(insertbackground="black")
        self.SaciarInput.configure(readonlybackground="#f0f0f0f0f0f0")
        self.SaciarInput.configure(relief="flat")
        self.SaciarInput.configure(selectbackground="blue")
        self.SaciarInput.configure(selectforeground="white")

        self.SaudeInput = tk.Entry(self.ComidaEditFrame)
        self.SaudeInput.place(x=80, y=130, height=20, width=64)
        self.SaudeInput.configure(background="white")
        self.SaudeInput.configure(disabledforeground="#a3a3a3")
        self.SaudeInput.configure(font="-family {Small Fonts} -size 8")
        self.SaudeInput.configure(foreground="#000000")
        self.SaudeInput.configure(highlightbackground="#d9d9d9")
        self.SaudeInput.configure(highlightcolor="black")
        self.SaudeInput.configure(insertbackground="black")
        self.SaudeInput.configure(readonlybackground="#f0f0f0f0f0f0")
        self.SaudeInput.configure(relief="flat")
        self.SaudeInput.configure(selectbackground="blue")
        self.SaudeInput.configure(selectforeground="white")

        self.FelizInput = tk.Entry(self.ComidaEditFrame)
        self.FelizInput.place(x=80, y=170, height=20, width=64)
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

        self.QuantLabel = tk.Label(self.ComidaEditFrame)
        self.QuantLabel.place(x=10, y=210, height=22, width=64)
        self.QuantLabel.configure(activebackground="#f9f9f9")
        self.QuantLabel.configure(activeforeground="black")
        self.QuantLabel.configure(anchor='w')
        self.QuantLabel.configure(background="#60F7DD")
        self.QuantLabel.configure(disabledforeground="#a3a3a3")
        self.QuantLabel.configure(font="-family {Small Fonts} -size 14")
        self.QuantLabel.configure(foreground="#5484d6")
        self.QuantLabel.configure(highlightbackground="#d9d9d9")
        self.QuantLabel.configure(highlightcolor="black")
        self.QuantLabel.configure(text='''Quant:''')

        self.QuantInput = tk.Entry(self.ComidaEditFrame)
        self.QuantInput.place(x=80, y=210, height=20, width=64)
        self.QuantInput.configure(background="white")
        self.QuantInput.configure(disabledforeground="#a3a3a3")
        self.QuantInput.configure(font="-family {Small Fonts} -size 8")
        self.QuantInput.configure(foreground="#000000")
        self.QuantInput.configure(highlightbackground="#d9d9d9")
        self.QuantInput.configure(highlightcolor="black")
        self.QuantInput.configure(insertbackground="black")
        self.QuantInput.configure(readonlybackground="#f0f0f0f0f0f0")
        self.QuantInput.configure(relief="flat")
        self.QuantInput.configure(selectbackground="blue")
        self.QuantInput.configure(selectforeground="white")

        self.AddComida = tk.Button(self.frame)
        self.AddComida.place(relx=0.684, rely=0.825, height=54, width=177)
        self.AddComida.configure(activebackground="#68BCED")
        self.AddComida.configure(activeforeground="#60F7DD")
        self.AddComida.configure(background="#60F7DD")
        self.AddComida.configure(borderwidth="0")
        self.AddComida.configure(disabledforeground="#a3a3a3")
        self.AddComida.configure(font="-family {Small Fonts} -size 23 -weight bold")
        self.AddComida.configure(foreground="#5484d6")
        self.AddComida.configure(highlightbackground="#d9d9d9")
        self.AddComida.configure(highlightcolor="black")
        self.AddComida.configure(pady="0")
        self.AddComida.configure(relief="flat")
        self.AddComida.configure(state='disabled')
        self.AddComida.configure(text='''Adicionar!''')
        self.AddComida.configure(command=self.button_row_add)

        self.EditarComida = tk.Button(self.frame)
        self.EditarComida.place(relx=0.033, rely=0.825, height=54, width=177)
        self.EditarComida.configure(activebackground="#68BCED")
        self.EditarComida.configure(activeforeground="#60F7DD")
        self.EditarComida.configure(background="#60F7DD")
        self.EditarComida.configure(borderwidth="0")
        self.EditarComida.configure(disabledforeground="#a3a3a3")
        self.EditarComida.configure(font="-family {Small Fonts} -size 23 -weight bold")
        self.EditarComida.configure(foreground="#5484d6")
        self.EditarComida.configure(highlightbackground="#d9d9d9")
        self.EditarComida.configure(highlightcolor="black")
        self.EditarComida.configure(pady="0")
        self.EditarComida.configure(relief="flat")
        self.EditarComida.configure(state='disabled')
        self.EditarComida.configure(text='''Editar!''')
        self.EditarComida.configure(command=self.button_row_edit)

        self.DelComida = tk.Button(self.frame)
        self.DelComida.place(relx=0.367, rely=0.825, height=54, width=177)
        self.DelComida.configure(activebackground="#68BCED")
        self.DelComida.configure(activeforeground="#60F7DD")
        self.DelComida.configure(background="#60F7DD")
        self.DelComida.configure(borderwidth="0")
        self.DelComida.configure(disabledforeground="#a3a3a3")
        self.DelComida.configure(font="-family {Small Fonts} -size 23 -weight bold")
        self.DelComida.configure(foreground="#5484d6")
        self.DelComida.configure(highlightbackground="#d9d9d9")
        self.DelComida.configure(highlightcolor="black")
        self.DelComida.configure(pady="0")
        self.DelComida.configure(relief="flat")
        self.DelComida.configure(state='disabled')
        self.DelComida.configure(text='''Deletar''')
        self.DelComida.configure(command=self.button_row_del)

    def row_select(self, e):
        item = self.Table.item(self.Table.focus())['values']

        # Deletando as coisas

        self.del_inputs()

        # Inserindo as coisas

        self.NameInput.insert(tk.INSERT, item[1])
        self.SaciarInput.insert(tk.INSERT, item[2])
        self.SaudeInput.insert(tk.INSERT, item[3])
        self.FelizInput.insert(tk.INSERT, item[4])
        self.QuantInput.insert(tk.INSERT, item[0])

        self.EditarComida['state'] = 'normal'
        self.DelComida['state'] = 'normal'

    def button_row_edit(self):
        item = self.Table.selection()[0]

        new_values = [self.QuantInput.get(), self.NameInput.get(), self.SaciarInput.get(), self.SaudeInput.get(),
                      self.FelizInput.get()]

        deboa = True
        for i in new_values:
            if i == '':
                deboa = False

        if deboa:
            self.Table.item(item, text='', values=new_values)
        else:
            messagebox.showerror('Erro!!', 'Ops, você deixou algum campo vazio.')

    def button_row_del(self):
        item = self.Table.selection()[0]

        self.Table.delete(item)

        self.del_inputs()

        self.EditarComida['state'] = 'disable'
        self.DelComida['state'] = 'disable'

    def button_row_add(self):
        values = [self.QuantInput.get(), self.NameInput.get(), self.SaciarInput.get(), self.SaudeInput.get(),
                  self.FelizInput.get()]

        podeadd = True
        for i in values:
            if i == '':
                podeadd = False

        if podeadd:
            self.Table.insert('', tk.END, values=values)
        else:
            messagebox.showerror('Erro!!', 'Ops, você deixou algum campo vazio.')

    def del_inputs(self):
        self.NameInput.delete(0, tk.END)
        self.SaciarInput.delete(0, tk.END)
        self.SaudeInput.delete(0, tk.END)
        self.FelizInput.delete(0, tk.END)
        self.QuantInput.delete(0, tk.END)