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
option: int
isLoggedIn: bool
email_usuario_autenticado: str
'''
def menu_completo():
    global isLoggedIn, email_usuario_autenticado

    mostrar_menu()

    option = validar_numero()
    while option < 0 and option > 4:
        print("Opción inválida")
        option = validar_numero()

    match option:
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
option: str
'''
def gestionar_mi_perfil():    
    os.system("cls")
    print("\nGestionar mi perfil")
    print(" a. Editar mis datos personales")
    print(" b. Eliminar mi perfil")
    print(" c. Volver")
    option = str(input("Ingrese su opción: "))

    while option  != "c":
        if option == "a": 
            editar_mis_datos_personales() # type: ignore            
        elif option == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. En construccion")

        os.system("cls")    
        print("\nGestionar mi perfil")
        print(" a. Editar mis datos personales")
        print(" b. Eliminar mi perfil")
        print(" c. Volver")
        option = str(input("Ingrese su opción 'a', 'b', 'c': "))

'''
FUN gestionar_candidatos
option: str
'''
def gestionar_candidatos():
    os.system("cls")
    print("\nGestionar candidatos")
    print(" En contruccion")
    print(" c. Volver")
    option = str(input("Ingrese su opción: "))  

    while option != "c":
        if option == "a": 
            #editar_mis_datos_personales() # type: ignore
            print("\n1. en construccion")
        elif option == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. en construccion")      

        os.system("cls")
        print("\nGestionar candidatos")
        print(" En contruccion")
        print(" c. Volver")     
        option = str(input("Ingrese su opción 'a', 'b', 'c': "))

'''
FUN matcheos-
option: str
'''
def matcheos():
    os.system("cls")
    print("\n3. Matcheos")
    print(" En contruccion")
    print(" c. Volver")
    option = str(input("Ingrese su opción 'c': "))

    while option != "c":
        if option == "a": 
            #editar_mis_datos_personales() # type: ignore
            print("\n1. en construccion")
        elif option == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. en construccion")  
        
        os.system("cls")
        print("\n3. Matcheos")
        print(" En contruccion")
        print(" c. Volver")         
        option = str(input("Ingrese su opción 'c': "))

'''
FUN reportes_estadisticos
option: str
'''
def reportes_estadisticos():
    os.system("cls")
    print("\nReportes estadisticos")
    print(" En contruccion")
    print(" c. Volver")
    option = str(input("Ingrese su opción 'c': "))

    while option != "c":
        if option == "a": 
            #editar_mis_datos_personales() # type: ignore
            print("\n1. option c")
        elif option == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. option b") 

        os.system("cls")
        print("\nReportes estadisticos")
        print(" En contruccion")
        print(" c. Volver")  
        option = str(input("Ingrese su opción 'c': "))

'''
FUN editar_mis_datos_personales
option: str
'''       
def editar_mis_datos_personales():
    os.system("cls")

    if (email_usuario_autenticado == usuario1_email):
        mostrar_mis_datos(usuario1_email, usuario1_contraseña, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, usuario1_me_gusta)
    elif (email_usuario_autenticado == usuario2_email):
        mostrar_mis_datos(usuario2_email, usuario2_contraseña, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, usuario2_me_gusta)
    elif (email_usuario_autenticado == usuario3_email):
        mostrar_mis_datos(usuario3_email, usuario3_contraseña, usuario3_fecha_de_nacimiento, usuario3_biografia, usuario3_hobbies, usuario3_me_gusta)

    print("\nEditar mis datos personales")
    print(" a. Editar mi fecha de nacimiento")
    print(" b. Editar mi biografía")
    print(" c. Editar mis hobbies")
    print(" d. Volver")  
    option = str(input("Ingrese su opción: "))

    while option != "d":
        if option == "a": 
            editar_mi_fecha_de_nacimiento()
        elif option == "b":
            editar_mi_biografia()          
        elif option == "c":
            editar_mis_hobbies()  

        os.system("cls")
        print("\nEditar mis datos personales")
        print(" a. Editar mi fecha de nacimiento")
        print(" b. Editar mi biografía")
        print(" c. Editar mis hobbies")  
        print(" d. Volver")  
        option = str(input("Ingrese su opción 'a', 'b', 'c', 'd': "))
    
'''
FUN editar_mi_fecha_de_nacimiento
usuario1_fecha_de_nacimiento, usuario2_fecha_de_nacimiento, usuario3_fecha_de_nacimiento, nueva_fecha_de_nacimiento: str
'''
def editar_mi_fecha_de_nacimiento():
    global usuario1_fecha_de_nacimiento, usuario2_fecha_de_nacimiento, usuario3_fecha_de_nacimiento 

    nueva_fecha_de_nacimiento = str(input("Ingrese su fecha de nacimiento: "))
    if (email_usuario_autenticado == usuario1_email):
        usuario1_fecha_de_nacimiento = nueva_fecha_de_nacimiento
    elif (email_usuario_autenticado == usuario2_email):
        usuario2_fecha_de_nacimiento = nueva_fecha_de_nacimiento
    elif (email_usuario_autenticado == usuario3_email):
        usuario3_fecha_de_nacimiento = nueva_fecha_de_nacimiento
    else:
        print("Error")

'''
FUN editar_mi_biografia
usuario1_biografia, usuario2_biografia, usuario3_biografia, nueva_biografia: str
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
        print("Error")

'''
FUN editar_mis_hobbies
usuario1_hobbies, usuario2_hobbies, usuario3_hobbies, nuevos_hobbies: str
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
FUN mostrar_mis_datos
usuario_email, usuario_contraseña, usuario_fecha_de_nacimiento, usuario_biografia, usuario_hobbies, usuario_me_gusta: str
'''
def mostrar_mis_datos(usuario_email, usuario_contraseña, usuario_fecha_de_nacimiento, usuario_biografia, usuario_hobbies, usuario_me_gusta):
    os.system("cls")
    print("\nEmail: ", usuario_email)
    print("Contraseña: ", usuario_contraseña)
    print("Mi fecha de nacimiento: ", usuario_fecha_de_nacimiento)
    print("Biografia: ", usuario_biografia)
    print("Mis hobbies: ", usuario_hobbies)
    print("Mis me gusta: ", usuario_me_gusta)

def validar_numero():
    while True:
        try:
            return int(input("Ingrese un número: "))
        except ValueError:
            print("Debe ingresar un número")

'''
FUN declarar_constantes
email_usuario_autenticado, usuario1_email, usuario1_biografia, usuario1_hobbies, usuario2_email, usuario2_biografia, usuario2_hobbies, usuario3_email, usuario3_biografia, usuario3_hobbies, usuario1_contraseña, usuario1_me_gusta, usuario1_fecha_de_nacimiento, usuario2_contraseña, usuario2_me_gusta, usuario2_fecha_de_nacimiento, usuario3_contraseña, usuario3_me_gusta, usuario3_fecha_de_nacimiento: str 
intentos_restantes: int
'''
def declarar_constantes():
    global usuario1_email, usuario1_contraseña, usuario1_me_gusta, usuario2_email, usuario2_contraseña, usuario2_me_gusta, usuario3_email, usuario3_me_gusta, usuario3_contraseña, intentos_restantes, email_usuario_autenticado, isLoggedIn, intentos_restantes, email_usuario_autenticado, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, usuario3_fecha_de_nacimiento,usuario3_biografia, usuario3_hobbies, usuario1_nombre, usuario2_nombre, usuario3_nombre

    #Usuario 1 dec vars
    usuario1_email = "111"
    usuario1_contraseña = "222"
    usuario1_me_gusta = ""
    usuario1_fecha_de_nacimiento = ""
    usuario1_nombre = ""
    usuario1_biografia = ""
    usuario1_hobbies = ""

    #Usuario2 decl vars
    usuario2_email = "estudiante2@ayed.com"
    usuario2_contraseña = "333444"
    usuario2_me_gusta = ""
    usuario2_fecha_de_nacimiento = ""
    usuario2_nombre = ""
    usuario2_biografia = ""
    usuario2_hobbies = ""

    #Usuario3 dec vars
    usuario3_email = "estudiante3@ayed.com"
    usuario3_contraseña = "555666"
    usuario3_me_gusta = ""
    usuario3_fecha_de_nacimiento = ""
    usuario3_nombre = ""
    usuario3_biografia = ""
    usuario3_hobbies = ""

    intentos_restantes = 3
    email_usuario_autenticado = ""

'''
FUN iniciar_sesion
email, usuario1_email, usuario2_email, usuario3_email, email_usuario_autenticado, contraseña, usuario1_contraseña, usuario2_contraseña, usuario3_contraseña: str
isLoggedIn: boolean
intentos_restantes: int
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
            print("Inicio de sesión exitoso!")
            print("Bienvenido!")
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