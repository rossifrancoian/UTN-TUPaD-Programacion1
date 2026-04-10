#EJERCICIO 1 "CAJA DE KIOSCO"
nombre = input ("Por favor, ingrese su nombre: ").strip()
while not nombre.isalpha() or nombre == "":
        print ("Error: El nombre debe contener solo caracteres alfabeticos y no puede estar vacio.")
        nombre = input("Intenta de nuevo: ").strip()
productos_compra=input("¿Cuantos productos desea comprar?: ")
while not productos_compra.isdigit() or int(productos_compra) < 0:
        print ("Por favor, ingrese un numero válido.")
        productos_compra= input("Intenta de nuevo:")
productos_compra = int(productos_compra)
total=0
total_descuento=0
for i in range (productos_compra):
        precio=input(f"¿Cuál es el precio del {i+1}° producto? ")
        while not precio.isdigit():
                print ("Por favor ingrese un precio válido.")
                precio=input("Intenta de nuevo: ")
        precio=float(precio)
        descuento=input("Tiene descuento? responder s/n ").strip().lower()
        while descuento not in ("s", "n"):
                print ("Recuerda que debes responder 'S' o 'N'.")
                descuento = input ("¿Tiene descuento? (S/N)").strip().lower()
        total+=precio
        if descuento == "s":
            precio *= 0.90
        total_descuento+= precio
        print(f"Producto {i+1} - Precio: {precio:.0f} Descuento (S/N): {descuento}")
ahorro=total - total_descuento
promedio = total_descuento / productos_compra
print(f"Total sin descuentos: {total:.2f}")
print(f"Total con descuentos: {total_descuento:.2f}")
print(f"Ahorro: {ahorro:.2f}")
print(f"Promedio por producto: {promedio:.2f}")

#EJERCICIO 2 "ACCESO AL CAMPUS Y MENU SEGURO"
usuario_correcto = "alumno"
clave_correcta = "python123"
acceso_concedido = False
for x in range (3):
        usuario = input("Ingrese su usuario: ")
        clave = input("Ingrese su clave: ")
        if usuario == usuario_correcto and clave == clave_correcta:
                print (f"Intento {x+1}/3 - Usuario: {usuario}")
                print (f"Clave: xxx")
                print (f"Acceso concedido")
                acceso_concedido = True
                break
        else:
                print (f"Intento {x+1}/3 - Usuario: {usuario}")
                print (f"Clave: xxx")
                print (f"Error: credenciales inválidas, vuelve a intentarlo.")
else:
        print ("Cuenta bloqueada")
if acceso_concedido == True:
        while True:
                print ("Menú:")
                print ("1. Ver estado de inscripción")
                print ("2. Cambiar clave")
                print ("3. Mostrar mensaje motivacional")
                print ("4. Salir.")
                opcion = (input("Selecciona una opción: "))
                while not opcion.isdigit():
                        print ("Error: no ha seleccionado una opción del menu.")
                opcion = input("Por favor, seleccione una opción del menú (1, 2, 3 o 4):")
                opcion = int(opcion)
                if opcion == 1:
                        print ("Inscripto")
                elif opcion == 2:
                        nueva_clave = input("Ingrese tu nueva clave: ")
                        confir_clave = input("Confirma tu nueva clave: ")
                        while len(nueva_clave) < 6:
                                print ("La contraseña debe tener al menos 6 caracteres, intentalo de nuevo.")
                                nueva_clave = input("Ingresa tu nueva clave: ")
                                confir_clave = input("Confirma tu nueva clave: ")
                        if nueva_clave != confir_clave:
                                print ("Las contraseñas no coinciden, intentalo de nuevo. ")
                                nueva_clave = input("Ingresa tu nueva clave: ")
                                confir_clave = input("Confirma tu nueva clave: ")
                        if len(nueva_clave) >= 6 and nueva_clave == confir_clave:
                                clave = nueva_clave
                                print ("Contraseña actualizada exitosamente.")
                elif opcion == 3:
                        print ("¡Dale que se puede! ¡No te rindas!")
                elif opcion == 4:
                        print ("Finalizando el programa.")
                        break
                else:
                        print ("Error. opción fuera de rango.")

#EJERCICIO 3 "AGENDA DE TURNOS CON NOMBRES (sin listas)"
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese nombre de operador: ").strip()
while not operador.isalpha() or operador == "":
        print ("Debe ingresar el nombre del operador con caracteres alfábeticos.")
        operador = input("Ingrese nombre de operador: ").strip()

while True:
        print ("Menú: ")
        print ("1. Reservar turno")
        print ("2. Cancelar turno ")
        print ("3. Ver agenda del día")
        print ("4. Ver resumen general")
        print ("5. Cerrar sistema")
        opcion = input("Por favor, ingrese una opción:")
        while not opcion.isdigit():
                print ("Error: ingrese una opción válida.")
                opcion = input("Por favor, seleccione una opcion del menú (1, 2, 3, 4 o 5) ")
        opcion = int(opcion)
        while opcion < 1 or opcion > 5:
                print ("Error: ingreso una opción fuera de rango.")
                opcion = int(input("Por favor, seleccione una opcion del menú (1, 2, 3, 4 o 5) "))
        if opcion == 1:
                print("¿Que día quiere reservar el turno?")
                turno = input("1. Lunes / 2. Martes.")
                while not turno.isdigit():
                        print ("Error: ingrese una opción válida.")
                        turno = (input("1. Lunes / 2. Martes."))
                turno = int(turno)
                while turno < 1 or turno > 2:
                        print ("Error: ingreso una opción fuera de rango.")
                        turno = int(input("Por favor ingrese el turno que desea reservar: 1. Lunes / 2. Martes: "))
                if turno == 1:
                        paciente = input("¿Cual es el tu nombre?").strip()
                while not paciente.isalpha() or paciente == "":
                        print ("Error: El nombre debe contener solo caracteres alfabeticos y no puede estar vacio.")
                        paciente = input("Intenta de nuevo: ").strip()
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                        print ("El paciente, se encuentra repetido en ese día.")
                elif lunes1 == "":
                        lunes1 = paciente
                elif lunes2 == "":
                        lunes2 = paciente
                elif lunes3 == "":
                        lunes3 = paciente
                elif lunes4 == "":
                        lunes4 = paciente
                else:
                        print("No existen turnos disponibles.")
                if turno == 2:
                        paciente = input("¿Cual es el tu nombre?").strip()
                while not paciente.isalpha() or paciente == "":
                        print ("Error: El nombre debe contener solo caracteres alfabeticos y no puede estar vacio.")
                        paciente = input("Intenta de nuevo: ").strip()
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                        print ("El paciente, se encuentra repetido en ese día.")
                elif martes1 == "":
                        martes1 = paciente
                elif martes2 == "":
                        martes2 = paciente
                elif martes3 == "":
                        martes3 = paciente
                else:
                        print ("No existen turnos disponibles. ")
        elif opcion == 2:
                print ("¿Qué día desea cancelar el turno?")
                cancela = input("1. Lunes / 2. Martes.")
                while not cancela.isdigit():
                        print ("Error: ingrese una opción válida.")
                        cancela = (input("1. Lunes / 2. Martes."))
                cancela = int(cancela)
                while cancela < 1 or cancela > 2:
                        print ("Error: ingreso una opción fuera de rango.")
                        cancela = int(input("Por favor ingrese el turno que desea cancelar: 1. Lunes / 2. Martes: "))
                if cancela == 1:
                        paciente = input("¿Cual es el tu nombre?").strip()
                while not paciente.isalpha() or paciente == "":
                        print ("Error: El nombre debe contener solo caracteres alfabeticos y no puede estar vacio.")
                        paciente = input("Intenta de nuevo: ").strip() 
                if lunes1 == paciente:
                        lunes1 = ""
                elif lunes2 == paciente:
                        lunes2 = ""
                elif lunes3 == paciente:
                        lunes3 = ""
                elif lunes4 == paciente:
                        lunes4 = ""
                else:
                        print ("No existen turnos a cancelar.")
                if cancela == 2:
                        paciente = input("¿Cual es el tu nombre?").strip()
                while not paciente.isalpha() or paciente == "":
                        print ("Error: El nombre debe contener solo caracteres alfabeticos y no puede estar vacio.")
                        paciente = input("Intenta de nuevo: ").strip() 
                if martes1 == paciente:
                        martes1 = ""
                elif martes2 == paciente:
                        martes2 = ""
                elif martes3 == paciente:
                        martes3 = ""
                else:
                        print ("No existen turnos a cancelar.")
        elif opcion == 3:
                print ("¿Qué día desea ver?")
                revisa = input("1. Lunes / 2. Martes.")
                while not revisa.isdigit():
                        print ("Error: ingrese una opción válida.")
                        revisa = (input("1. Lunes / 2. Martes."))
                revisa = int(revisa)
                while revisa < 1 or revisa > 2:
                        print ("Error: ingreso una opción fuera de rango.")
                        revisa = int(input("Por favor ingrese el día que desea revisar: 1. Lunes / 2. Martes: "))
                if revisa == 1:
                        if lunes1 == "":
                                print ("El turno 1 del Lunes se encuentra libre")
                        else:
                                print (f"El turno 1 se encuentra ocupado por: {lunes1}")
                        if lunes2 == "":
                                print ("El turno 2 del Lunes se encuentra libre")
                        else: 
                                print (f"El turno 2 se encuentra ocupado por: {lunes2}")
                        if lunes3 == "":
                                print ("El turno 3 del Lunes se encuentra libre")
                        else: 
                                print (f"El turno 3 se encuentra ocupado por: {lunes3}")
                        if lunes4 == "":
                                print ("El turno 4 del Lunes se encuentra libre")
                        else: 
                                print (f"El turno 4 se encuentra ocupado por: {lunes4}")
                elif revisa == 2:
                        if martes1 == "":
                                print ("El turno 1 del Martes se encuentra libre")
                        else:
                                print (f"El turno 1 se encuentra ocupado por: {martes1}")
                        if martes2 == "":
                                print ("El turno 2 del Martes se encuentra libre")
                        else: 
                                print (f"El turno 2 se encuentra ocupado por: {martes2}")
                        if martes3 == "":
                                print ("El turno 3 del Martes se encuentra libre")
                        else: 
                                print (f"El turno 3 se encuentra ocupado por: {martes3}")
        elif opcion == 4:
                lunes_ocupado = 0
                martes_ocupado = 0
                if lunes1 != "":
                        lunes_ocupado +=1
                if lunes2 != "":
                        lunes_ocupado +=1
                if lunes3 != "":
                        lunes_ocupado +=1
                if lunes4 != "":
                        lunes_ocupado +=1
                if martes1 != "":
                        martes_ocupado +=1
                if martes2 != "":
                        martes_ocupado +=1
                if martes3 != "":
                        martes_ocupado +=1
                lunes_disponibles = 4 - lunes_ocupado
                martes_disponibles = 3 - martes_ocupado
                print (f"Los turnos ocupados del Lunes son: {lunes_ocupado} y los disponibles son: {lunes_disponibles}")
                print (f"Los turnos ocupados del Martes son: {martes_ocupado} y los disponibles son: {martes_disponibles}")
                if lunes_ocupado > martes_ocupado:
                        print ("El día Lunes tiene mayor cantidad de turnos.")
                elif martes_ocupado > lunes_ocupado:
                        print ("El día Martes tiene mayor cantidad de turnos.")
                else:
                        print ("El día Lunes y Martes se encuentran empatados en cantidad de turnos.")
        elif opcion == 5:
                print ("Finalizando el programa.")
                break

#EJERCICIO 4 

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
contador_forzado_seguido = 0

nombre_agente = input("Ingrese el nombre del agente: ").strip()
while not nombre_agente.isalpha() or nombre_agente == "":
        print("Error: El nombre debe contener solo letras y no puede estar vacío.")
        nombre_agente = input("Intenta de nuevo: ").strip()

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False:
        print(f"\nEnergía: {energia}")
        print(f"Tiempo restante: {tiempo}")
        print(f"Alarma: {'ACTIVA' if alarma else 'DESACTIVADA'}")
        print("\nMenú:")
        print("1. Forzar cerradura")
        print("2. Hackear panel")
        print("3. Descansar")
        opcion = input("¿Qué desea hacer? ")
        while not opcion.isdigit():
                opcion = input("Ingrese una opción válida (1, 2 o 3): ")
                opcion = int(opcion)
        while opcion < 1 or opcion > 3:
                opcion = int(input("Ingrese una opción válida (1, 2 o 3): "))
        if opcion == 1:
                print("Has elegido forzar la cerradura.")
                energia -= 20
                tiempo -= 2
                contador_forzado_seguido += 1
        if contador_forzado_seguido == 3:
                alarma = True
                print("La cerradura se trabó y se activó la alarma.")
        else:
                if energia < 40:
                        riesgo_alarma = input("Riesgo de alarma. Ingrese un número del 1 al 3: ")
                while not riesgo_alarma.isdigit():
                        riesgo_alarma = input("Ingrese un número del 1 al 3: ")
                riesgo_alarma = int(riesgo_alarma)

                while riesgo_alarma < 1 or riesgo_alarma > 3:
                        riesgo_alarma = int(input("Ingrese un número válido del 1 al 3: "))

                if riesgo_alarma == 3:
                        alarma = True
                        print("¡Se ha activado la alarma!")
                if alarma == False:
                        cerraduras_abiertas += 1
                        print("¡Has abierto una cerradura!")
                else:
                        contador_forzado_seguido = 0
        if opcion == 2:
                print("Has elegido hackear el panel.")
                energia -= 10
                tiempo -= 3
                contador_forzado_seguido = 0
        for paso in range(4):
                print(f"Hackeando... paso {paso + 1}/4")
                codigo_parcial += "X"
                print(f"Código parcial: {codigo_parcial}")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("¡Una cerradura se abrió automáticamente!")
        if opcion == 3:
                print("Has elegido descansar.")
                energia += 15
                tiempo -= 1
                contador_forzado_seguido = 0
        if energia > 100:
                energia = 100
        if alarma:
                energia -= 10
        print("Descansas y recuperas energía.")
        if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
                print("\n La alarma bloqueó la bóveda. DERROTA.")
                break
if cerraduras_abiertas == 3:
        print("\n ¡VICTORIA! Abriste la bóveda.")
elif energia <= 0:
        print("\n DERROTA: te quedaste sin energía.")
elif tiempo <= 0:
        print("\n DERROTA: se acabó el tiempo.")
elif alarma == True:
        print("\n DERROTA: la alarma impidió abrir la bóveda.")

#ACTIVIDAD Escape Room: "La Arena del Gladiador"
vida_gladiador = int(100)
vida_enemigo = int(100)
pocion_vida = int(3)
daño_base_pesado = int(15)
daño_base_enemigo = int(12)
turno_gladiador = True
print ("--- BIENVENIDO A LA ARENA ---")
nombre_gladiador = input ("Ingrese el nombre del Gladiador: ")
while not nombre_gladiador.isalpha() or nombre_gladiador == "":
        print ("Error: el nombre solo puede contener letras")
        nombre_gladiador = input("Ingrese el nombre del Gladiador: ")
print ("=== INICIO DEL COMBATE ===")
while vida_gladiador > 0 and vida_enemigo > 0:
        print (f"{nombre_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pocion_vida}")
        print ("Elige acción:")
        print ("1. Ataque pesado.")
        print ("2. Ráfaga Veloz.")
        print ("3. Curar.")
        opcion = input("¿Qué desea hacer?")
        while not opcion.isdigit():
                opcion = input("Error: Ingrese una opción válida (1, 2 o 3):")
        opcion = int(opcion)
        while opcion < 1 or opcion > 3:
                opcion = int(input("Error: Ingrese una opción válida (1, 2 o 3):"))
                while not opcion.isdigit():
                        opcion =input("Opción: ")
        if opcion == 1:
                print ("¡Has atacado al enemigo!")
                if vida_enemigo < 20:
                        daño_base_pesado *= 1.5
                        print ("¡Golpe crítico!")
        vida_enemigo -= daño_base_pesado
        print (f"¡Atacaste al enemigo por {daño_base_pesado} puntos de daño!")
        if opcion == 2:
                print ("¡Has utilizado la Ráfaga Veloz!")
                for i in range (3):
                        vida_enemigo -= 5
                        print ("> Golpe conectado por 5 de daño.")
        if opcion == 3:
                if pocion_vida > 0:
                        vida_gladiador += 30
                        pocion_vida -= 1
                        print (f"Utilizaste una pocion y tu vida es de {vida_gladiador}, y te quedan {pocion_vida} pociones de vida.")
                elif pocion_vida == 0:
                        print ("¡No quedan pociones!")
                        print ("Has perdido tu turno.")
        vida_gladiador -= 12
        print (">>¡El enemigo te ataco por 12 puntos de daño!")
        print ("=== NUEVO TURNO ===")
if vida_gladiador > 0:
        print (f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
if vida_gladiador <= 0:
        print ("¡DERROTA! Has caído en combate.")