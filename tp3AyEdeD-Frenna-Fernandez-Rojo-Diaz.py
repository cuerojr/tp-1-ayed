'''
TP#3 AyED Comisión 113
Rojo Nicolás
Frenna Luca Daniel
Fernández Lucas
Diaz Santiago
'''
# Librerias
import os
import os.path
import getpass
from datetime import datetime
import random
import pickle

""" MODELO ADMIN
# 0 ID: string
# 1 nombre: string
# 2 apellido: string
# 3 email: string
# 4 contraseña: string
# 5 type: string
"""
class Admin:
    def __init__(self):
        self.id_admin = 0       #int
        self.email = ""         #string 32
        self.contraseña = ""    #string 32

""" MODELO MODERADOR
# 0 ID: string
# 1 nombre: string
# 2 apellido: string
# 3 email: string
# 4 contraseña: string
# 5 type: string
"""
class Moderador:
    def __init__(self):
        self.id = 0             #int
        self.email = ""         #string 32
        self.contraseña = ""    #string 32
        self.estado = False     #boolean

""" MODELO ESTUDIANTE
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
"""
class Estudiante:
    def __init__(self):
        self.id_estudiante = 0      #int
        self.email = ""             #string 32
        self.nombre = ""            #string 32
        self.contraseña = ""        #string 32
        self.sexo = ""              #char
        self.estado = False         #boolean
        self.hobbies = ""           #string 255
        self.materia_favorita = ""  #string 16
        self.deporte_favorito = ""  #string 16
        self.materia_fuerte = ""    #string 16
        self.materia_debil = ""     #string 16
        self.biografia = ""         #string 255
        self.pais = ""              #string 32
        self.ciudad = ""            #string 32        
        self.fecha_nacimiento = ""  #string 10

class Likes:
    def __init__(self):
        self.id_remitente = 0       #int
        self.id_destinatario = 0    #int

class Reportes:
    def __init__(self):
        self.id_reportante = 0      #int
        self.id_reportado = 0       #int
        self.motivo = ""            #string 255
        self.estado = 0             #int

# Constantes
MIN_CANT_ESTUDIANTES  = 4   # enteros
MAX_CANT_ESTUDIANTES  = 8   # enteros
MIN_CANT_MODERADORES  = 1   # enteros
MAX_CANT_MODERADORES  = 4   # enteros
ESTUDIANTES_INDEX  = 0      # enteros
MODERADORES_INDEX  = 1      # enteros
USUARIO_INDEX = 2           # enteros

arreglo_de_estudiantes      = [[""]*12  for _ in range(8)]  # Arreglo bidimensional de 8x12 de strings
arreglo_de_moderadores      = [[""]*8   for _ in range(4)]  # Arreglo bidimensional de 8x4 de strings
arreglo_informe_reportes    = [[""]*8   for _ in range(8)]  # Arreglo bidimensional de 8x8 de caracteres
arreglo_reportes            = [[["" for _ in range(2)] for _ in range(8)] for _ in range(8)] # Arreglo tridimensional de 8x8x2 de strings
arreglo_me_gusta            = [[0]*8    for i in range(8)]  # Arreglo bidimensional de 8x8 de enteros
arreglo_sesion              = [False]*2                     # Arreglo unidimensional de booleanos
arreglo_usuarios            = [0]*3                         # Arreglo unidimensional de enteros

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

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def popular_db_estudiantes(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    for i in range(4):        
        arreglo_de_estudiantes[i][0] = str(i)
        arreglo_de_estudiantes[i][1] = "est" + str(i+1)
        arreglo_de_estudiantes[i][2] = "est" + str(i+1)
        arreglo_de_estudiantes[i][3] = "est" + str(i+1) + "@ayed.com"
        arreglo_de_estudiantes[i][4] = "est" + str(i+1)
        arreglo_de_estudiantes[i][5] = "estudiante"
        arreglo_de_estudiantes[i][8] = str(random.randint(1,30))+"-"+str(random.randint(1, 12))+"-"+"19"+str(random.randint(80, 99))
        arreglo_de_estudiantes[i][9] = "activo"

    arreglo_usuarios[ESTUDIANTES_INDEX] = 4

#popular_db_estudiantes(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes)


"""
FUNCIÓN
arr: arreglo unidimensional de enteros
i, j, aux: enteros
"""
def ordenar_arreglo(arr):
    for i in range(0, 6):
        for j in range(0, 6-i-1):
            if arr[j] > arr[j+1]:
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
    return arr
"""
FUNCIÓN
izquierda, derecha, medio: enteros
arr: arreglo unidimensional de enteros
"""
def busqueda_dicotomica(arr, x):
    izquierda = 0
    derecha = 6
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == x:
            return medio
        elif arr[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return izquierda

"""
PROCEDIMIENTO
edades : enteros
"""
def encontrar_huecos(edades):
    edades = ordenar_arreglo(edades)
    huecos = 0
    actual = edades[0]
    fin = edades[-1]

    for i in range(actual, fin):
        idx = busqueda_dicotomica(edades, i)
        if idx >= 6 or edades[idx] != i:
            huecos += 1
    os.system("cls")
    print("Huecos encontrados:", huecos)

"""
PROCEDIMIENTO
matcheosposibles , ESTUDIANTES_INDEX:  enteros
arreglo_usuarios : arreglo unidimensional de enteros
"""
def matcheos_posibles():
    os.system("cls")
    matcheosposibles = (arreglo_usuarios[ESTUDIANTES_INDEX]* (arreglo_usuarios[ESTUDIANTES_INDEX] - 1))//2
    print("Cantidad de matcheos posibles: ", matcheosposibles)

"""
PROCEDIMIENTO mostrar_menu_estudiante
MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, ESTUDIANTES_INDEX, MODERADORES_INDEX, opc: enteros

arreglo_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_de_moderadores:     arreglo bidimensional de 8*8 de strings
arreglo_informe_reportes:   arreglo bidimensional de 8x8 de caracteres
arreglo_reportes:           arreglo bidimensional de 8x8 de strings
"""
def mostrar_menu_estudiante():
    print("\nMenu ")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir\n")

"""
PROCEDIMIENTO menu_estudiante
ESTUDIANTES_INDEX, USUARIO_INDEX, opc: enteros

arreglo_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def menu_estudiante(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta, USUARIO_INDEX):
    mostrar_menu_estudiante()
    
    opc = validar_numero()
    while opc < 0 and opc > 4:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                gestionar_mi_perfil(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, USUARIO_INDEX)
            case 2:
                gestionar_candidatos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)
            case 3:
                matcheos()
            case 4:
                mostrar_reportes_estadisticos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes)

        os.system("cls")
        mostrar_menu_estudiante()
        opc = validar_numero()
        while opc < 0 and opc > 4:
            print("Opción inválida")
            opc = validar_numero()
    
    arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][10] = 0
    os.system("cls")

"""
PROCEDIMIENTO gestionar_mi_perfil
ESTUDIANTES_INDEX, USUARIO_INDEX: enteros
opc: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8x12 de strings
"""
def gestionar_mi_perfil(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, USUARIO_INDEX):    
    os.system("cls")
    print("\nGestionar mi perfil\n")
    print("a. Editar mis datos personales")
    print("b. Eliminar mi perfil")    
    print("c. Volver\n") 

    opc = str(input("Ingrese su opción: "))

    while opc != "c":
        match opc:
            case "a": 
                editar_mis_datos_personales(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, USUARIO_INDEX)
            case "b":
                eliminar_mi_perfil(arreglo_usuarios, arreglo_de_estudiantes, USUARIO_INDEX) 
    
        os.system("cls")    
        print("\nGestionar mi perfil\n")
        print("a. Editar mis datos personales")
        print("b. Eliminar mi perfil")    
        print("c. Volver\n") 
        opc = str(input("Ingrese de nuevo: "))

"""
PROCEDIMIENTO editar_mis_datos_personales
ESTUDIANTES_INDEX, USUARIO_INDEX: enteros
opc: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8x12 de strings
"""
def editar_mis_datos_personales(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, USUARIO_INDEX):
    os.system("cls")

    mostrar_menu_de_mis_datos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, USUARIO_INDEX)

    print("\nEditar mis datos personales\n")
    print("a. Editar mi fecha de nacimiento")
    print("b. Editar mi biografía")
    print("c. Editar mis hobbies")
    print("d. Eliminar mis me gusta")
    print("e. Volver\n")  
    opc = str(input("Ingrese su opción: "))

    while opc != "e":
        match opc:    
            case "a": 
                editar_mi_fecha_de_nacimiento(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes)
            case "b":
                editar_mi_biografia(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes)          
            case "c":
                editar_mis_hobbies(arreglo_usuarios, USUARIO_INDEX, arreglo_de_estudiantes)  
            case "d":
                eliminar_mis_me_gusta(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes)

        os.system("cls")
        mostrar_menu_de_mis_datos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, USUARIO_INDEX)

        print("\nEditar mis datos personales\n")
        print("a. Editar mi fecha de nacimiento")
        print("b. Editar mi biografía")
        print("c. Editar mis hobbies")  
        print("d. Eliminar mis me gusta")
        print("e. Volver\n")   
        opc = str(input("Ingrese de nuevo: "))

"""
PROCEDIMIENTO mostrar_menu_de_mis_datos
ESTUDIANTES_INDEX, USUARIO_INDEX, i: enteros

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def mostrar_menu_de_mis_datos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, USUARIO_INDEX):
    print("\nMi ID: ", arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][0])
    print("Mi nombre: ", arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][1])
    print("Mi apellido: ", arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][2])
    print("Mi fecha de nacimiento: ", arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][8])
    print("Mi biografia: ", arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][11])
    print("Mi edad: ", mostrar_edad(arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][8] or ""), "años")
    print("Mis hobbies: ", arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][6])
    mostrar_mis_me_gusta(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)
    print("Mi estado: ", arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][9])

"""
PROCEDIMIENTO editar_mi_fecha_de_nacimiento
ESTUDIANTES_INDEX, i: enteros
nueva_fecha_de_nacimiento: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def editar_mi_fecha_de_nacimiento(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    nueva_fecha_de_nacimiento = str(input("Ingrese su fecha de nacimiento: "))
    arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][8] = nueva_fecha_de_nacimiento

"""
PROCEDIMIENTO editar_mi_biografia
ESTUDIANTES_INDEX, i: enteros
nueva_biografia: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def editar_mi_biografia(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    nueva_biografia = str(input("Ingrese su biografia: "))
    arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][11] = nueva_biografia

"""
PROCEDIMIENTO editar_mis_hobbies
ESTUDIANTES_INDEX, MODERADORES_INDEX, i: enteros
nuevos_hobbies: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def editar_mis_hobbies(arreglo_usuarios, USUARIO_INDEX, arreglo_de_estudiantes):
    nuevos_hobbies = str(input("Ingrese sus hobbies: "))
    arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][6] = nuevos_hobbies

"""
PROCEDIMIENTO eliminar_mis_me_gusta
ESTUDIANTES_INDEX, i, j: enteros
eliminar_me_gusta: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def eliminar_mis_me_gusta(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    mostrar_mis_me_gusta(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)
    eliminar_me_gusta = str(input("Ingrese nombre de usuario para eliminar de la lista: "))
    for j in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
        if eliminar_me_gusta == arreglo_de_estudiantes[j][1]:
            arreglo_me_gusta[arreglo_usuarios[USUARIO_INDEX]][j] = 0
        else:
            print("Error")

"""
PROCEDIMIENTO mostrar_me_gusta
ESTUDIANTES_INDEX, MODERADORES_INDEX, i, j: enteros

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_me_gusta:           arreglo bidimensional de 8x8 de enteros
"""
def mostrar_mis_me_gusta(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta):
    print("\nMis me gusta\n")
    for j in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
        if arreglo_me_gusta[arreglo_usuarios[USUARIO_INDEX]][j] == 1 and arreglo_de_estudiantes[j][1] != "":
            print (arreglo_de_estudiantes[j][1])

def mostrar_me_gusta(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta, i):
    print("\nMis me gusta\n")
    for j in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
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

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_me_gusta:           arreglo unidimensional de 8*8 de enteros
"""
def mostrar_datos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta):   ## MODELO ESTUDIANTE
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
    for i in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
        print("\nID: ",arreglo_de_estudiantes[i][0])
        print("Nombre: ", arreglo_de_estudiantes[i][1])
        print("Apellido: ", arreglo_de_estudiantes[i][2])
        print("Email: ", arreglo_de_estudiantes[i][3])
        print("Fecha de nacimiento: ", arreglo_de_estudiantes[i][8])
        print("Biografia: ", arreglo_de_estudiantes[i][11])
        print("Edad: ", mostrar_edad(arreglo_de_estudiantes[i][8]), "años")
        print("Hobbies: ", arreglo_de_estudiantes[i][6])
        mostrar_me_gusta(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta, i)
        print("Estado: ", arreglo_de_estudiantes[i][9])

"""
PROCEDIMIENTO me_gusta
ESTUDIANTES_INDEX, i, j: enteros
megusta: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_me_gusta:
"""
def me_gusta(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta):
    print("\nDar me gusta\n")
    megusta = str(input("Ingresar nombre de estudiante: "))
    for j in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
        if arreglo_usuarios[USUARIO_INDEX] != j:
            if megusta == arreglo_de_estudiantes[j][1]:
                arreglo_me_gusta[arreglo_usuarios[USUARIO_INDEX]][j] = 1           

"""
PROCEDIMIENTO eliminar_mi_perfil
USUARIO_INDEX: enteros
opc: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def eliminar_mi_perfil(arreglo_usuarios, arreglo_de_estudiantes, USUARIO_INDEX):
    os.system("cls")
    print("\nEliminar mi perfil")
    print("Cuidado! Al aceptar se eliminara todo tu perfi!\n")
    print("a. Si, continuar")
    print("b. No. Volver")
    
    opc = str(input("Ingrese su opción: "))
    while opc != "a" and opc != "b":
        print("Ingrese de nuevo: ")
        opc = str(input("Ingrese su opción: "))
  
    match opc:
        case "a": 
            arreglo_de_estudiantes[arreglo_usuarios[USUARIO_INDEX]][9] = "inactivo"

"""
PROCEDIMIENTO gestionar_candidatos
ESTUDIANTES_INDEX: enteros
opc: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8x12 de strings
arreglo_me_gusta:           arreglo unidimensional de enteros
"""
def gestionar_candidatos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta):
    os.system("cls")

    print("\nGestionar candidatos\n")
    print("a. Ver candidatos")
    print("b. Reportar candidato")    
    print("c. Volver") 
    opc = str(input("Ingrese su opción: "))

    while opc != "c":
        match opc:
            case "a":
                ver_candidatos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)
            case "b":
                reportar_candidato(arreglo_usuarios, ESTUDIANTES_INDEX)


        os.system("cls")
        print("\nGestionar candidatos\n")
        print("a. Ver candidatos")
        print("b. Reportar candidato")    
        print("c. Volver") 
        opc = str(input("Ingrese de nuevo: "))

"""
PROCEDIMIENTO ver_candidatos
ESTUDIANTES_INDEX: enteros
opc: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_me_gusta:           arreglo unidimensional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def ver_candidatos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta):
    print("\nCandidatos\n")
    mostrar_datos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)
    print("\n\na. Dar me gusta")
    print("b. Volver")

    opc = str(input("Ingrese su opción: "))
    while opc != "b":
        match opc:
            case "a":
                me_gusta(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)

        os.system("cls")
        print("\nCandidatos\n")
        mostrar_datos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta)
        print("\n\na. Dar me gusta")
        print("b. Volver")
        opc = str(input("Ingrese de nuevo: "))

"""
PROCEDIMIENTO reportar_candidato
ESTUDIANTES_INDEX, i, j: enteros
reportado, reporte: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_informe_reportes:   arreglo bidimensional de 8x8 de caracteres
arreglo_reportes:           arreglo bidimensional de 8x8 de strings
"""
def reportar_candidato(arreglo_usuarios, ESTUDIANTES_INDEX):
    os.system("cls")
    print("\nReportar candidatos")

    reportado = str(input("Ingrese nombre o ID de usuario a reportar: "))
    reporte = str(input("Ingrese su reporte: "))
    for j in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
        if reportado == str(arreglo_de_estudiantes[j][1]) or reportado == str(arreglo_de_estudiantes[j][0]):
            arreglo_reportes[arreglo_usuarios[USUARIO_INDEX]][j][0] = "0"
            arreglo_reportes[arreglo_usuarios[USUARIO_INDEX]][j][1] = reporte
            print("\nReporte exitoso.")
                    
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
        opc = str(input("Ingrese de nuevo: "))

"""
PROCEDIMIENTO mostrar_reportes_estadisticos
ESTUDIANTES_INDEX: enteros
opc: string

arreglo_usuarios:   arreglo unidimesional de enteros
"""
def mostrar_reportes_estadisticos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes):
    os.system("cls")
    print("\nReportes estadísticos\n")
    mostrar_porcentaje_matcheos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_me_gusta)
    mostrar_likes_dados(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes)
    mostrar_likes_recibidos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes)
    print("a. Volver")
    opc = str(input("Ingrese su opción: "))

    while opc != "a":
        os.system("cls")
        print("\nReportes estadísticos\n")
        mostrar_porcentaje_matcheos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_me_gusta)
        mostrar_likes_dados(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes)
        mostrar_likes_recibidos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes)
        print("a. Volver")  
        opc = str(input("Ingrese de nuevo: "))

"""
PROCEDIMIENTO mostrar_porcentaje_matcheos
ESTUDIANTES_INDEX, i, j, matcheos: enteros
porcentaje: float

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def mostrar_porcentaje_matcheos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_me_gusta):
    matcheos = 0
    for j in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
        if arreglo_me_gusta[arreglo_usuarios[USUARIO_INDEX]][j] == 1 and arreglo_me_gusta[j][arreglo_usuarios[USUARIO_INDEX]] == 1:
            matcheos = matcheos + 1

    porcentaje = (matcheos * 100)//arreglo_usuarios[ESTUDIANTES_INDEX]
    print("Matcheados sobre el % posible: ", porcentaje, "%")

"""
PROCEDIMIENTO mostrar_likes_dados
ESTUDIANTES_INDEX, i, j, contador: enteros

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_me_gusta:     arreglo bidimensional de 8*8 de enteros
"""
def mostrar_likes_dados(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes):
    contador = 0
    for j in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
        if arreglo_me_gusta[arreglo_usuarios[USUARIO_INDEX]][j] == 1 and arreglo_me_gusta[j][arreglo_usuarios[USUARIO_INDEX]] == 0:
            contador = contador + 1
    
    print("Likes dados y no recibidos: ", contador)

"""
PROCEDIMIENTO mostrar_likes_recibidos
ESTUDIANTES_INDEX, i, j, contador: enteros

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_me_gusta:     arreglo bidimensional de 8*8 de enteros
"""
def mostrar_likes_recibidos(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_me_gusta, arreglo_de_estudiantes):
    contador = 0
   
    for j in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
        if arreglo_me_gusta[arreglo_usuarios[USUARIO_INDEX]][j] == 0 and arreglo_me_gusta[j][arreglo_usuarios[USUARIO_INDEX]] == 1:
            contador = contador + 1
    
    print("Likes recibidos y no respondidos: ", contador)

"""
PROCEDIMIENTO
"""
def mostrar_menu_moderadores():
        print("\nMenu Moderadores\n")
        print("1. Gestionar usuarios")
        print("2. Gestionar reportes")
        print("3. Reportes estadísticos")
        print("0. Salir\n")

"""
PROCEDIMIENTO menu_moderadores
ESTUDIANTES_INDEX, MODERADORES_INDEX, opc: enteros

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_informe_reportes:   arreglo bidimensional de 8x8 de caracteres
arreglo_reportes:           arreglo bidimensional de 8x8 de strings
"""
def menu_moderadores(arreglo_usuarios, MODERADORES_INDEX, ESTUDIANTES_INDEX, arreglo_reportes, arreglo_informe_reportes):
    mostrar_menu_moderadores()
    opc = validar_numero()
    while opc < 0 and opc > 3:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                gestionar_usuarios(arreglo_usuarios, ESTUDIANTES_INDEX)
            case 2:
                gestionar_reportes(arreglo_reportes, arreglo_informe_reportes, arreglo_usuarios, ESTUDIANTES_INDEX)
            case 3:
                mostrar_menu_reportes_estadisticos()

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

arreglo_usuarios:   arreglo unidimesional de enteros
"""
def gestionar_usuarios(arreglo_usuarios, ESTUDIANTES_INDEX):
    os.system("cls")
    print("\nGestionar usuarios\n")
    print("a. Desactivar usuario")  
    print("b. Volver\n") 
    opc = str(input("Ingrese su opción: "))

    while opc != "b":
        match opc:
            case "a":
                desactivar_usuario(arreglo_usuarios, ESTUDIANTES_INDEX)

        os.system("cls")
        print("\nGestionar usuarios\n")
        print("a. Desactivar usuario")  
        print("b. Volver\n") 
        opc = str(input("Ingrese de nuevo: "))

"""
PROCEDIMIENTO desactivar_usuario
i, ESTUDIANTES_INDEX: enteros
opc, desactivar: string

arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_usuarios    arreglo unidimensional de enteros
"""
def desactivar_usuario(arreglo_usuarios, ESTUDIANTES_INDEX):
    os.system("cls")
    print("\nDesactivar usuario\n")
    desactivar = str(input("Ingresar nombre o ID de usuario a desactivar: "))
    for i in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
        if desactivar == arreglo_de_estudiantes[i][0] or desactivar == arreglo_de_estudiantes[i][1]:
            arreglo_de_estudiantes[i][9] = "inactivo"

"""
PROCEDIMIENTO gestionar_reportes
opc: string

arreglo_reportes:           arreglo bidimensional de 8x8 de strings
arreglo_informe_reportes:   arreglo bidimensional de 8x8 de caracteres
"""
def gestionar_reportes(arreglo_reportes, arreglo_informe_reportes, arreglo_usuarios, ESTUDIANTES_INDEX):
    os.system("cls")
    print("\nGestionar reportes\n")
    print("a. Ver reportes")  
    print("b. Volver") 
    opc = str(input("Ingrese su opción: "))

    while opc != "b":
        match opc:
            case "a":
                ver_reportes(arreglo_reportes, arreglo_informe_reportes, arreglo_usuarios, ESTUDIANTES_INDEX)
        print("\nGestionar reportes\n")
        print("a. Ver reportes")  
        print("b. Volver") 
        opc = str(input("Ingrese de nuevo: "))

"""
PROCEDIMIENTO ver_reportes
i, j, k: enteros
opc: string

arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_reportes:           arreglo bidimensional de 8x8 de strings
arreglo_informe_reportes:   arreglo bidimensional de 8x8 de caracteres
"""
def ver_reportes(arreglo_reportes, arreglo_informe_reportes, arreglo_usuarios, ESTUDIANTES_INDEX):   

    for i in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
        os.system("cls")
        print("\nReportes\n")
        for j in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
            if i != j:
                if  arreglo_reportes[i][j][0] == "0":                    
                    if arreglo_reportes[i][j][0] == "0":
                        print("\nReporte")
                        print("ID de reportante: ", arreglo_de_estudiantes[i][0])
                        print("ID de reportado: ", arreglo_de_estudiantes[j][0])
                        print("Motivo: ", arreglo_reportes[i][j][1])
                        print("\n¿Que acción desea tomar?\n")
                        print("a. Ignorar reporte")
                        print("b. Desactivar usuario")
                        opc = str(input("Ingrese su opción:"))
                        while opc != "a" and opc != "b":
                            print("ID de reportante: ", arreglo_de_estudiantes[i][0])
                            print("ID de reportado: ", arreglo_de_estudiantes[j][0])
                            print("Motivo: ", arreglo_reportes[i][j][1])
                            print("\n¿Que acción desea tomar?\n")
                            print("a. Ignorar reporte")
                            print("b. Desactivar usuario")
                            opc = str(input("Ingrese de nuevo: "))
                        match opc:
                            case "a":
                                arreglo_reportes[i][j][0] = "2"
                            case "b":
                                arreglo_reportes[i][j][0] = "1"
                                arreglo_de_estudiantes[j][9] = "inactivo"
                        print("\nEl reporte ha sido tomado\n")
        else:
            print("No hay reportes pendientes")

"""
PROCEDIMIENTO mostrar_menu_reportes_estadisticos
opc: enteros

"""
def mostrar_menu_reportes_estadisticos():
    print("\nReportes estadisticos\n")
    print("En construcción")  
    print("a. Volver\n") 
    opc = str(input("Ingrese su opción: "))

    while opc != "a":
        print("\nReportes estadisticos\n")
        print("En construcción")  
        print("a. Volver\n") 
        opc = str(input("Ingrese de nuevo: "))

"""
PROCEDIMIENTO validar_ingreso
ESTUDIANTES_INDEX, USUARIO_INDEX, MODERADORES_INDEX, intentos, i: enteros
email, contraseña: string

arreglo_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_de_moderadores:     arreglo bidimensional de 8*8 de strings
arreglo_me_gusta:           arreglo bidimensional de 8*8 de enteros
"""
def validar_ingreso(arreglo_usuarios, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_sesion, arreglo_reportes, arreglo_informe_reportes, arreglo_me_gusta, USUARIO_INDEX):
    intentos = 3

    email = input("Ingrese su email: ")
    contraseña = getpass.getpass("Ingrese su contraseña: ")
    while intentos > 1 and (not arreglo_sesion[ESTUDIANTES_INDEX] and not arreglo_sesion[MODERADORES_INDEX]):
        for i in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
            if ((email == arreglo_de_estudiantes[i][3] and contraseña == arreglo_de_estudiantes[i][4] and arreglo_de_estudiantes[i][9] == "activo")):
                arreglo_sesion[ESTUDIANTES_INDEX] = True
                arreglo_usuarios[USUARIO_INDEX] = i
                os.system("cls")
                print("Sesión iniciada correctamente")
                menu_estudiante(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes, arreglo_me_gusta, USUARIO_INDEX)

        for i in range(arreglo_usuarios[MODERADORES_INDEX]):
            if (email == arreglo_de_moderadores[i][3] and contraseña == arreglo_de_moderadores[i][4]):
                arreglo_sesion[MODERADORES_INDEX] = True
                os.system("cls")
                print("Sesión iniciada correctamente")
                menu_moderadores(arreglo_usuarios, MODERADORES_INDEX, ESTUDIANTES_INDEX, arreglo_reportes, arreglo_informe_reportes)

        if(not arreglo_sesion[ESTUDIANTES_INDEX] and not arreglo_sesion[MODERADORES_INDEX]):
            os.system("cls")
            print("Email o contraseña incorrectos")
            intentos -= 1
            print("\nQuedan ", intentos, "intentos\n")
            email = input("Ingrese su email: ")
            contraseña = getpass.getpass("Ingrese su contraseña: ")
    os.system("cls")

"""
PROCEDIMIENTO ingresar
MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, ESTUDIANTES_INDEX, MODERADORES_INDEX, USUARIO_INDEX: enteros

arreglo_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_reportes
arreglo_informe_reportes
arreglo_me_gusta:           arreglo bidimensional de 8*8 de enteros
"""
def ingresar(MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, arreglo_sesion, arreglo_usuarios, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_reportes, arreglo_informe_reportes, arreglo_me_gusta, USUARIO_INDEX):
    os.system("cls")
    if(MIN_CANT_ESTUDIANTES <= arreglo_usuarios[ESTUDIANTES_INDEX] and MIN_CANT_MODERADORES <= arreglo_usuarios[MODERADORES_INDEX]):        
        arreglo_sesion[MODERADORES_INDEX] = False
        arreglo_sesion[ESTUDIANTES_INDEX] = False
        validar_ingreso(arreglo_usuarios, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_sesion, arreglo_reportes, arreglo_informe_reportes, arreglo_me_gusta, USUARIO_INDEX)
    else:        
        print("No se puede ingresar, cantidad de estudiantes y moderadores insuficientes")

"""
PROCEDIMIENTO ingresar_datos_moderadores
MODERADORES_INDEX: enteros
nombre, apellido, email, contraseña, confirmar_contraseña: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_moderadores:     arreglo bidimensional de 8*8 de strings
"""
def ingresar_datos_moderadores(arreglo_usuarios, MODERADORES_INDEX, arreglo_de_moderadores ):
    os.system("cls")
    nombre = input("Ingrese el nombre del moderador: ")
    apellido = input("Ingrese el apellido del moderador: ")
    email = input("Ingrese el email del moderador: ")
    arreglo_de_moderadores[arreglo_usuarios[MODERADORES_INDEX]][0] = str(arreglo_usuarios[MODERADORES_INDEX])
    arreglo_de_moderadores[arreglo_usuarios[MODERADORES_INDEX]][1] = nombre
    arreglo_de_moderadores[arreglo_usuarios[MODERADORES_INDEX]][2] = apellido
    arreglo_de_moderadores[arreglo_usuarios[MODERADORES_INDEX]][3] = email
    arreglo_de_moderadores[arreglo_usuarios[MODERADORES_INDEX]][5] = "moderador"

    contraseña = input("Ingrese su contraseña: ")
    confirmar_contraseña = input("Vuelva a ingresar su contraseña: ")
    while contraseña != confirmar_contraseña:
        print("La contraseña no coincide, vuelva a intentar: ")
        contraseña = input("Ingrese su contraseña: ")
        confirmar_contraseña = input("Vuelva a ingresar su contraseña: ")

    if contraseña == confirmar_contraseña:
        arreglo_de_moderadores[arreglo_usuarios[MODERADORES_INDEX]][4] = contraseña

"""
PROCEDIMIENTO ingresar_datos_de_estudiantes
ESTUDIANTES_INDEX: enteros
nombre, apellido, email, contraseña, confirmar_contraseña: string

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def ingresar_datos_de_estudiantes(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes ):
    os.system("cls")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    email = input("Ingrese el email del estudiante: ")
    arreglo_de_estudiantes[arreglo_usuarios[ESTUDIANTES_INDEX]][0] = str(arreglo_usuarios[ESTUDIANTES_INDEX])
    arreglo_de_estudiantes[arreglo_usuarios[ESTUDIANTES_INDEX]][1] = nombre
    arreglo_de_estudiantes[arreglo_usuarios[ESTUDIANTES_INDEX]][2] = apellido
    arreglo_de_estudiantes[arreglo_usuarios[ESTUDIANTES_INDEX]][3] = email
    arreglo_de_estudiantes[arreglo_usuarios[ESTUDIANTES_INDEX]][5] = "estudiante"
    arreglo_de_estudiantes[arreglo_usuarios[ESTUDIANTES_INDEX]][9] = "activo"

    contraseña = input("Ingrese su contraseña: ")
    confirmar_contraseña = input("Vuelva a ingresar su contraseña: ")    
    while contraseña != confirmar_contraseña:
        print("La contraseña no coincide, vuelva a intentar: ")
        contraseña = input("Ingrese su contraseña: ")
        confirmar_contraseña = input("Vuelva a ingresar su contraseña: ")

    if contraseña == confirmar_contraseña:
        arreglo_de_estudiantes[arreglo_usuarios[ESTUDIANTES_INDEX]][4] = contraseña

"""
PROCEDIMIENTO registrar_estudiante
MAX_CANT_ESTUDIANTES, ESTUDIANTES_INDEX: enteros

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def registrar_estudiante(arreglo_usuarios, MAX_CANT_ESTUDIANTES, ESTUDIANTES_INDEX, arreglo_de_estudiantes):
    global arFiEst, arLoEst

    estudiante = Estudiante()
    continuar = str(input("Seguro deasea registrar un estudiante (S/N)?: "))
    # ingresar_datos_de_estudiantes(arreglo_usuarios, ESTUDIANTES_INDEX, arreglo_de_estudiantes)
    continuar.upper()
    while continuar != "S" and continuar != "N":
        print("Por favor, ingrese una opción válida (S/N)")
        continuar = str(input("Seguro deasea registrar un estudiante (S/N)?: "))
        continuar.upper()
    while continuar == "S":
        if os.path.getsize(arFiEst) == 0:
            estudiante.id = 1
        else:
            arLoEst.seek(0,0)
            estudiante = pickle.load(arLoEst)
            tamReg = arLoEst.tell()
            tamArc = os.path.getsize(arFiEst)
            cantReg = tamArc // tamReg
            estudiante.id = cantReg + 1




    os.system("cls")
    print("Estudiante registrado")

"""
PROCEDIMIENTO registrar_moderador
MAX_CANT_MODERADORES, MODERADORES_INDEX: enteros

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_moderadores:     arreglo bidimensional de 8*8 de strings
"""
def registrar_moderador(arreglo_usuarios, MAX_CANT_MODERADORES, MODERADORES_INDEX, arreglo_de_moderadores):
    if (arreglo_usuarios[MODERADORES_INDEX] < MAX_CANT_MODERADORES):
        ingresar_datos_moderadores(arreglo_usuarios, MODERADORES_INDEX, arreglo_de_moderadores)
        os.system("cls")
        arreglo_usuarios[MODERADORES_INDEX] = arreglo_usuarios[MODERADORES_INDEX]+1
        print("Moderador registrado")
    else:
        print("Todos los moderadores fueron cargados")

"""
PROCEDIMIENTO registrar
MAX_CANT_ESTUDIANTES, MAX_CANT_MODERADORES, ESTUDIANTES_INDEX, MODERADORES_INDEX, opc: enteros

arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
"""
def registrar(MAX_CANT_ESTUDIANTES, MAX_CANT_MODERADORES, arreglo_usuarios, ESTUDIANTES_INDEX , MODERADORES_INDEX, arreglo_de_estudiantes, arreglo_de_moderadores):
    
    mostrar_menu_registrar()

    opc = str(input("Ingrese su opción: "))
    while opc != "c":
        match opc:
            case "a": 
                registrar_estudiante(arreglo_usuarios, MAX_CANT_ESTUDIANTES, ESTUDIANTES_INDEX, arreglo_de_estudiantes) # type: ignore            
            case "b": 
                registrar_moderador(arreglo_usuarios, MAX_CANT_MODERADORES, MODERADORES_INDEX, arreglo_de_moderadores) # type: ignore            
           
        mostrar_menu_registrar()
        opc = str(input("Ingrese su opción: "))
    os.system("cls")

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
    os.system("cls")
    print("\nRegistrar usuario\n")
    print(" a. Registrar estudiante")
    print(" b. Registrar moderador")
    print(" c. Volver\n")

"""
PROCEDIMIENTO mostrar_menu_principal
"""
def mostrar_menu_principal():
    print("\nMenu ")
    print("\n1. Registro")
    print("2. Iniciar sesion")
    print("0. Salir\n")

"""
PROCEDIMIENTO abrir_archivos
arFiAdmin, arFiMod, arFiEst: string

arLoAdmin: 
arLoMod: 
arLoEst: 
"""
def abrir_archivos():
    global arFiAdmin, arLoAdmin, arFiMod, arLoMod, arFiEst, arLoEst

    arFiAdmin = "registroAdmins.dat"
    arFiMod = "registroMods.dat"
    arFiEst = "registroEsts.dat"

    if os.path.exists(arFiEst):
        arLoEst = open(arFiEst, "r+b")
    else:
        print(f"El archivo {arFiEst} se creo")
        arLoEst = open(arFiEst, "w+b")

    if os.path.exists(arFiAdmin):
        arLoAdmin = open(arFiAdmin, "r+b")
    else:
        print(f"El archivo {arFiAdmin} se creo")
        arLoAdmin = open(arFiAdmin, "w+b") 

    if os.path.exists(arFiMod):
        arLoMod = open(arFiMod, "r+b")
    else:
        print(f"El archivo {arFiAdmin} se creo")
        arLoMod = open(arFiMod, "w+b")       

def cerrar_archivos():
    global arFiAdmin, arLoAdmin, arFiMod, arLoMod, arFiEst, arLoEst
    arLoEst.close()
    arLoAdmin.close()
    arLoMod.close()
    print("Archivos cerrados")

"""
PROCEDIMIENTO ejecutar_programa_principal
MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, USUARIO_INDEX, ESTUDIANTES_INDEX, MODERADORES_INDEX, opc: enteros

arreglo_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios:   arreglo unidimesional de enteros
arreglo_de_estudiantes:     arreglo bidimensional de 8*12 de strings
arreglo_de_moderadores:     arreglo bidimensional de 8*8 de strings
arreglo_informe_reportes:   arreglo bidimensional de 8x8 de caracteres
arreglo_reportes:           arreglo bidimensional de 8x8 de strings
arreglo_me_gusta:           arreglo bidimensional de 8*8 de enteros
"""
def ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, arreglo_sesion, arreglo_usuarios, arreglo_de_estudiantes, arreglo_de_moderadores, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_reportes, arreglo_informe_reportes, arreglo_me_gusta, USUARIO_INDEX):
    
    ## iniciar archivos
    abrir_archivos()
    mostrar_menu_principal()     
    opc = validar_numero()
    while opc < 0 and opc > 4:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                registrar(MAX_CANT_ESTUDIANTES, MAX_CANT_MODERADORES, arreglo_usuarios, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_de_estudiantes, arreglo_de_moderadores)
            case 2:
                ingresar(MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, arreglo_sesion, arreglo_usuarios, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_reportes, arreglo_informe_reportes, arreglo_me_gusta, USUARIO_INDEX)
            case 3:
                encontrar_huecos([21, 18, 20, 19, 23, 24])
            case 4:
                matcheos_posibles()

        mostrar_menu_principal()
        opc = validar_numero()
        while opc < 0 and opc > 4:
            print("Opción inválida")
            opc = validar_numero()

    os.system("cls")
    cerrar_archivos()
    print("\nPrograma finalizado, esperamos tu regreso...\n")

global arFiAdmin, arLoAdmin, arFiMod, arLoMod, arFiEst, arLoEst  

ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, arreglo_sesion, arreglo_usuarios, arreglo_de_estudiantes, arreglo_de_moderadores, ESTUDIANTES_INDEX, MODERADORES_INDEX, arreglo_reportes, arreglo_informe_reportes, arreglo_me_gusta, USUARIO_INDEX)