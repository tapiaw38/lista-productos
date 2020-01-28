from tkinter import *
from tkinter import ttk
import sqlite3

class Product:
    db_name='database.db'

    def __init__(self, window):
        self.root=window
        self.root.title('Products Application')
         #creating frame
        frame=LabelFrame(self.root, text='Registra un nuevo producto')
        frame.grid(row=0,column=0, columnspan=3,pady=20)
        #input
        Label(frame,text='Nombre: ').grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1,column=3)
        #--
        Label(frame,text='Precio: ').grid(row=2, column=0)
        self.price = Entry(frame)
        self.price.grid(row=2,column=3)
        #button
        ttk.Button(frame,text='Guardar Producto').grid(row=3,columnspan=2,sticky= W + E)
        #table
        self.tree=ttk.Treeview(height=10,columns=2)
        self.tree.grid(row=4,column=0, columnspan=2)
        self.tree.heading('#0', text='Nombre',anchor=CENTER)
        self.tree.heading('#1', text='Precio',anchor=CENTER)

        self.get_products()

    #iniciar consulta
    def run_query(self,query,parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor =conn.cursor()
            result=cursor.execute(query,parameters)
            conn.commit()
        return result
    #consulta trae datos de productos
    def get_products(self):
        #obtener todos los datos de la tabla para limpiarlos
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query='SELECT * FROM productos ORDER BY nombre DESC'
        db_rows=self.run_query(query)
        for row in db_rows:
            self.tree.insert('',0,text=row[1],values=row[2])
    def validation(self):
        return len(self.name.get()) != 0 and len(self.price.get()) != 0
    def add_product(self):
        if self.validation():
            pass
        else:
            pass


if __name__=='__main__':
    window=Tk()
    application = Product(window)
    if __name__ == '__main__':
        window.mainloop()
