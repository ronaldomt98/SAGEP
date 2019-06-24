from controller.Controller import *
from models.Cliente import Cliente

from tkinter import *
from tkinter import font
from tkinter import messagebox
import tkinter.ttk as ttk

tamano = '600x400+480+195'


class agregar_venta():

    def __init__(self, ventana):
        self.ventana = ventana
        self.iniciar(self.ventana)

    def iniciar(self, ventana):

        'Tipo de fuente de la letra'
        self.ComicSansMS = font.Font(family="Comic Sans MS", size=13, weight="bold")

        self.ven_mue = Toplevel(ventana)
        self.ven_mue.config(bg="white")
        self.ven_mue.resizable(0, 0)
        self.ven_mue.geometry(tamano)
        self.ven_mue.title("AGREGAR VENTA")
        self.ven_mue.grab_set()

        '''intancia las notebook(pestañas)'''
        self.pestana = ttk.Notebook(self.ven_pedi)
        self.pestana.pack(fill='both', expand='yes')

        '''se istancias los frames que va contener los labeles, etc'''
        self.frmcli = frame(self.pestana, bg='white', highlightthickness=2, highlightbackground='black')
        self.frmbien = frame(self.pestana, bg='white', highlightthickness=2, highlightbackground='black')

        '''se agrega los frames a las pestañas'''
        self.pestana.add(self.frmbien, text='Muebles')

        Label(self.frmcli, text="Cedula:", bg='White', fg='red', font=self.ComicSansMS).place(x=60, y=25)
        self.cedula = Entry(self.frmcli)
        self.cedula.focus()
        self.cedula.place(x=160, y=30)

        ''''''
        self.MVBoli = font.Font(family="MV Boli", size=9, weight="bold")

        Label(self.frmbien, text="MUEBLES", bg='White', fg='red', font=self.ComicSansMS).place(x=250, y=0)

        Label(self.frmbien, text="CANT. ARMARIO", bg='White', fg='black', font=self.MVBoli).place(x=125, y=24)
        self.grande = Entry(self.frmbien)
        self.grande.place(x=330, y=26)
        Label(self.frmbien, text="CANT. CAMA:", bg='White', fg='black', font=self.MVBoli).place(x=125, y=75)
        self.pequena = Entry(self.frmbien)
        self.pequena.place(x=330, y=77)
        Label(self.frmbien, text="CANT. COMODA", bg='White', fg='blue', font=self.MVBoli).place(x=125, y=101)
        self.rectangulo = Entry(self.frmbien)
        self.rectangulo.place(x=330, y=103)
        Label(self.frmbien, text="CANT. ESCRITORIO:", bg='White', fg='blue', font=self.MVBoli).place(x=125, y=148)
        self.redonda = Entry(self.frmbien)
        self.redonda.place(x=330, y=150)
        Label(self.frmbien, text="CANT. ESTANTERIA:", bg='White', fg='blue', font=self.MVBoli).place(x=125, y=122)
        self.shabbychic = Entry(self.frmbien)
        self.shabbychic.place(x=330, y=126)
        Label(self.frmbien, text="CANT. MESA:", bg='White', fg='green', font=self.MVBoli).place(x=125, y=172)
        self.vaso = Entry(self.frmbien)
        self.vaso.place(x=330, y=174)
        Label(self.frmbien, text="CANT. SILLA:", bg='White', fg='green', font=self.MVBoli).place(x=125, y=198)
        self.plato = Entry(self.frmbien)
        self.plato.place(x=330, y=200)
        Label(self.frmbien, text="CANT. TABURETE:", bg='White', fg='green', font=self.MVBoli).place(x=125, y=224)
        self.partc = Entry(self.frmbien)
        self.partc.place(x=330, y=226)
        Label(self.frmbien, text="CANT. VITRINA:", bg='White', fg='orange', font=self.MVBoli).place(x=125, y=250)
        self.cubre = Entry(self.frmbien)
        self.cubre.place(x=330, y=252)

        self.btonAgregar = Button(self.ven_pedi, text="Reservar", command=self.addCliente)
        self.btonAgregar.place(x=430, y=365)

        Button(self.ven_pedi, text="Cancelar", command=self.ven_pedi.destroy).place(x=510, y=365)

        self.ven_pedi.mainloop()

    def obtener_cliente(self):
        ci = self.cedula.get()
        cliente = Controller.buscar_por_cedula(ci)

    def add_venta(self):
        can_grande = self.grande.get()
        can_pequena = self.pequena.get()
        can_tiffany = self.tiffany.get()
        can_rectangulo = self.rectangulo.get()
        can_redonda = self.redonda.get()
        can_shabbychic = self.shabbychic.get()
        can_vaso = self.vaso.get()
        can_plato = self.plato.get()
        can_partc = self.partc.get()
        can_cubre = self.cubre.get()
        can_diolen = self.diolen.get()
        can_brocato = self.brocato.get()

        self.pedido = {'Silla Grande': int(can_grande), 'Silla Pequena': int(can_pequena),
                       'Silla Tiffany': int(can_tiffany), 'Mesa Rectangulo': int(can_rectangulo),
                       'Mesa Redonda': int(can_redonda), 'Mesa Shabby Chic': int(can_shabbychic),
                       'Cubre': int(can_cubre), 'Diolen': int(can_diolen), 'Brocato': int(can_brocato),
                       'Vaso': int(can_vaso), 'Plato': int(can_plato), 'ParTC': int(can_partc)}
        return self.pedido

#    def factura(self, cliente):
 #       messagebox.showinfo('Factura', Factura.calcular(cliente))