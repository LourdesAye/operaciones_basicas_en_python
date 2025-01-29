#diccionario
inventario = {
    1: {"nombre": "Manzana", 
        "descripcion": "fruta fresca y deliciosa", 
        "cantidad": 10, 
        "precio": 1, 
        "categoria": "Frutas"},
    2: {"nombre": "Naranja", 
        "descripcion": "fruta ácida pero dulce", 
        "cantidad": 20, 
        "precio": 2, 
        "categoria": "Frutas"},
    3: {"nombre": "Pera", 
        "descripcion": "fruta fresca pero se pudre rápido", 
        "cantidad": 30, 
        "precio": 3.5, 
        "categoria": "Frutas"},
    4: {"nombre": "Pomelo", 
        "descripcion": "fruta ácida pero corta la sed", 
        "cantidad": 50, 
        "precio": 0.5, 
        "categoria": "Frutas"},
    5: {"nombre": "Vigilante", 
        "descripcion": "factura con dulce de membrillo", 
        "cantidad": 20, 
        "precio": 30, 
        "categoria": "Panadería"},
    6: {"nombre": "Bola de Fraile", 
        "descripcion": "factura redonda rellena de dulce de leche", 
        "cantidad": 40, 
        "precio": 50, 
        "categoria": "Panadería"},
    7: {"nombre": "Churro", 
        "descripcion": "factura con relleno de dulce de leche y baño de chocolate", 
        "cantidad": 40, 
        "precio": 30.50, 
        "categoria": "Panadería"}
}

codigo_actual = 8

#funcion de menú interactivo
def mostrar_menu():
    print("Menú de Gestión de Inventario:")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Reporte de Bajo Stock")
    print("7. Salir")
    
def registrar_producto():
    global codigo_actual
    print("***Registrar producto***\n")
    nombre_producto = input("Ingrese el nombre del producto: ")
    
    # Verificar si el producto ya está en el inventario por nombre
    producto_existente = False
    for datos in inventario.values():
        if datos["nombre"].lower() == nombre_producto.lower():
            producto_existente = True
            break
    
    if producto_existente:
        print("ESE PRODUCTO YA SE ENCUENTRA EN EL STOCK")
        print()
    else:
        descripcion = input("Ingrese la descripcion del producto: ").title()
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio del producto: "))
        categoria = input("Ingrese la categoria: ").title()
        
        # Agregar el producto al inventario
        inventario[codigo_actual] = {
            "nombre" : nombre_producto,
            "descripcion": descripcion, 
            "cantidad": cantidad, 
            "precio": precio, 
            "categoria": categoria}
    
        # Incrementar el código para el siguiente producto
        codigo_actual += 1
        print(f"Producto {nombre_producto} registrado exitosamente con el código {codigo_actual}")
        print()
    
def mostrar_productos(): 
    print()
    print("*** Mostrar productos ***\n")
    if not inventario: #verificando si el inventario esta vacio
        print("El inventario está vacío.") # si esta vacio se muestra mensaje por pantalla
    else:
        for codigo, datos in inventario.items(): # devuelve tupla (clave,valor) : (numero id unico de producto, diccionario con todos los datos del producto)
            print(f"Código: {codigo}")
            print(f"Nombre: {datos['nombre']}")
            print(f"Descripción: {datos['descripcion']}")
            print(f"Cantidad: {datos['cantidad']}")
            print(f"Precio: {datos['precio']}")
            print(f"Categoría: {datos['categoria']}")
            print("-" * 30)
    
    
def actualizar_producto():
    print()
    print("*** Actualizar Producto ***\n")
    codigo = int(input("Ingrese el código del producto que desea actualizar: "))
    print()
    if codigo in inventario:
        print(f"Actualmente hay {inventario[codigo]['cantidad']} unidades en stock de {inventario[codigo]["nombre"]}")
        print()
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        while nueva_cantidad < 0:
            print("LA CANTIDAD NO PUEDE SER NEGATIVA. Reingrese cantidad")
            nueva_cantidad = int(input("Ingrese la nueva cantidad de peliculas"))
        inventario[codigo]["cantidad"] = nueva_cantidad
        print()
        print("El Producto", inventario[codigo]["nombre"], "se actualizado con éxito.")
        print()
    else:
        print("Producto no encontrado.")
        print()
     
def eliminar_producto():
    print()
    print("*** Eliminar producto ***\n")
    codigo = int(input("Ingrese el código del producto que desea eliminar: "))
    print()
    if codigo in inventario:
        produto_borrado = inventario[codigo]["nombre"]
        del inventario[codigo]
        print(f"Producto {produto_borrado} con código {codigo} eliminado con éxito.")
    else:
         print("Producto no encontrado.")
    print()

def buscar_producto():
    print()
    print("*** Buscar producto ***\n")
    codigo = int(input("Ingrese el código del producto a buscar: ")) # se le solicita al usuario que ingrese el código correspondiente a un producto
    print()
    if codigo in inventario: # si el código existe en el inventario se guardan datos en una variable y luego se muestran
        datos = inventario[codigo]
        print("Nombre:", datos['nombre'])
        print("Descripción:", datos['descripcion'])
        print("Cantidad:", datos['cantidad'])
        print("Precio:", datos['precio'])
        print("Categoría:", datos['categoria'])
        print()
    else:
        print("Producto no encontrado.")
        print()

def reporte_bajo_stock():
    print()
    print("*** Reporte de Bajo Stock ***")
    limite = int(input("Ingrese el límite de stock para generar el reporte: "))
    while limite < 0:
        print()
        print("El límite no puede ser negativo. Reingrese el valor")
        print()
        limite = int(input("Ingrese el límite de stock para generar el reporte: "))
    print()
    print("Productos con stock igual o inferior a", limite, ":")
    print()
    productos_bajo_stock = False  # Variable para analizar si hay productos con bajo stock
    for codigo, datos in inventario.items():
        if datos["cantidad"] <= limite:
            productos_bajo_stock = True  # Se encontró al menos un producto con bajo stock
            print("Código:", codigo)
            print("Nombre:", datos['nombre'])
            print("Cantidad:", datos['cantidad'])
            print()
            
    if not productos_bajo_stock:
        print("No hay productos con bajo stock.")
        print()

while True:
    mostrar_menu()
    print()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        registrar_producto()
    elif opcion == 2:
        mostrar_productos()
    elif opcion == 3:
        actualizar_producto()
    elif opcion == 4:
        eliminar_producto()
    elif opcion == 5:
        buscar_producto()
    elif opcion == 6:
        reporte_bajo_stock()
    elif opcion == 7:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")