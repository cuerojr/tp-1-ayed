'''
TP#1 AyED Comisión 113
Rojo Nicolás
Frenna Luca
Giuliano 
Cosenza María Soledad
'''
# Librerias
import os
import getpass
from datetime import datetime
import random

MIN_CANT_ESTUDIANTES = 4
MAX_CANT_ESTUDIANTES = 8
MIN_CANT_MODERADORES = 1
MAX_CANT_MODERADORES = 4

estudiantes_registrados = 0
moderadores_registrados = 0

isLoggedIn = False
arreglo_de_estudiantes = [[""]*12 for i in range(8)] # Arreglo multidimensional de 8x8 de caracteres
arreglo_de_moderadores = [[""]*9 for i in range(4)] # Arreglo multidimensional de 8x4 de caracteres
arreglo_likes = [[0]*8 for i in range(8)] # Arreglo multidimensional de 8x8 de enteros
for i in range(8):
    for j in range(8):
        arreglo_likes[i][j] = random.randint(0, 1) # Populacion aleatoria de likes

def ingresar_datos_estudiantes(estudiantes_registrados):
    print(f"ingresar_datos_estudiantes {estudiantes_registrados}")

def ver_estadisticas():
    print("ver_estadisticas")

def mostrar_menu_estudiante():
    print("Menu ")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

def menu_estudiante():
    global isLoggedIn
    mostrar_menu_estudiante()
    
    opc = validar_numero()
    while opc < 0 and opc > 3:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                gestionar_mi_perfil()
            case 2:
                gestionar_candidatos()
            case 3:
                matcheos()
            case 4:
                reportes_estadisticos()
            case 0:
                print("Sesión cerrada. ¡Hasta luego!")
                isLoggedIn = False
                os.system("cls")
        os.system("cls")
        mostrar_menu_estudiante()
        opc = validar_numero()
        while opc < 0 and opc > 3:
            print("Opción inválida")
            opc = validar_numero()

def gestionar_mi_perfil():    
    os.system("cls")
    print("\nGestionar mi perfil\n")
    print("a. Editar mis datos personales")
    print("b. Eliminar mi perfil")    
    print("c. Volver") 
    opc = str(input("Ingrese su opción: "))

    while opc != "c":
        match opc:
            case "a": 
                editar_mis_datos_personales()
            case "b":
                eliminar_mi_perfil() 
    
        os.system("cls")    
        print("\nGestionar mi perfil\n")
        print("a. Editar mis datos personales")
        print("b. Eliminar mi perfil")    
        print("c. Volver") 
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

def editar_mis_datos_personales():
    os.system("cls")

    mostrar_menu_de_mis_datos()

    print("\nEditar mis datos personales\n")
    print("a. Editar mi fecha de nacimiento")
    print("b. Editar mi biografía")
    print("c. Editar mis hobbies")
    print("d. Volver")  
    opc = str(input("Ingrese su opción: "))

    while opc != "d":
        match opc:    
            case "a": 
                editar_mi_fecha_de_nacimiento()
            case "b":
                editar_mi_biografia()          
            case "c":
                editar_mis_hobbies()  

        os.system("cls")
        mostrar_menu_de_mis_datos()

        print("\nEditar mis datos personales\n")
        print("a. Editar mi fecha de nacimiento")
        print("b. Editar mi biografía")
        print("c. Editar mis hobbies")  
        print("d. Volver")  
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

def editar_mi_fecha_de_nacimiento():
    nueva_fecha_de_nacimiento = str(input("Ingrese su fecha de nacimiento: "))
    for i in range(estudiantes_registrados):
        if  arreglo_de_estudiantes[i][7] == "iniciado":
            arreglo_de_estudiantes[i][8] = nueva_fecha_de_nacimiento
        else:
            print("Error")

def editar_mi_biografia():
    nueva_biografia = str(input("Ingrese su biografia: "))
    for i in range(estudiantes_registrados):
        if  arreglo_de_estudiantes[i][7] == "iniciado":
            arreglo_de_estudiantes[i][9] = nueva_biografia
        else:
            print("Error")

def editar_mis_hobbies():
    nuevos_hobbies = str(input("Ingrese sus hobbies: "))
    for i in range(estudiantes_registrados):
        if  arreglo_de_estudiantes[i][7] == "iniciado":
            arreglo_de_estudiantes[i][10] = nuevos_hobbies
        else:
            print("Error")

def mostrar_edad(fecha):
    fecha_nacimiento = datetime.strptime(fecha, '%Y-%m-%d')
    fecha_actual = datetime.now()
    
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    
    return edad

def mostrar_datos():

    for i in range(estudiantes_registrados):
        print("\nNombre: ", arreglo_de_estudiantes[i][1])
        print("Apellido: ", arreglo_de_estudiantes[i][2])
        print("Fecha de nacimiento: ", arreglo_de_estudiantes[i][8])
        print("Biografia: ", arreglo_de_estudiantes[i][9])
        print("Edad: ", mostrar_edad(arreglo_de_estudiantes[i][8]), "años")
        print("Hobbies: ", arreglo_de_estudiantes[i][10])
        print("Me gusta: ", arreglo_de_estudiantes[i][11])
        print("Estado: ", arreglo_de_estudiantes[i][2])

def me_gusta():
    print("\nDar me gusta\n")
    megusta = str(input("Ingresar nombre de estudiante: "))
    for i in range(estudiantes_registrados):
        if  arreglo_de_estudiantes[i][7] == "iniciado":
            arreglo_de_estudiantes[i][8] = megusta
            arreglo_likes

def gestionar_candidatos():
    os.system("cls")

    print("\nGestionar candidatos\n")
    print("a. Ver candidatos")
    print("b. Reportar candidato")    
    print("c. Volver") 
    opc = str(input("Ingrese su opción: "))

    while opc != "c":
        match opc:
            case "a":
                ver_candidatos()
            case "b":
                reportar_candidato()

        os.system("cls")
        print("\nGestionar candidatos\n")
        print("a. Ver candidatos")
        print("b. Reportar candidato")    
        print("c. Volver") 
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

def matcheos():
    os.system("cls")
    print("\nMatcheos\n")
    print("En contruccion")
    print(" a. Volver")
    opc = str(input("Ingrese su opción: "))

    while opc != "a":
        os.system("cls")
        print("\nMatcheos\n")
        print("En contruccion!\n")
        print("a. Volver")         
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

def reportes_estadisticos():
    os.system("cls")
    print("\nReportes estadísticos\n")
    print("En contruccion")
    print("a. Volver")
    opc = str(input("Ingrese su opción: "))

    while opc != "a":
        os.system("cls")
        print("\nReportes estadísticos\n")
        print("En contruccion")
        print("a. Volver")  
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

def menu_moderadores():
    global isLoggedIn
    print("\nMenu Moderadores\n")
    print("1. Ingresar datos")
    print("2. Ver estadísticas")
    print("0. Salir")
    
    opc = validar_numero()
    while opc < 0 and opc > 3:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                ingresar_datos_estudiantes(estudiantes_registrados)                
            case 2:
                ver_estadisticas()  
            case 0:
                isLoggedIn = False  

        # os.system("cls")
        print("\nMenu Estudiante")
        print("1. Ingresar datos")
        print("2. Ver estadísticas")
        print("0. Salir")
        opc = validar_numero()
        while opc < 0 and opc > 3:
            print("Opción inválida")
            opc = validar_numero()

def validar_ingreso():
    global isLoggedIn
    intentos = 3

    print("Inicia sesión\n")
    email = input("Ingrese su email: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    while isLoggedIn:
        for i in range(estudiantes_registrados):
            if (email == "admin@ayed.com" and contraseña == "admin123" or email == arreglo_de_estudiantes[i][6] and contraseña == arreglo_de_estudiantes[i][6] and arreglo_de_estudiantes[i][5] == "activo"):
                isLoggedIn = True
                arreglo_de_estudiantes[i][7] = "iniciado"
                print("Sesión iniciada correctamente")
                menu_estudiante()
        for i in range(moderadores_registrados):
            if (email == arreglo_de_moderadores[i][5] and contraseña == arreglo_de_moderadores[i][5]):
                isLoggedIn = True
                arreglo_de_moderadores[i][6] = "iniciado"
                print("Sesión iniciada correctamente")
                menu_moderadores()
        print("Email o contraseña incorrectos")
        intentos -= 1
        print("\nQuedan ", intentos, "intentos\n")
        email = input("Ingrese su email: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")

def ingresar(MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, estudiantes_registrados, moderadores_registrados):
    if(MIN_CANT_ESTUDIANTES <= estudiantes_registrados and MIN_CANT_MODERADORES <= moderadores_registrados):
        os.system("cls")
        validar_ingreso()
    else:
        os.system("cls")
        print("No se puede ingresar, cantidad de estudiantes y moderadores insuficientes")

def ingresar_datos_moderadores(moderadores_registrados):
    os.system("cls")
    nombre = input("Ingrese el nombre del moderador: ")
    apellido = input("Ingrese el apellido del moderador: ")
    email = input("Ingrese el email del moderador: ")
    arreglo_de_moderadores[moderadores_registrados][0] = str(moderadores_registrados)
    arreglo_de_moderadores[moderadores_registrados][1] = nombre
    arreglo_de_moderadores[moderadores_registrados][2] = apellido
    arreglo_de_moderadores[moderadores_registrados][3] = email
    arreglo_de_moderadores[moderadores_registrados][4] = "moderador"
    contraseña = input("Ingrese su contraseña: ")
    asegurar_contraseña = input("Vuelva a ingresar su contraseña: ")
    while contraseña != asegurar_contraseña:
        print("La contraseña no coincide, vuelva a intentar: ")
        contraseña = input("Ingrese su contraseña: ")
        asegurar_contraseña = input("Vuelva a ingresar su contraseña: ")
        if contraseña == asegurar_contraseña:
            arreglo_de_moderadores[moderadores_registrados][5] = contraseña
    arreglo_de_moderadores[moderadores_registrados][6] = "no iniciado"

def ingresar_datos_de_estudiantes(estudiantes_registrados):
    os.system("cls")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    email = input("Ingrese el email del estudiante: ")

    arreglo_de_estudiantes[estudiantes_registrados][0] = str(estudiantes_registrados)
    arreglo_de_estudiantes[estudiantes_registrados][1] = nombre
    arreglo_de_estudiantes[estudiantes_registrados][2] = apellido
    arreglo_de_estudiantes[estudiantes_registrados][3] = email
    arreglo_de_estudiantes[estudiantes_registrados][4] = "estudiante"
    arreglo_de_estudiantes[estudiantes_registrados][5] = "inactivo"
    contraseña = input("Ingrese su contraseña: ")
    asegurar_contraseña = input("Vuelva a ingresar su contraseña: ")
    while contraseña != asegurar_contraseña:
        print("La contraseña no coincide, vuelva a intentar: ")
        contraseña = input("Ingrese su contraseña: ")
        asegurar_contraseña = input("Vuelva a ingresar su contraseña: ")
        if contraseña == asegurar_contraseña:
            arreglo_de_estudiantes[estudiantes_registrados][6] = contraseña
    arreglo_de_estudiantes[estudiantes_registrados][7] = "no iniciado"

def registrar_estudiante(estudiantes_registrados, MAX_CANT_ESTUDIANTES):
    if (estudiantes_registrados < MAX_CANT_ESTUDIANTES):
        ingresar_datos_de_estudiantes(estudiantes_registrados)
        os.system("cls")
        estudiantes_registrados = estudiantes_registrados+1
        print("Estudiante registrado")
        print(arreglo_de_estudiantes)
    else: 
        print("Todos los estudiantes fueron cargados")
    
    return estudiantes_registrados

def registrar_moderador(moderadores_registrados, MAX_CANT_MODERADORES):
    if (moderadores_registrados < MAX_CANT_MODERADORES):
        ingresar_datos_moderadores(moderadores_registrados)
        os.system("cls")
        moderadores_registrados = moderadores_registrados+1
        print("Moderador registrado")
        print(arreglo_de_moderadores)
    else:
        print("Todos los moderadores fueron cargados")
    return moderadores_registrados

def registrar(MAX_CANT_ESTUDIANTES,MAX_CANT_MODERADORES,estudiantes_registrados,moderadores_registrados):
    os.system("cls")
    print("\nRegistrar usuario\n")
    print(" a. Registrar estudiante")
    print(" b. Registrar moderador")
    print(" c. Volver")

    opc = str(input("Ingrese su opción: "))
    while opc != "c":
        match opc:
            case "a": 
                estudiantes_registrados = registrar_estudiante(estudiantes_registrados, MAX_CANT_ESTUDIANTES) # type: ignore            
            case "b": 
                moderadores_registrados = registrar_moderador(moderadores_registrados, MAX_CANT_MODERADORES) # type: ignore            
        
           
        print("\nRegistrar usuario")
        print(" a. Registrar estudiante")
        print(" b. Registrar moderador")
        print(" c. Volver")
        opc = str(input("Ingrese su opción: "))
    return estudiantes_registrados, moderadores_registrados

def validar_numero():
    while True:
        try:
            return int(input("Ingrese un número: "))
        except ValueError:
            print("Debe ingresar un número")

def mostrar_menu():
    #os.system("cls")
    print("Menu ")
    print("\n1. Registro")
    print("2. Iniciar sesion")
    print("0. Salir\n")

def ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES,MIN_CANT_MODERADORES,MAX_CANT_MODERADORES,estudiantes_registrados,moderadores_registrados,arreglo_de_estudiantes,arreglo_de_moderadores):
    os.system("cls")
    mostrar_menu()     
    opc = validar_numero()
    while opc < 0 and opc > 3:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                estudiantes_registrados, moderadores_registrados = registrar(MAX_CANT_ESTUDIANTES, MAX_CANT_MODERADORES, estudiantes_registrados,moderadores_registrados)
            case 2:
                ingresar(MIN_CANT_ESTUDIANTES,MIN_CANT_MODERADORES,estudiantes_registrados,moderadores_registrados)
            case 3:
                print("Bonuses")
        
        mostrar_menu()
        opc = validar_numero()
        while opc < 0 and opc > 3:
            print("Opción inválida")
            opc = validar_numero()

    os.system("cls")
    print("\n\nSesión cerrada. ¡Hasta luego!\n\n")
  
ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES,MIN_CANT_MODERADORES,MAX_CANT_MODERADORES,estudiantes_registrados,moderadores_registrados,arreglo_de_estudiantes,arreglo_de_moderadores)