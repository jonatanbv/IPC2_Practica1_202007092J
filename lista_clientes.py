class Cliente:
    def __init__(self, nit, nombre, correo):
        self.nombre = nombre
        self.nit = nit
        self.correo = correo
        self.siguiente = None

    def mostrar(self):
        print(f'Nombre:\t{self.nombre}\nNit:\t{self.nit}\nCorreo:\t{self.correo}\n')


class Lista_clientes:
    def __init__(self):
        self.primer_nodo = None

    def insertar_cliente(self, nit, nombre, correo):
        nuevo_nodo = Cliente(nit, nombre, correo)
        nuevo_nodo.siguiente = self.primer_nodo
        self.primer_nodo = nuevo_nodo

    def buscar_cliente(self, nit):
        actual = self.primer_nodo
        while actual is not None:
            if actual.nit == nit:
                return actual
            actual = actual.siguiente
        return None
    
    def mostrar_clientes(self):
        actual = self.primer_nodo
        while actual:
            actual.mostrar()
            actual = actual.siguiente

