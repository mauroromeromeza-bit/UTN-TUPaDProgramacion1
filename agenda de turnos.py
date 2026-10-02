# ========== INICIO: Pedir nombre del operador ==========
while True:
    operador = input("Ingrese nombre del operador: ").strip()
    if operador == "":
        print("Error: El nombre no puede estar vacío.")
    elif operador.isalpha():
        break
    else:
        print("Error: Solo se permiten letras. Intente nuevamente.")

# ========== VARIABLES DE TURNOS (sin estructuras) ==========
# Lunes: 4 cupos
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Martes: 3 cupos
martes1 = ""
martes2 = ""
martes3 = ""

# ========== FUNCIONES AUXILIARES ==========
def elegir_dia():
    while True:
        print("\n1 - Lunes")
        print("2 - Martes")
        dia_op = input("Seleccione día: ").strip()
        if not dia_op.isdigit():
            print("Error: Ingrese un número.")
            continue
        dia_op = int(dia_op)
        if dia_op == 1 or dia_op == 2:
            return dia_op
        else:
            print("Error: Opción inválida. Elija 1 o 2.")

def pedir_nombre_paciente():
    while True:
        nombre = input("Nombre del paciente: ").strip()
        if nombre == "":
            print("Error: El nombre no puede estar vacío.")
        elif nombre.isalpha():
            return nombre
        else:
            print("Error: Solo letras. Intente nuevamente.")

# ========== MENÚ PRINCIPAL ==========
while True:
    print("\n" + "="*40)
    print(f"Sistema de Turnos — Operador: {operador}")
    print("="*40)
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("Seleccione una opción (1-5): ").strip()
    if not opcion.isdigit():
        print("Error: Debe ingresar un número.")
        continue
    opcion = int(opcion)
    if opcion < 1 or opcion > 5:
        print("Error: Opción fuera de rango (1-5).")
        continue

    # ========== 1. RESERVAR ==========
    if opcion == 1:
        dia = elegir_dia()
        nombre_pac = pedir_nombre_paciente()
        reservado = False

        if dia == 1:  # Lunes
            # Verificar duplicado
            if lunes1 == nombre_pac or lunes2 == nombre_pac or lunes3 == nombre_pac or lunes4 == nombre_pac:
                print(f"El paciente {nombre_pac} ya tiene turno el Lunes.")
                continue
            # Buscar primer espacio libre
            if lunes1 == "":
                lunes1 = nombre_pac
                reservado = True
            elif lunes2 == "":
                lunes2 = nombre_pac
                reservado = True
            elif lunes3 == "":
                lunes3 = nombre_pac
                reservado = True
            elif lunes4 == "":
                lunes4 = nombre_pac
                reservado = True

        else:  # Martes
            if martes1 == nombre_pac or martes2 == nombre_pac or martes3 == nombre_pac:
                print(f"El paciente {nombre_pac} ya tiene turno el Martes.")
                continue
            if martes1 == "":
                martes1 = nombre_pac
                reservado = True
            elif martes2 == "":
                martes2 = nombre_pac
                reservado = True
            elif martes3 == "":
                martes3 = nombre_pac
                reservado = True

        if reservado:
            print(f"Turno reservado con éxito para {nombre_pac}.")
        else:
            print("No hay cupos disponibles para ese día.")

    # ========== 2. CANCELAR ==========
    elif opcion == 2:
        dia = elegir_dia()
        nombre_pac = pedir_nombre_paciente()
        encontrado = False

        if dia == 1:
            if lunes1 == nombre_pac:
                lunes1 = ""
                encontrado = True
            elif lunes2 == nombre_pac:
                lunes2 = ""
                encontrado = True
            elif lunes3 == nombre_pac:
                lunes3 = ""
                encontrado = True
            elif lunes4 == nombre_pac:
                lunes4 = ""
                encontrado = True
        else:
            if martes1 == nombre_pac:
                martes1 = ""
                encontrado = True
            elif martes2 == nombre_pac:
                martes2 = ""
                encontrado = True
            elif martes3 == nombre_pac:
                martes3 = ""
                encontrado = True

        if encontrado:
            print(f"Turno de {nombre_pac} cancelado correctamente.")
        else:
            print(f"No se encontró turno para {nombre_pac} en ese día.")

    # ========== 3. VER AGENDA ==========
    elif opcion == 3:
        dia = elegir_dia()
        if dia == 1:
            print("\n--- Agenda Lunes ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print("\n--- Agenda Martes ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    # ========== 4. RESUMEN GENERAL ==========
    elif opcion == 4:
        # Contar lunes
        lun_ocu = 0
        if lunes1 != "": lun_ocu += 1
        if lunes2 != "": lun_ocu += 1
        if lunes3 != "": lun_ocu += 1
        if lunes4 != "": lun_ocu += 1
        lun_lib = 4 - lun_ocu

        # Contar martes
        mar_ocu = 0
        if martes1 != "": mar_ocu += 1
        if martes2 != "": mar_ocu += 1
        if martes3 != "": mar_ocu += 1
        mar_lib = 3 - mar_ocu

        print("\n===== RESUMEN GENERAL =====")
        print(f"Lunes   → Ocupados: {lun_ocu} | Disponibles: {lun_lib}")
        print(f"Martes  → Ocupados: {mar_ocu} | Disponibles: {mar_lib}")

        # Día con más turnos
        if lun_ocu > mar_ocu:
            print("El día con más turnos ocupados es: Lunes")
        elif mar_ocu > lun_ocu:
            print("El día con más turnos ocupados es: Martes")
        else:
            print("Hay empate en la cantidad de turnos ocupados entre Lunes y Martes")

    # ========== 5. SALIR ==========
    elif opcion == 5:
        print(f"Gracias {operador}, cerrando sistema...")
        break