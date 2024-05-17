def menu_completo():
    global isLoggedIn, usuario_autenticado

    os.system("cls")
    print("Menu ")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

    option = int(input("Ingrese su opción "))
    while option < 0 and option > 4:
        print("Opción inválida")
        option = int(input("Ingrese su opción '0', '1', '2', '3': "))

    if option == 1:
        gestionar_mi_perfil()
    elif option == 2:
        gestionar_candidatos()
    elif option == 3:
        matcheos()
    elif option == 4:
        reportes_estadisticos()
    elif option == 0:
        print("Sesión cerrada. ¡Hasta luego!")
        isLoggedIn = False

def gestionar_mi_perfil():    
    os.system("cls")

    print("Menu gestionar_mi_perfil")
    print("\n1. Gestionar mi perfil")
    print(" a. Editar mis datos personales")
    print(" b. Eliminar mi perfil")
    print(" c. Volver")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

    option = input("Ingrese su opción 'a', 'b', 'c': ")
    while option  != "c":
        if option == "a": 
            editar_mis_datos_personales() # type: ignore            
        elif option == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. option b")
        option = input("Ingrese su opción 'a', 'b', 'c': ")


def gestionar_candidatos():
    os.system("cls")

    print("Menu gestionar_candidatos")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print(" En contruccion")
    print(" c. Volver")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

    option = input("Ingrese su opción 'a', 'b', 'c': ")    
    while option != "c":
        if option == "a": 
            #editar_mis_datos_personales() # type: ignore
            print("\n1. option a")
        elif option == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. option b")           
        option = input("Ingrese su opción 'a', 'b', 'c': ")

def matcheos():
    os.system("cls")

    print("Menu matcheos")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print(" En contruccion")
    print(" c. Volver")
    print("4. Reportes estadisticos")
    print("0. Salir")

    option = input("Ingrese su opción 'a', 'b', 'c': ")
    while option != "c":
        if option == "a": 
            #editar_mis_datos_personales() # type: ignore
            print("\n1. option c")
        elif option == "b":
            #eliminar_mi_perfil() # type: ignore 
            print("\n1. option b")            
        option = input("Ingrese su opción 'a', 'b', 'c': ")

def reportes_estadisticos():
    os.system("cls")

    print("Menu")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print(" En contruccion")
    print(" c. Volver")
    print("0. Salir")

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
    print("\n1. editar_mis_datos_personales")

# Programa principal
import msvcrt
import random
import os



def iniciar_sesion():
    # Constantes con los datos de los estudiantes
    global isLoggedIn, intentos, intentos_restantes, usuario_autenticado
    
    intentos = 3
    usuario1_email = "111"
    usuario1_contraseña = "222"
    usuario2_email = "estudiante2@ayed.com"
    usuario2_contraseña = "333444"
    usuario3_email = "estudiante3@ayed.com"
    usuario3_contraseña = "555666"
    
    intentos_restantes = 3
    usuario_autenticado = ""
    
    while intentos_restantes > 0 and not usuario_autenticado:
        email = input("Ingrese su email: ")
        contraseña = input("Ingrese su contraseña: ")
        
        if (email == usuario1_email and contraseña == usuario1_contraseña) or (email == usuario2_email and contraseña == usuario2_contraseña) or (email == usuario3_email and contraseña == usuario3_contraseña):
            os.system("cls")
            print("Inicio de sesión exitoso!")
            print("Bienvenido!")
            usuario_autenticado = email
            isLoggedIn = True
        else:
            intentos_restantes -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")
    

def main():
    global usuario_autenticado, isLoggedIn
    
    iniciar_sesion()
    
    while usuario_autenticado and isLoggedIn:        
        menu_completo()
            

if __name__ == "__main__":
    main()

