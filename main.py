from tkinter import Entry, Label, Frame, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END
from conexion import *


class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column =0, row =0)
        self.frame2 = Frame(master, bg='gray22')
        self.frame2.grid(column =0, row =1)
        self.frame3 = Frame(master)
        self.frame3.grid(rowspan=2, column =1, row =1)

        self.frame4 = Frame(master, bg='black')
        self.frame4.grid(column =0, row =2)

        self.codigo = StringVar()
        self.articulo = StringVar()
        self.cantidad = StringVar()
        self.importe = StringVar()
        self.saldo = StringVar()
        self.cant_hoy = StringVar()
        self.cant_ant = StringVar()
        self.import_ant = StringVar()
        self.faltante = StringVar()
        self.fisico = StringVar()
        self.buscar = StringVar()

        #self.naodatabase = Registro_datos()
        self.create_wietgs()

    def create_wietgs(self):
        Label(self.frame1, text = "I N V E N T A R I O   \t     N A O",bg='gray22', fg='white', font=('ERAS DEMI ITC',15,'bold')).grid(column=0, row=0)

        Label(self.frame2, text = 'AGREGAR NUEVOS DATOS', fg='white', bg='gray22', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0, row=0, pady=5)
        Label(self.frame2, text = 'Codigo', fg='white', bg='gray22', font=('Rockwell',10,'bold')).grid(column=0,row=1,pady=15)
        Label(self.frame2, text = 'Articulo', fg='white', bg='gray22', font=('Rockwell',10,'bold')).grid(column=0,row=2,pady=15)
        Label(self.frame2, text = 'Cantidad', fg='white', bg='gray22', font=('Rockwell',10,'bold')).grid(column=0,row=3,pady=15)
        Label(self.frame2, text = 'Importe', fg='white', bg='gray22', font=('Rockwell',10,'bold')).grid(column=0,row=4,pady=15)
        Label(self.frame2, text = 'Saldo', fg='white', bg='gray22', font=('Rockwell',10,'bold')).grid(column=0,row=5,pady=15)
        Label(self.frame2, text = 'Cant. Hoy', fg='white', bg='gray22', font=('Rockwell',10,'bold')).grid(column=0,row=6,pady=15)
        Label(self.frame2, text = 'Cant. Ant', fg='white', bg='gray22', font=('Rockwell',10,'bold')).grid(column=0,row=7,pady=15)
        Label(self.frame2, text = 'Import. Ant', fg='white', bg='gray22', font=('Rockwell',10,'bold')).grid(column=0,row=8,pady=15)
        Label(self.frame2, text = 'Faltante', fg='white', bg='gray22', font=('Rockwell',10,'bold')).grid(column=0,row=9,pady=15)
        Label(self.frame2, text = 'Fisico', fg='white', bg='gray22', font=('Rockwell',10,'bold')).grid(column=0,row=10,pady=15)   
        
        Entry(self.frame2, textvariable= self.codigo, font=('Arial',12)).grid(column=1, row=1, padx=5)
        Entry(self.frame2, textvariable= self.articulo, font=('Arial',12)).grid(column=1, row=2)
        Entry(self.frame2, textvariable= self.cantidad, font=('Arial',12)).grid(column=1, row=3)
        Entry(self.frame2, textvariable= self.importe, font=('Arial',12)).grid(column=1, row=4)
        Entry(self.frame2, textvariable= self.saldo, font=('Arial',12)).grid(column=1, row=5)
        Entry(self.frame2, textvariable= self.cant_hoy, font=('Arial',12)).grid(column=1, row=6)
        Entry(self.frame2, textvariable= self.cant_ant, font=('Arial',12)).grid(column=1, row=7)
        Entry(self.frame2, textvariable= self.import_ant, font=('Arial',12)).grid(column=1, row=8)
        Entry(self.frame2, textvariable= self.faltante, font=('Arial',12)).grid(column=1, row=9)
        Entry(self.frame2, textvariable= self.fisico, font=('Arial',12)).grid(column=1, row=10)


        Label(self.frame4,text='Control', fg='white', bg='black', font=('ERAS DEMI ITC',12,'bold')).grid(columnspan=3, column=0, row=0, pady=1, padx=4)
        Button(self.frame4,command= self.agregar_datos, text='REGISTRAR',font=('Arial',10,'bold'), bg='magenta2').grid(column=0, row=1, padx=4,pady=10)
        Button(self.frame4,command= self.limpiar_datos, text='LIMPIAR',font=('Arial',10,'bold'), bg='orange red').grid(column=1, row=1, padx=10)
        Button(self.frame4,command= self.eliminar_fila,text='ELIMINAR',font=('Arial',10,'bold'), bg='yellow').grid(column=2, row=1, padx=4)
        Button(self.frame4,command= self.buscar_nombre, text='BUSCAR POR NOMBRE',font=('Arial',8,'bold'), bg='orange').grid(columnspan=2, column=1, row=2, padx=4,pady=10)
        Entry(self.frame4, textvariable= self.buscar, font=('Arial',12),width=10).grid(column=0, row=2,padx=8, pady=1)
        Button(self.frame4,command= self.mostrar_todo, text='MOSTRAR DATOS DE MYSQL', font=('Arial',10,'bold'), bg='green').grid(columnspan=3, column=0, row=3, padx=4,pady=5)


        self.tabla = ttk.Treeview(self.frame3, height=33)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient=HORIZONTAL, command = self.tabla.xview)
        ladox.grid(column=0, row=1, sticky="ew")
        ladoy = Scrollbar(self.frame3, orient=VERTICAL, command = self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky="ns")

        self.tabla.configure(xscrollcommand= ladox.set, yscrollcommand= ladoy.set)
        self.tabla['columns'] = ('ARTICULO', 'CANTIDAD', 'IMPORTE', 'SALDO', 'CANT_HOY', 'CANT_ANT', 'IMPORT_ANT', 'FALTANTE', 'FISICO')

        self.tabla.column('#0', minwidth=80, width=100, anchor='center')
        self.tabla.column('ARTICULO', minwidth=100, width=170, anchor='center')
        self.tabla.column('CANTIDAD', minwidth=80, width=100, anchor='center')
        self.tabla.column('IMPORTE', minwidth=80, width=100, anchor='center')
        self.tabla.column('SALDO', minwidth=80, width=100, anchor='center')
        self.tabla.column('CANT_HOY', minwidth=80, width=100, anchor='center')
        self.tabla.column('CANT_ANT', minwidth=80, width=100, anchor='center')
        self.tabla.column('IMPORT_ANT', minwidth=80, width=100, anchor='center')
        self.tabla.column('FALTANTE', minwidth=80, width=100, anchor='center')
        self.tabla.column('FISICO', minwidth=80, width=100, anchor='center')

        self.tabla.heading('#0', text='CODIGO', anchor= 'center')
        self.tabla.heading('ARTICULO', text='ARTICULO', anchor= 'center')
        self.tabla.heading('CANTIDAD', text='CANTIDAD', anchor= 'center')
        self.tabla.heading('IMPORTE', text='IMPORTE', anchor= 'center')
        self.tabla.heading('SALDO', text='SALDO', anchor= 'center')
        self.tabla.heading('CANT_HOY', text='CANT_HOY', anchor= 'center')
        self.tabla.heading('CANT_ANT', text='CANT_ANT', anchor= 'center')
        self.tabla.heading('IMPORT_ANT', text='IMPORT_ANT', anchor= 'center')
        self.tabla.heading('FALTANTE', text='FALTANTE', anchor= 'center')
        self.tabla.heading('FISICO', text='FISICO', anchor= 'center')


        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt')
        estilo.configure(".", font=('Helvetica',12,'bold'), foreground='red2')
        estilo.configure("Treeview", font=('Helvetica',10,'bold'), foreground='black', background= 'white')
        estilo.map('Treeview', background= [('selected', 'violet' )], foreground= [('selected', 'white')] )

        self.tabla.bind ("<<TreeviewSelect>>", self.obtener_fila)      # Seleccionar Fila
   
    
    def agregar_datos(self):
        self.tabla.get_children()
        codigo = self.codigo.get()
        articulo = self.articulo.get()
        cantidad = self.cantidad.get()
        importe = self.importe.get()
        saldo = self.saldo.get()
        cant_hoy = self.cant_hoy.get()
        cant_ant = self.cant_ant.get()
        import_ant = self.import_ant.get()
        faltante = self.faltante.get()
        fisico = self.fisico.get()
        datos = (articulo, cantidad, importe, saldo, cant_hoy, cant_ant, import_ant, faltante, fisico)
        if codigo and articulo and cantidad and importe and saldo and cant_hoy and cant_ant and import_ant and faltante and fisico != '':
            self.tabla.insert('', 0, text= codigo, values=datos)
            self.naodatabase.inserta_producto(codigo, articulo, cantidad, importe, saldo, cant_hoy, cant_ant, import_ant, faltante, fisico)
        
        
    def limpiar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        self.codigo.set('')
        self.articulo.set('')
        self.cantidad.set('')
        self.importe.set('')
        self.saldo.set('')
        self.cant_hoy.set('')
        self.cant_ant.set('')
        self.import_ant.set('')
        self.faltante.set('')
        self.fisico.set('')

    def buscar_nombre(self):
        nombre_producto = self.buscar.get()
        nombre_producto = str("'" + nombre_producto + "'")
        nombre_buscado = self.naodatabase.busca_producto(nombre_producto)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in nombre_buscado:
            i =i+1
            self.tabla.insert('', i, text=nombre_buscado[i][1:2], values=nombre_buscado[i][2:11])

    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.naodatabase.mostrar_productos()
        i= -1
        for dato in registro:
            i=i+1
            self.tabla.insert('',i, text= registro[i][1:2], values=registro[i][2:11])

    def eliminar_fila(self):
        fila = self.tabla.selection()
        if len(fila) != 0:
            self.tabla.delete(fila)
            nombre = ("'"+ str(self.nombre_borrar) + "'")
            self.naodatabase.elimina_producto(nombre)

    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borrar = data['values'][0]
             

def main():
    ventana = Tk()
    ventana.title("Inventario Nao")
    ventana.config(background="gray22")
    ventana.geometry("900x500")
    #ventana.resizable(0,0)
    app = Registro(ventana) 
    app.mainloop()

if __name__=="__main__":
    main() 
