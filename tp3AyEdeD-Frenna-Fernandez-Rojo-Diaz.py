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
import emoji

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
        self.contrasena = ""    #string 32

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
        self.contrasena = ""    #string 32
        self.estado = False     #boolean
        self.ignorado = 0       #int
        self.aceptado = 0       #int
        self.baja = "N"         #char

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
        self.contrasena = ""        #string 32
        self.sexo = ""              #char
        self.estado = False         #boolean
        self.baja = "N"             #char
        self.hobbies = ""           #string 255
        self.materia_favorita = ""  #string 16
        self.deporte_favorito = ""  #string 16
        self.materia_fuerte = ""    #string 16
        self.materia_debil = ""     #string 16
        self.biografia = ""         #string 255
        self.pais = ""              #string 32
        self.ciudad = ""            #string 32        
        self.fecha_nacimiento = ""  #string 10

""" MODELO LIKES
# 0 remitente: int
# 1 destinatario: int
# 2 activo: char
"""
class Likes:
    def __init__(self):
        self.id_remitente = 0       #int
        self.id_destinatario = 0    #int
        self.activo = "S"           #char

class Reportes:
    def __init__(self):
        self.id_reportante = 0      #int
        self.id_reportado = 0       #int
        self.motivo = ""            #string 255
        self.estado = 0             #int 0 reportado por ver, 1 usuario baneado, 2 omitido

# Constantes

global arFiAdmin, arLoAdmin, arFiMod, arLoMod, arFiEst, arLoEst, arFiLi, arLoLi, arFiRep, arLoRep

MIN_CANT_ESTUDIANTES  = 4   # enteros
MAX_CANT_ESTUDIANTES  = 8   # enteros
MIN_CANT_MODERADORES  = 1   # enteros
MAX_CANT_MODERADORES  = 4   # enteros
ESTUDIANTES_INDEX  = 0      # enteros
MODERADORES_INDEX  = 1      # enteros
USUARIO_INDEX = 2           # enteros
ADMINISTRADOR_INDEX = 3     # enteros

arreglo_sesion              = [False]*4                     # Arreglo unidimensional de booleanos
arreglo_usuarios            = [0]*3                         # Arreglo unidimensional de enteros

"""            
PROCEDIMIENTO calcular_puntaje_candidatos
arLoLi, arLoEst: BufferedRandom
arFiLi, arFiEst: str
tamArcLikes, tamArcEst, puntaje, racha: enteros
"""
def calcular_puntaje_candidatos():
    global arLoLi, arLoEst, arFiLi, arFiEst

    tamArcLikes = os.path.getsize(arFiLi)
    tamArcEst = os.path.getsize(arFiEst)
    
    if tamArcLikes == 0 or tamArcEst == 0:
        print("No hay likes o estudiantes registrados.")
        return
    
    print("\nPuntajes de todos los estudiantes:")
    
    arLoEst.seek(0, 0)  # Asegurarse de que estamos al comienzo del archivo de estudiantes
    while arLoEst.tell() < tamArcEst:
        estudiante = pickle.load(arLoEst)  # Leer cada estudiante
        puntaje = 0
        racha = 0
        
        if estudiante.baja == "N":  # Solo procesar estudiantes activos
            # Recorrer el archivo de likes para calcular los puntos de este estudiante
            arLoLi.seek(0, 0)  # Reiniciar el puntero de likes para cada estudiante
            while arLoLi.tell() < tamArcLikes:
                like = pickle.load(arLoLi)
                
                # Verificar si el estudiante es el remitente del like y si es activo
                if like.id_remitente == estudiante.id_estudiante and like.activo == "S":
                    if mostrar_si_dio_like(like.id_destinatario, like.id_remitente):
                        puntaje += 1  # Sumar 1 punto por match
                        racha += 1  # Aumentar racha
                    else:
                        puntaje -= 1  # Restar 1 punto por like no correspondido
                        racha = 0  # Resetear la racha si no hay match
            
            # Sumar puntos adicionales por racha de 3 o más likes correspondidos
            if racha >= 3:
                puntaje += 1
            
            # Mostrar el puntaje del estudiante actual
            print(f"{estudiante.nombre.strip()}: {puntaje} puntos")
    
    # Resetear la posición de lectura de estudiantes
    arLoEst.seek(0, 0)

""""
PROCEDIMIENTO popular_likes_aleatorios
arLoLi: BufferedRandom
arFiLi: str
like: Likes
likePos, i: entero
"""
def popular_likes_aleatorios():
    global arLoLi, arFiLi

    like = Likes()
    likePos = 0
    if os.path.getsize(arFiLi) == 0:        
        for i in range(4):
            arLoLi.seek(likePos, 0)
            like.id_remitente = i
            like.id_destinatario = random.randint(i+1, 4)
            like.activo = "S"

            pickle.dump(like, arLoLi)
            arLoLi.flush()

            arLoLi.seek(likePos, 0)
            like = pickle.load(arLoLi)
            likePos = arLoLi.tell()

"""
PROCEDIMIENTO mostrar_menu_estudiante
"""
def mostrar_menu_estudiante():
    print("\nMenu Estudiante")
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
"""
def menu_estudiante(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX):
    mostrar_menu_estudiante()
    
    opc = validar_numero()
    while opc < 0 and opc > 4:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                gestionar_mi_perfil(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX)
            case 2:
                gestionar_candidatos(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX)
            case 3:
                matcheos()
            case 4:
                mostrar_reportes_estadisticos(arreglo_usuarios, USUARIO_INDEX)

        os.system("cls")
        mostrar_menu_estudiante()
        opc = validar_numero()
        while opc < 0 and opc > 4:
            print("Opción inválida")
            opc = validar_numero()
    
    os.system("cls")

"""
PROCEDIMIENTO gestionar_mi_perfil
ESTUDIANTES_INDEX, USUARIO_INDEX: enteros
opc: string

arreglo_usuarios:   arreglo unidimesional de enteros
"""
def gestionar_mi_perfil(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX):    
    os.system("cls")
    print("\nGestionar mi perfil\n")
    print("a. Editar mis datos personales")
    print("b. Eliminar mi perfil")    
    print("c. Volver\n") 

    opc = str(input("Ingrese su opción: "))

    while opc != "c":
        match opc:
            case "a": 
                editar_mis_datos_personales(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX)
            case "b":
                eliminar_mi_perfil(arreglo_usuarios, USUARIO_INDEX) 
    
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
"""
def editar_mis_datos_personales(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX):
    os.system("cls")

    mostrar_menu_de_mis_datos(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX)

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
                editar_mi_fecha_de_nacimiento(arreglo_usuarios)
            case "b":
                editar_mi_biografia(arreglo_usuarios, ESTUDIANTES_INDEX)          
            case "c":
                editar_mis_hobbies(arreglo_usuarios, USUARIO_INDEX)  
            case "d":
                eliminar_mis_me_gusta(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX)

        os.system("cls")
        mostrar_menu_de_mis_datos(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX)

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
"""
def mostrar_menu_de_mis_datos(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX):
    global arLoEst, arFiEst
    usuarioPos = arreglo_usuarios[USUARIO_INDEX]
    arLoEst.seek(usuarioPos, 0)
    est = pickle.load(arLoEst)
    
    print("\n==============================================================")
    print("\nMi ID: ", est.id_estudiante)
    print("Mi nombre: ", est.nombre.strip())
    print("Mi email: ", est.email.strip())
    print("Mi sexo: ", est.sexo.strip())
    print("Mi fecha de nacimiento: ", est.fecha_nacimiento.strip())
    print("Mi biografia: ", est.biografia.strip())
    print("Mi edad: ", mostrar_edad(est.fecha_nacimiento), "años")
    print("Mis hobbies: ", est.hobbies.strip())
    mostrar_mis_me_gusta(arreglo_usuarios, ESTUDIANTES_INDEX)
    print("Mi estado: ", est.estado)
    print("Mi baja: ", est.baja)
    print("==============================================================")

"""
PROCEDIMIENTO editar_mi_fecha_de_nacimiento
USUARIO_INDEX, usuarioPos: enteros
nueva_fecha_de_nacimiento: string

arreglo_usuarios:   arreglo unidimesional de enteros
"""
def editar_mi_fecha_de_nacimiento(arreglo_usuarios):
    usuarioPos = arreglo_usuarios[USUARIO_INDEX]
    arLoEst.seek(usuarioPos, 0)
    est = pickle.load(arLoEst)

    nueva_fecha_de_nacimiento = str(input("Ingrese su fecha de nacimiento: "))    
    while len(nueva_fecha_de_nacimiento) > 10:
        print("La fecha no pueden tener más de 10 caracteres")
        nueva_fecha_de_nacimiento = str(input("Ingrese sus hobbies: "))
    if len(nueva_fecha_de_nacimiento) < 10:        
        est.fecha_nacimiento = nueva_fecha_de_nacimiento.ljust(10, " ")
    elif len(nueva_fecha_de_nacimiento) == 10:
        est.fecha_nacimiento = nueva_fecha_de_nacimiento

    arLoEst.seek(usuarioPos, 0)
    pickle.dump(est, arLoEst)
    arLoEst.flush()

"""
PROCEDIMIENTO editar_mi_biografia
ESTUDIANTES_INDEX, i: enteros
nueva_biografia: string

arreglo_usuarios:   arreglo unidimesional de enteros
"""
def editar_mi_biografia(arreglo_usuarios, ESTUDIANTES_INDEX):
    usuarioPos = arreglo_usuarios[USUARIO_INDEX]
    arLoEst.seek(usuarioPos, 0)
    est = pickle.load(arLoEst)

    nueva_biografia = str(input("Ingrese su biografia: "))    
    while len(nueva_biografia) > 255:
        print("La biografía no pueden tener más de 255 caracteres")
        nueva_biografia = str(input("Ingrese sus hobbies: "))
    if len(nueva_biografia) < 255:
        est.biografia = nueva_biografia.ljust(255, " ")
    elif len(nueva_biografia) == 255:        
        est.biografia = nueva_biografia

    arLoEst.seek(usuarioPos, 0)
    pickle.dump(est, arLoEst)
    arLoEst.flush()

"""
PROCEDIMIENTO editar_mis_hobbies
ESTUDIANTES_INDEX, MODERADORES_INDEX, usuarioPos: enteros
nuevos_hobbies: string
arLoEst: BufferedRandom
arreglo_usuarios:   arreglo unidimesional de enteros
"""
def editar_mis_hobbies(arreglo_usuarios, USUARIO_INDEX):
    usuarioPos = arreglo_usuarios[USUARIO_INDEX]
    arLoEst.seek(usuarioPos, 0)
    est = pickle.load(arLoEst)
   
    nuevos_hobbies = str(input("Ingrese sus hobbies: "))
    while len(nuevos_hobbies) > 255:
        print("Los hobbies no pueden tener más de 255 caracteres")
        nuevos_hobbies = str(input("Ingrese sus hobbies: "))
    if len(nuevos_hobbies) < 255:
        est.hobbies = nuevos_hobbies.ljust(255, " ")
    elif len(nuevos_hobbies) == 255:        
        est.hobbies = nuevos_hobbies

    arLoEst.seek(usuarioPos, 0)
    pickle.dump(est, arLoEst)
    arLoEst.flush()
    
"""
PROCEDIMIENTO eliminar_mis_me_gusta
ESTUDIANTES_INDEX,: enteros
eliminar_me_gusta: string

arreglo_usuarios:   arreglo unidimesional de enteros
"""
def eliminar_mis_me_gusta(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX):
    global arLoLi, arLoEst, arFiLi

    #mostrar_mis_me_gusta(arreglo_usuarios, USUARIO_INDEX)
    
    tamArc = os.path.getsize(arFiLi)
    if tamArc > 0:
        print("\nMis me gusta")

        arLoLi.seek(0, 0)
        like = Likes()
        like = pickle.load(arLoLi)
        arLoEst.seek(arreglo_usuarios[USUARIO_INDEX], 0)
        estudiante = Estudiante()
        estudiante = pickle.load(arLoEst)

        arLoLi.seek(0, 0)
        
        cantMegustaDados = 0
        while arLoLi.tell() < tamArc:
            like = pickle.load(arLoLi)
            if (estudiante.id_estudiante == like.id_remitente) and like.activo == "S":                
                estPos = buscar_estudiante("id_estudiante", int(like.id_destinatario))
                arLoEst.seek(estPos, 0)
                estudiante_destinatario = pickle.load(arLoEst)
                print("- ", estudiante_destinatario.nombre, emoji.emojize(':red_heart:'))
                cantMegustaDados = cantMegustaDados +1
            
        if cantMegustaDados != 0:
            nombre_estudiante = str(input("Ingresar nombre y apellido de estudiante para eliminar el me gusta: "))
            while len(nombre_estudiante) > 32:
                print("El nombre y apellido no puede tener más de 32 caracteres")
                nombre_estudiante = str(input("Ingresar nombre y apellido de estudiante para eliminar el me gusta: "))
            if len(nombre_estudiante) < 32:
                nombre_estudiante = nombre_estudiante.ljust(32, " ")
            elif len(nombre_estudiante) == 32:
                nombre_estudiante = nombre_estudiante
            estPos = buscar_estudiante("nombre", nombre_estudiante)
            
            if estPos != -1:
                arLoEst.seek(estPos, 0)
                arLoLi.seek(0, 0)
                estudiante = pickle.load(arLoEst)
                while arLoLi.tell() < tamArc:
                    likePos = arLoLi.tell()
                    like = pickle.load(arLoLi)
                    if like.id_destinatario == estudiante.id_estudiante:
                        like.activo = "N"
                        arLoLi.seek(likePos, 0)
                        pickle.dump(like, arLoLi)
                        arLoLi.flush()
                        print("Me gusta eliminado exitosamente")      
                #mostrar_mis_me_gusta(arreglo_usuarios, USUARIO_INDEX)
                
            else:
                print("Estudiante no encontrado")
        else:
            print("No tienes ningún like registrado\n")
            print("s. Volver") 
            opc = str(input("Ingrese su opción: "))
            while opc != "s":
                print("s. Volver") 
                opc = str(input("Ingrese su opción: "))
            os.system("cls")
    else:
        print("\nNo hay ningún like registrado\n")
        print("s. Volver") 
        opc = str(input("Ingrese su opción: "))
        while opc != "s":
            print("s. Volver") 
            opc = str(input("Ingrese su opción: "))
        os.system("cls")

"""
PROCEDIMIENTO mostrar_mis_me_gusta
tamArc,: enteros
arLoLi, arLoEst: BufferedRandom
arFiLi: str
arreglo_usuarios:   arreglo unidimesional de enteros
"""
def mostrar_mis_me_gusta(arreglo_usuarios, USUARIO_INDEX):
    global arLoLi, arLoEst, arFiLi

    tamArc = os.path.getsize(arFiLi)
    if tamArc > 0:
        print("\nMis me gusta")

        arLoLi.seek(0, 0)
        like = Likes()
        like = pickle.load(arLoLi)
        arLoEst.seek(arreglo_usuarios[USUARIO_INDEX], 0)
        estudiante = Estudiante()
        estudiante = pickle.load(arLoEst)

        arLoLi.seek(0, 0)
        
        cantMegustaDados = 0
        while arLoLi.tell() < tamArc:
            like = pickle.load(arLoLi)
            if (estudiante.id_estudiante == like.id_remitente) and like.activo == "S":                
                estPos = buscar_estudiante("id_estudiante", int(like.id_destinatario))
                arLoEst.seek(estPos, 0)
                estudiante_destinatario = pickle.load(arLoEst)
                print("- ", estudiante_destinatario.nombre, emoji.emojize(':red_heart:'))
                cantMegustaDados = cantMegustaDados +1
            
        if cantMegustaDados == 0:
            print("No tienes ningún like registrado\n")
    else:
        print("\nNo hay ningún like registrado\n")

"""
PROCEDIMIENTO mostrar_me_gusta
tamArc,: enteros
arLoLi, arLoEst: BufferedRandom
arFiLi: str
arreglo_usuarios:   arreglo unidimesional de enteros
"""
def mostrar_me_gusta(pos):
    global arLoLi, arLoEst, arFiLi

    tamArc = os.path.getsize(arFiLi)
    if tamArc > 0:
        print("\nMis me gusta")

        arLoLi.seek(0, 0)
        like = Likes()
        like = pickle.load(arLoLi)
        arLoEst.seek(pos, 0)
        estudiante = Estudiante()
        estudiante = pickle.load(arLoEst)

        arLoLi.seek(0, 0)
        
        cantMegustaDados = 0
        while arLoLi.tell() < tamArc:
            like = pickle.load(arLoLi)
            if (estudiante.id_estudiante == like.id_remitente) and like.activo == "S":                
                estPos = buscar_estudiante("id_estudiante", int(like.id_destinatario))
                arLoEst.seek(estPos, 0)
                estudiante_destinatario = pickle.load(arLoEst)
                print("- ", estudiante_destinatario.nombre, emoji.emojize(':red_heart:'))
                cantMegustaDados = cantMegustaDados +1
            
        if cantMegustaDados == 0:
            print("No tienes ningún like registrado\n")
    else:
        print("\nNo hay ningún like registrado\n")

"""
FUNCION mostrar_edad
edad: enteros
fecha: string
fecha_nacimiento, fecha_actual: datetime
"""
def mostrar_edad(fecha):
    
    if(not fecha or fecha == "00-00-0000"): 
        return "-"
    fecha_nacimiento = datetime.strptime(fecha, '%d-%m-%Y')
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    
    return edad

"""
PROCEDIMIENTO mostrar_datos_otros_usuarios
arreglo_usuarios:   arreglo unidimesional de enteros
"""
def mostrar_datos_otros_usuarios(arreglo_usuarios, USUARIO_INDEX):   
    global arFiEst, arLoEst
    pos = 0    
    tamArc = os.path.getsize(arFiEst)
    arLoEst.seek(pos, 0)    
    
    while arLoEst.tell() < tamArc:
        pos = arLoEst.tell()
        estudiante = pickle.load(arLoEst)
        if (pos != arreglo_usuarios[USUARIO_INDEX]):        
            print("\n==============================================================")
            print("Datos del estudiante:")
            print("ID: ", estudiante.id_estudiante)
            print("Nombre: ", estudiante.nombre.strip())
            print("Email: ", estudiante.email.strip())
            print("Fecha de nacimiento: ", estudiante.fecha_nacimiento.strip())
            print("Biografia: ", estudiante.biografia.strip())
            print("Edad: ", mostrar_edad(estudiante.fecha_nacimiento), "años")
            print("Hobbies: ", estudiante.hobbies.strip())
            mostrar_me_gusta(pos)
            print("Estado: ", estudiante.estado)
            print("Baja: ", estudiante.baja)
            print("==============================================================")

"""
PROCEDIMIENTO dar_me_gusta
ESTUDIANTES_INDEX, posCandPorNombre: entero
arLoEst, arLoLi:    BufferedRandom
arFiEst, arFiLi,nombre_usuario :    str
arreglo_usuarios:   arreglo unidimesional de enteros
like: Likes
remitente, destinatario: Estudiante
"""
def dar_me_gusta(arreglo_usuarios, USUARIO_INDEX):
    global arLoEst, arFiEst, arLoLi, arFiLi

    print("\nDar me gusta\n")
    nombre_usuario = str(input("Ingresar nombre y apellido de estudiante: "))
    while len(nombre_usuario) > 32:
        print("El nombre y apellido no puede tener más de 32 caracteres")
        nombre_usuario = str(input("Ingresar nombre y apellido de estudiante: "))
    if len(nombre_usuario) < 32:
        nombre_usuario = nombre_usuario.ljust(32, " ")
    elif len(nombre_usuario) == 32:
        nombre_usuario = nombre_usuario

    posCandPorNombre = buscar_estudiante("nombre", nombre_usuario)

    if posCandPorNombre != -1:
        print("Estudiante encontrado!")
        print("pos: ", posCandPorNombre)
        like = Likes()
        destinatario = Estudiante()
        remitente = Estudiante()

        arLoEst.seek(posCandPorNombre, 0)
        destinatario = pickle.load(arLoEst)        
        like.id_destinatario = destinatario.id_estudiante 

        arLoEst.seek(arreglo_usuarios[USUARIO_INDEX], 0)
        remitente = pickle.load(arLoEst)
        like.id_remitente = remitente.id_estudiante

        if not mostrar_si_dio_like(remitente.id_estudiante, destinatario.id_estudiante):
            arLoLi.seek(0, 2)
            pickle.dump(like, arLoLi)
            arLoLi.flush()
            print("El like ha sido entregado!")   
        else:
            print("El like ya fue entregado!") 
        
    else:
        print("Estudiante no encontrado!")

"""
PROCEDIMIENTO eliminar_mi_perfil
USUARIO_INDEX, usuarioPos: enteros
opc: string

arreglo_usuarios:   arreglo unidimesional de enteros
"""
def eliminar_mi_perfil(arreglo_usuarios, USUARIO_INDEX):
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
            usuarioPos = arreglo_usuarios[USUARIO_INDEX]
            arLoEst.seek(usuarioPos, 0)
            est = pickle.load(arLoEst)                      
            est.estado = True
            est.baja = "S"
            arLoEst.seek(usuarioPos, 0)
            pickle.dump(est, arLoEst)
            arLoEst.flush()

"""
PROCEDIMIENTO gestionar_candidatos
ESTUDIANTES_INDEX: enteros
opc: string

arreglo_usuarios:   arreglo unidimesional de enteros
"""
def gestionar_candidatos(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX):
    os.system("cls")

    print("\nGestionar candidatos\n")
    print("a. Ver candidatos")
    print("b. Reportar candidato")    
    print("c. Volver") 
    opc = str(input("Ingrese su opción: "))

    while opc != "c":
        match opc:
            case "a":
                ver_candidatos(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX)
            case "b":
                reportar_candidato(arreglo_usuarios, USUARIO_INDEX)

        #os.system("cls")
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
"""
def ver_candidatos(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX):
    print("\nCandidatos\n")
    mostrar_datos_otros_usuarios(arreglo_usuarios, USUARIO_INDEX)
    print("\n\na. Dar me gusta")
    print("b. Dar Super Like")
    print("c. Volver")

    opc = str(input("Ingrese su opción: "))
    while opc != "c":
        match opc:
            case "a":
                dar_me_gusta(arreglo_usuarios, USUARIO_INDEX)
            case "b":
                #dar_super_like()
                pass
        #os.system("cls")
        print("\nCandidatos\n")
        mostrar_datos_otros_usuarios(arreglo_usuarios, USUARIO_INDEX)
        print("\n\na. Dar me gusta")
        print("c. Volver")
        opc = str(input("Ingrese de nuevo: "))

"""
FUNCION mostrar_si_dio_like
remitente, destinatario, tamArc: enteros
arFiLi: str
arLoLi: BufferedRandom
like: Likes
return boolean
"""
def mostrar_si_dio_like(remitente, destinatario):
    global arLoLi, arFiLi

    like = Likes()
    tamArc = os.path.getsize(arFiLi)
    arLoLi.seek(0,0)
    while arLoLi.tell() < tamArc:
        like = pickle.load(arLoLi)
        if (like.id_remitente == remitente and like.id_destinatario == destinatario) and like.activo == "S":
            return True
    return False

"""
PROCEDIMIENTO reportar_candidato
ESTUDIANTES_INDEX, estPos: enteros
nombre_reportado, motivo: string

arreglo_usuarios: arreglo unidimesional de enteros
reporte: Reportes
arLoEst, arLoRep: BufferedRandom
"""

def reportar_candidato(arreglo_usuarios, USUARIO_INDEX):
    global arLoEst, arLoRep
    os.system("cls")
    global arFiEst, arLoEst, arFiRep, arLoRep
    rep = Reportes()
    val = input('¿Está seguro que quiere reportar a un usuario? (S/N): ')
    val = val.upper()
    while val != 'S' and val != 'N':
        val = input('¿Está seguro que quiere reportar a un usuario? (S/N): ')
        val = val.upper()

    nombre_reportado = str(input("Ingrese nombre o ID de usuario a reportar: "))
    while len(nombre_reportado) > 32:
        print("El nombre y apellido no puede tener más de 32 caracteres")
        nombre_reportado = str(input("Ingresar nombre y apellido de estudiante: "))
    if len(nombre_reportado) < 32:
        nombre_reportado = nombre_reportado.ljust(32, " ")
    elif len(nombre_reportado) == 32:
        nombre_reportado = nombre_reportado
    
    estPos = buscar_estudiante("nombre", nombre_reportado)
    
    if estPos != -1:
        if estPos != arreglo_usuarios[USUARIO_INDEX]:
            reporte = Reportes()
            motivo_reporte = str(input("Ingrese su reporte: "))
            while len(motivo_reporte) > 255:
                print("El motivo no puede tener más de 255 caracteres")
                motivo_reporte = str(input("Ingresar motivo de estudiante: "))
            if len(motivo_reporte) < 255:
                motivo_reporte = motivo_reporte.ljust(255, " ")
            elif len(motivo_reporte) == 255:
                motivo_reporte = motivo_reporte        

            estudiante1 = Estudiante()
            arLoEst.seek(arreglo_usuarios[USUARIO_INDEX], 0)
            estudiante1 = pickle.load(arLoEst)
            reporte.id_reportante = estudiante1.id_estudiante

            estudiante2 = Estudiante()
            arLoEst.seek(estPos, 0)
            estudiante2 = pickle.load(arLoEst)
            reporte.id_reportado = estudiante2.id_estudiante
            reporte.estado = 0

            arLoRep.seek(0, 2)
            pickle.dump(reporte, arLoRep)
            arLoRep.flush()
            print("\nReporte fue enviado exitosamente.")
        else:
            print("\nNo puedes reportarte a ti mismo.")
    else:        
        print("\nEl usuario no existe.")
                    
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
FUNCION mostrar_cantidad_registros_estudiantes
return entero
"""
def mostrar_cantidad_registros_estudiantes():
    global arLoEst, arFiEst

    tamArc = os.path.getsize(arFiEst)
    if tamArc > 0:
        arLoEst.seek(0, 0)
        est = pickle.load(arLoEst)
        tamReg = arLoEst.tell()
        cantReg = tamArc // tamReg
        return cantReg
    else:
        return 0

"""
FUNCION mostrar_cantidad_registros_moderadores
return entero
"""
def mostrar_cantidad_registros_moderadores():
    global arLoMod, arFiMod

    tamArc = os.path.getsize(arFiMod)
    if tamArc > 0:
        arLoMod.seek(0, 0)
        mod = pickle.load(arLoMod)
        tamReg = arLoMod.tell()
        cantReg = tamArc // tamReg
        return cantReg
    else:
        return 0

"""
FUNCION mostrar_cantidad_registros_administradores
return entero
"""
def mostrar_cantidad_registros_administradores():
    global arLoAdmin, arFiAdmin

    tamArc = os.path.getsize(arFiAdmin)
    if tamArc > 0:
        arLoAdmin.seek(0, 0)
        admin = pickle.load(arLoAdmin)
        tamReg = arLoAdmin.tell()
        cantReg = tamArc // tamReg
        return cantReg
    else:
        return 0
     
"""
PROCEDIMIENTO mostrar_reportes_estadisticos
USUARIO_INDEX: enteros
opc: string

arreglo_usuarios:   arreglo unidimesional de enteros
"""
def mostrar_reportes_estadisticos(arreglo_usuarios, USUARIO_INDEX):
    os.system("cls")
    print("\nReportes estadísticos\n")
    mostrar_reporte_matcheos(arreglo_usuarios, USUARIO_INDEX)
    print("a. Volver")
    opc = str(input("Ingrese su opción: "))

    while opc != "a":
        os.system("cls")
        print("\nReportes estadísticos\n")
        mostrar_reporte_matcheos(arreglo_usuarios, USUARIO_INDEX)
        print("a. Volver")  
        opc = str(input("Ingrese de nuevo: "))

"""
PROCEDIMIENTO mostrar_reporte_matcheos
ESTUDIANTES_INDEX, USUARIO_INDEX, matcheos: enteros
porcentaje: float

arreglo_usuarios:   arreglo unidimesional de enteros
"""
def mostrar_reporte_matcheos(arreglo_usuarios, USUARIO_INDEX):
    global arLoEst, arFiEst, arLoLi, arFiLi

    matcheos = 0
    cantEst = mostrar_cantidad_registros_estudiantes()
    tamArc = os.path.getsize(arFiEst)
    tamReg = tamArc // cantEst
    
    arLoEst.seek(arreglo_usuarios[USUARIO_INDEX], 0)
    est = pickle.load(arLoEst)
    miId = est.id_estudiante
    arLoEst.seek(0, 0)

    accu = 0
    cantMeGustaDados = 0
    cantMeGustaRecibidos = 0
    matcheos = 0
    porcentaje = 0
    for _ in range(cantEst):
        arLoEst.seek(accu, 0)
        est2 = pickle.load(arLoEst)
        diLike = mostrar_si_dio_like(miId, est2.id_estudiante)
        meDioLike = mostrar_si_dio_like(est2.id_estudiante, miId)
        matching = mostrar_si_dio_like(miId, est2.id_estudiante) and mostrar_si_dio_like(est2.id_estudiante, miId)
        if diLike:
            cantMeGustaDados = cantMeGustaDados + 1
        if meDioLike:
            cantMeGustaRecibidos = cantMeGustaRecibidos + 1
        if matching:
            matcheos = matcheos + 1
        accu = accu + tamReg
    print(emoji.emojize(":red_heart:"), " ~ Me gusta dados:", cantMeGustaDados)
    print(emoji.emojize(":red_heart:"), " ~ Me gusta recibidos:", cantMeGustaRecibidos)
    print(emoji.emojize(":two_hearts:"), "~ Matcheos:", matcheos)
    porcentaje = (matcheos * 100) // (cantEst - 1)
    print(" ~ Matcheos sobre el total posible: ", porcentaje, "%\n")

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
"""
def menu_moderadores(arreglo_usuarios, MODERADORES_INDEX, ESTUDIANTES_INDEX, USUARIO_INDEX):
    mostrar_menu_moderadores()
    opc = validar_numero()
    while opc < 0 and opc > 3:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                gestionar_usuarios_moderador(arreglo_usuarios, ESTUDIANTES_INDEX)
            case 2:
                gestionar_reportes_moderador(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX)
            case 3:
                mostrar_menu_reportes_estadisticos_moderador()

        os.system("cls")
        mostrar_menu_moderadores()
        opc = validar_numero()
        while opc < 0 and opc > 3:
            print("Opción inválida")
            opc = validar_numero()

"""
PROCEDIMIENTO gestionar_usuarios_moderador
ESTUDIANTES_INDEX: enteros
opc: string

arreglo_usuarios:   arreglo unidimesional de enteros
"""
def gestionar_usuarios_moderador(arreglo_usuarios, ESTUDIANTES_INDEX):
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

arreglo_usuarios    arreglo unidimensional de enteros
"""
def desactivar_usuario(arreglo_usuarios, ESTUDIANTES_INDEX):
    os.system("cls")
    print("\nDesactivar usuario\n")
    desactivar = str(input("Ingresar nombre o ID de usuario a desactivar: "))
    for i in range(arreglo_usuarios[ESTUDIANTES_INDEX]):
        pass
        #if desactivar == arreglo_de_estudiantes[i][0] or desactivar == arreglo_de_estudiantes[i][1]:
        #    arreglo_de_estudiantes[i][9] = "inactivo"

"""
PROCEDIMIENTO gestionar_reportes_moderador
opc: string
"""
def gestionar_reportes_moderador(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX):
    print("\nGestionar reportes\n")
    print("a. Ver reportes")  
    print("b. Volver") 
    opc = str(input("Ingrese su opción: "))

    while opc != "b":
        match opc:
            case "a":
                ver_reportes(arreglo_usuarios, USUARIO_INDEX)
        print("\nGestionar reportes\n")
        print("a. Ver reportes")  
        print("b. Volver") 
        opc = str(input("Ingrese de nuevo: "))

"""
FUNCION BUSCAR_REPORTEs_pendientes
TAMARC: INT
pos: int
"""
def buscar_reportes_pendientes():
    global arLoRep, arFiRep
    rep = Reportes()
    tamArc = os.path.getsize(arFiRep)
    arLoRep.seek(0,0)
    cont = 0
    while arLoRep.tell() < tamArc:
        rep = pickle.load(arLoRep)
        print(rep.estado)
        if rep.estado == 0:
            cont = cont + 1
    arLoRep.seek(0,0)
    if cont == 0:
        return False
    else:
        return True

"""
FUNCION INTERFAZ_REPORTE
opc: string
pos: int
"""
def interfaz_reporte(pos):
    global arFiRep, arLoRep
    rep = Reportes()
    arLoRep.seek(pos,0)
    rep = pickle.load(arLoRep)
    # motivo = rep.motivo.rstrip()

    print("\nReporte")
    print("ID de reportante: ", rep.id_reportante)
    print("ID de reportado: ", rep.id_reportado)
    print("Motivo: ", rep.motivo)
    print("\n¿Que acción desea tomar?\n")
    print("a. Ignorar reporte")
    print("b. Desactivar usuario")
    opc = str(input("Ingrese su opción: "))
    return opc

"""
PROCEDIMIENTO PARA ANALIZAR LOS REPORTES ver_reportes
arreglo_usuarios: array of int
USUARIO_INDEX: int
"""
def ver_reportes(arreglo_usuarios, USUARIO_INDEX):
    os.system('cls')
    global arFiRep, arFiMod, arFiEst
    global arLoRep, arLoMod, arLoEst
    rep = Reportes()
    mod = Moderador()
    est = Estudiante()
    tamArch = os.path.getsize(arFiRep)
    if tamArch > 0:
        if buscar_reportes_pendientes():
            while tamArch > arLoRep.tell():
                pos = arLoRep.tell()
                rep = pickle.load(arLoRep)
                arLoEst.seek(0,0)
                est = pickle.load(arLoEst)
                pos_est = buscar_estudiante("id_estudiante", int(rep.id_reportado))
                arLoEst.seek(pos_est,0)
                est = pickle.load(arLoEst)
                opc = interfaz_reporte(pos)
                while opc != "a" and opc != "b":
                    opc = interfaz_reporte(pos)
                match opc:
                    case "a":
                        pos_mod = arreglo_usuarios[USUARIO_INDEX]
                        arLoMod.seek(pos_mod,0)
                        mod = pickle.load(arLoMod)
                        mod.ignorado += 1
                        arLoMod.seek(pos_mod,0)
                        pickle.dump(mod,arLoMod)
                        arLoMod.flush()
                        rep.estado = 2
                        arLoRep.seek(pos,0)
                        pickle.dump(rep,arLoRep)
                        arLoRep.flush()
                    case "b":
                        pos_mod = arreglo_usuarios[USUARIO_INDEX]
                        arLoMod.seek(pos_mod,0)
                        mod = pickle.load(arLoMod)
                        mod.aceptado += 1
                        arLoMod.seek(pos_mod,0)
                        pickle.dump(mod,arLoMod)
                        arLoMod.flush()
                        rep.estado = 1
                        arLoRep.seek(pos,0)
                        pickle.dump(rep,arLoRep)
                        arLoRep.flush()
                        arLoEst.seek(pos_est,0)
                        est = pickle.load(arLoEst)
                        est.baja = "S"
                        pickle.dump(est,arLoEst)
                        arLoEst.flush()
                print("\nEl reporte ha sido tomado\n")
            print("Ya revisaste todos los reportes")
        else:
            print("No hay reportes pendientes")
    else:
        print("No hay ningún reporte hecho")

"""
PROCEDIMIENTO mostrar_menu_reportes_estadisticos_moderador
opc: enteros
"""
def mostrar_menu_reportes_estadisticos_moderador():
    print("\nReportes estadisticos\n")
    print("En construcción")  
    print("a. Volver\n") 
    opc = str(input("Ingrese su opción: "))

    while opc != "a":
        print("\nReportes estadisticos\n")
        print("En construcción")  
        print("a. Volver\n") 
        opc = str(input("Ingrese de nuevo: "))

def mostrar_menu_administradores():
        print("\nMenu Administradores\n")
        print("1. Gestionar usuarios")
        print("2. Gestionar reportes")
        print("3. Reportes estadísticos")
        print("0. Salir\n")

def menu_administradores(arreglo_usuarios, ADMINISTRADOR_INDEX, ESTUDIANTES_INDEX):
    mostrar_menu_administradores()
    opc = validar_numero()
    while opc < 0 and opc > 3:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                gestionar_usuarios_administrador(arreglo_usuarios, ESTUDIANTES_INDEX)
            case 2:
                gestionar_reportes_administrador(arreglo_usuarios, ESTUDIANTES_INDEX)
            case 3:
                mostrar_menu_reportes_estadisticos_administrador()

        os.system("cls")
        mostrar_menu_administradores()
        opc = validar_numero()
        while opc < 0 and opc > 3:
            print("Opción inválida")
            opc = validar_numero()

def gestionar_usuarios_administrador(arreglo_usuarios, ESTUDIANTES_INDEX):
    os.system("cls")
    print("\nGestionar usuarios\n")
    print("a. Eliminar un usuario")  
    print("b. Dar de alta a un moderador")  
    print("c. Desactivar usuario")  
    print("d. Volver\n") 
    opc = str(input("Ingrese su opción: "))

    while opc != "d":
        match opc:
            case "a":
                os.system("cls")
                eliminar_usuario()
            case "b":
                dar_alta_moderador()
            case "c":
                desactivar_usuario(arreglo_usuarios, ESTUDIANTES_INDEX)

        os.system("cls")
        print("\nGestionar usuarios\n")
        print("a. Eliminar un usuario")  
        print("b. Dar de alta a un moderador")  
        print("c. Desactivar usuario")  
        print("d. Volver\n") 
        opc = str(input("Ingrese de nuevo: "))

def eliminar_usuario():
    print("\nEliminar un usuario\n")
    print("a. Eliminar un estudiante")
    print("b. Eliminar un moderador")
    print("c. Volver\n")
    opc = str(input("Ingrese su opción: "))

    while opc != "c":
        match opc:
            case "a":
                os.system("cls")
                eliminar_usuario_estudiante()
            case "b":
                os.system("cls")
                eliminar_usuario_moderador()

        os.system("cls")
        print("\nEliminar un usuario\n")
        print("a. Eliminar un estudiante")
        print("b. Eliminar un moderador")
        print("c. Volver\n")
        opc = str(input("Ingrese de nuevo: "))

def eliminar_usuario_estudiante():
    global arLoEst
    print("\nEliminar un estudiante\n")
    id = int(input("Ingrese el ID del estudiante a eliminar: "))
    estPos = buscar_estudiante("id_estudiante", id)
    if estPos != -1:
        arLoEst.seek(estPos, 0)
        est = pickle.load(arLoEst)                      
        est.estado = True
        est.baja = "S"
        arLoEst.seek(estPos, 0)
        pickle.dump(est, arLoEst)
        arLoEst.flush()
        print("\nEl estudiante con el ID ", id, " se ha eliminado exitosamente.\n")
    else:
        os.system("cls")
        print("\nEl ID de estudiante no se ha encontrado\n")

def eliminar_usuario_moderador():
    global arLoMod
    print("\nEliminar un moderador\n")
    id = int(input("Ingrese el ID del moderador a eliminar: "))
    modPos = buscar_moderador("id", id)
    if modPos != -1:
        arLoMod.seek(modPos, 0)
        mod = pickle.load(arLoMod)                      
        mod.estado = True
        mod.baja = "S"
        arLoMod.seek(modPos, 0)
        pickle.dump(mod, arLoMod)
        arLoEst.flush()
        print("\nEl moderador con el ID ", id, " se ha eliminado exitosamente.\n")
    else:
        os.system("cls")
        print("\nEl ID de moderador no se ha encontrado\n")

def dar_alta_moderador():
    global arFiMod, arLoMod
    os.system("cls")
    print("\nCrear un moderador\n")
    mod = Moderador()
    continuar = str(input("Seguro deasea crear un moderador (S/N)?: "))
    continuar = continuar.upper()
    while continuar != "S" and continuar != "N":
        print("Por favor, ingrese una opción válida (S/N)")
        continuar = str(input("Seguro deasea crear un moderador (S/N)?: "))
        continuar.upper()
    while continuar == "S":
        if os.path.getsize(arFiMod) == 0:
            mod.id = 1
        else:
            arLoMod.seek(0,0)
            mod = pickle.load(arLoMod)
            tamReg = arLoEst.tell()
            tamArc = os.path.getsize(arFiMod)
            cantReg = tamArc // tamReg
            mod.id = cantReg + 1
        # Ingreso y formateo campo email
        email = str(input("Ingrese email: "))
        while len(email) > 32:
            print("El email no puede tener más de 32 caracteres")
            email = str(input("Ingrese email: "))
        if len(email) < 32:
            mod.email = email.ljust(32, " ")
        elif len(email) == 32:
            mod.email = email
        # Ingreso y formateo campo contraseña
        contraseña = str(input("Ingrese contraseña: "))
        while len(contraseña) > 32:
            print("La contraseña no puede tener más de 32 caracteres")
            contraseña = str(input("Ingrese contraseña: "))
        if len(contraseña) < 32:
            mod.contrasena = contraseña.ljust(32, " ")
        elif len(contraseña) == 32:
            mod.contrasena = contraseña

        mod.estado = True
        mod.baja = "N"
        arLoMod.seek(0, 2)
        pickle.dump(mod, arLoMod)
        arLoMod.flush()

        continuar = str(input("Desea crear otro moderador (S/N)?: "))
        continuar = continuar.upper()
        while continuar != "S" and continuar != "N":
            print("Por favor, ingrese una opción válida (S/N)")
            continuar = str(input("Desea crear otro moderador (S/N)?: "))
            continuar = continuar.upper()
    os.system("cls")
    print("Moderador creado\n")

def gestionar_reportes_administrador(arreglo_usuarios, ESTUDIANTES_INDEX):
    os.system("cls")
    print("\nGestionar reportes\n")
    print("a. Ver reportes")  
    print("b. Volver") 
    opc = str(input("Ingrese su opción: "))

    while opc != "b":
        match opc:
            case "a":
                ver_reportes(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX)
        print("\nGestionar reportes\n")
        print("a. Ver reportes")  
        print("b. Volver") 
        opc = str(input("Ingrese de nuevo: "))

def mostrar_menu_reportes_estadisticos_administrador():
    print("\nReportes estadisticos\n") 
    reportes_estadisticos(arreglo_usuarios,USUARIO_INDEX)
    print("a. Volver\n") 
    opc = str(input("Ingrese su opción: "))

    while opc != "a":
        print("a. Volver\n") 
        opc = str(input("Ingrese de nuevo: "))

"""
FUNCION buscar_estudiante
param, busqueda: string
"""
def buscar_estudiante(param, busqueda):
    global arLoEst, arFiEst
    estudiante = Estudiante()
    tamArc = os.path.getsize(arFiEst)
    arLoEst.seek(0, 0)    
    while arLoEst.tell() < tamArc:
        pos = arLoEst.tell()
        estudiante = pickle.load(arLoEst)        
        if getattr(estudiante, param) == busqueda:
            return pos
    return -1

"""
FUNCION buscar_moderador
param, busqueda: string
"""
def buscar_moderador(param, busqueda):
    global arLoMod, arFiMod
    moderador = Moderador()
    tamArc = os.path.getsize(arFiMod)
    arLoMod.seek(0, 0)    
    while arLoMod.tell() < tamArc:
        pos = arLoMod.tell()
        moderador = pickle.load(arLoMod)
        if getattr(moderador, param) == busqueda:
            return pos
    return -1

def reportes_estadisticos(arreglo_usuarios,USUARIO_INDEX):
    global arFiMod, arFiRep
    global arLoRep, arLoMod
    rep = Reportes()
    mod = Moderador()
    arLoRep.seek(0,0)
    tamArch = os.path.getsize(arFiRep)
    if tamArch > 0:
        rep = pickle.load(arLoRep)
        tamReg = arLoRep.tell()
        cant = tamArch//tamReg
        arLoRep.seek(0,0)
        cont1 = 0
        cont2 = 0
        print(tamArch)
        print(tamReg)
        while arLoRep.tell() < tamArch:
            print(rep.estado)
            rep = pickle.load(arLoRep)
            if rep.estado == 1:
                cont1 = cont1 + 1
            elif rep.estado == 2:
                cont2 = cont2 + 1
        print(f'La cantidad de reportes hechos es: {cant}')
        print(f'El porcentaje de reportes ignorados es: {(cont2*100)//cant}')
        print(f'El porcentaje de reportes aceptados es: {(cont1*100)//cant}')
        pos = arreglo_usuarios[USUARIO_INDEX]
        arLoMod.seek(pos,0)
        aux_ignorado = 0
        aux_aceptado = 0
        aux_total = 0
        id_ignorado = 0
        id_aceptado = 0
        id_total = 0
        while os.path.getsize(arFiMod) > arLoMod.tell():
            mod = pickle.load(arLoMod)

            if mod.ignorado > aux_ignorado:
                aux_ignorado = mod.ignorado
                id_ignorado = mod.id

            if mod.aceptado > aux_aceptado:
                aux_aceptado = mod.aceptado
                id_aceptado = mod.id

            if mod.aceptado+mod.ignorado > aux_total:
                aux_total = mod.aceptado+mod.ignorado
                id_total = mod.id

        if id_ignorado > 0:
            print(f"El moderador {id_ignorado} fue el que más reportes ignoró: {aux_ignorado}")
        else:
            print("No hubo reportes ignorados")

        if id_aceptado > 0:
            print(f"El moderador {id_aceptado} fue el que más reportes aceptó: {aux_aceptado}")
        else:
            print("No hubo reportes aceptados")

        if id_total > 0:
            print(f"El moderador {id_total} fue el que más reportes revisó en total: {aux_total}")
        else:
            print("No hubo reportes revisados")
    else:
        print("No hay reportes que analizar")

def buscar_administrador(param, busqueda):
    global arLoAdmin, arFiAdmin
    admin = Admin()
    tamArc = os.path.getsize(arFiAdmin)
    arLoAdmin.seek(0, 0)    
    while arLoAdmin.tell() < tamArc:
        pos = arLoAdmin.tell()
        admin = pickle.load(arLoAdmin)
        if getattr(admin, param) == busqueda:
            return pos
    return -1

"""
PROCEDIMIENTO validar_ingreso
ESTUDIANTES_INDEX, USUARIO_INDEX, MODERADORES_INDEX, intentos, i: enteros
email, contraseña: string

arreglo_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios:   arreglo unidimesional de enteros
"""
def validar_ingreso(arreglo_usuarios, ESTUDIANTES_INDEX, MODERADORES_INDEX, ADMINISTRADOR_INDEX, arreglo_sesion, USUARIO_INDEX):
    global arLoEst, arLoAdmin, arLoMod
    intentos = 3

    email = str(input("Ingrese email: "))
    while len(email) > 32:
        print("El email no puede tener más de 32 caracteres")
        email = str(input("Ingrese email: "))
    if len(email) < 32:
        email = email.ljust(32, " ")
    elif len(email) == 32:
        email = email
    
    estPos = buscar_estudiante("email", email)
    modPos = buscar_moderador("email", email)
    adminPos = buscar_administrador("email", email)
    #print(estPos, modPos, adminPos)
          
    contraseña = getpass.getpass("Ingrese su contraseña: ")

    while len(contraseña) > 32:
        print("La contraseña no puede tener más de 32 caracteres")
        contraseña = getpass.getpass("Ingrese contraseña: ")
    if len(contraseña) < 32:
        contraseña = contraseña.ljust(32, " ")
    elif len(contraseña) == 32:
        contraseña = contraseña
    print(contraseña)

    if estPos != -1:
        arLoEst.seek(estPos, 0)
        estudiante = Estudiante()
        estudiante = pickle.load(arLoEst)

        if ((contraseña == estudiante.contrasena and estudiante.baja == "N")):
            arreglo_sesion[ESTUDIANTES_INDEX] = True
            arreglo_usuarios[USUARIO_INDEX] = estPos
            
            os.system("cls")
            print("Sesión iniciada correctamente")
            menu_estudiante(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX)
    elif modPos != -1:
        arLoMod.seek(modPos, 0)
        moderador = Moderador()
        moderador = pickle.load(arLoMod)

        if ((contraseña == moderador.contrasena and moderador.baja == "N")):
            arreglo_sesion[MODERADORES_INDEX] = True
            arreglo_usuarios[USUARIO_INDEX] = modPos
            
            os.system("cls")
            print("Sesión iniciada correctamente")
            menu_moderadores(arreglo_usuarios, MODERADORES_INDEX, ESTUDIANTES_INDEX, USUARIO_INDEX)
    elif adminPos != -1:
        arLoAdmin.seek(adminPos, 0)
        admin = Admin()
        admin = pickle.load(arLoAdmin)

        if (contraseña == admin.contrasena):
            arreglo_sesion[ADMINISTRADOR_INDEX] = True
            arreglo_usuarios[USUARIO_INDEX] = adminPos
            
            os.system("cls")
            print("Sesión iniciada correctamente")
            menu_administradores(arreglo_usuarios, MODERADORES_INDEX, USUARIO_INDEX)

    while intentos > 1 and (not arreglo_sesion[ESTUDIANTES_INDEX] and not arreglo_sesion[MODERADORES_INDEX] and not arreglo_sesion[ADMINISTRADOR_INDEX]):

        while intentos > 1 and (not arreglo_sesion[ESTUDIANTES_INDEX] and not arreglo_sesion[MODERADORES_INDEX] and not arreglo_sesion[ADMINISTRADOR_INDEX]) and (estPos == -1 or modPos == -1 or adminPos == -1):
            os.system("cls")
            print("Email o contraseña incorrectos")
            intentos -= 1
            print("\nQuedan ", intentos, "intentos\n")

            email = str(input("Ingrese email: "))
            while len(email) > 32:
                print("El email no puede tener más de 32 caracteres")
                email = str(input("Ingrese email: "))
            if len(email) < 32:
                email = email.ljust(32, " ")
            elif len(email) == 32:
                email = email

            
            estPos = buscar_estudiante("email", email)
            modPos = buscar_moderador("email", email)
            adminPos = buscar_administrador("email", email)

            contraseña = getpass.getpass("Ingrese su contraseña: ")
            while len(contraseña) > 32:
                print("La contraseña no puede tener más de 32 caracteres")
                contraseña = getpass.getpass("Ingrese contraseña: ")
            if len(contraseña) < 32:
                contraseña = contraseña.ljust(32, " ")
            elif len(contraseña) == 32:
                contraseña = contraseña

        if estPos != -1:
            arLoEst.seek(estPos, 0)
            estudiante = Estudiante()
            estudiante = pickle.load(arLoEst)

            if ((contraseña == estudiante.contrasena and estudiante.baja == "N")):
                arreglo_sesion[ESTUDIANTES_INDEX] = True
                arreglo_usuarios[USUARIO_INDEX] = estPos
                
                os.system("cls")
                print("Sesión iniciada correctamente")
                menu_estudiante(arreglo_usuarios, ESTUDIANTES_INDEX, USUARIO_INDEX)
        elif modPos != -1:
            arLoMod.seek(modPos, 0)
            moderador = Moderador()
            moderador = pickle.load(arLoMod)

            if ((contraseña == moderador.contrasena and moderador.baja == "N")):
                arreglo_sesion[MODERADORES_INDEX] = True
                arreglo_usuarios[USUARIO_INDEX] = modPos
                
                os.system("cls")
                print("Sesión iniciada correctamente")
                menu_moderadores(arreglo_usuarios, MODERADORES_INDEX, ESTUDIANTES_INDEX, USUARIO_INDEX)
        elif adminPos != -1:
            arLoAdmin.seek(adminPos, 0)
            admin = Admin()
            admin = pickle.load(arLoAdmin)

            if (contraseña == admin.contrasena):
                arreglo_sesion[ADMINISTRADOR_INDEX] = True
                arreglo_usuarios[USUARIO_INDEX] = adminPos
                
                os.system("cls")
                print("Sesión iniciada correctamente")
                menu_administradores(arreglo_usuarios, MODERADORES_INDEX, USUARIO_INDEX)
    os.system("cls")

"""
PROCEDIMIENTO ingresar
MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, ESTUDIANTES_INDEX, MODERADORES_INDEX, USUARIO_INDEX: enteros

arreglo_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios:   arreglo unidimesional de enteros
"""
def ingresar(MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, arreglo_sesion, arreglo_usuarios, ESTUDIANTES_INDEX, MODERADORES_INDEX, ADMINISTRADOR_INDEX, USUARIO_INDEX):
    os.system("cls")
    if(MIN_CANT_ESTUDIANTES <= mostrar_cantidad_registros_estudiantes() and MIN_CANT_MODERADORES <= mostrar_cantidad_registros_moderadores()):        
        arreglo_sesion[MODERADORES_INDEX] = False
        arreglo_sesion[ESTUDIANTES_INDEX] = False
        arreglo_sesion[ADMINISTRADOR_INDEX] = False
        validar_ingreso(arreglo_usuarios, ESTUDIANTES_INDEX, MODERADORES_INDEX, ADMINISTRADOR_INDEX, arreglo_sesion, USUARIO_INDEX)
    else:        
        print("No se puede ingresar, cantidad de estudiantes y moderadores insuficientes")

"""
PROCEDIMIENTO ingresar_datos_moderadores
MODERADORES_INDEX: enteros
nombre, apellido, email, contraseña, confirmar_contraseña: string

arreglo_usuarios:   arreglo unidimesional de enteros
"""
def ingresar_datos_moderadores(arreglo_usuarios, MODERADORES_INDEX):
    os.system("cls")
    nombre = input("Ingrese el nombre del moderador: ")
    apellido = input("Ingrese el apellido del moderador: ")
    email = input("Ingrese el email del moderador: ")

    contraseña = input("Ingrese su contraseña: ")
    confirmar_contraseña = input("Vuelva a ingresar su contraseña: ")
    while contraseña != confirmar_contraseña:
        print("La contraseña no coincide, vuelva a intentar: ")
        contraseña = input("Ingrese su contraseña: ")
        confirmar_contraseña = input("Vuelva a ingresar su contraseña: ")

    if contraseña == confirmar_contraseña:
        pass

"""
PROCEDIMIENTO registrar_estudiante
tamReg, tamArc, cantReg: enteros
arFiEst, nomYApe, email, continuar: str
estudiante: Estudiante
arreglo_usuarios:   arreglo unidimesional de enteros
arLoEst: BufferedRandom
"""
def registrar_estudiante(arreglo_usuarios, MAX_CANT_ESTUDIANTES, ESTUDIANTES_INDEX):
    global arFiEst, arLoEst
    os.system("cls")
    print("\nRegistrar estudiante\n")
    estudiante = Estudiante()
    continuar = str(input("Seguro deasea registrar un estudiante (S/N)?: "))
    continuar = continuar.upper()
    while continuar != "S" and continuar != "N":
        print("Por favor, ingrese una opción válida (S/N)")
        continuar = str(input("Seguro deasea registrar un estudiante (S/N)?: "))
        continuar.upper()
    while continuar == "S":
        if os.path.getsize(arFiEst) == 0:
            estudiante.id_estudiante = 1
        else:
            arLoEst.seek(0,0)
            estudiante = pickle.load(arLoEst)
            tamReg = arLoEst.tell()
            tamArc = os.path.getsize(arFiEst)
            cantReg = tamArc // tamReg
            estudiante.id_estudiante = cantReg + 1
            
        # Ingreso y formateo campo nombre
        nomYApe = str(input("Ingrese nombre y apellido: "))
        while len(nomYApe) > 32:
            print("El nombre y apellido no puede tener más de 32 caracteres")
            nomYApe = str(input("Ingrese nombre y apellido: "))
        if len(nomYApe) < 32:
            estudiante.nombre = nomYApe.ljust(32, " ")
        elif len(nomYApe) == 32:
            estudiante.nombre = nomYApe

        # Ingreso y formateo campo email
        email = str(input("Ingrese email: "))
        while len(email) > 32:
            print("El email no puede tener más de 32 caracteres")
            email = str(input("Ingrese email: "))
        if len(email) < 32:
            estudiante.email = email.ljust(32, " ")
        elif len(email) == 32:
            estudiante.email = email

        #validar email
        while buscar_administrador("email", estudiante.email) != -1 or buscar_moderador("email", estudiante.email) != -1 or buscar_estudiante("email", estudiante.email) != -1:
            print("Email inválido, intente de nuevo")
            email = str(input("Ingrese un mail valido: "))
            while len(email) > 32:
                print("El email no puede tener más de 32 caracteres")
                email = str(input("Ingrese email: "))
            if len(email) < 32:
                estudiante.email = email.ljust(32, " ")
            elif len(email) == 32:
                estudiante.email = email

        # Ingreso y formateo campo contraseña
        contraseña = str(input("Ingrese contraseña: "))
        while len(contraseña) > 32:
            print("La contraseña no puede tener más de 32 caracteres")
            contraseña = str(input("Ingrese contraseña: "))
        if len(contraseña) < 32:
            estudiante.contrasena = contraseña.ljust(32, " ")
        elif len(contraseña) == 32:
            estudiante.contrasena = contraseña
        
        empty = ""
        estudiante.biografia = empty.ljust(255, " ")
        estudiante.hobbies = empty.ljust(255, " ")
        estudiante.fecha_nacimiento = "00-00-0000"
        estudiante.baja = "N"

        arLoEst.seek(0, 2)
        pickle.dump(estudiante, arLoEst)
        arLoEst.flush()

        continuar = str(input("Seguro deasea registrar otro estudiante (S/N)?: "))
        continuar = continuar.upper()
        while continuar != "S" and continuar != "N":
            print("Por favor, ingrese una opción válida (S/N)")
            continuar = str(input("Seguro deasea registrar un estudiante (S/N)?: "))
            continuar = continuar.upper()
    os.system("cls")
    print("Estudiante registrado\n")

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
    print(" b. Volver\n")

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
arLoAdmin, arLoMod, arLoEst: BufferedRandom 
"""
def abrir_archivos():
    global arFiAdmin, arLoAdmin, arFiMod, arLoMod, arFiEst, arLoEst, arFiLi, arLoLi, arLoRep, arFiRep

    arFiAdmin = "registroAdmins.dat"
    arFiMod =   "registroMods.dat"
    arFiEst =   "registroEsts.dat"
    arFiLi =    "registroLikes.dat"
    arFiRep =   "registroReportes.dat"

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

    if os.path.exists(arFiLi):
        arLoLi = open(arFiLi, "r+b")
    else:
        print(f"El archivo {arFiLi} se creo")
        arLoLi = open(arFiLi, "w+b")

    if os.path.exists(arFiRep):
        arLoRep = open(arFiRep, "r+b")
    else:
        print(f"El archivo {arFiRep} se creo")
        arLoRep = open(arFiRep, "w+b")   

"""
PROCEDIMIENTO cerrar_archivos
arLoAdmin, arLoMod, arLoEst: BufferedRandom 
"""
def cerrar_archivos():
    global arLoAdmin, arLoMod, arLoEst, arLoLi, arLoRep
    arLoEst.close()
    arLoAdmin.close()
    arLoMod.close()
    arLoRep.close()
    arLoLi.close()
    print("Archivos cerrados")

def crearadmin():
    global arFiAdmin, arLoAdmin
    if os.path.getsize(arFiAdmin) == 0: 
        admin = Admin()

        admin.id_admin = 999
        email = "admin"
        admin.email = email.ljust(32, " ")
        contraseña = "admin"
        admin.contrasena = contraseña.ljust(32, " ")
        pickle.dump(admin, arLoAdmin)
        arLoAdmin.flush()

"""
PROCEDIMIENTO crear_moderador

arFiMod, email, contraseña: str
arLoMod: BufferedRandom
moderador: Moderador
"""
def crear_moderardor():
    global arFiMod, arLoMod

    if os.path.getsize(arFiMod) == 0: 
        moderador = Moderador()

        moderador.id = 1
        email = "mod@ayed.com"
        moderador.email = email.ljust(32, " ")
        contraseña = "mod"
        moderador.contrasena = contraseña.ljust(32, " ")
        pickle.dump(moderador, arLoMod)
        arLoMod.flush()

"""
PROCEDIMIENTO ejecutar_programa_principal
MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, USUARIO_INDEX, ESTUDIANTES_INDEX, MODERADORES_INDEX, opc: enteros

arreglo_sesion:    arreglo unidimensional de booleanos
arreglo_usuarios:   arreglo unidimesional de enteros
"""
def ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, arreglo_sesion, arreglo_usuarios, ESTUDIANTES_INDEX, MODERADORES_INDEX, USUARIO_INDEX, ADMINISTRADOR_INDEX):
    
    ## iniciar archivos
    abrir_archivos()
    popular_likes_aleatorios()
    crearadmin()
    crear_moderardor()
    mostrar_menu_principal()

    opc = validar_numero()
    while opc < 0 and opc > 4:
        print("Opción inválida")
        opc = validar_numero()

    while opc != 0:
        match opc:
            case 1:
                registrar_estudiante(arreglo_usuarios, MAX_CANT_ESTUDIANTES, ESTUDIANTES_INDEX)
            case 2:
                ingresar(MIN_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, arreglo_sesion, arreglo_usuarios, ESTUDIANTES_INDEX, MODERADORES_INDEX, ADMINISTRADOR_INDEX, USUARIO_INDEX)
            case 3:
                #bonus1
                calcular_puntaje_candidatos()
                pass
            case 4:
                #bonus2
                pass
            case 5:
                #bonus3
                pass

        mostrar_menu_principal()
        opc = validar_numero()
        while opc < 0 and opc > 4:
            print("Opción inválida")
            opc = validar_numero()

    os.system("cls")
    cerrar_archivos()
    print("\nPrograma finalizado, esperamos tu regreso...\n")

ejecutar_programa_principal(MIN_CANT_ESTUDIANTES, MAX_CANT_ESTUDIANTES, MIN_CANT_MODERADORES, MAX_CANT_MODERADORES, arreglo_sesion, arreglo_usuarios, ESTUDIANTES_INDEX, MODERADORES_INDEX, USUARIO_INDEX, ADMINISTRADOR_INDEX)
