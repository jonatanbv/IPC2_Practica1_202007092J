from lista_clientes import Lista_clientes, Cliente
from lista_productos import listaProducto, Producto
from lista_compras import Lista_compras

lista_productor_ingresados = listaProducto()
lista_compras_realizadas = Lista_compras()
lista_clientes_resgistrados = Lista_clientes()

codigo_compra_realizada = 10000


def registrar_producto():
    codigo = input('Ingrese el codigo del producto: ')
    nombre = input('Ingrese el nombre del producto: ')
    descripcion = input('Ingrese una descripcion: ')
    precio = input('Ingrese el precio: ')

    lista_productor_ingresados.insertar_producto(codigo, nombre, descripcion, precio)
    print('se registro producto')

def mostrar_productos_ingresados():
    lista_productor_ingresados.mostrar()

def registrar_cliente():
    nit = input('NIT: ')
    nombre = input('Nombre: ')
    correo = input('Correo: ')
    lista_clientes_resgistrados.insertar_cliente(nit, nombre, correo)
    print('Se registro cliente')

def mostrar_clientes_ingresados():
    lista_clientes_resgistrados.mostrar_clientes()

def realizar_compra():
    print('se realizar compra')

def reporte_de_compra():
    lista_compras_realizadas.mostrar()
    print('se muestra un reporte de las compras')

def datos_del_estudiante():
    print('Nombre:\tJonatan Josue Vasquez Pastor\nCarnet:\t202007092\nCorreo:\t3786578280101@ingenieria.usac.edu.gt')
    print('Se muestran los datos del estudiante')

def salir():
    print('Te esperamos pronto!!!')

def agregar_producto(lista, codigo_compra):
    sku = input('Ingrese el codigo del producto: ')
    producto = lista_productor_ingresados.buscar(sku)
    if producto:
        nombre = producto.nombre
        descripcion = producto.descipcion 
        precio = producto.precio_unitario

        producto = [sku, nombre, descripcion, precio]
        lista.append(producto)
        lista_compras_realizadas.insertar_producto(codigo_compra, sku, nombre, descripcion, precio)

        print('Se agrego un producto')


def terminar_compra_y_facturar(nit, lista, codigo_compra):
    cliente = lista_clientes_resgistrados.buscar_cliente(nit)
    #lista_compras_realizadas.insertar_cliente()
    if cliente:
        nombre = cliente.nombre
        correo = cliente.correo
        print(f'Nombre:\t{nombre}\nNit:\t{nit}\nCorreo:\t{correo}')
        lista_compras_realizadas.insertar_cliente(codigo_compra, nit, nombre, correo)

        total = 0

        for productos in lista:
            sku = productos[0]
            nombre_producto = productos[1]
            descripcion = productos[2]
            precio_unitario = productos[3]
            print(f'{nombre_producto}, {sku}, {descripcion}, {precio_unitario}')

            total = total + float(precio_unitario)

        
        print('Total sin IVA:\t\t\t', total)
        total = total*0.12+total
        print(f'Total:\t\t\t{total}')
        print(f'------------- Total: {total} ----------------')

        print('fianlizo la compra y se procede a facturar')

def menu():
    bandera = True
    while bandera:
        print('--------------- Menu principal ---------------')
        print('1. Registrar Producto\n2. Registrar Clientes\n3. Realizar compras\n4. Reporte de compras\n5. Datos del estudiante\n6. Ver productos registrados\n7. Ver clientes registrados\n8. Salir')
        print('----------------------------------------------')
        opcion = input('Ingrese la opcion: ')
        if opcion == "1":
            registrar_producto()
        elif opcion == '2': 
            registrar_cliente()
        elif opcion == '3':
            realizar_compra()
            global codigo_compra_realizada
            compras = []
            flag = True
            while flag:
                print('---------------- Menu compra -----------------')
                print('1. Agregar Producto')
                print('2. Terminar compra y facturar')
                print('---------------------------------------------')
                opcion2 = input('Ingrese una opcion: ')
                if int(opcion2) == 1:
                    agregar_producto(compras, codigo_compra_realizada)
                elif opcion2 == '2':
                    nit = input('Ingrese el nit: ')
                    terminar_compra_y_facturar(nit, compras, codigo_compra_realizada)
                    flag= False
                else:
                    print('No se encontro la opcion solicitada, intente nuevamente')

            
            codigo_compra_realizada = codigo_compra_realizada+1

        elif opcion == '4':
            reporte_de_compra()
        elif opcion == '5':
            datos_del_estudiante()
        elif opcion == '6':
            mostrar_productos_ingresados()
        elif opcion == '7':
            mostrar_clientes_ingresados()
        elif opcion == "8":
            salir()
            bandera = False
        else:
            print('esta opcion no existe, por favor intentelo de nuevo')
        

menu()