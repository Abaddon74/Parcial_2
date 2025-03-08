import csv


def cargar_productos(archivo):
    productos = []
    try:
        with open(archivo, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                nombre_producto = row['nombre_producto']
                precio = float(row['precio'])
                porcentaje_descuento = float(row['porcentaje_descuento'])
                productos.append({
                    'nombre_producto': nombre_producto,
                    'precio': precio,
                    'porcentaje_descuento': porcentaje_descuento
                })
    except FileNotFoundError:
        print("Error: El archivo no se encuentra.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return productos


def calcular_precio_promedio(productos):
    if len(productos) == 0:
        return 0
    total_precio = sum([producto['precio'] for producto in productos])
    return total_precio / len(productos)


def aplicar_descuento(productos):
    descuento = lambda precio, porcentaje_descuento: precio * (1 - porcentaje_descuento / 100)
    for producto in productos:
        producto['precio_con_descuento'] = descuento(producto['precio'], producto['porcentaje_descuento'])
    return productos


def gestionar_tienda():
    archivo = 'productos.csv'
    
   
    productos = cargar_productos(archivo)
    
    if productos:
    
        promedio = calcular_precio_promedio(productos)
        print(f"El precio promedio de los productos es: {promedio:.2f}")
        
      
        productos_con_descuento = aplicar_descuento(productos)
        
        print(f"\nPrecios después de aplicar los descuentos:")
        for producto in productos_con_descuento:
            print(f"{producto['nombre_producto']}: Precio original: {producto['precio']:.2f} | Precio con descuento: {producto['precio_con_descuento']:.2f}")
    else:
        print("No se pudieron cargar los productos.")

if __name__ == '__main__':
    gestionar_tienda()
