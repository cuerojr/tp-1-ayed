import getpass
import random
import os

# Constantes para los usuarios precargados
USUARIOS = {
    "111": "222",
    "estudiante2@ayed.com": "333444",
    "estudiante3@ayed.com": "555666"
}

# Función para ocultar la contraseña mientras se escribe--------------------(arreglar: la frase se puede borrar al correr el programa)
def ocultar_contraseña():
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    print(contraseña)

# Función para menu completo
def menu_completo():
    print("1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

# Función para gestionar mi perfil
def gestionar_mi_perfil():
    while True:
        print("a. Editar mis datos personales")
        print("b. Eliminar mi perfil")
        print("c. Volver")
        opcion = input("Ingrese su opción: ")
        if opcion == "a":
            os.system("cls")
            editar_datos_personales()
        elif opcion == "b":
            os.system("cls")
            cons()
        elif opcion == "c":
            os.system("cls")
            return # Salir de la función
        else:
            os.system("cls")
            print("Opción inválida.")
# Función para gestionar candidatos
def gestionar_candidatos():
    while True:
        print("a. Ver candidatos")
        print("b. Reportar un candidato")
        print("c. Volver")
        opcion = input("Ingrese su opción: ")
        if opcion == "a":
            os.system("cls")
            ver_candidatos()
        elif opcion == "b":
            os.system("cls")
            cons()
        elif opcion == "c":
            os.system("cls")
            return # Salir de la función
        else:
            os.system("cls")
            print("Opción inválida.")
# Función para matcheos
def matcheos():
    while True:
        print("a. Ver matcheos")
        print("B. Eliminar un matcheo")
        print("c. Volver")
        opcion = input("Ingrese su opción: ")
        if opcion == "a":
            os.system("cls")
            cons()
        elif opcion == "b":
            os.system("cls")
            cons()
        elif opcion == "c":
            os.system("cls")
            return # Salir de la función
        else:
            os.system("cls")
            print("Opción inválida.")
# Función para editar datos personales
def editar_datos_personales():
    # Implementar la edición de datos personales
    print("Editar datos personales")


# Función para ver candidatos
def ver_candidatos():
    # Implementar la visualización de candidatos
    print("Ver candidatos")

# Funciones para "En Construcción"
def cons():
    while True:
        print("En Construcción")
        print("0. Volver")
        volver = input("Ingrese su opción: ")
        if volver == "0":
          os.system("cls")
          return # Salir de la función
        else:
            os.system("cls")
            print("Opción inválida.")


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

# Programa principal (poner arriba de todo)

intentos = 3

def iniciar_sesion():
    intentos_restantes = 3
    usuario_autenticado = False
    
    while intentos_restantes > 0 and not usuario_autenticado:
        email = input("Ingrese su email: ")
        contraseña = getpass.getpass("Ingrese su contraseña: ")
        
        if email in USUARIOS and contraseña == USUARIOS[email]:
            usuario_autenticado = True
        else:
            intentos_restantes -= 1
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")
    
    return usuario_autenticado

def sesion_iniciada():
    os.system("cls")
    print("Acceso concedido. ¡Bienvenido!")
    while True:
        menu_completo()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            os.system("cls")
            gestionar_mi_perfil()
        elif opcion == "2":
            os.system("cls")
            gestionar_candidatos()
        elif opcion == "3":
            os.system("cls")
            matcheos()
        elif opcion == "4":
            os.system("cls")
            cons()
        elif opcion == "0":
            os.system("cls")
            print("Sesión cerrada. ¡Hasta luego!")
            return  # Salir de la función
        else:
            os.system("cls")
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
                os.system("cls")
                print("Reintentar iniciar sesión.")
                sesion_activa = True  # Reiniciar la sesión activa para volver a intentar iniciar sesión

    print("Programa finalizado.")  # Agregar un mensaje de finalización al salir del bucle

if __name__ == "__main__":
    main()
