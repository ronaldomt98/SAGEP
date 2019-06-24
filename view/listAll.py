from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
from controller.Controller import *

'tamaño de ventanas'
tamano = "600x325+430+150"
tamano2 = "520x370+470+151"
'clor de las ventanas'
color = 'White'


class ListAll:

    def __init__(self, ventana):
        self.ventana = ventana
        self.run(self.ventana)

    def run(self, ventana):
        self.venLista = Toplevel(ventana)
        self.venLista.config(bg=color)
        self.venLista.resizable(0, 0)
        self.venLista.geometry(tamano)
        self.venLista.title("LISTADO DE CLIENTES")
        self.venLista.grab_set()

        self.ComicSansMS = font.Font(family="Comic Sans MS", size=11, weight="bold")
        self.DejaVuSansMono = font.Font(family="DejaVu Sans Mono", size=15, weight="bold")

        Label(self.venLista, text="CLIENTES", bg='White', font=self.ComicSansMS).pack()

        # Crear una barra de deslizamiento con orientación vertical.
        scrollbarVertical = ttk.Scrollbar(self.venLista, orient=VERTICAL)
        scrollbarHorizontal = ttk.Scrollbar(self.venLista, orient=HORIZONTAL)

        # Vincularla con la lista.
        self.listbox = Listbox(self.venLista, yscrollcommand=scrollbarVertical.set,
                               xscrollcommand=scrollbarHorizontal.set,
                               borderwidth=8, activestyle=None, bg='black', fg='gray', selectbackground='Red',
                               selectborderwidth=2, font=self.ComicSansMS, selectmode=EXTENDED)
        scrollbarVertical.config(command=self.listbox.yview)
        scrollbarHorizontal.config(command=self.listbox.xview)
        # Ubicarla a la derecha.
        scrollbarVertical.pack(side=RIGHT, fill=Y, expand=False)
        scrollbarHorizontal.pack(side=BOTTOM, fill=X, expand=False)
        self.listbox.pack(fill='both', expand='yes')

        listClient = Controller.listar_clientes()

        for i in listClient:
            self.listbox.insert(END, i)

        self.venLista.mainloop()