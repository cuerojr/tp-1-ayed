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

arreglo_de_estudiantes:     list[list[str]] = [[""]*12 for i in range(8)]   # Arreglo multidimensional de 8x8 de strings
arreglo_de_moderadores:     list[list[str]] = [[""]*9 for i in range(4)]    # Arreglo multidimensional de 8x4 de strings
arreglo_informe_reportes:   list[list[str]] = [[""]*8 for i in range(8)]    # Arreglo multidimensional de 8x8 de caracteres
arreglo_reportes:           list[list[str]] = [[""]*8 for i in range(8)]      # Arreglo multidimensional de 8x8 de strings
arreglo_me_gusta:           list[list[int]] = [[0]*8 for i in range(8)]     # Arreglo multidimensional de 8x8 de enteros

arreglo_usuarios_sesion:    list[bool] = [False]*2  # Arreglo unidimensional de booleanos
arreglo_usuarios_creados:   list[int] = [0]*2       # Arreglo unidimensional de enteros

for i in range(8):
    for j in range(8):
        arreglo_me_gusta[i][j] = random.randint(0, 1) # Populacion aleatoria de likes







########
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

        # os.system("cls")
        print("\nMenu Estudiante")
        print("1. Ingresar datos")
        print("2. Ver estadísticas")
        print("0. Salir")
        opc = validar_numero()
        while opc <= 0 and opc > 3:
            print("Opción inválida")
            opc = validar_numero()

def validar_ingreso(arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_usuarios_sesion):
    intentos = 3

    print("Inicia sesión\n")
    email = input("Ingrese su email: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    while intentos > 1 and (not arreglo_usuarios_sesion[ESTUDIANTES_INDEX] and not arreglo_usuarios_sesion[MODERADORES_INDEX]):
        for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
            if ((email == arreglo_de_estudiantes[i][3] and contraseña == arreglo_de_estudiantes[i][4] and arreglo_de_estudiantes[i][9] == "activo")):
                # isLoggedIn = True
                arreglo_usuarios_sesion[ESTUDIANTES_INDEX] = True
                print("Sesión iniciada correctamente")
                menu_estudiante(arreglo_usuarios_creados[ESTUDIANTES_INDEX])

        for i in range(arreglo_usuarios_creados[MODERADORES_INDEX]):
            if (email == arreglo_de_moderadores[i][3] and contraseña == arreglo_de_moderadores[i][4]):
                # isLoggedIn = True
                arreglo_usuarios_sesion[MODERADORES_INDEX] = True
                print("Sesión iniciada correctamente")
                menu_moderadores(arreglo_usuarios_creados[MODERADORES_INDEX], arreglo_usuarios_sesion[MODERADORES_INDEX])

        print( arreglo_usuarios_sesion[ESTUDIANTES_INDEX], arreglo_usuarios_sesion[MODERADORES_INDEX])
        if(not arreglo_usuarios_sesion[ESTUDIANTES_INDEX] and not arreglo_usuarios_sesion[MODERADORES_INDEX]):
            print("Email o contraseña incorrectos")
            intentos -= 1
            print("\nQuedan ", intentos, "intentos\n")
            email = input("Ingrese su email: ")
            contraseña = getpass.getpass("Ingrese su contraseña: ")

def ingresar(MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, arreglo_usuarios_sesion, arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX):
    if(MIN_CANT_ESTUDIANTES <= arreglo_usuarios_creados[ESTUDIANTES_INDEX] and MIN_CANT_MODERADORES <= arreglo_usuarios_creados[MODERADORES_INDEX]):
        os.system("cls")
        validar_ingreso(arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_usuarios_sesion)
    else:
        os.system("cls")
        print("No se puede ingresar, cantidad de estudiantes y moderadores insuficientes")

def ingresar_datos_moderadores(arreglo_usuarios_creados: list[int], MODERADORES_INDEX: int):
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

def ingresar_datos_de_estudiantes(arreglo_usuarios_creados: list[int], ESTUDIANTES_INDEX: int):
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

def registrar_estudiante(arreglo_usuarios_creados: list[int], MAX_CANT_ESTUDIANTES: int, ESTUDIANTES_INDEX: int):
    if (arreglo_usuarios_creados[ESTUDIANTES_INDEX] < MAX_CANT_ESTUDIANTES):
        ingresar_datos_de_estudiantes(arreglo_usuarios_creados, ESTUDIANTES_INDEX)
        os.system("cls")
        arreglo_usuarios_creados[ESTUDIANTES_INDEX] = arreglo_usuarios_creados[ESTUDIANTES_INDEX]+1
        print("Estudiante registrado")
        print(arreglo_de_estudiantes)
    else: 
        print("Todos los estudiantes fueron cargados")
  
def registrar_moderador(arreglo_usuarios_creados: list[int], MAX_CANT_MODERADORES: int, MODERADORES_INDEX: int):
    if (arreglo_usuarios_creados[MODERADORES_INDEX] < MAX_CANT_MODERADORES):
        ingresar_datos_moderadores(arreglo_usuarios_creados, MODERADORES_INDEX)
        os.system("cls")
        arreglo_usuarios_creados[MODERADORES_INDEX] = arreglo_usuarios_creados[MODERADORES_INDEX]+1
        print("Moderador registrado")
        print(arreglo_de_moderadores)
    else:
        print("Todos los moderadores fueron cargados")

def registrar(MAX_CANT_ESTUDIANTES: int, MAX_CANT_MODERADORES: int, arreglo_usuarios_creados: list[int], ESTUDIANTES_INDEX: int, MODERADORES_INDEX: int):
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

"""
FUN

return entero
"""
def validar_numero() -> int:
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

"""

"""
def mostrar_menu_principal():
    #os.system("cls")
    print("\nMenu ")
    print("\n1. Registro")
    print("2. Iniciar sesion")
    print("0. Salir\n")

"""

"""
def ejecutar_programa_principal(MIN_CANT_ESTUDIANTES: int, MAX_CANT_ESTUDIANTES: int, MIN_CANT_MODERADORES: int, MAX_CANT_MODERADORES: int, arreglo_usuarios_sesion: list[bool], arreglo_usuarios_creados: list[int], arreglo_de_estudiantes: list[list[str]], arreglo_de_moderadores: list[list[str]], ESTUDIANTES_INDEX: int, MODERADORES_INDEX: int):
    os.system("cls")
    # print(arreglo_usuarios_sesion)
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
                ingresar(MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, arreglo_usuarios_sesion, arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX)
            case 3:
                print("Bonuses")
        
        mostrar_menu_principal()
        opc = validar_numero()
        while opc < 0 and opc > 4:
            print("Opción inválida")
            opc = validar_numero()

    os.system("cls")
    print("\n\nSesión cerrada. ¡Hasta luego!\n\n")
  
ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES,MIN_CANT_MODERADORES,MAX_CANT_MODERADORES,arreglo_usuarios_sesion,arreglo_usuarios_creados, arreglo_de_estudiantes, arreglo_de_moderadores, ESTUDIANTES_INDEX, MODERADORES_INDEX)