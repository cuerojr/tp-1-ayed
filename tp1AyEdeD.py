def mostrar_menu():
    os.system("cls")
    print("Menu ")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

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

def gestionar_mi_perfil():    
    os.system("cls")

    print("\nGestionar mi perfil")
    print(" a. Editar mis datos personales")
    print(" b. Eliminar mi perfil")
    print(" c. Volver")

    option = input("Ingrese su opción: ")
    while option  != "c":
        if option == "a": 
            editar_mis_datos_personales() # type: ignore            
        elif option == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. En construccion")
        option = input("Ingrese su opción 'a', 'b', 'c': ")


def gestionar_candidatos():
    os.system("cls")

    print("\nGestionar candidatos")
    print(" En contruccion")
    print(" c. Volver")

    option = input("Ingrese su opción: ")    
    while option != "c":
        if option == "a": 
            #editar_mis_datos_personales() # type: ignore
            print("\n1. en construccion")
        elif option == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. en construccion")           
        option = input("Ingrese su opción 'a', 'b', 'c': ")

def matcheos():
    os.system("cls")

    print("\n3. Matcheos")
    print(" En contruccion")
    print(" c. Volver")

    option = input("Ingrese su opción 'a', 'b', 'c': ")
    while option != "c":
        if option == "a": 
            #editar_mis_datos_personales() # type: ignore
            print("\n1. en construccion")
        elif option == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. en construccion")           
        option = input("Ingrese su opción 'a', 'b', 'c': ")

def reportes_estadisticos():
    os.system("cls")

    print("\nReportes estadisticos")
    print(" En contruccion")
    print(" c. Volver")

    option = input("Ingrese su opción 'a', 'b', 'c': ")
    while option != "c":
        if option == "a": 
            #editar_mis_datos_personales() # type: ignore
            print("\n1. option c")
        elif option == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. option b")           
        option = input("Ingrese su opción 'a', 'b', 'c': ")
        
def editar_mis_datos_personales():
    global usuario1_email, email_usuario_autenticado
    
    
    if (usuario1_email == email_usuario_autenticado):
        print("\n1. editar_mis_datos_personales", email_usuario_autenticado)

def validar_numero():
    while True:
        try:
            return int(input("Ingrese un número: "))
        except ValueError:
            print("Debe ingresar un número")

def declarar_variables_globales():
    # Constantes con los datos de los estudiantes
    global usuario1_email, usuario1_contraseña, usuario2_email, usuario2_contraseña, usuario3_email,   usuario3_contraseña, intentos_restantes, email_usuario_autenticado

    usuario1_email = "111"
    usuario1_contraseña = "222"
    #agregar el me gusta y el resto de los datos para cada usuarios
    usuario2_email = "estudiante2@ayed.com"
    usuario2_contraseña = "333444"
    
    usuario3_email = "estudiante3@ayed.com"
    usuario3_contraseña = "555666"
    
    intentos_restantes = 3
    email_usuario_autenticado = ""

# Programa principal
import msvcrt
import random
import os

def iniciar_sesion():    
    global isLoggedIn, intentos_restantes, email_usuario_autenticado
    declarar_variables_globales()    
    
    while intentos_restantes > 0 and not email_usuario_autenticado:
        email = input("Ingrese su email: ")
        contraseña = input("Ingrese su contraseña: ")
        
        if (email == usuario1_email and contraseña == usuario1_contraseña) or (email == usuario2_email and contraseña == usuario2_contraseña) or (email == usuario3_email and contraseña == usuario3_contraseña):
            os.system("cls")
            print("Inicio de sesión exitoso!")
            print("Bienvenido!")
            email_usuario_autenticado = email
            isLoggedIn = True
        else:
            intentos_restantes -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")

def main():
    global email_usuario_autenticado, isLoggedIn
    
    iniciar_sesion()
    
    while email_usuario_autenticado and isLoggedIn:        
        menu_completo()
            

main()

