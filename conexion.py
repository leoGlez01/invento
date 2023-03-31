import mysql.connector

class Registro_datos():

    # def __init__(self):    
    #     self.conexion = mysql.connector.connect(user = 'root', password =  '123456789',
    #                                         host='localHost',
    #                                         database = 'naodatabase',
    #                                         port = '3306')
                                            

    def inserta_producto(self, codigo, articulo, cantidad, importe, saldo, cant_hoy, cant_ant, import_ant, faltante, fisico):
        cur = self.conexion.cursor()
        sql = ''' INSERT INTO inventario (CODIGO, ARTICULO, CANTIDAD, IMPORTE, SALDO, CANT_HOY, CANT_ANT, IMPORT_ANT, FALTANTE, FISICO)
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(codigo, articulo, cantidad, importe, saldo, cant_hoy, cant_ant, import_ant, faltante, fisico)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM inventario"
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_articulo):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM inventario WHERE ARTICULO = {}", format(nombre_articulo)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def elimina_producto(self,nombre):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM inventario WHERE ARTICULO = {}''',format(nombre)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()
        

        