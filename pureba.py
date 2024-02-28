lista = [['melo', 'nose', 343.234], ['sandi', 'rabano', 343.43]]

total = 0.0
print(total)

for listarar in lista:
    nombre = listarar[0]
    especi = listarar[1]
    precio = listarar[2]

    total = total+float(precio)

    print(f'nombre: {nombre}\nEspecificacion: {especi}\nPrecio: {precio}')

print('total: ', total)
    