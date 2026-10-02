# ========== PASO 1: NOMBRE DEL GLADIADOR ==========
while True:
    nombre = input("Ingrese el nombre de su Gladiador: ").strip()
    if nombre == "":
        print("Error: Solo se permiten letras")
    elif nombre.isalpha():
        break
    else:
        print("Error: Solo se permiten letras")

# ========== PASO 2: ESTADÍSTICAS INICIALES ==========
vida_jugador = 100       # int
vida_enemigo = 100        # int
pociones = 3              # int
danio_ataque_pesado = 15  # int
danio_enemigo = 12        # int
turno_gladiador = True    # bool
juego_activo = True       # bool

# ========== PASO 3: CICLO DE COMBATE ==========
while vida_jugador > 0 and vida_enemigo > 0 and juego_activo:
    # --- Turno del Jugador ---
    if turno_gladiador:
        print("\n" + "="*45)
        print(f"Gladiador: {nombre} | ❤️ Vida: {vida_jugador}")
        print(f"Enemigo   | ❤️ Vida: {vida_enemigo}")
        print(f"🧪 Pociones disponibles: {pociones}")
        print("="*45)
        print("\n--- Tus acciones ---")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        # Validación estricta del menú
        while True:
            opcion = input("Elija una acción (1-3): ").strip()
            if not opcion.isdigit():
                print("Error: Debe ingresar un número.")
                continue
            opcion = int(opcion)
            if opcion < 1 or opcion > 3:
                print("Error: Elija una opción entre 1 y 3.")
                continue
            break

        # --- Lógica de acciones ---
        if opcion == 1:
            # Ataque Pesado con crítico
            if vida_enemigo < 20:
                danio_final = danio_ataque_pesado * 1.5  # float
                print("💥 ¡Golpe Crítico!")
            else:
                danio_final = danio_ataque_pesado  # int

            vida_enemigo -= int(danio_final)
            print(f"¡Atacaste al enemigo por {int(danio_final)} puntos de daño!")

        elif opcion == 2:
            # Ráfaga Veloz con for
            for golpe in range(3):
                vida_enemigo -= 5
                print(f" > Golpe conectado por 5 de daño")

        elif opcion == 3:
            # Curar
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print(f"💚 Te curaste 30 puntos de vida. Pociones restantes: {pociones}")
            else:
                print("¡No quedan pociones!")

        # Verificar si el enemigo cayó
        if vida_enemigo <= 0:
            juego_activo = False
            continue

        # Cambiar turno
        turno_gladiador = False

    # --- Turno del Enemigo ---
    else:
        vida_jugador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")
        turno_gladiador = True

# ========== PASO 4: FIN DEL JUEGO ==========
print("\n" + "🏆"*15)
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
print("🏆"*15)