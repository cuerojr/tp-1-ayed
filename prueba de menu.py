def menu_completo(isLoggedIn):
    os.system("cls")
    print("Menu")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")
    option = int(input("Ingrese su opción: "))

    if option == 1: 
        isLoggedIn = gestionar_mi_perfil(isLoggedIn)
    elif option == 2:
        gestionar_candidatos() # type: ignore
    elif option == 3:
        matcheos() # type: ignore
    elif option == 4:
        reportes_estadisticos() # type: ignore
    elif option == 0:
        print("Sesión cerrada. ¡Hasta luego!")
        isLoggedIn = False
    else:
        print("Opción inválida")
    return isLoggedIn


def gestionar_mi_perfil(isLoggedIn):
    os.system("cls")
    print("Menu")
    print("\n1. Gestionar mi perfil")
    print(" a. Editar mis datos personales")
    print(" b. Eliminar mi perfil")
    print(" c. Volver")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")
    option = input("Ingrese su opción: ")
    
    if option == "a": 
        editar_mis_datos_personales() # type: ignore
    elif option == "b":
        eliminar_mi_perfil() # type: ignore
    elif option == "c":
        os.system("cls")
        isLoggedIn = menu_completo(isLoggedIn)
    else:
        print("Opción inválida")
        option = input("Ingrese su opción: ")

    return isLoggedIn

# Programa principal
import msvcrt
import random
import os

intentos = 3

def iniciar_sesion():
    # Constantes con los datos de los estudiantes
    usuario1_email = "111"
    usuario1_contraseña = "222"
    usuario2_email = "estudiante2@ayed.com"
    usuario2_contraseña = "333444"
    usuario3_email = "estudiante3@ayed.com"
    usuario3_contraseña = "555666"
    
    intentos_restantes = 3
    usuario_autenticado = False
    
    while intentos_restantes > 0 and not usuario_autenticado:
        email = input("Ingrese su email: ")
        contraseña = input("Ingrese su contraseña: ")
        
        if email == usuario1_email and contraseña == usuario1_contraseña:
            print("Inicio de sesión exitoso!")
            usuario_autenticado = True
        else:
            intentos_restantes -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")
    
    return usuario_autenticado

def main():
    isLoggedIn = True 
        
    if iniciar_sesion():
        while isLoggedIn:
            os.system("cls")
            print("Bienvenido!")            
            isLoggedIn = menu_completo(isLoggedIn)
            

if __name__ == "__main__":
    main()

