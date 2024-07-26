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

MIN_CANT_ESTUDIANTES: int = 4 # enteros
MAX_CANT_ESTUDIANTES: int = 8 # enteros
MIN_CANT_MODERADORES: int = 1 # enteros
MAX_CANT_MODERADORES: int = 4 # enteros
ESTUDIANTES_INDEX: int = 0 # enteros
MODERADORES_INDEX: int = 1 # enteros

## MODELO MODERADOR
# 0 ID: string
# 1 nombre: string
# 2 apellido: string
# 3 email: string
# 4 contraseña: string
# 5 type: string

## MODELO ESTUDIANTE
# 0 ID: string
# 1 nombre: string
# 2 apellido: string
# 3 email: string
# 4 contraseña: string
# 5 fecha de nacimiento: string
# 6 hobbies: string
# 7 me gusta: string
# 8 type: string
# 9 status: string

arreglo_de_estudiantes = [[""]*12 for i in range(8)] # Arreglo multidimensional de 8x8 de strings
arreglo_de_moderadores = [[""]*9 for i in range(4)] # Arreglo multidimensional de 8x4 de strings
arreglo_likes = [[0]*8 for i in range(8)] # Arreglo multidimensional de 8x8 de enteros

arreglo_logged_in = [False]*2 # Arreglo unidimensional de booleanos
arreglo_usuarios_creados = [0]*2 # Arreglo unidimensional de enteros

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

def menu_estudiante(estudiantes_registrados):
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

                for i in range(estudiantes_registrados):
                    if  arreglo_de_estudiantes[i][7] == "iniciado":  # en vez de utilizar la global, usamos un slot del arreglo <------ Miralo nico(borrar) lo mismo para el loggedIn se puede hacer me imagino
                        arreglo_de_estudiantes[i][7] = "no iniciado"

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

def mostrar_menu_de_mis_datos():
    for i in range(estudiantes_registrados):
        if  arreglo_de_estudiantes[i][7] == "iniciado":
            print("\nMi ID: ", arreglo_de_estudiantes[i][0])
            print("Mi nombre: ", arreglo_de_estudiantes[i][1])
            print("Mi apellido: ", arreglo_de_estudiantes[i][2])
            print("Mi fecha de nacimiento: ", arreglo_de_estudiantes[i][8])
            print("Mi biografia: ", arreglo_de_estudiantes[i][9])
            print("Mi edad: ", mostrar_edad(arreglo_de_estudiantes[i][8]), "años")
            print("Mis hobbies: ", arreglo_de_estudiantes[i][10])
            print("Mis me gusta: ", arreglo_de_estudiantes[i][11])
            print("Mi estado: ", arreglo_de_estudiantes[i][2])

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
        print("\nID: ",arreglo_de_estudiantes[i][0])
        print("Nombre: ", arreglo_de_estudiantes[i][1])
        print("Apellido: ", arreglo_de_estudiantes[i][2])
        print("Fecha de nacimiento: ", arreglo_de_estudiantes[i][8])
        print("Biografia: ", arreglo_de_estudiantes[i][9])
        print("Edad: ", mostrar_edad(arreglo_de_estudiantes[i][8]), "años")
        print("Hobbies: ", arreglo_de_estudiantes[i][10])
        print("Me gusta: ", arreglo_de_estudiantes[i][11])
        print("Estado: ", arreglo_de_estudiantes[i][2])

def me_gusta():
    print("\nDar me gusta\n")
    megusta = str(input("Ingresar nombre 0 ID de estudiante: "))
    for i in range(estudiantes_registrados):
        if  arreglo_de_estudiantes[i][7] == "iniciado":
            arreglo_de_estudiantes[i][8] = megusta
            arreglo_likes

def eliminar_mi_perfil():
    print("\nEliminar mi perfil")
    print("Cuidado! Al aceptar se eliminara todo tu perfi!\n")
    print("a. Si, continuar")
    print("b. No. Volver")
    opc = str(input("Ingrese su opción: "))
    while opc != "b" or opc != "a":
        match opc:
            case "a": 
                perfil_eliminado()
    
        os.system("cls")    
        print("\nEliminar mi perfil")
        print("Cuidado! Al aceptar se eliminara todo tu perfi!\n")
        print("a. Si, continuar")
        print("b. No. Volver")
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

def perfil_eliminado():
    for i in range(estudiantes_registrados):
        if  arreglo_de_estudiantes[i][7] == "iniciado":
            arreglo_de_estudiantes[i][1] = "" #nombre
            arreglo_de_estudiantes[i][2] = "" #apellido
            arreglo_de_estudiantes[i][8] = "" #fecha de nacimiento
            arreglo_de_estudiantes[i][9] = "" #bibliografia
            arreglo_de_estudiantes[i][10] = "" #hobbies
            arreglo_de_estudiantes[i][11] = "" #likes
    print("\nPerfil eliminado exitosamente\n")

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

def ver_candidatos():
    print("\nCandidatos\n")
    mostrar_datos()
    print("\n\n\na. Dar me gusta")
    print("\nb. Volver")
    opc = str(input("Ingrese su opción: "))
    while opc != "b":
        match opc:
            case "a":
                me_gusta()
        os.system("cls")
        print("\nCandidatos\n")
        mostrar_datos()
        print("\n\n\na. Dar me gusta")
        print("\nb. Volver")
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

def reportar_candidato():
    print("reportar")

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

def menu_moderadores(arreglo_usuarios_creados, MODERADORES_INDEX):

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
                ingresar_datos_estudiantes(arreglo_usuarios_creados)                
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
        while opc <= 0 and opc > 3:
            print("Opción inválida")
            opc = validar_numero()

def validar_ingreso(arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_logged_in):
    intentos = 3

    print("Inicia sesión\n")
    email = input("Ingrese su email: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    while intentos > 1 and (not arreglo_logged_in[ESTUDIANTES_INDEX] and not arreglo_logged_in[MODERADORES_INDEX]):
        for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
            if ((email == arreglo_de_estudiantes[i][3] and contraseña == arreglo_de_estudiantes[i][4] and arreglo_de_estudiantes[i][9] == "activo")):
                # isLoggedIn = True
                arreglo_logged_in[ESTUDIANTES_INDEX] = True
                print("Sesión iniciada correctamente")
                menu_estudiante(arreglo_usuarios_creados[ESTUDIANTES_INDEX])

        for i in range(arreglo_usuarios_creados[MODERADORES_INDEX]):
            if (email == arreglo_de_moderadores[i][3] and contraseña == arreglo_de_moderadores[i][4]):
                # isLoggedIn = True
                arreglo_logged_in[MODERADORES_INDEX] = True
                print("Sesión iniciada correctamente")
                menu_moderadores(arreglo_usuarios_creados[MODERADORES_INDEX], arreglo_logged_in[MODERADORES_INDEX])

        print( arreglo_logged_in[ESTUDIANTES_INDEX], arreglo_logged_in[MODERADORES_INDEX])
        if(not arreglo_logged_in[ESTUDIANTES_INDEX] and not arreglo_logged_in[MODERADORES_INDEX]):
            print("Email o contraseña incorrectos")
            intentos -= 1
            print("\nQuedan ", intentos, "intentos\n")
            email = input("Ingrese su email: ")
            contraseña = getpass.getpass("Ingrese su contraseña: ")

def ingresar(MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, arreglo_logged_in, arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX):
    if(MIN_CANT_ESTUDIANTES <= arreglo_usuarios_creados[ESTUDIANTES_INDEX] and MIN_CANT_MODERADORES <= arreglo_usuarios_creados[MODERADORES_INDEX]):
        os.system("cls")
        validar_ingreso(arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_logged_in)
    else:
        os.system("cls")
        print("No se puede ingresar, cantidad de estudiantes y moderadores insuficientes")

def ingresar_datos_moderadores(arreglo_usuarios_creados, MODERADORES_INDEX):
    ## MODELO MODERADOR
    # ID
    # nombre
    # apellido
    # email
    # contraseña
    # type

    os.system("cls")
    nombre = input("Ingrese el nombre del moderador: ")
    apellido = input("Ingrese el apellido del moderador: ")
    email = input("Ingrese el email del moderador: ")
    arreglo_de_moderadores[arreglo_usuarios_creados[MODERADORES_INDEX]][0] = str(arreglo_usuarios_creados[MODERADORES_INDEX])
    arreglo_de_moderadores[arreglo_usuarios_creados[MODERADORES_INDEX]][1] = nombre
    arreglo_de_moderadores[arreglo_usuarios_creados[MODERADORES_INDEX]][2] = apellido
    arreglo_de_moderadores[arreglo_usuarios_creados[MODERADORES_INDEX]][3] = email
    arreglo_de_moderadores[arreglo_usuarios_creados[MODERADORES_INDEX]][5] = "moderador"

    contraseña = input("Ingrese su contraseña: ")
    confirmar_contraseña = input("Vuelva a ingresar su contraseña: ")
    while contraseña != confirmar_contraseña:
        print("La contraseña no coincide, vuelva a intentar: ")
        contraseña = input("Ingrese su contraseña: ")
        confirmar_contraseña = input("Vuelva a ingresar su contraseña: ")

    if contraseña == confirmar_contraseña:
        arreglo_de_moderadores[arreglo_usuarios_creados[MODERADORES_INDEX]][4] = contraseña

def ingresar_datos_de_estudiantes(arreglo_usuarios_creados, ESTUDIANTES_INDEX):
    ## MODELO ESTUDIANTE
    # 0 ID
    # 1 nombre
    # 2 apellido
    # 3 email
    # 4 contraseña
    # 5 fecha de nacimiento
    # 6 hobbies
    # 7 me gusta
    # 8 type
    # 9 status
    os.system("cls")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    email = input("Ingrese el email del estudiante: ")
    arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][0] = str(arreglo_usuarios_creados[ESTUDIANTES_INDEX])
    arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][1] = nombre
    arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][2] = apellido
    arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][3] = email
    arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][8] = "estudiante"
    arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][9] = "inactivo"

    contraseña = input("Ingrese su contraseña: ")
    confirmar_contraseña = input("Vuelva a ingresar su contraseña: ")    
    while contraseña != confirmar_contraseña:
        print("La contraseña no coincide, vuelva a intentar: ")
        contraseña = input("Ingrese su contraseña: ")
        confirmar_contraseña = input("Vuelva a ingresar su contraseña: ")

    if contraseña == confirmar_contraseña:
        arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][4] = contraseña

def registrar_estudiante(arreglo_usuarios_creados, MAX_CANT_ESTUDIANTES, ESTUDIANTES_INDEX):
    if (arreglo_usuarios_creados[ESTUDIANTES_INDEX] < MAX_CANT_ESTUDIANTES):
        ingresar_datos_de_estudiantes(arreglo_usuarios_creados, ESTUDIANTES_INDEX)
        os.system("cls")
        arreglo_usuarios_creados[ESTUDIANTES_INDEX] = arreglo_usuarios_creados[ESTUDIANTES_INDEX]+1
        print("Estudiante registrado")
        print(arreglo_de_estudiantes)
    else: 
        print("Todos los estudiantes fueron cargados")
  
def registrar_moderador(arreglo_usuarios_creados, MAX_CANT_MODERADORES, MODERADORES_INDEX):
    if (arreglo_usuarios_creados[MODERADORES_INDEX] < MAX_CANT_MODERADORES):
        ingresar_datos_moderadores(arreglo_usuarios_creados, MODERADORES_INDEX)
        os.system("cls")
        arreglo_usuarios_creados[MODERADORES_INDEX] = arreglo_usuarios_creados[MODERADORES_INDEX]+1
        print("Moderador registrado")
        print(arreglo_de_moderadores)
    else:
        print("Todos los moderadores fueron cargados")

def registrar(MAX_CANT_ESTUDIANTES,MAX_CANT_MODERADORES, arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX):
    os.system("cls")
    mostrar_menu_registrar()

    opc = str(input("Ingrese su opción: "))
    while opc != "c":
        match opc:
            case "a": 
                registrar_estudiante(arreglo_usuarios_creados, MAX_CANT_ESTUDIANTES, ESTUDIANTES_INDEX) # type: ignore            
            case "b": 
                registrar_moderador(arreglo_usuarios_creados, MAX_CANT_MODERADORES, MODERADORES_INDEX) # type: ignore            
        
           
        mostrar_menu_registrar()
        opc = str(input("Ingrese su opción: "))
    
def validar_numero():
    while True:
        try:
            return int(input("Ingrese un número: "))
        except ValueError:
            print("Debe ingresar un número")

def mostrar_menu_registrar():
    print("\nRegistrar usuario\n")
    print(" a. Registrar estudiante")
    print(" b. Registrar moderador")
    print(" c. Volver")

def mostrar_menu_principal():
    #os.system("cls")
    print("\nMenu ")
    print("\n1. Registro")
    print("2. Iniciar sesion")
    print("0. Salir\n")

def ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, arreglo_logged_in,arreglo_usuarios_creados, arreglo_de_estudiantes, arreglo_de_moderadores, ESTUDIANTES_INDEX, MODERADORES_INDEX):
    os.system("cls")
    # print(arreglo_logged_in)
    # print(arreglo_usuarios_creados)
    mostrar_menu_principal()     
    opc = validar_numero()
    while opc < 0 and opc > 4:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                registrar(MAX_CANT_ESTUDIANTES, MAX_CANT_MODERADORES, arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX)
            case 2:
                ingresar(MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, arreglo_logged_in, arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX)
            case 3:
                print("Bonuses")
        
        mostrar_menu_principal()
        opc = validar_numero()
        while opc < 0 and opc > 4:
            print("Opción inválida")
            opc = validar_numero()

    os.system("cls")
    print("\n\nSesión cerrada. ¡Hasta luego!\n\n")
  
ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES,MIN_CANT_MODERADORES,MAX_CANT_MODERADORES,arreglo_logged_in,arreglo_usuarios_creados, arreglo_de_estudiantes, arreglo_de_moderadores, ESTUDIANTES_INDEX, MODERADORES_INDEX)