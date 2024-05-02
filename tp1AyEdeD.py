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

# Función para menu completo
def menu_completo():
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

# Función para gestionar mi perfil
def gestionar_mi_perfil():
    print("a. Editar mis datos personales")
    print("b. Eliminar mi perfil")
    print("c. Volver")

# Función para gestionar candidatos
def gestionar_candidatos():
    print("a. Ver candidatos")
    print("b. Reportar un candidato")
    print("c. Volver")

# Función para matcheos
def matcheos():
    print("a. Ver matcheos")
    print("b. Eliminar un matcheo")
    print("c. Volver")

# Función para editar datos personales
def editar_datos_personales():
    # Implementar la edición de datos personales
    print("Editar datos personales")

# Base de datos de estudiantes
estudiantes = [
    {"nombre": "Estudiante 1", "fecha_nacimiento": "2000-01-01", "biografia": "Soy el Estudiante 1", "hobbies": ["Fútbol", "Música"]},
    {"nombre": "Estudiante 2", "fecha_nacimiento": "2001-02-02", "biografia": "Soy el Estudiante 2", "hobbies": ["Pintura", "Videojuegos"]},
    {"nombre": "Estudiante 3", "fecha_nacimiento": "2002-03-03", "biografia": "Soy el Estudiante 3", "hobbies": ["Lectura", "Cine"]}
]

# Función para calcular la edad a partir de la fecha de nacimiento
def calcular_edad(fecha_nacimiento):
    from datetime import datetime
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

# Función para ver candidatos
def ver_candidatos(estudiantes):
    print("Candidatos:")
    for estudiante in estudiantes:
        edad = calcular_edad(estudiante["fecha_nacimiento"])
        print("\nNombre:", estudiante["nombre"])
        print("Edad:", edad)
        print("Biografía:", estudiante["biografia"])
        print("Hobbies:", ", ".join(estudiante["hobbies"]))

# Funciones para "En Construcción"
def cons():
    print("En Construcción.")

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

# Programa principal---------------------------------------------------------------------------------------------------------------------------------------------
import msvcrt
import random

intentos = 3
salir = True

while intentos > 0 and salir:
    print("Ingrese su email y contraseña.")
    email = input("Email: ")
    contraseña = ocultar_contraseña()

    if email == usuario1_email and contraseña == usuario1_contraseña:
        print("Bienvenido Usuario 1.")
        menu_completo()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            gestionar_mi_perfil()
            opcion == input("Ingrese su opción:")
            if opcion == "a":
                editar_datos_personales()
            else:
                cons()
        elif opcion == "2":
            gestionar_candidatos()
            opcion == input("Ingrese su opción:")
            if opcion == "a":
                ver_candidatos()
            else:
                cons()        
        elif opcion == "3":
            cons()
        elif opcion == "4":
            cons()
        elif opcion == "0":
            salir = False
        else:
            print("Opción inválida.")
    elif email == usuario2_email and contraseña == usuario2_contraseña:
        print("Bienvenido Usuario 1.")
        menu_completo()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            gestionar_mi_perfil()
            opcion == input("Ingrese su opción:")
            if opcion == "a":
                editar_datos_personales()
            else:
                cons()
        elif opcion == "2":
            gestionar_candidatos()
            opcion == input("Ingrese su opción:")
            if opcion == "a":
                ver_candidatos()
            else:
                cons()        
        elif opcion == "3":
            cons()
        elif opcion == "4":
            cons()
        elif opcion == "0":
            salir = False
        else:
            print("Opción inválida.")
    elif email == usuario3_email and contraseña == usuario3_contraseña:
        print("Bienvenido Usuario 1.")
        menu_completo()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            gestionar_mi_perfil()
            opcion == input("Ingrese su opción:")
            if opcion == "a":
                editar_datos_personales()
            else:
                cons()
        elif opcion == "2":
            gestionar_candidatos()
            opcion == input("Ingrese su opción:")
            if opcion == "a":
                ver_candidatos()
            else:
                cons()        
        elif opcion == "3":
            cons()
        elif opcion == "4":
            cons()
        elif opcion == "0":
            salir = False
        else:
            print("Opción inválida.")
    else:
        intentos -= 1
        print("Email o contraseña incorrectos.")

if intentos == 0:
    print("Ha excedido el número de intentos permitidos. Cerrando el programa.")