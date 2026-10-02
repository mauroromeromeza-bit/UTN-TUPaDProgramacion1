# 1. Credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

# 2. Máximo 3 intentos
intentos = 0
acceso_permitido = False

while intentos < 3:
    usuario = input("Usuario: ").strip()
    clave = input("Clave: ").strip()
    
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso_permitido = True
        break
    else:
        intentos += 1
        restantes = 3 - intentos
        if restantes > 0:
            print(f"Datos incorrectos. Te quedan {restantes} intento(s).")

# 3. Bloqueo si agota intentos
if not acceso_permitido:
    print("Cuenta bloqueada")
else:
    # 4. Menú repetitivo
    while True:
        print("\n===== MENÚ =====")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje motivacional")
        print("4. Salir")
        
        # 5. Validación estricta del menú
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if not opcion.isdigit():
            print("Error: Debe ingresar un número.")
            continue
        
        opcion = int(opcion)
        
        if opcion < 1 or opcion > 4:
            print("Error: Opción fuera de rango. Elija entre 1 y 4.")
            continue
        
        # Ejecutar acción según opción
        if opcion == 1:
            print("Inscripto")
        
        elif opcion == 2:
            while True:
                nueva_clave = input("Ingrese nueva clave (mínimo 6 caracteres): ").strip()
                if len(nueva_clave) < 6:
                    print("Error: La clave debe tener al menos 6 caracteres.")
                    continue
                confirmacion = input("Confirme la nueva clave: ").strip()
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada exitosamente.")
                    break
                else:
                    print("Error: Las claves no coinciden. Intente nuevamente.")
        
        elif opcion == 3:
            print("¡El esfuerzo constante te lleva a la cima, no te rindas!")
        
        elif opcion == 4:
            print("Saliendo del sistema...")
            break