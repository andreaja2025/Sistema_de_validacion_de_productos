## Entrenamiento Módulo 1 – Semana 1
## Sistema de validación de productos
# ANDREA ARIAS-RIWI

# Mostrar un mensaje de bienvenida para los clientes de la tienda
print("=" * 60)  
print("Bienvenidos a la Tienda Tecnológica RIWI".center(60))  # .center() centra el texto
print("=" * 60)  
print("*" * 60)  

# Solicitar al usuario que ingrese el nombre del producto
nombre_del_producto = input("Ingrese el nombre del producto: ").strip()
# .strip() elimina espacios en blanco al inicio y al final

# Solicitar el precio del producto
precio_por_unidad = input("Ingrese el precio del producto: ").strip().replace(',', '.')

# Validar que el precio ingresado sea un número positivo
if precio_por_unidad.replace('.', '').isdigit():  
    precio_por_unidad_float = float(precio_por_unidad)  # Convertir a número decimal

    if precio_por_unidad_float > 0:
        # Solicitar la cantidad de unidades compradas del producto
        cantidad_productos = input("Ingrese la cantidad de productos: ").strip()

        # Validar que la cantidad ingresada sea un número entero positivo
        if cantidad_productos.isdigit():  
            cantidad_productos_int = int(cantidad_productos)

            if cantidad_productos_int > 0:
                # Calcular el costo total sin aplicar ningún descuento
                costo_total_sin_descuento = precio_por_unidad_float * cantidad_productos_int

                # Solicitar al usuario si hay algún descuento aplicado
                descuento_porcentaje = input(
                    "Ingrese el porcentaje de descuento o si no aplica escriba 'no': "
                ).replace('%', '').strip().lower()

                # .replace('%', '') elimina el símbolo de porcentaje si el usuario lo escribe
                # .strip() elimina espacios extra
                # .lower() convierte la entrada a minúsculas para evitar errores con "No" o "NO"

                # Verificar si el usuario ingresó un número como descuento
                if descuento_porcentaje.isdigit():
                    descuento_porcentaje_int = int(descuento_porcentaje)  # Convertir a entero

                    # Validar que el descuento ingresado sea un número entre 0 y 100
                    if 0 <= descuento_porcentaje_int <= 100:
                        monto_descuento = costo_total_sin_descuento * (descuento_porcentaje_int / 100)
                        costo_total_con_descuento = costo_total_sin_descuento - monto_descuento

                        # Mostrar el resultado de la compra con formato claro
                        print("=" * 60)  
                        print(f"Producto: {nombre_del_producto}".ljust(30) +
                              f"Costo total: ${costo_total_con_descuento:.2f}".rjust(30))
                        print("=" * 60)

                    else:
                        print("Error: El descuento debe estar entre 0 y 100.")
                
                # Si no hay descuento, mostrar el cálculo sin descuento
                elif descuento_porcentaje == "no":
                    print("=" * 60)
                    print(f"Producto: {nombre_del_producto}".ljust(30) +
                          f"Costo total: ${costo_total_sin_descuento:.2f}".rjust(30))
                    print("¡Gracias por confiar en RIWI!".center(60))
                    print("=" * 60)
                    print("Apreciamos tu visita, ¡esperamos verte pronto!".center(60))
                
                else:
                    print("Error: Ingrese un valor válido para el descuento.")
            
            else:
                print("Error: La cantidad de productos debe ser mayor que 0.")
        
        else:
            print("Error: La cantidad debe ser un número entero positivo.")
    
    else:
        print("Error: El precio debe ser mayor positivo.")

else:
    print("Error: El precio debe ser un número positivo.")
