# Constantes con los datos de los estudiantes
ESTUDIANTE_1_EMAIL = "estudiante1@ayed.com"
ESTUDIANTE_1_CONTRASEÑA = "111222"
ESTUDIANTE_2_EMAIL = "estudiante2@ayed.com"
ESTUDIANTE_2_CONTRASEÑA = "333444"
ESTUDIANTE_3_EMAIL = "estudiante3@ayed.com"
ESTUDIANTE_3_CONTRASEÑA = "555666"

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
    print("Bienvenido al sistema. Por favor, ingrese su email y contraseña.")
    email = input("Email: ")
    contraseña = ocultar_contraseña()

    if email == ESTUDIANTE_1_EMAIL and contraseña == ESTUDIANTE_1_CONTRASEÑA:
        print("Acceso concedido como Estudiante 1.")
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
    elif email == ESTUDIANTE_2_EMAIL and contraseña == ESTUDIANTE_2_CONTRASEÑA:
        print("Acceso concedido como Estudiante 2.")
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
    elif email == ESTUDIANTE_3_EMAIL and contraseña == ESTUDIANTE_3_CONTRASEÑA:
        print("Acceso concedido como Estudiante 3.")
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
        print("Email o contraseña incorrectos. Intentos restantes:", intentos)

if intentos == 0:
    print("Ha excedido el número de intentos permitidos. Cerrando el programa.")
  print ("hola fin")
