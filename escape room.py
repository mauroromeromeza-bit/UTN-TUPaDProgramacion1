# ========== PEDIR NOMBRE DEL AGENTE ==========
while True:
    nombre = input("Ingrese nombre del agente: ").strip()
    if nombre == "":
        print("Error: El nombre no puede estar vacío.")
    elif nombre.isalpha():
        break
    else:
        print("Error: Solo se permiten letras. Intente nuevamente.")

# ========== VARIABLES INICIALES ==========
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
contador_forzar_seguidas = 0  # Para la regla anti-spam

# ========== BUCLE PRINCIPAL DEL JUEGO ==========
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    # Mostrar estado actual
    print("\n" + "="*50)
    print(f"Agente: {nombre}")
    print(f"⚡ Energía: {energia}")
    print(f"⏱️  Tiempo: {tiempo}")
    print(f"🔐 Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"📡 Alarma: {'ACTIVADA' if alarma else 'Desactivada'}")
    print(f"🔑 Código parcial: {codigo_parcial}")
    print("="*50)

    # Menú
    print("\n--- Acciones ---")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía máx 100, -1 tiempo)")

    # Validar opción
    while True:
        opcion = input("Elija una opción (1-3): ").strip()
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 3:
                break
            else:
                print("Error: Opción fuera de rango. Elija 1, 2 o 3.")
        else:
            print("Error: Ingrese un número válido.")

    # ========== OPCIÓN 1: FORZAR CERRADURA ==========
    if opcion == 1:
        contador_forzar_seguidas += 1
        energia -= 20
        tiempo -= 2

        # Regla anti-spam: 3 veces seguidas
        if contador_forzar_seguidas == 3:
            print("⚠️  La cerradura se trabó por uso excesivo → ¡ALARMA ACTIVADA!")
            alarma = True
            continue  # No abre cerradura

        # Riesgo de alarma si energía baja
        if energia < 40 and not alarma:
            print("⚠️  Energía baja — Riesgo de alarma")
            while True:
                eleccion = input("Ingrese un número del 1 al 3: ").strip()
                if eleccion.isdigit():
                    eleccion = int(eleccion)
                    if 1 <= eleccion <= 3:
                        break
                    else:
                        print("Error: Solo 1, 2 o 3.")
                else:
                    print("Error: Ingrese un número.")
            if eleccion == 3:
                print("🚨 ¡Seleccionó 3! Alarma activada.")
                alarma = True
                continue

        # Abrir cerradura si no hay alarma
        if not alarma:
            cerraduras_abiertas += 1
            print(f"✅ Cerradura abierta. Total: {cerraduras_abiertas}/3")

    # ========== OPCIÓN 2: HACKEAR PANEL ==========
    elif opcion == 2:
        contador_forzar_seguidas = 0  # Corta la racha de forzar
        energia -= 10
        tiempo -= 3
        letra = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Letras para el código

        print("\nProgreso del hackeo:")
        for paso in range(4):
            codigo_parcial += letra[paso]
            print(f"  Paso {paso+1}/4 → Código: {codigo_parcial}")

        # Verificar si se completa el código para abrir cerradura
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f"✅ Código completo. Cerradura abierta. Total: {cerraduras_abiertas}/3")

    # ========== OPCIÓN 3: DESCANSAR ==========
    elif opcion == 3:
        contador_forzar_seguidas = 0  # Corta la racha de forzar
        tiempo -= 1
        energia += 15
        if energia > 100:
            energia = 100

        # Penalización extra si hay alarma
        if alarma:
            energia -= 10
            print("⚠️  Alarma activada → Penalización: -10 energía extra")

        print(f"💤 Descansaste. Energía actual: {energia}")

    # ========== VERIFICAR BLOQUEO POR ALARMA ==========
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\n🚨 SISTEMA BLOQUEADO — La alarma activó el cerrojo de seguridad")
        break

# ========== FIN DEL JUEGO — RESULTADO ==========
print("\n" + "🔒"*20)
if cerraduras_abiertas == 3:
    print(f"🏆 ¡VICTORIA, {nombre}! Abriste la bóveda con éxito.")
elif alarma and tiempo <= 3:
    print(f"❌ DERROTA — Sistema bloqueado por alarma, {nombre}.")
elif energia <= 0:
    print(f"❌ DERROTA — Te quedaste sin energía, {nombre}.")
elif tiempo <= 0:
    print(f"❌ DERROTA — Se agotó el tiempo, {nombre}.")
print("🔒"*20)