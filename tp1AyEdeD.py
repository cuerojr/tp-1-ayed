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

def mostrar_menu():
    os.system("cls")
    print("Menu ")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

'''
FUN menu_completo
opcion: integer
isLoggedIn: boolean
'''
def menu_completo():
    global isLoggedIn

    mostrar_menu()

    opcion = validar_numero("Ingrese un número: ")
    while opcion < 0 or opcion > 4:
        print("Opción inválida")
        opcion = validar_numero("Ingrese un número: ")

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
opcion: string
'''
def gestionar_mi_perfil():    
    os.system("cls")
    print("\nGestionar mi perfil")
    print(" a. Editar mis datos personales")
    print(" c. Volver")
    opcion = str(input("Ingrese su opción: "))

    while opcion != "c":
        if opcion == "a": 
            editar_mis_datos_personales() # type: ignore            
        
        os.system("cls")    
        print("\nGestionar mi perfil")
        print(" a. Editar mis datos personales")
        print(" c. Volver")
        opcion = str(input("Ingrese su opción 'a', 'c': "))

'''
FUN gestionar_candidatos
opcion: string
'''
def gestionar_candidatos():
    os.system("cls")

    print("\nGestionar candidatos")
    print(" a. Elegir candidato para matchear")
    print(" c. Volver")
    opcion = str(input("Ingrese su opción: "))  

    while opcion != "c":
        if opcion == "a":
            ver_candidatos() 

        os.system("cls")
        print("\nGestionar candidatos")
        print(" a. Elegir candidato para matchear")
        print(" c. Volver")     
        opcion = str(input("Ingrese su opción 'a', 'c': "))

'''
FUN matcheos
opcion: string
'''
def matcheos():
    os.system("cls")
    print("\n3. Matcheos")
    print(" En construcción")
    print(" c. Volver")
    opcion = str(input("Ingrese su opción 'c': "))

    while opcion != "c":
        if opcion == "a": 
            #editar_mis_datos_personales() # type: ignore
            print("\n1. en construccion")
        elif opcion == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. en construccion")  
        
        os.system("cls")
        print("\n3. Matcheos")
        print(" En construcción")
        print(" c. Volver")         
        opcion = str(input("Ingrese su opción 'c': "))

'''
FUN reportes_estadisticos
opcion: string
'''
def reportes_estadisticos():
    os.system("cls")
    print("\nReportes estadisticos")
    print(" En construcción")
    print(" c. Volver")
    opcion = str(input("Ingrese su opción 'c': "))

    while opcion != "c":
        if opcion == "a": 
            #editar_mis_datos_personales() # type: ignore
            print("\n1. opcion c")
        elif opcion == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. opcion b") 

        os.system("cls")
        print("\nReportes estadisticos")
        print(" En construcción")
        print(" c. Volver")  
        opcion = str(input("Ingrese su opción 'c': "))

'''
FUN editar_mis_datos_personales
opcion: string
'''       
def editar_mis_datos_personales():
    os.system("cls")

    menu_de_mis_datos()

    print("\nEditar mis datos personales")
    print(" a. Editar mi fecha de nacimiento")
    print(" b. Editar mi biografía")
    print(" c. Editar mis hobbies")
    print(" d. Volver")  
    opcion = str(input("Ingrese su opción: "))

    while opcion != "d":
        if opcion == "a": 
            editar_mi_fecha_de_nacimiento()
        elif opcion == "b":
            editar_mi_biografia()          
        elif opcion == "c":
            editar_mis_hobbies()  

        os.system("cls")
        menu_de_mis_datos()

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
        if opcion == "a": 
            dar_me_gusta_al_candidato()
        
        print("\nGestionar candidatos")
        print(" a. Ingresar el nombre del candidato")
        print(" c. Volver")  
        opcion = str(input("Ingrese su opción 'a', 'c': "))

'''
FUN mostrar_todos_los_candidatos
email_usuario_autenticado, usuario1_email, usuario2_email, usuario3_email, usuario1_nombre, usuario1_biografia, usuario1_hobbies, usuario2_nombre, usuario2_biografia, usuario2_hobbies, usuario3_nombre, usuario3_biografia, usuario3_hobbies, campo_vacio: string
usuario2_año_de_nacimiento, usuario2_mes_de_nacimiento, usuario2_dia_de_nacimiento, usuario3_año_de_nacimiento, usuario3_mes_de_nacimiento, usuario3_dia_de_nacimiento, usuario1_año_de_nacimiento, usuario1_mes_de_nacimiento, usuario1_dia_de_nacimiento: integer
'''
def mostrar_todos_los_candidatos():
    campo_vacio = ""
    print("Candidatos\n")
    if email_usuario_autenticado == usuario1_email:
        mostrar_datos(campo_vacio, campo_vacio, usuario2_nombre, usuario2_año_de_nacimiento, usuario2_mes_de_nacimiento, usuario2_dia_de_nacimiento,usuario2_biografia, usuario2_hobbies, campo_vacio)
        print("\n")
        mostrar_datos(campo_vacio, campo_vacio, usuario3_nombre, usuario3_año_de_nacimiento, usuario3_mes_de_nacimiento, usuario3_dia_de_nacimiento, usuario3_biografia, usuario3_hobbies, campo_vacio)
    elif email_usuario_autenticado == usuario2_email:
        mostrar_datos(campo_vacio, campo_vacio, usuario1_nombre, usuario1_año_de_nacimiento, usuario1_mes_de_nacimiento, usuario1_dia_de_nacimiento, usuario1_biografia, usuario1_hobbies, campo_vacio)
        print("\n")
        mostrar_datos(campo_vacio, campo_vacio, usuario3_nombre, usuario3_año_de_nacimiento, usuario3_mes_de_nacimiento, usuario3_dia_de_nacimiento, usuario3_biografia, usuario3_hobbies, campo_vacio)
    elif email_usuario_autenticado == usuario3_email:
        mostrar_datos(campo_vacio, campo_vacio, usuario1_nombre, usuario1_año_de_nacimiento, usuario1_mes_de_nacimiento, usuario1_dia_de_nacimiento, usuario1_biografia, usuario1_hobbies, campo_vacio)
        print("\n")
        mostrar_datos(campo_vacio, campo_vacio, usuario2_nombre, usuario2_año_de_nacimiento, usuario2_mes_de_nacimiento, usuario2_dia_de_nacimiento,usuario2_biografia, usuario2_hobbies, campo_vacio)

'''
FUN dar_me_gusta_al_candidato
usuario1_me_gusta, usuario2_me_gusta, usuario3_me_gusta, nombre_candidato, email_usuario_autenticado, usuario1_nombre, usuario2_nombre, usuario3_nombre: string
'''
def dar_me_gusta_al_candidato():
    global usuario1_me_gusta, usuario2_me_gusta, usuario3_me_gusta

    nombre_candidato = str(input("Ingrese el nombre su candidato: "))
    while (nombre_candidato != usuario1_nombre and nombre_candidato != usuario2_nombre and nombre_candidato != usuario3_nombre):
        print("El nombre del candidato no es válido")
        nombre_candidato = str(input("Ingrese un nombre válido: "))
    
    if email_usuario_autenticado == usuario1_email:
        usuario1_me_gusta = nombre_candidato
    elif email_usuario_autenticado == usuario2_email:
        usuario2_me_gusta = nombre_candidato
    elif email_usuario_autenticado == usuario3_email:
        usuario3_me_gusta = nombre_candidato
    
    print("El candidato ha sido seleccionado correctamente")

'''
FUN menu_de_mis_datos()
usuario1_email, usuario1_contraseña, usuario1_nombre, usuario1_biografia, usuario1_hobbies, usuario1_me_gusta, usuario2_email, usuario2_contraseña, usuario2_nombre, usuario2_biografia, usuario2_hobbies, usuario2_me_gusta, email_usuario_autenticado, usuario3_email, usuario3_contraseña, usuario3_nombre, usuario3_biografia, usuario3_hobbies, usuario3_me_gusta: string
usuario1_año_de_nacimiento, usuario1_mes_de_nacimiento, usuario1_dia_de_nacimiento, usuario2_año_de_nacimiento, usuario2_mes_de_nacimiento, usuario2_dia_de_nacimiento,  usuario3_año_de_nacimiento, usuario3_mes_de_nacimiento, usuario3_dia_de_nacimiento: integer
''' 
def menu_de_mis_datos():
    os.system("cls")
    print("Mis datos personales")
    if (email_usuario_autenticado == usuario1_email):
        mostrar_datos(usuario1_email, usuario1_contraseña, usuario1_nombre, usuario1_año_de_nacimiento, usuario1_mes_de_nacimiento, usuario1_dia_de_nacimiento, usuario1_biografia, usuario1_hobbies, usuario1_me_gusta)
    elif (email_usuario_autenticado == usuario2_email):
        mostrar_datos(usuario2_email, usuario2_contraseña, usuario2_nombre, usuario2_año_de_nacimiento, usuario2_mes_de_nacimiento, usuario2_dia_de_nacimiento, usuario2_biografia, usuario2_hobbies, usuario2_me_gusta)
    elif (email_usuario_autenticado == usuario3_email):
        mostrar_datos(usuario3_email, usuario3_contraseña, usuario3_nombre, usuario3_año_de_nacimiento, usuario3_mes_de_nacimiento, usuario3_dia_de_nacimiento, usuario3_mes_de_nacimiento, usuario3_dia_de_nacimiento, usuario3_biografia, usuario3_hobbies, usuario3_me_gusta)

'''
FUN editar_mi_fecha_de_nacimiento
usuario1_año_de_nacimiento, usuario1_mes_de_nacimiento, usuario1_dia_de_nacimiento, usuario2_año_de_nacimiento, usuario2_mes_de_nacimiento, usuario2_dia_de_nacimiento, usuario3_año_de_nacimiento, usuario3_mes_de_nacimiento, usuario3_dia_de_nacimiento, nuevo_año_de_nacimiento, nuevo_mes_de_nacimiento, nuevo_dia_de_nacimiento: int
'''
def editar_mi_fecha_de_nacimiento():
    global usuario1_año_de_nacimiento, usuario1_mes_de_nacimiento, usuario1_dia_de_nacimiento, usuario2_año_de_nacimiento, usuario2_mes_de_nacimiento, usuario2_dia_de_nacimiento, usuario3_año_de_nacimiento, usuario3_mes_de_nacimiento, usuario3_dia_de_nacimiento

    nuevo_año_de_nacimiento = validar_numero("Ingrese su año de nacimiento: ")
    while nuevo_año_de_nacimiento < 1900 or nuevo_año_de_nacimiento >= 2024:
        print("El año de nacimiento no es válido")
        nuevo_año_de_nacimiento = validar_numero("Ingrese su año de nacimiento: ")

    nuevo_mes_de_nacimiento = validar_numero("Ingrese su mes de nacimiento: ")
    while nuevo_mes_de_nacimiento <= 0 or nuevo_mes_de_nacimiento > 12:
        print("El mes de nacimiento no es válido")
        nuevo_mes_de_nacimiento = validar_numero("Ingrese su mes de nacimiento: ")

    nuevo_dia_de_nacimiento = validar_numero("Ingrese su dia de nacimiento: ")
    while nuevo_dia_de_nacimiento <= 0 or nuevo_dia_de_nacimiento > 31:
        print("El dia de nacimiento no es válido")
        nuevo_dia_de_nacimiento = validar_numero("Ingrese su dia de nacimiento: ")

    if (email_usuario_autenticado == usuario1_email):
        usuario1_año_de_nacimiento = nuevo_año_de_nacimiento
        usuario1_mes_de_nacimiento = nuevo_mes_de_nacimiento
        usuario1_dia_de_nacimiento = nuevo_dia_de_nacimiento
    elif (email_usuario_autenticado == usuario2_email):
        usuario2_año_de_nacimiento = nuevo_año_de_nacimiento
        usuario2_mes_de_nacimiento = nuevo_mes_de_nacimiento
        usuario2_dia_de_nacimiento = nuevo_dia_de_nacimiento
    elif (email_usuario_autenticado == usuario3_email):
        usuario3_año_de_nacimiento = nuevo_año_de_nacimiento
        usuario3_mes_de_nacimiento = nuevo_mes_de_nacimiento
        usuario3_dia_de_nacimiento = nuevo_dia_de_nacimiento

'''
FUN editar_mi_biografia
usuario1_biografia, usuario2_biografia, usuario3_biografia, nueva_biografia: string
'''
def editar_mi_biografia():
    global usuario1_biografia, usuario2_biografia, usuario3_biografia

    nueva_biografia = str(input("Ingrese su biografia: "))
    if (email_usuario_autenticado == usuario1_email):
        usuario1_biografia = nueva_biografia
    elif (email_usuario_autenticado == usuario2_email):
        usuario2_biografia = nueva_biografia
    elif (email_usuario_autenticado == usuario3_email):
        usuario3_biografia = nueva_biografia
    else:
        print("El ususario no existe")

'''
FUN editar_mis_hobbies
usuario1_hobbies, usuario2_hobbies, usuario3_hobbies, nuevos_hobbies: string
'''
def editar_mis_hobbies():
    global usuario1_hobbies, usuario2_hobbies, usuario3_hobbies

    nuevos_hobbies = str(input("Ingrese sus hobbies: "))
    if (email_usuario_autenticado == usuario1_email):
        usuario1_hobbies = nuevos_hobbies
    elif (email_usuario_autenticado == usuario2_email):
        usuario2_hobbies = nuevos_hobbies
    elif (email_usuario_autenticado == usuario3_email):
        usuario3_hobbies = nuevos_hobbies
    else:
        print("Error")

'''
FUN mostrar_edad
fecha_actual: date
usuario_año_de_nacimiento, usuario_mes_nacimiento, usuario_dia_nacimiento, edad: int
'''
def mostrar_edad(usuario_año_de_nacimiento, usuario_mes_nacimiento, usuario_dia_nacimiento):    
    fecha_actual = datetime.now()    
    edad = fecha_actual.year - usuario_año_de_nacimiento
    if (fecha_actual.month, fecha_actual.day) < (usuario_mes_nacimiento, usuario_dia_nacimiento):
        edad -= 1
    
    return edad

'''
FUN mostrar_datos
usuario_email, usuario_contraseña, usuario_nombre, usuario_biografia, usuario_hobbies, usuario_me_gusta: string
usuario_año_de_nacimiento, usuario_mes_nacimiento, usuario_dia_nacimiento: integer
'''
def mostrar_datos(usuario_email, usuario_contraseña, usuario_nombre, usuario_año_de_nacimiento, usuario_mes_de_nacimiento, usuario_dia_de_nacimiento, usuario_biografia, usuario_hobbies, usuario_me_gusta):
    
    if(usuario_email):
        print("\nEmail: ", usuario_email)
    if(usuario_contraseña):
        print("Contraseña: ", usuario_contraseña)
    if(usuario_nombre):   
        print("Nombre: ", usuario_nombre)
    if(usuario_año_de_nacimiento and usuario_mes_de_nacimiento and usuario_dia_de_nacimiento):   
        print("Fecha de nacimiento: ", f"{usuario_año_de_nacimiento}-{usuario_mes_de_nacimiento}-{usuario_dia_de_nacimiento}")
    if(usuario_biografia):   
        print("Biografia: ", usuario_biografia)
    if(usuario_año_de_nacimiento and usuario_mes_de_nacimiento and usuario_dia_de_nacimiento):   
        print("Edad: ", mostrar_edad(usuario_año_de_nacimiento, usuario_mes_de_nacimiento, usuario_dia_de_nacimiento), "años")
    if(usuario_hobbies):   
        print("Hobbies: ", usuario_hobbies)
    if(usuario_me_gusta):   
        print("Me gusta: ", usuario_me_gusta)

'''
FUN validar_numero
mensaje: string
'''
def validar_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número")

'''
FUN declarar_constantes
email_usuario_autenticado, usuario1_email, usuario1_biografia, usuario1_hobbies, usuario2_email, usuario2_biografia, usuario2_hobbies, usuario3_email, usuario3_biografia, usuario3_hobbies, usuario1_contraseña, usuario1_nombre, usuario1_me_gusta, usuario1_fecha_de_nacimiento, usuario2_contraseña, usuario2_nombre, usuario2_me_gusta, usuario2_fecha_de_nacimiento, usuario3_contraseña, usuario3_nombre, usuario3_me_gusta, usuario3_fecha_de_nacimiento: string 
intentos_restantes, usuario1_año_de_nacimiento, usuario1_mes_de_nacimiento, usuario1_dia_de_nacimiento, usuario2_año_de_nacimiento, usuario2_mes_de_nacimiento, usuario2_dia_de_nacimiento, usuario3_año_de_nacimiento, usuario3_mes_de_nacimiento, usuario3_dia_de_nacimiento: integer
isLoggedIn: boolean
'''
def declarar_constantes():
    global usuario1_email, usuario1_contraseña, usuario1_nombre, usuario1_me_gusta, usuario2_email, usuario2_contraseña, usuario2_nombre, usuario2_me_gusta, usuario3_email, usuario3_me_gusta, usuario3_contraseña, usuario3_nombre, intentos_restantes, isLoggedIn, intentos_restantes, email_usuario_autenticado,  usuario1_biografia, usuario1_hobbies, usuario2_biografia, usuario2_hobbies, usuario3_biografia, usuario3_hobbies, usuario1_año_de_nacimiento, usuario1_mes_de_nacimiento, usuario1_dia_de_nacimiento, usuario2_año_de_nacimiento, usuario2_mes_de_nacimiento, usuario2_dia_de_nacimiento, usuario3_año_de_nacimiento, usuario3_mes_de_nacimiento, usuario3_dia_de_nacimiento

    #Usuario 1 dec vars
    usuario1_email = "estudiante1@ayed.com"
    usuario1_contraseña = "111222"
    usuario1_me_gusta = ""
    usuario1_nombre = "Carlos"
    usuario1_biografia = "Nacido en Rosario"
    usuario1_hobbies = "tocar la guitarra y correr"
    usuario1_año_de_nacimiento  = 1985
    usuario1_mes_de_nacimiento  = 2
    usuario1_dia_de_nacimiento  = 25

    #Usuario2 decl vars
    usuario2_email = "estudiante2@ayed.com"
    usuario2_contraseña = "333444"
    usuario2_me_gusta = ""
    usuario2_nombre = "Ramiro"
    usuario2_biografia = "Nacido en Misiones"
    usuario2_hobbies = "Dibujar y pintar"
    usuario2_año_de_nacimiento = 2001
    usuario2_mes_de_nacimiento = 12
    usuario2_dia_de_nacimiento = 6

    #Usuario3 dec vars
    usuario3_email = "estudiante3@ayed.com"
    usuario3_contraseña = "555666"
    usuario3_me_gusta = ""
    usuario3_nombre = "Sandra"
    usuario3_biografia = "Nacida en San Francisco"
    usuario3_hobbies = "Cocinar y cantar en el coro"
    usuario3_año_de_nacimiento = 1993
    usuario3_mes_de_nacimiento = 5
    usuario3_dia_de_nacimiento = 25

    intentos_restantes = 3
    email_usuario_autenticado = ""

'''
FUN iniciar_sesion
email, usuario1_email, usuario2_email, usuario3_email, email_usuario_autenticado, contraseña, usuario1_contraseña, usuario2_contraseña, usuario3_contraseña: string
isLoggedIn: boolean
intentos_restantes: integer
'''
def iniciar_sesion():    
    global isLoggedIn, intentos_restantes, email_usuario_autenticado
    declarar_constantes()    
    
    while intentos_restantes > 0 and not email_usuario_autenticado:
        print("\nLog In")
        email = input("Ingrese su email: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        
        if (email == usuario1_email and contraseña == usuario1_contraseña) or (email == usuario2_email and contraseña == usuario2_contraseña) or (email == usuario3_email and contraseña == usuario3_contraseña):
            os.system("cls")
            email_usuario_autenticado = email
            isLoggedIn = True
        else:
            intentos_restantes -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")

'''
FUN main
email_usuario_autenticado: string
isLoggedIn: boolean
'''
def main():    
    iniciar_sesion()    
    while email_usuario_autenticado and isLoggedIn:        
        menu_completo()
            
main()