class Producto_comprado:
    def __init__(self, codigo_compra, codigo_producto, nombre, descripcion, precio_unitario):
        self.codigo_producto = codigo_producto
        self.nombre = nombre
        self.descipcion = descripcion
        self.precio_unitario = precio_unitario
        self.codigo_compra = codigo_compra
        self.siguiente = None

    def imprimir(self):
        print(f'\t{self.nombre}, {self.codigo_producto}, {self.descipcion}, {self.precio_unitario}, {self.codigo_compra}')
        

class Cliente_comprado:
    def __init__(self, codigo_compra, nit, nombre, correo):
        self.nombre = nombre
        self.nit = nit
        self.correo = correo
        self.codigo_compra = codigo_compra
        self.siguiente = None

    def imprimir(self):
        
        print('----------------------------------------------')
        print('CLIENTE')
        print(f'\tNombre:\t{self.nombre}\n\tNit:\t{self.nit}\n\tCorreo:\t{self.correo}\n\tCompra:\t{self.codigo_compra}')
        print('PRODUCTOS')
        

class Lista_compras:
    def __init__(self):
        self.primer_nodo = None
        
    def insertar_cliente(self, codigo_compra, nit, nombre, correo):
        nuevo_nodo = Cliente_comprado(codigo_compra, nit, nombre, correo)
        nuevo_nodo.siguiente = self.primer_nodo
        self.primer_nodo = nuevo_nodo

    def insertar_producto(self,codigo_compra, codigo_producto, nombre, descripcion, precio_unitario):
        nuevo_nodo = Producto_comprado(codigo_compra, codigo_producto, nombre, descripcion, precio_unitario)
        nuevo_nodo.siguiente = self.primer_nodo
        self.primer_nodo = nuevo_nodo

    def buscar(self, codigo_producto):
        actual = self.primer_nodo
        while actual is not None:
            if actual.codigo_producto == codigo_producto:
                return actual
            actual = actual.siguiente
        return None
    
    def editar(self, codigo_producto,nombre, descripcion, precio_unitario):
        nodo = self.buscar(codigo_producto)
        if nodo:
            nodo.precio_unitario = precio_unitario
            nodo.nombre = nombre
            nodo.descipcion = descripcion
            return True
        return False
    
    def eliminar_producto(self, codigo_producto):
        actual = self.primer_nodo
        anterior = None
        while actual:
            if actual.codigo_producto == codigo_producto:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.primer_nodo = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def mostrar(self):
        actual = self.primer_nodo
        while actual:
            actual.imprimir()
            actual = actual.siguiente



