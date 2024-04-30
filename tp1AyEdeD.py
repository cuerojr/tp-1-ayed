# Constantes con los datos de los estudiantes
usuario1_email = "estudiante1@ayed.com"
usuario1_contraseña = "111222"
usuario2_email = "estudiante2@ayed.com"
usuario2_contraseña = "333444"
usuario3_email = "estudiante3@ayed.com"
usuario3_contraseña = "555666"

# Función para ocultar la contraseña mientras se escribe
def ocultar_contraseña():
    contraseña = ""
    while True:
        caracter = msvcrt.getch().decode("utf-8")
        if caracter == "\r":
            print()
            return contraseña
        elif caracter == "\b":
            contraseña = contraseña[:-1]
            print("\b \b", end="", flush=True)
        else:
            contraseña += caracter
            print("*", end="", flush=True)

# Función para gestionar el perfil
def gestionar_mi_perfil():
    print("1. Gestionar mi perfil")
    print("a. Editar mis datos personales")
    print("2. Gestionar candidatos")
    print("a. Ver candidatos")
    print("En Construcción")
    print("0. Salir")

# Función para editar datos personales
def editar_datos_personales():
    # Implementar la edición de datos personales
    print("Editar datos personales")

# Función para ver candidatos
def ver_candidatos():
    # Implementar la visualización de candidatos
    print("Ver candidatos")

# Función para la ruleta
def ruleta():
    # Solicitar al usuario las probabilidades de matcheo
    while True:
        try:
            probabilidad_a = int(input("Ingrese la probabilidad de matcheo para la Persona A: "))
            probabilidad_b = int(input("Ingrese la probabilidad de matcheo para la Persona B: "))
            probabilidad_c = int(input("Ingrese la probabilidad de matcheo para la Persona C: "))
            if probabilidad_a + probabilidad_b + probabilidad_c != 100:
                print("La suma de las probabilidades debe ser igual a 100. Intente de nuevo.")
            else:
                break
        except ValueError:
            print("Ingrese números enteros.")

    # Simular la ruleta
    ruleta = [1] * probabilidad_a + [2] * probabilidad_b + [3] * probabilidad_c
    seleccion = random.choice(ruleta)

    # Mostrar el resultado
    if seleccion == 1:
        print("Persona seleccionada: A")
    elif seleccion == 2:
        print("Persona seleccionada: B")
    else:
        print("Persona seleccionada: C")

# Programa principal
import msvcrt
import random

intentos = 3

while intentos > 0:
    print("Ingrese su email y contraseña.")
    email = input("Email: ")
    contraseña = ocultar_contraseña()

    if email == usuario1_email and contraseña == usuario1_contraseña:
        print("Bienvenido Usuario 1.")
        gestionar_mi_perfil()
        opcion = input("Ingrese su opción: ")
        if opcion == "a":
            editar_datos_personales()
        elif opcion == "2":
            ver_candidatos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
    elif email == usuario2_email and contraseña == usuario2_contraseña:
        print("Bienvenido Usuario 2.")
        gestionar_mi_perfil()
        opcion = input("Ingrese su opción: ")
        if opcion == "a":
            editar_datos_personales()
        elif opcion == "2":
            ver_candidatos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
    elif email == usuario3_email and contraseña == usuario3_contraseña:
        print("Bienvenido Usuario 3.")
        gestionar_mi_perfil()
        opcion = input("Ingrese su opción: ")
        if opcion == "a":
            editar_datos_personales()
        elif opcion == "2":
            ver_candidatos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
    else:
        intentos -= 1
        print("Email o contraseña incorrectos.")

if intentos == 0:
    print("Ha excedido el número de intentos permitidos. Cerrando el programa.")