'''
TP#1 AyED Comisión 113
Rojo Nicolás
Frenna Luca
Alegre Sebastian
Cosenza María Soledad
'''
# Librerias
import os
import getpass
from datetime import datetime
import random

def mostrar_menu():
    os.system("cls")
    print("Menu ")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")
    print(arreglo_de_estudiantes)
'''
FUN mostrar_menu_completo
opcion: integer
isLoggedIn: bool
email_usuario_autenticado: str
'''
def mostrar_menu_completo():
    global isLoggedIn, email_usuario_autenticado

    mostrar_menu()
     
    opcion = validar_numero()
    while opcion < 0 and opcion > 4:
        print("Opción inválida")
        opcion = validar_numero()

    match opcion:
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

'''
FUN gestionar_mi_perfil
opcion: str
'''
def gestionar_mi_perfil():    
    os.system("cls")
    print("\nGestionar mi perfil")
    print(" a. Editar mis datos personales")
    print(" c. Volver")
    opcion = str(input("Ingrese su opción: "))

    while opcion != "c":
        match opcion:
            case "a": 
                editar_mis_datos_personales() # type: ignore            
        
        os.system("cls")    
        print("\nGestionar mi perfil")
        print(" a. Editar mis datos personales")
        print(" c. Volver")
        opcion = str(input("Ingrese su opción 'a', 'c': "))

'''
FUN gestionar_candidatos
opcion: str
'''
def gestionar_candidatos():
    os.system("cls")

    print("\nGestionar candidatos")
    print(" a. Elegir candidato para matchear")
    print(" c. Volver")
    opcion = str(input("Ingrese su opción: "))  

    while opcion != "c":
        match opcion:
            case "a":
                ver_candidatos() 

        os.system("cls")
        print("\nGestionar candidatos")
        print(" a. Elegir candidato para matchear")
        print(" c. Volver")     
        opcion = str(input("Ingrese su opción 'a', 'c': "))

'''
FUN matcheos-
opcion: str
'''
def matcheos():
    os.system("cls")
    print("\n3. Matcheos")
    print(" En contruccion")
    print(" c. Volver")
    opcion = str(input("Ingrese su opción 'c': "))

    while opcion != "c":
        match opcion:
            case "a": 
                #editar_mis_datos_personales() # type: ignore
                print("\n1. en construccion")
            case "b":
                #eliminar_mi_perfil() # type: ignore 
                print("\n1. en construccion")  
        
        os.system("cls")
        print("\n3. Matcheos")
        print(" En contruccion")
        print(" c. Volver")         
        opcion = str(input("Ingrese su opción 'c': "))

'''
FUN reportes_estadisticos
opcion: str
'''
def reportes_estadisticos():
    os.system("cls")
    print("\nReportes estadisticos")
    print(" En contruccion")
    print(" c. Volver")
    opcion = str(input("Ingrese su opción 'c': "))

    while opcion != "c":
        match opcion:
            case "a": 
                #editar_mis_datos_personales() # type: ignore
                print("\n1. opcion c")
            case "b":
                #eliminar_mi_perfil() # type: ignore 
                print("\n1. opcion b") 

        os.system("cls")
        print("\nReportes estadisticos")
        print(" En contruccion")
        print(" c. Volver")  
        opcion = str(input("Ingrese su opción 'c': "))

'''
FUN editar_mis_datos_personales
opcion: str
'''       
def editar_mis_datos_personales():
    os.system("cls")

    mostrar_menu_de_mis_datos()

    print("\nEditar mis datos personales")
    print(" a. Editar mi fecha de nacimiento")
    print(" b. Editar mi biografía")
    print(" c. Editar mis hobbies")
    print(" d. Volver")  
    opcion = str(input("Ingrese su opción: "))

    while opcion != "d":
        match opcion:    
            case "a": 
                editar_mi_fecha_de_nacimiento()
            case "b":
                editar_mi_biografia()          
            case "c":
                editar_mis_hobbies()  

        os.system("cls")
        mostrar_menu_de_mis_datos()

        print("\nEditar mis datos personales")
        print(" a. Editar mi fecha de nacimiento")
        print(" b. Editar mi biografía")
        print(" c. Editar mis hobbies")  
        print(" d. Volver")  
        opcion = str(input("Ingrese su opción 'a', 'b', 'c', 'd': "))

'''

'''
def ver_candidatos():
    os.system("cls")

    mostrar_todos_los_candidatos()

    print("\nGestionar candidatos")
    print(" a. Ingresar el nombre del candidato")
    print(" c. Volver")  
    opcion = str(input("Ingrese su opción: "))

    while opcion != "c":
        match opcion:
            case "a": 
                dar_me_gusta_al_candidato()
        
        print("\nGestionar candidatos")
        print(" a. Ingresar el nombre del candidato")
        print(" c. Volver")  
        opcion = str(input("Ingrese su opción 'a', 'c': "))

'''
FUN mostrar_todos_los_candidatos
email_usuario_autenticado, usuario1_email, usuario2_email, usuario3_email, usuario1_nombre, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, usuario2_nombre, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, usuario3_nombre, usuario3_fecha_de_nacimiento, usuario3_biografia, usuario3_hobbies: str
'''
def mostrar_todos_los_candidatos():
    print("Candidatos\n")
    # if email_usuario_autenticado == usuario1_email:
    #     mostrar_datos("", "", usuario2_nombre, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, "")
    #     print("\n")
    #     mostrar_datos("", "", usuario3_nombre, usuario3_fecha_de_nacimiento, usuario3_biografia, usuario3_hobbies, "")
    # elif email_usuario_autenticado == usuario2_email:
    #     mostrar_datos("", "", usuario1_nombre, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, "")
    #     print("\n")
    #     mostrar_datos("", "", usuario3_nombre, usuario3_fecha_de_nacimiento, usuario3_biografia, usuario3_hobbies, "")
    # elif email_usuario_autenticado == usuario3_email:
    #     mostrar_datos("", "", usuario1_nombre, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, "")
    #     print("\n")
    #     mostrar_datos("", "", usuario2_nombre, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, "")

'''
FUN dar_me_gusta_al_candidato
usuario1_me_gusta, usuario2_me_gusta, usuario3_me_gusta, nombre_candidato, email_usuario_autenticado, usuario1_nombre, usuario2_nombre, usuario3_nombre: str
'''
def dar_me_gusta_al_candidato():
    # global usuario1_me_gusta, usuario2_me_gusta, usuario3_me_gusta

    # nombre_candidato = str(input("Ingrese el nombre su candidato: "))
    # while (nombre_candidato != usuario1_nombre and nombre_candidato != usuario2_nombre and nombre_candidato != usuario3_nombre):
    #     print("El nombre del candidato no es válido")
    #     nombre_candidato = str(input("Ingrese un nombre válido: "))
    
    # if email_usuario_autenticado == usuario1_email:
    #     usuario1_me_gusta = nombre_candidato
    # elif email_usuario_autenticado == usuario2_email:
    #     usuario2_me_gusta = nombre_candidato
    # elif email_usuario_autenticado == usuario3_email:
    #     usuario3_me_gusta = nombre_candidato
    
    os.system("cls")

'''
FUN mostrar_menu_de_mis_datos()
usuario1_email, usuario1_contraseña, usuario1_nombre, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, usuario1_me_gusta, usuario2_email, usuario2_contraseña, usuario2_nombre, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, usuario2_me_gusta, email_usuario_autenticado, usuario3_email, usuario3_contraseña, usuario3_nombre, usuario3_fecha_de_nacimiento, usuario3_biografia, usuario3_hobbies, usuario3_me_gusta: str
''' 
def mostrar_menu_de_mis_datos():
    os.system("cls")
    # print("Mis datos personales")
    # if (email_usuario_autenticado == usuario1_email):
    #     mostrar_datos(usuario1_email, usuario1_contraseña, usuario1_nombre, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, usuario1_me_gusta)
    # elif (email_usuario_autenticado == usuario2_email):
    #     mostrar_datos(usuario2_email, usuario2_contraseña, usuario2_nombre, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, usuario2_me_gusta)
    # elif (email_usuario_autenticado == usuario3_email):
    #     mostrar_datos(usuario3_email, usuario3_contraseña, usuario3_nombre, usuario3_fecha_de_nacimiento, usuario3_biografia, usuario3_hobbies, usuario3_me_gusta)

'''
FUN editar_mi_fecha_de_nacimiento
usuario1_fecha_de_nacimiento, usuario2_fecha_de_nacimiento, usuario3_fecha_de_nacimiento, nueva_fecha_de_nacimiento: str
'''
def editar_mi_fecha_de_nacimiento():
    global usuario1_fecha_de_nacimiento, usuario2_fecha_de_nacimiento, usuario3_fecha_de_nacimiento 

    # nueva_fecha_de_nacimiento = str(input("Ingrese su fecha de nacimiento: "))
    # if (email_usuario_autenticado == usuario1_email):
    #     usuario1_fecha_de_nacimiento = nueva_fecha_de_nacimiento
    # elif (email_usuario_autenticado == usuario2_email):
    #     usuario2_fecha_de_nacimiento = nueva_fecha_de_nacimiento
    # elif (email_usuario_autenticado == usuario3_email):
    #     usuario3_fecha_de_nacimiento = nueva_fecha_de_nacimiento
    # else:
    #     print("Error")

'''
FUN editar_mi_biografia
usuario1_biografia, usuario2_biografia, usuario3_biografia, nueva_biografia: str
'''
def editar_mi_biografia():
    global usuario1_biografia, usuario2_biografia, usuario3_biografia

    # nueva_biografia = str(input("Ingrese su biografia: "))
    # if (email_usuario_autenticado == usuario1_email):
    #     usuario1_biografia = nueva_biografia
    # elif (email_usuario_autenticado == usuario2_email):
    #     usuario2_biografia = nueva_biografia
    # elif (email_usuario_autenticado == usuario3_email):
    #     usuario3_biografia = nueva_biografia
    # else:
    #     print("El ususario no existe")

'''
FUN editar_mis_hobbies
usuario1_hobbies, usuario2_hobbies, usuario3_hobbies, nuevos_hobbies: str
'''
def editar_mis_hobbies():
    global usuario1_hobbies, usuario2_hobbies, usuario3_hobbies

    # nuevos_hobbies = str(input("Ingrese sus hobbies: "))
    # if (email_usuario_autenticado == usuario1_email):
    #     usuario1_hobbies = nuevos_hobbies
    # elif (email_usuario_autenticado == usuario2_email):
    #     usuario2_hobbies = nuevos_hobbies
    # elif (email_usuario_autenticado == usuario3_email):
    #     usuario3_hobbies = nuevos_hobbies
    # else:
    #     print("Error")

'''
FUN mostrar_edad
fecha_nacimiento, fecha_actual: date
edad: int
'''
def mostrar_edad(fecha):
    fecha_nacimiento = datetime.strptime(fecha, '%Y-%m-%d')   #dudoso 
    fecha_actual = datetime.now()
    
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    
    return edad

'''
FUN mostrar_datos
usuario_email, usuario_contraseña, usuario_nombre, usuario_fecha_de_nacimiento, usuario_biografia, usuario_hobbies, usuario_me_gusta: str
'''
def mostrar_datos(usuario_email, usuario_contraseña, usuario_nombre, usuario_fecha_de_nacimiento, usuario_biografia, usuario_hobbies, usuario_me_gusta):
    
    if(usuario_email):
        print("\nEmail: ", usuario_email)
    if(usuario_contraseña):
        print("Contraseña: ", usuario_contraseña)
    if(usuario_nombre):   
        print("Nombre: ", usuario_nombre)
    if(usuario_fecha_de_nacimiento):   
        print("Fecha de nacimiento: ", usuario_fecha_de_nacimiento)
    if(usuario_biografia):   
        print("Biografia: ", usuario_biografia)
    if(usuario_fecha_de_nacimiento):   
        print("Edad: ", mostrar_edad(usuario_fecha_de_nacimiento), "años")
    if(usuario_hobbies):   
        print("Hobbies: ", usuario_hobbies)
    if(usuario_me_gusta):   
        print("Me gusta: ", usuario_me_gusta)
    

def validar_numero():
    while True:
        try:
            return int(input("Ingrese un número: "))
        except ValueError:
            print("Debe ingresar un número")

def popular_likes():
    global arreglo_multidemensional
    for i in range(8):
        for j in range(8):
            arreglo_multidemensional[i][j] = random.randint(0, 1)
'''
FUN declarar_constantes
email_usuario_autenticado, usuario1_email, usuario1_biografia, usuario1_hobbies, usuario2_email, usuario2_biografia, usuario2_hobbies, usuario3_email, usuario3_biografia, usuario3_hobbies, usuario1_contraseña, usuario1_nombre, usuario1_me_gusta,  usuario2_contraseña, usuario2_nombre, usuario2_me_gusta, usuario2_fecha_de_nacimiento, , usuario3_nombre, usuario3_me_gusta, usuario3_fecha_de_nacimiento: str 
intentos_restantes: integer
'''
def declarar_constantes():
    global  intentos_restantes, email_usuario_autenticado, isLoggedIn, arreglo_unidimensional, arreglo_bidimensional, arreglo_multidemensional, arreglo_de_estudiantes, tipo_usuario_autenticado, MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, estudiantesRegistrados, moderadoresRegistrados

    MIN_CANT_ESTUDIANTES = 4
    MAX_CANT_ESTUDIANTES = 8

    MIN_CANT_MODERADORES = 1
    MAX_CANT_MODERADORES = 4

    estudiantesRegistrados = 0
    moderadoresRegistrados = 0

    isLoggedIn = False
    arreglo_unidimensional = [0]*8 # Arreglo unidimensional de 0 a 7 de enteros
    arreglo_bidimensional = [[0]*8 for i in range(2)] # Arreglo bidimensional de 8x2 de enteros
    arreglo_multidemensional = [[0]*8 for i in range(8)] # Arreglo multidimensionl de 8x8 de enteros
    arreglo_de_estudiantes = [[""]*8 for i in range(8)] # Arreglo multidimensionl de 8x8 de caracteres
    arreglo_de_moderadores = [[""]*8 for i in range(4)] # Arreglo multidimensionl de 8x4 de caracteres

    #Usuario 1 dec vars
    arreglo_de_estudiantes[0][0] = "111"
    arreglo_de_estudiantes[0][1] = "222"
    arreglo_de_estudiantes[0][2] = "activo"
    arreglo_de_estudiantes[0][3] = "1985-02-25"
    arreglo_de_estudiantes[0][4] = "Carlos"
    arreglo_de_estudiantes[0][5] = "Nacido en Rosario"
    arreglo_de_estudiantes[0][6] = "tocar la guitarra y correr"
    arreglo_de_estudiantes[0][7] = "estudiante"

    #Usuario2 decl vars
    arreglo_de_estudiantes[1][0] = "estudiante2@ayed.com"
    arreglo_de_estudiantes[1][1] = "333444"
    arreglo_de_estudiantes[1][2] = "activo"
    arreglo_de_estudiantes[1][3] = "2001-12-06"
    arreglo_de_estudiantes[1][4] = "Ramiro"
    arreglo_de_estudiantes[1][5] = "Nacido en Misiones"
    arreglo_de_estudiantes[1][6] = "Dibujar y pintar"
    arreglo_de_estudiantes[1][7] = "estudiante"

    #Usuario3 dec vars
    arreglo_de_estudiantes[2][0] = "estudiante3@ayed.com"
    arreglo_de_estudiantes[2][1] = "555666"
    arreglo_de_estudiantes[2][2] = "activo"
    arreglo_de_estudiantes[2][3] = "1993-05-25"
    arreglo_de_estudiantes[2][4] = "Sandra"
    arreglo_de_estudiantes[2][5] = "Nacida en San Francisco"
    arreglo_de_estudiantes[2][6] = "Cocinar y cantar en el coro"
    arreglo_de_estudiantes[2][7] = "estudiante"

    #Usuario4 dec vars
    arreglo_de_estudiantes[3][0] = "estudiante4@ayed.com"
    arreglo_de_estudiantes[3][1] = "777888"
    arreglo_de_estudiantes[3][2] = "inactivo"
    arreglo_de_estudiantes[3][3] = "2000-08-03"
    arreglo_de_estudiantes[3][4] = "Pedro"
    arreglo_de_estudiantes[3][5] = "Nacida en San Fernando"
    arreglo_de_estudiantes[3][6] = "Cocinar y cantar en el coro"
    arreglo_de_estudiantes[3][7] = "estudiante"

    #Moderador1 dec vars
    arreglo_de_moderadores[0][0] = "mod1@ayed.com"
    arreglo_de_moderadores[0][1] = "111222"
    arreglo_de_moderadores[0][2] = "activo"
    arreglo_de_moderadores[0][3] = "2002-12-08"
    arreglo_de_moderadores[0][4] = "Román"
    arreglo_de_moderadores[0][5] = "Nacida en Rosario"
    arreglo_de_moderadores[0][6] = "Viajar"
    arreglo_de_moderadores[0][7] = "moderador"

    intentos_restantes = 3
    email_usuario_autenticado = ""
    tipo_usuario_autenticado = ""
    
    popular_likes()
    
    print(arreglo_de_moderadores)

'''
FUN iniciar_sesion
email, usuario1_email, usuario2_email, usuario3_email, email_usuario_autenticado, contraseña, usuario1_contraseña, usuario2_contraseña, usuario3_contraseña: str
isLoggedIn: boolean
intentos_restantes: integer
'''
def iniciar_sesion():    
    global isLoggedIn, intentos_restantes, email_usuario_autenticado, tipo_usuario_autenticado 
    declarar_constantes()    
    
    while intentos_restantes > 0 and not email_usuario_autenticado:
        print("\nLog In")
        email = input("Ingrese su email: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        
        for i in range(5):
            if (email == arreglo_de_estudiantes[i][0] and contraseña == arreglo_de_estudiantes[i][1] and arreglo_de_estudiantes[i][2] == "activo"):
                os.system("cls")                
                email_usuario_autenticado = email
                isLoggedIn = True
                tipo_usuario_autenticado = arreglo_de_estudiantes[i][7]

        intentos_restantes -= 1
        print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")

'''
FUN ejecutar_sistema_principal
email_usuario_autenticado: string
isLoggedIn: boolean
'''
def ejecutar_sistema_principal():    
    iniciar_sesion()    
    while email_usuario_autenticado and isLoggedIn:            
        mostrar_menu_completo()
            
ejecutar_sistema_principal()