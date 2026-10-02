# 1. Pedir nombre del cliente (solo letras, no vacío)
while True:
    nombre = input("Ingrese nombre del cliente: ").strip()
    if nombre == "":
        print("Error: El nombre no puede quedar vacío. Intente nuevamente.")
    elif nombre.isalpha():
        break
    else:
        print("Error: El nombre solo puede contener letras. Intente nuevamente.")

# 2. Pedir cantidad de productos (entero positivo)
while True:
    cantidad = input("Ingrese cantidad de productos a comprar: ").strip()
    if cantidad.isdigit():
        cantidad = int(cantidad)
        if cantidad > 0:
            break
        else:
            print("Error: La cantidad debe ser mayor a 0. Intente nuevamente.")
    else:
        print("Error: Debe ingresar un número entero válido. Intente nuevamente.")

# Inicializar acumuladores
total_sin_descuento = 0
total_con_descuento = 0

# 3. Por cada producto
for i in range(1, cantidad + 1):
    print(f"\n--- Producto {i} de {cantidad} ---")
    
    # Pedir precio
    while True:
        precio = input(f"Ingrese precio del producto {i}: ").strip()
        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("Error: Debe ingresar un número entero válido.")
    
    # Pedir descuento S/N
    while True:
        descuento = input("¿Tiene descuento? (S/N): ").strip().lower()
        if descuento in ("s", "n"):
            break
        else:
            print("Error: Solo debe ingresar S o N (cualquier mayúscula/minúscula).")
    
    # Aplicar descuento si corresponde
    precio_con_desc = precio
    if descuento == "s":
        precio_con_desc = precio * 0.9  # 10% de descuento
    
    # Acumular totales
    total_sin_descuento += precio
    total_con_descuento += precio_con_desc

# Cálculos finales
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

# 4. Mostrar resultados
print("\n" + "="*40)
print(f"Nombre del cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
print("="*40)