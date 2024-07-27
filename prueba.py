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

MIN_CANT_ESTUDIANTES  = 4   # enteros
MAX_CANT_ESTUDIANTES  = 8   # enteros
MIN_CANT_MODERADORES  = 1   # enteros
MAX_CANT_MODERADORES  = 4   # enteros
ESTUDIANTES_INDEX  = 0      # enteros
MODERADORES_INDEX  = 1      # enteros
USUARIO_INDEX = 2           # enteros

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
# 5 type: string
# 6 hobbies: string
# 7 me gusta: string
# 8 fecha de nacimiento: string
# 9 status: string
# 10 iniciado: string
# 11 biografia: string

arreglo_de_estudiantes      = [[""]*12  for i in range(8)] # Arreglo bidimensional de 8x12 de strings
arreglo_de_moderadores      = [[""]*8   for i in range(4)] # Arreglo bidimensional de 8x4 de strings
arreglo_informe_reportes    = [[""]*8   for i in range(8)] # Arreglo bidimensional de 8x8 de caracteres
arreglo_reportes            = [[[""]*2]*8   for i in range(8)] # Arreglo tridimensional de 8x8x2 de strings
arreglo_me_gusta            = [[0]*8    for i in range(8)] # Arreglo bidimensional de 8x8 de enteros

arreglo_usuarios_sesion     = [False]*2 # Arreglo unidimensional de booleanos
arreglo_usuarios_creados    = [0]*2     # Arreglo unidimensional de enteros
""""
PROCEDIMIENTO popular_likes_aleatorios
i, j: enteros
arreglo_me_gusta:    arreglo bidimensional de 8*8 de enteros
"""
def popular_likes_aleatorios(arreglo_me_gusta):
    for i in range(8):
        for j in range(8):
            if i != j:
                arreglo_me_gusta[i][j] = random.randint(0, 1)
            else:
                arreglo_me_gusta[i][j] = 0

popular_likes_aleatorios(arreglo_me_gusta)
"""
PROCEDIMIENTO popular_db_estudiantes
ESTUDIANTES_INDEX, i: enteros

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def popular_db_estudiantes(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    for i in range(4):        
        arreglo_de_estudiantes[i][0] = str(i)
        arreglo_de_estudiantes[i][1] = "est" + str(i+1)
        arreglo_de_estudiantes[i][2] = "est" + str(i+1)
        arreglo_de_estudiantes[i][3] = "est" + str(i+1) + "@ayed.com"
        arreglo_de_estudiantes[i][4] = "est" + str(i+1)
        arreglo_de_estudiantes[i][5] = "estudiante"
        arreglo_de_estudiantes[i][8] = str(random.randint(1,30))+"-"+str(random.randint(1, 12))+"-"+"19"+str(random.randint(80, 99))
        arreglo_de_estudiantes[i][9] = "activo"

    arreglo_usuarios_creados[ESTUDIANTES_INDEX] = 4

popular_db_estudiantes(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes)


"""
PROCEDIMIENTO mostrar_menu_estudiante
MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, ESTUDIANTES_INDEX, MODERADORES_INDEX, opc: enteros

arreglo_usuarios_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_de_moderadores:     arreglo bidimensional de 8*8 de strings
arreglo_informe_reportes:   arreglo bidimensional de 8x8 de caracteres
arreglo_reportes:           arreglo bidimensional de 8x8 de strings
"""
def mostrar_menu_estudiante():
    print("Menu ")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

"""
PROCEDIMIENTO menu_estudiante
ESTUDIANTES_INDEX, opc: enteros

arreglo_usuarios_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def menu_estudiante(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta):
    mostrar_menu_estudiante()
    
    opc = validar_numero()
    while opc < 0 and opc > 4:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                gestionar_mi_perfil(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes)
            case 2:
                gestionar_candidatos(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)
            case 3:
                matcheos()
            case 4:
                reportes_estadisticos(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes)

        os.system("cls")
        mostrar_menu_estudiante()
        opc = validar_numero()
        while opc < 0 and opc > 4:
            print("Opción inválida")
            opc = validar_numero()
    
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            arreglo_de_estudiantes[i][10] = ""
    # arreglo_usuarios_sesion[ESTUDIANTES_INDEX]  = False


"""
PROCEDIMIENTO gestionar_mi_perfil
ESTUDIANTES_INDEX: enteros
opc: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8x12 de strings
"""
def gestionar_mi_perfil(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes):    
    os.system("cls")
    print("\nGestionar mi perfil\n")
    print("a. Editar mis datos personales")
    print("b. Eliminar mi perfil")    
    print("c. Volver") 
    opc = str(input("Ingrese su opción: "))

    while opc != "c":
        match opc:
            case "a": 
                editar_mis_datos_personales(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes)
            case "b":
                eliminar_mi_perfil(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes) 
    
        os.system("cls")    
        print("\nGestionar mi perfil\n")
        print("a. Editar mis datos personales")
        print("b. Eliminar mi perfil")    
        print("c. Volver") 
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

"""
PROCEDIMIENTO editar_mis_datos_personales
ESTUDIANTES_INDEX: enteros
opc: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8x12 de strings
"""
def editar_mis_datos_personales(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    os.system("cls")

    mostrar_menu_de_mis_datos(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes)

    print("\nEditar mis datos personales\n")
    print("a. Editar mi fecha de nacimiento")
    print("b. Editar mi biografía")
    print("c. Editar mis hobbies")
    print("d. Eliminar mis me gusta")
    print("e. Volver")  
    opc = str(input("Ingrese su opción: "))

    while opc != "e":
        match opc:    
            case "a": 
                editar_mi_fecha_de_nacimiento(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes)
            case "b":
                editar_mi_biografia(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes)          
            case "c":
                editar_mis_hobbies(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes)  
            case "d":
                eliminar_mis_me_gusta(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes)

        os.system("cls")
        mostrar_menu_de_mis_datos(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes)

        print("\nEditar mis datos personales\n")
        print("a. Editar mi fecha de nacimiento")
        print("b. Editar mi biografía")
        print("c. Editar mis hobbies")  
        print("d. Eliminar mis me gusta")
        print("e. Volver")   
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

"""
PROCEDIMIENTO mostrar_menu_de_mis_datos
ESTUDIANTES_INDEX, i: enteros

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def mostrar_menu_de_mis_datos(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            print("\nMi ID: ", arreglo_de_estudiantes[i][0])
            print("Mi nombre: ", arreglo_de_estudiantes[i][1])
            print("Mi apellido: ", arreglo_de_estudiantes[i][2])
            print("Mi fecha de nacimiento: ", arreglo_de_estudiantes[i][8])
            print("Mi biografia: ", arreglo_de_estudiantes[i][11])
            print("Mi edad: ", mostrar_edad(arreglo_de_estudiantes[i][8] or ""), "años")
            print("Mis hobbies: ", arreglo_de_estudiantes[i][6])
            mostrar_mis_me_gusta(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)
            print("Mi estado: ", arreglo_de_estudiantes[i][9])

"""
PROCEDIMIENTO editar_mi_fecha_de_nacimiento
ESTUDIANTES_INDEX, i: enteros
nueva_fecha_de_nacimiento: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def editar_mi_fecha_de_nacimiento(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes): # chequear el tema de que pasa si no esta bien escrita la fecha
    nueva_fecha_de_nacimiento = str(input("Ingrese su fecha de nacimiento: "))
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            arreglo_de_estudiantes[i][8] = nueva_fecha_de_nacimiento

"""
PROCEDIMIENTO editar_mi_biografia
ESTUDIANTES_INDEX, i: enteros
nueva_biografia: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def editar_mi_biografia(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    nueva_biografia = str(input("Ingrese su biografia: "))
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            arreglo_de_estudiantes[i][11] = nueva_biografia

"""
PROCEDIMIENTO editar_mis_hobbies
ESTUDIANTES_INDEX, MODERADORES_INDEX, i: enteros
nuevos_hobbies: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def editar_mis_hobbies(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    nuevos_hobbies = str(input("Ingrese sus hobbies: "))
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            arreglo_de_estudiantes[i][6] = nuevos_hobbies

"""
PROCEDIMIENTO eliminar_mis_me_gusta
ESTUDIANTES_INDEX, i, j: enteros
eliminar_me_gusta: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def eliminar_mis_me_gusta(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    mostrar_mis_me_gusta(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)
    eliminar_me_gusta = str(input("Ingrese nombre de usuario para eliminar de la lista: "))
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            for j in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
                if eliminar_me_gusta == arreglo_de_estudiantes[j][1]:
                    arreglo_me_gusta[i][j] = 0
                else:
                    print("Error")
        else:
            print("Error")

"""
PROCEDIMIENTO mostrar_me_gusta
ESTUDIANTES_INDEX, MODERADORES_INDEX, i, j: enteros

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_me_gusta:           arreglo bidimensional de 8x8 de enteros
"""
def mostrar_mis_me_gusta(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta):
    print("\nMis me gusta\n")
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            for j in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
                if arreglo_me_gusta[i][j] == 1 and arreglo_de_estudiantes[j][1] != "":
                    print (arreglo_de_estudiantes[j][1])

def mostrar_me_gusta(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta, i):
    print("\nMis me gusta\n")
    for j in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if arreglo_me_gusta[i][j] == 1 and arreglo_de_estudiantes[j][1] != "":
            print (arreglo_de_estudiantes[j][1])

"""
FUNCION mostrar_edad
edad: enteros
fecha: string
fecha_nacimiento, fecha_actual: datetime
"""
def mostrar_edad(fecha):
    if(not fecha): 
        return "000"
    fecha_nacimiento = datetime.strptime(fecha, '%d-%m-%Y')
    fecha_actual = datetime.now()
    
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    
    return edad

"""
PROCEDIMIENTO mostrar_datos
ESTUDIANTES_INDEX, i: enteros

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_me_gusta:           arreglo unidimensional de 8*8 de enteros
"""
def mostrar_datos(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta):   ## MODELO ESTUDIANTE
# 0 ID: string
# 1 nombre: string
# 2 apellido: string
# 3 email: string
# 4 contraseña: string
# 5 type: string
# 6 hobbies: string
# 7 me gusta: string
# 8 fecha de nacimiento: string
# 9 status: string
# 10 iniciado: string
# 11 biografia: string
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        print("\nID: ",arreglo_de_estudiantes[i][0])
        print("Nombre: ", arreglo_de_estudiantes[i][1])
        print("Apellido: ", arreglo_de_estudiantes[i][2])
        print("Email: ", arreglo_de_estudiantes[i][3])
        print("Fecha de nacimiento: ", arreglo_de_estudiantes[i][8])
        print("Biografia: ", arreglo_de_estudiantes[i][11])
        print("Edad: ", mostrar_edad(arreglo_de_estudiantes[i][8]), "años")
        print("Hobbies: ", arreglo_de_estudiantes[i][6])
        mostrar_me_gusta(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta, i)
        print("Estado: ", arreglo_de_estudiantes[i][9])

"""
PROCEDIMIENTO me_gusta
ESTUDIANTES_INDEX, i, j: enteros
megusta: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_me_gusta:
"""
def me_gusta(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta):
    print("\nDar me gusta\n")
    megusta = str(input("Ingresar nombre de estudiante: "))
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            for j in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
                if i != j:
                    if megusta == arreglo_de_estudiantes[j][1]:
                        arreglo_me_gusta[i][j] = 1           

"""
PROCEDIMIENTO eliminar_mi_perfil
ESTUDIANTES_INDEX: enteros
opc: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def eliminar_mi_perfil(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    print("\nEliminar mi perfil")
    print("Cuidado! Al aceptar se eliminara todo tu perfi!\n")
    print("a. Si, continuar")
    print("b. No. Volver")
    opc = str(input("Ingrese su opción: "))
    while opc != "b" and opc != "a":
        match opc:
            case "a": 
                perfil_eliminado(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes)
    
        os.system("cls")    
        print("\nEliminar mi perfil")
        print("Cuidado! Al aceptar se eliminara todo tu perfi!\n")
        print("a. Si, continuar")
        print("b. No. Volver")
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

"""
PROCEDIMIENTO perfil_eliminado
ESTUDIANTES_INDEX, i: enteros

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def perfil_eliminado(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes):  # solo cambiar a inactivo
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            arreglo_de_estudiantes[i][9] = "inactivo" #nombre
    print("\nPerfil eliminado exitosamente\n")

"""
PROCEDIMIENTO gestionar_candidatos
ESTUDIANTES_INDEX: enteros
opc: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8x12 de strings
arreglo_me_gusta:           arreglo unidimensional de enteros
"""
def gestionar_candidatos(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta):
    os.system("cls")

    print("\nGestionar candidatos\n")
    print("a. Ver candidatos")
    print("b. Reportar candidato")    
    print("c. Volver") 
    opc = str(input("Ingrese su opción: "))

    while opc != "c":
        match opc:
            case "a":
                ver_candidatos(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)
            case "b":
                reportar_candidato(arreglo_usuarios_creados, ESTUDIANTES_INDEX)

        os.system("cls")
        print("\nGestionar candidatos\n")
        print("a. Ver candidatos")
        print("b. Reportar candidato")    
        print("c. Volver") 
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

"""
PROCEDIMIENTO ver_candidatos
ESTUDIANTES_INDEX: enteros
opc: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_me_gusta:           arreglo unidimensional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def ver_candidatos(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta):
    print("\nCandidatos\n")
    mostrar_datos(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)
    print("\n\na. Dar me gusta")
    print("b. Volver")

    opc = str(input("Ingrese su opción: "))
    while opc != "b":
        match opc:
            case "a":
                me_gusta(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)

        os.system("cls")
        print("\nCandidatos\n")
        mostrar_datos(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)
        print("\n\na. Dar me gusta")
        print("b. Volver")
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

"""
PROCEDIMIENTO reportar_candidato
ESTUDIANTES_INDEX, i, j: enteros
reportado, reporte: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_informe_reportes:   arreglo bidimensional de 8x8 de caracteres
arreglo_reportes:           arreglo bidimensional de 8x8 de strings
"""
def reportar_candidato(arreglo_usuarios_creados, ESTUDIANTES_INDEX):
    print("\nReportar candidatos\n")
    reportado = str(input("Ingrese nombre o ID de usuario a reportar: "))
    reporte = str(input("Ingrese su reporte: "))
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            for j in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
                if reportado == arreglo_de_estudiantes[j][1] or reportado == arreglo_de_estudiantes[j][0]:
                    arreglo_reportes[i][j][0] = "0"
                    arreglo_reportes[i][j][1] = reporte
                    os.system("cls")
                    print("\nReporte exitoso.\n")

"""
PROCEDIMIENTO matcheos
opc: string

"""
def matcheos():
    os.system("cls")
    print("\nMatcheos\n")
    print("En contruccion")
    print(" a. Volver")
    opc = str(input("Ingrese su opción: "))

    while opc != "a":
        os.system("cls")
        print("\nMatcheos\n")
        print("En contruccion!\n")
        print("a. Volver")         
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

"""
PROCEDIMIENTO reportes_estadisticos
ESTUDIANTES_INDEX: enteros
opc: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
"""
def reportes_estadisticos(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes):
    os.system("cls")
    print("\nReportes estadísticos\n")
    porcentaje_matcheos()
    like1(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes)
    like2(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes)
    print("a. Volver")
    opc = str(input("Ingrese su opción: "))

    while opc != "a":
        os.system("cls")
        print("\nReportes estadísticos\n")
        porcentaje_matcheos()
        like1(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes)
        like2(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes)
        print("a. Volver")  
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

"""
PROCEDIMIENTO porcentaje_matcheos
ESTUDIANTES_INDEX, i, j, matcheos: enteros

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def porcentaje_matcheos(arreglo_usuarios_creados, ESTUDIANTES_INDEX):
    matcheos = 0
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            for j in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
                if arreglo_me_gusta[i][j] == 1 and arreglo_me_gusta[j][i] == 1:
                    matcheos = matcheos + 1
                else:
                    print("Error")
            porcentaje = (matcheos * 100)/arreglo_usuarios_creados[ESTUDIANTES_INDEX] - 1
        else:
            print("Error")
    os.system("cls")
    print("Matcheados sobre el % posible: ", int(porcentaje), "%")

"""
PROCEDIMIENTO like1
ESTUDIANTES_INDEX, i, j, contador: enteros

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_me_gusta:     arreglo bidimensional de 8*8 de enteros
"""
def like1(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes):
    contador = 0
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            for j in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
                if arreglo_me_gusta[i][j] == 1 and arreglo_me_gusta[j][i] == 0:
                    contador = contador + 1
                else:
                    print("Error")
        else:
            print("Error")
    os.system("cls")
    print("Likes dados y no recibidos: ", contador)

"""
PROCEDIMIENTO like2
ESTUDIANTES_INDEX, i, j, contador: enteros

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_me_gusta:     arreglo bidimensional de 8*8 de enteros
"""
def like2(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes):
    contador = 0
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if  arreglo_de_estudiantes[i][10] == "iniciado":
            for j in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
                if arreglo_me_gusta[i][j] == 0 and arreglo_me_gusta[j][i] == 1:
                    contador = contador + 1
                else:
                    print("Error")
        else:
            print("Error")
    os.system("cls")
    print("Likes recibidos y no respondidos: ", contador)

"""
PROCEDIMIENTO
"""
def mostrar_menu_moderadores():
        print("\nMenu Moderadores\n")
        print("1. Gestionar usuarios")
        print("2. Gestionar reportes")
        print("3. Reportes estadísticos")
        print("0. Salir")

"""
PROCEDIMIENTO menu_moderadores
ESTUDIANTES_INDEX, MODERADORES_INDEX, opc: enteros

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_informe_reportes:   arreglo bidimensional de 8x8 de caracteres
arreglo_reportes:           arreglo bidimensional de 8x8 de strings
"""
def menu_moderadores(arreglo_usuarios_creados, MODERADORES_INDEX, ESTUDIANTES_INDEX, arreglo_reportes, arreglo_informe_reportes):
    mostrar_menu_moderadores()
    opc = validar_numero()
    while opc < 0 and opc > 3:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                gestionar_usuarios(arreglo_usuarios_creados, ESTUDIANTES_INDEX)
            case 2:
                gestionar_reportes(arreglo_reportes, arreglo_informe_reportes, arreglo_usuarios_creados, ESTUDIANTES_INDEX)
            case 3:
                reportes_estadisticos_mods()
            case 0:
                print("Sesión cerrada. ¡Hasta luego!")
                # for i in range(arreglo_usuarios_creados[MODERADORES_INDEX]):
                #     if  arreglo_de_moderadores[i][7] == "iniciado":  # <------ chequear esto
                #         arreglo_de_moderadores[i][7] = "no iniciado"
                os.system("cls")
        os.system("cls")
        mostrar_menu_moderadores()
        opc = validar_numero()
        while opc < 0 and opc > 3:
            print("Opción inválida")
            opc = validar_numero()

"""
PROCEDIMIENTO gestionar_usuarios
ESTUDIANTES_INDEX: enteros
opc: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
"""
def gestionar_usuarios(arreglo_usuarios_creados, ESTUDIANTES_INDEX):
    os.system("cls")
    print("\nGestionar usuarios\n")
    print("a. Desactivar usuario")  
    print("b. Volver") 
    opc = str(input("Ingrese su opción: "))

    while opc != "b":
        match opc:
            case "a":
                desactivar_usuario(arreglo_usuarios_creados, ESTUDIANTES_INDEX)

        os.system("cls")
        print("\nGestionar usuarios\n")
        print("a. Desactivar usuario")  
        print("b. Volver") 
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

"""
PROCEDIMIENTO desactivar_usuario
i, ESTUDIANTES_INDEX: enteros
opc, desactivar: string

arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_usuarios_creados    arreglo unidimensional de enteros
"""
def desactivar_usuario(arreglo_usuarios_creados, ESTUDIANTES_INDEX):
    os.system("cls")
    print("\nDesactivar usuario\n")
    desactivar = str(input("Ingresar nombre o ID de usuario a desactivar: "))
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
        if desactivar == arreglo_de_estudiantes[i][0] or desactivar == arreglo_de_estudiantes[i][1]:
            arreglo_de_estudiantes[i][9] = "inactivo"
        else:
            print("Error")

"""
PROCEDIMIENTO gestionar_reportes
opc: string

arreglo_reportes:           arreglo bidimensional de 8x8 de strings
arreglo_informe_reportes:   arreglo bidimensional de 8x8 de caracteres
"""
def gestionar_reportes(arreglo_reportes, arreglo_informe_reportes, arreglo_usuarios_creados, ESTUDIANTES_INDEX):
    os.system("cls")
    print("\nGestionar reportes\n")
    print("a. Ver reportes")  
    print("b. Volver") 
    opc = str(input("Ingrese su opción: "))

    while opc != "b":
        match opc:
            case "a":
                ver_reportes(arreglo_reportes, arreglo_informe_reportes, arreglo_usuarios_creados, ESTUDIANTES_INDEX)
        print("\nGestionar reportes\n")
        print("a. Ver reportes")  
        print("b. Volver") 
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

"""
PROCEDIMIENTO ver_reportes
i, j, k: enteros
opc: string

arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_reportes:           arreglo bidimensional de 8x8 de strings
arreglo_informe_reportes:   arreglo bidimensional de 8x8 de caracteres
"""
def ver_reportes(arreglo_reportes, arreglo_informe_reportes, arreglo_usuarios_creados, ESTUDIANTES_INDEX):   #<-----------------------------------------------------bastante dudoso(no lo probe)
    for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):       #slot usuario
        os.system("cls")
        print("\nReportes\n")
        for j in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):       #slot del reporte
            if i != j:
                if  arreglo_reportes[i][j][0] == "0":
                    # for h in range(8):                   #para revisar cada reporte y tomar una decisión
                    if arreglo_reportes[i][j][0] == "0":
                        print("\nReporte")
                        print("ID de reportante: ", arreglo_de_estudiantes[i][0])
                        print("ID de reportado: ", arreglo_de_estudiantes[j][0])
                        print(arreglo_reportes[i][j][1])
                        print("\n¿Que acción desea tomar?\n")
                        print("a. Ignorar reporte")
                        print("b. Desactivar usuario")
                        opc = str(input("Ingrese su opción:"))
                        while opc != "a" and opc != "b":
                            print("ID de reportante: ", arreglo_de_estudiantes[i][0])
                            print("ID de reportado: ", arreglo_de_estudiantes[j][0])
                            print(arreglo_reportes[i][j][1])
                            print("\n¿Que acción desea tomar?\n")
                            print("a. Ignorar reporte")
                            print("b. Desactivar usuario")
                            opc = str(input("Opción inválida. Ingrese de nuevo: "))
                        match opc:
                            case "a":
                                arreglo_reportes[i][j][0] = "2"
                            case "b":
                                arreglo_reportes[i][j][0] = "1"
                                arreglo_de_estudiantes[i][9] = "inactivo"
                        os.system("cls")
                        # print("ID de reportante: ", arreglo_de_estudiantes[i][0])
                        # print("ID de reportado: ", arreglo_de_estudiantes[j][0])
                        # print(arreglo_reportes[i][j][1])
                        # print("\n¿Que acción desea tomar?\n")
                        # print("a. Ignorar reporte")
                        # print("b. Desactivar usuario")
                        # opc = str(input("Opción inválida. Ingrese de nuevo: "))
                        os.system("cls")
                        print("\nEl reporte ha sido tomado\n")
        else:
            print("No hay reportes pendientes")

"""
PROCEDIMIENTO reportes_estadisticos_mods
opc: enteros

"""
def reportes_estadisticos_mods():
    print("\nReportes estadisticos\n")
    print("En construcción")  
    print("a. Volver") 
    opc = str(input("Ingrese su opción: "))

    while opc != "a":
        print("\nReportes estadisticos\n")
        print("En construcción")  
        print("a. Volver") 
        opc = str(input("Opción inválida. Ingrese de nuevo: "))

"""
PROCEDIMIENTO validar_ingreso
ESTUDIANTES_INDEX, MODERADORES_INDEX, intentos, i: enteros
email, contraseña: string

arreglo_usuarios_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_de_moderadores:     arreglo bidimensional de 8*8 de strings
arreglo_me_gusta:           arreglo bidimensional de 8*8 de enteros
"""
def validar_ingreso(arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_usuarios_sesion, arreglo_reportes, arreglo_informe_reportes, arreglo_me_gusta):
    intentos = 3

    email = input("Ingrese su email: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    while intentos > 1 and (not arreglo_usuarios_sesion[ESTUDIANTES_INDEX] and not arreglo_usuarios_sesion[MODERADORES_INDEX]):
        for i in range(arreglo_usuarios_creados[ESTUDIANTES_INDEX]):
            if ((email == arreglo_de_estudiantes[i][3] and contraseña == arreglo_de_estudiantes[i][4] and arreglo_de_estudiantes[i][9] == "activo")):
                arreglo_usuarios_sesion[ESTUDIANTES_INDEX] = True
                arreglo_de_estudiantes[i][10] = "iniciado"
                os.system("cls")
                print("Sesión iniciada correctamente")
                menu_estudiante(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)

        for i in range(arreglo_usuarios_creados[MODERADORES_INDEX]):
            if (email == arreglo_de_moderadores[i][3] and contraseña == arreglo_de_moderadores[i][4]):
                arreglo_usuarios_sesion[MODERADORES_INDEX] = True
                print("Sesión iniciada correctamente")
                menu_moderadores(arreglo_usuarios_creados, MODERADORES_INDEX, ESTUDIANTES_INDEX, arreglo_reportes, arreglo_informe_reportes)

        if(not arreglo_usuarios_sesion[ESTUDIANTES_INDEX] and not arreglo_usuarios_sesion[MODERADORES_INDEX]):
            print("Email o contraseña incorrectos")
            intentos -= 1
            print("\nQuedan ", intentos, "intentos\n")
            email = input("Ingrese su email: ")
            contraseña = getpass.getpass("Ingrese su contraseña: ")

"""
PROCEDIMIENTO ingresar
MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, ESTUDIANTES_INDEX, MODERADORES_INDEX: enteros

arreglo_usuarios_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_reportes
arreglo_informe_reportes
arreglo_me_gusta:           arreglo bidimensional de 8*8 de enteros
"""
def ingresar(MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, arreglo_usuarios_sesion, arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_reportes, arreglo_informe_reportes, arreglo_me_gusta):
    if(MIN_CANT_ESTUDIANTES <= arreglo_usuarios_creados[ESTUDIANTES_INDEX] and MIN_CANT_MODERADORES <= arreglo_usuarios_creados[MODERADORES_INDEX]):        
        arreglo_usuarios_sesion[MODERADORES_INDEX] = False
        arreglo_usuarios_sesion[ESTUDIANTES_INDEX] = False
        os.system("cls")
        validar_ingreso(arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_usuarios_sesion, arreglo_reportes, arreglo_informe_reportes, arreglo_me_gusta)
    else:
        os.system("cls")
        print("No se puede ingresar, cantidad de estudiantes y moderadores insuficientes")

"""
PROCEDIMIENTO ingresar_datos_moderadores
MODERADORES_INDEX: enteros
nombre, apellido, email, contraseña, confirmar_contraseña: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_moderadores:     arreglo bidimensional de 8*8 de strings
"""
def ingresar_datos_moderadores(arreglo_usuarios_creados, MODERADORES_INDEX, arreglo_de_moderadores ):
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

"""
PROCEDIMIENTO ingresar_datos_de_estudiantes
ESTUDIANTES_INDEX: enteros
nombre, apellido, email, contraseña, confirmar_contraseña: string

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def ingresar_datos_de_estudiantes(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes ):
    os.system("cls")
    ## MODELO ESTUDIANTE
# 0 ID: string
# 1 nombre: string
# 2 apellido: string
# 3 email: string
# 4 contraseña: string
# 5 type: string
# 6 hobbies: string
# 7 me gusta: string
# 8 fecha de nacimiento: string
# 9 status: string
# 10 iniciado: string
# 11 biografia: string
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    email = input("Ingrese el email del estudiante: ")
    arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][0] = str(arreglo_usuarios_creados[ESTUDIANTES_INDEX])
    arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][1] = nombre
    arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][2] = apellido
    arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][3] = email
    arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][5] = "estudiante"
    arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][9] = "activo"

    contraseña = input("Ingrese su contraseña: ")
    confirmar_contraseña = input("Vuelva a ingresar su contraseña: ")    
    while contraseña != confirmar_contraseña:
        print("La contraseña no coincide, vuelva a intentar: ")
        contraseña = input("Ingrese su contraseña: ")
        confirmar_contraseña = input("Vuelva a ingresar su contraseña: ")

    if contraseña == confirmar_contraseña:
        arreglo_de_estudiantes[arreglo_usuarios_creados[ESTUDIANTES_INDEX]][4] = contraseña

"""
PROCEDIMIENTO registrar_estudiante
MAX_CANT_ESTUDIANTES, ESTUDIANTES_INDEX: enteros

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def registrar_estudiante(arreglo_usuarios_creados, MAX_CANT_ESTUDIANTES, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    if (arreglo_usuarios_creados[ESTUDIANTES_INDEX] < MAX_CANT_ESTUDIANTES):
        ingresar_datos_de_estudiantes(arreglo_usuarios_creados, ESTUDIANTES_INDEX, arreglo_de_estudiantes)
        os.system("cls")
        arreglo_usuarios_creados[ESTUDIANTES_INDEX] = arreglo_usuarios_creados[ESTUDIANTES_INDEX]+1
        print("Estudiante registrado")
        print(arreglo_de_estudiantes)
    else: 
        print("Todos los estudiantes fueron cargados")

"""
PROCEDIMIENTO registrar_moderador
MAX_CANT_MODERADORES, MODERADORES_INDEX: enteros

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_moderadores:     arreglo bidimensional de 8*8 de strings
"""
def registrar_moderador(arreglo_usuarios_creados, MAX_CANT_MODERADORES, MODERADORES_INDEX, arreglo_de_moderadores):
    if (arreglo_usuarios_creados[MODERADORES_INDEX] < MAX_CANT_MODERADORES):
        ingresar_datos_moderadores(arreglo_usuarios_creados, MODERADORES_INDEX, arreglo_de_moderadores)
        os.system("cls")
        arreglo_usuarios_creados[MODERADORES_INDEX] = arreglo_usuarios_creados[MODERADORES_INDEX]+1
        print("Moderador registrado")
    else:
        print("Todos los moderadores fueron cargados")

"""
PROCEDIMIENTO registrar
MAX_CANT_ESTUDIANTES, MAX_CANT_MODERADORES, ESTUDIANTES_INDEX, MODERADORES_INDEX, opc: enteros

arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def registrar(MAX_CANT_ESTUDIANTES, MAX_CANT_MODERADORES, arreglo_usuarios_creados, ESTUDIANTES_INDEX , MODERADORES_INDEX, arreglo_de_estudiantes, arreglo_de_moderadores):
    os.system("cls")
    mostrar_menu_registrar()

    opc = str(input("Ingrese su opción: "))
    while opc != "c":
        match opc:
            case "a": 
                registrar_estudiante(arreglo_usuarios_creados, MAX_CANT_ESTUDIANTES, ESTUDIANTES_INDEX, arreglo_de_estudiantes) # type: ignore            
            case "b": 
                registrar_moderador(arreglo_usuarios_creados, MAX_CANT_MODERADORES, MODERADORES_INDEX, arreglo_de_moderadores) # type: ignore            
           
        mostrar_menu_registrar()
        opc = str(input("Ingrese su opción: "))

"""
FUNCION validar_numero
return entero
"""
def validar_numero():
    while True:
        try:
            return int(input("Ingrese un número: "))
        except ValueError:
            print("\nDebe ingresar un número")

"""
PROCEDIMIENTO mostrar_menu_registrar
"""
def mostrar_menu_registrar():
    print("\nRegistrar usuario\n")
    print(" a. Registrar estudiante")
    print(" b. Registrar moderador")
    print(" c. Volver")

"""
PROCEDIMIENTO mostrar_menu_principal
"""
def mostrar_menu_principal():
    #os.system("cls")
    print("\nMenu ")
    print("\n1. Registro")
    print("2. Iniciar sesion")
    print("0. Salir\n")

"""
PROCEDIMIENTO ejecutar_programa_principal
MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, ESTUDIANTES_INDEX, MODERADORES_INDEX, opc: enteros

arreglo_usuarios_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios_creados:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_de_moderadores:     arreglo bidimensional de 8*8 de strings
arreglo_informe_reportes:   arreglo bidimensional de 8x8 de caracteres
arreglo_reportes:           arreglo bidimensional de 8x8 de strings
arreglo_me_gusta:           arreglo bidimensional de 8*8 de enteros
"""
def ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, arreglo_usuarios_sesion, arreglo_usuarios_creados, arreglo_de_estudiantes, arreglo_de_moderadores, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_reportes, arreglo_informe_reportes, arreglo_me_gusta):
    os.system("cls")
    print(arreglo_reportes)
    mostrar_menu_principal()     
    opc = validar_numero()
    while opc < 0 and opc > 4:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                registrar(MAX_CANT_ESTUDIANTES, MAX_CANT_MODERADORES, arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_de_estudiantes, arreglo_de_moderadores)
            case 2:
                ingresar(MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, arreglo_usuarios_sesion, arreglo_usuarios_creados, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_reportes, arreglo_informe_reportes, arreglo_me_gusta)
            case 3:
                print("Bonuses")
        
        mostrar_menu_principal()
        opc = validar_numero()
        while opc < 0 and opc > 4:
            print("Opción inválida")
            opc = validar_numero()

    os.system("cls")
    print("\n\nSesión cerrada. ¡Hasta luego!\n\n")
  
ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, arreglo_usuarios_sesion, arreglo_usuarios_creados, arreglo_de_estudiantes, arreglo_de_moderadores, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_reportes, arreglo_informe_reportes, arreglo_me_gusta)