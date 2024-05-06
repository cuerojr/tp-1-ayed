

# Función para ocultar la contraseña mientras se escribe--------------------(arreglar: la frase se puede borrar al correr el programa)
def ocultar_contraseña():
    print("Ingrese su contraseña: ", end="", flush=True)
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
    os.system("cls")
    print("a. Editar mis datos personales")
    print("b. Eliminar mi perfil")
    print("c. Volver")
    opcion = input("Ingrese su opción: ")
    if opcion == "a":
        editar_datos_personales()
    elif opcion == "b":
        cons()
    elif opcion == "c":
        os.system("cls")
        return
    else:
        gestionar_mi_perfil()
# Función para gestionar candidatos
def gestionar_candidatos():
    os.system("cls")
    print("a. Ver candidatos")
    print("b. Reportar un candidato")
    print("c. Volver")
    opcion = input("Ingrese su opción: ")
    if opcion == "a":
        ver_candidatos()
    elif opcion == "b":
        cons()
    elif opcion == "c":
        os.system("cls")
        return
    else:
        gestionar_candidatos()
# Función para matcheos
def matcheos():
    os.system("cls")
    print("a. Ver matcheos")
    print("B. Eliminar un matcheo")
    print("c. Volver")
    opcion = input("Ingrese su opción: ")
    if opcion == "a":
        cons()
    elif opcion == "b":
        cons()
    elif opcion == "c":
        os.system("cls")
        return
    else:
        matcheos()
# Función para editar datos personales
def editar_datos_personales():
    os.system("cls")
    # Implementar la edición de datos personales
    print("Editar datos personales")


# Función para ver candidatos
def ver_candidatos():
    os.system("cls")
    # Implementar la visualización de candidatos
    print("Ver candidatos")

# Funciones para "En Construcción"
def cons():
    os.system("cls")
    print("En Construcción")
    print("0. Volver al inicio.")
    volver = input("Ingrese su opción: ")
    if volver == "0":
        os.system("cls")
        return


#Funcion ruleta
def ruleta():
    probabilidad_a = int(input("Ingrese la probabilidad de matcheo para la Persona A: "))
    probabilidad_b = int(input("Ingrese la probabilidad de matcheo para la Persona B: "))
    probabilidad_c = int(input("Ingrese la probabilidad de matcheo para la Persona C: "))
    if probabilidad_a + probabilidad_b + probabilidad_c != 100:
        print("La suma de las probabilidades debe ser igual a 100. Intente de nuevo.")
    else:
        return
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
import os

intentos = 3

def iniciar_sesion():
    # Constantes con los datos de los estudiantes
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
        contraseña = ocultar_contraseña()
        
        if email == usuario1_email and contraseña == usuario1_contraseña:
            print("Inicio de sesión exitoso!")
            usuario_autenticado = True
        else:
            intentos_restantes -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")
    
    return usuario_autenticado

def sesion_iniciada():
    os.system("cls")
    print("Bienvenido!")
    while True:
        menu_completo()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            gestionar_mi_perfil()
        elif opcion == "2":
            gestionar_candidatos()
        elif opcion == "3":
            matcheos()
        elif opcion == "4":
            cons()
        elif opcion == "0":
            os.system("cls")
            print("Sesión cerrada. ¡Hasta luego!")
            return  # Salir de la función sesion_iniciada() cuando se elija salir
        else:
            print("Opción inválida.")

def main():
    sesion_activa = True

    while sesion_activa:
        if iniciar_sesion():
            sesion_iniciada()
            respuesta = input("¿Desea iniciar sesión nuevamente? (s/n): ")
            if respuesta.lower() != 's':
                print("Adiós.")
                sesion_activa = False
        else:
            respuesta = input("¿Desea intentar iniciar sesión nuevamente? (s/n): ")
            if respuesta.lower() != 's':
                print("Adiós.")
                sesion_activa = False
            else:
                print("Reintentar iniciar sesión.")
                sesion_activa = True  # Reiniciar la sesión activa para volver a intentar iniciar sesión

    print("Programa finalizado.")  # Agregar un mensaje de finalización al salir del bucle

if __name__ == "__main__":
    main()
