class Producto:
    def __init__(self, id, codigo_producto, nombre, descripcion, precio_unitario):
        self.id = id
        self.codigo_producto = codigo_producto
        self.nombre = nombre
        self.descipcion = descripcion
        self.precio_unitario = precio_unitario

    def mostrar(self):
        print(f'codigo producto: {self.codigo_producto}\nNombre{self.nombre}\nDescripcion{self.descipcion}\nPrecio unitario: {self.precio_unitario}')
