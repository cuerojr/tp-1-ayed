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
arreglo_de_estudiantes = [[""]*9 for i in range(8)] # Arreglo multidimensionl de 8x8 de caracteres
arreglo_de_moderadores = [[""]*9 for i in range(4)] # Arreglo multidimensionl de 8x4 de caracteres

def ingresar_datos_estudiantes(estudiantes_registrados):
    print(f"ingresar_datos_estudiantes {estudiantes_registrados}")
def ver_estadisticas():
    print("ver_estadisticas")

def menu_estudiante():
    global isLoggedIn
    print("\nMenu Estudiante\n")
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

    print("Inicia sesión")
    email = input("Ingrese su email: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    if email == "admin@ayed.com" and contraseña == "admin123":
        isLoggedIn = True
        print("Sesión iniciada correctamente")
        menu_estudiante()
    else:
        print("Email o contraseña incorrectos")
        intentos -= 1

def ingresar(MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, estudiantes_registrados, moderadores_registrados):
    if(MIN_CANT_ESTUDIANTES <= estudiantes_registrados and MIN_CANT_MODERADORES <= moderadores_registrados):
        print("ingreso exitoso")
        validar_ingreso()
    else:
       # os.system("cls")
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
    print("\nRegistrar usuario")
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
    print("0. Salir")

def ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES,MIN_CANT_MODERADORES,MAX_CANT_MODERADORES,estudiantes_registrados,moderadores_registrados,arreglo_de_estudiantes,arreglo_de_moderadores):

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
    print("Sesión cerrada. ¡Hasta luego!")
  
ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES,MIN_CANT_MODERADORES,MAX_CANT_MODERADORES,estudiantes_registrados,moderadores_registrados,arreglo_de_estudiantes,arreglo_de_moderadores)