# Mensaje de bienvenida
print("=" * 60)
print("Bienvenidos a la Tienda Tecnológica RIWI".center(60))
print("=" * 60)
print("*" * 60)

# Ingreso de datos
nombre_del_producto = input("Ingrese el nombre del producto: ")
precio_unitario = input("Ingrese el precio unitario del producto: ")
cantidad_de_productos = input("Ingrese cantidad de productos adquiridos: ")
pregunta_de_descuento = input("¿El producto tiene descuento? si/no: ")

# Conversión de datos y validación de números
precio_unitario_float = float(precio_unitario)
cantidad_de_productos_int = int(cantidad_de_productos)

# Validación: que el precio y la cantidad sean números positivos
if precio_unitario_float > 0 and cantidad_de_productos_int > 0:
    # Cálculo del costo sin descuento
    costo_sin_descuento = precio_unitario_float * cantidad_de_productos_int

    # Validacion de si aplica descuento
    if pregunta_de_descuento.lower() == "si":
        valor_de_descuento = input("¿Cuánto es el porcentaje de descuento del producto?: ")
        
        valor_de_descuento = valor_de_descuento.replace('%', '')
        valor_de_descuento_float = float(valor_de_descuento)
        
        # Validación del descuento (es un número y está entre 0 y 100)
        if valor_de_descuento_float >= 0 and  valor_de_descuento_float <= 100:
            calculo_de_descuento = (valor_de_descuento_float / 100) * precio_unitario_float
            descuento_sobre_producto = precio_unitario_float - calculo_de_descuento
            costo_total_con_descuento = descuento_sobre_producto * cantidad_de_productos_int
                
            print("=" * 60)
            print(f"Producto: {nombre_del_producto}".ljust(30) + f"Costo total: ${costo_total_con_descuento:.2f}".rjust(30))
            print(" " * 60)
            print("¡Gracias por confiar en RIWI!".center(60))
            print("=" * 60)
            print("Apreciamos tu visita, ¡esperamos verte pronto!".center(60))
        else:
            print("Error: el descuento debe estar entre 0 y 100%.")
    
    elif pregunta_de_descuento.lower() == "no":
        print("=" * 60)
        print(f"Producto: {nombre_del_producto}".ljust(30) + f"Costo total: ${costo_sin_descuento:.2f}".rjust(30))
        print(" " * 60)
        print("¡Gracias por confiar en RIWI!".center(60))
        print("=" * 60)
        print("Apreciamos tu visita, ¡esperamos verte pronto!".center(60))
    else:
        print("Error: debe escoger entre las opciones 'si' o 'no'.")
else:
    print("Error: El precio y la cantidad de productos deben ser números positivos.")
