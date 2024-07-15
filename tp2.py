'''
TP#1 AyED Comisión 113
Rojo Nicolás
Frenna Luca
Alegre Sebastian
Cosenza María Soledad
'''
# Librerias
import os
import getpass
from datetime import datetime

def usu_mm():#el prefijo "usu" nos permite ver todas las funciones dedicadas a los usuarios, para facil acceso y no confundirse
    os.system("cls")
    print("Menu ")
    print("\n1. Gestionar mi perfil")
    print("2. Gestionar candidatos")
    print("3. Matcheos")
    print("4. Reportes estadisticos")
    print("0. Salir")

def mod_mm():#el prefijo "mod" nos deja ver todas las funciones de los mods, para facil acceso y no confundirse
    os.system("cls")
    print("Menu ")
    print("\n1. Gestionar usuarios")
    print("2. Gestionar reportes")
    print("3. Reportes estadisticos")
    print("0. Salir")

def main_usuarios():
    opc = 1 
    while (opc!=0):
        os.system("cls")
        usu_mm()
        opc = int(input("Ingrese su opcion: "))
        match opc:
            case 1: usu_gestionar_mi_perfil()
            case 2: usu_gestionar_candidatos() 
            case 3: usu_matcheos() 
            case 4: reportes_estadisticos() 
            case 0: print('\n\n GRACIAS POR USAR NUESTRO SISTEMA!!!!')
        while (opc<0 or opc>4):
            os.system("cls")
            usu_mm()
            opc = int(input("Ingreso Invalido - reintente ... "))
            match opc:
                case 1: usu_gestionar_mi_perfil()
                case 2: usu_gestionar_candidatos() 
                case 3: usu_matcheos() 
                case 4: reportes_estadisticos()
                case 0: print('\n\n GRACIAS POR USAR NUESTRO SISTEMA!!!!')

def main_mods():
    opc = 1 
    while (opc!=0):
        os.system("cls")
        mod_mm()
        opc = int(input("Ingrese su opcion: "))
        match opc:
            case 1: mod_gestionar_usuarios()
            case 2:  mod_gestionar_reportes()
            case 3:  reportes_estadisticos()
            case 0: print('\n\n GRACIAS POR USAR NUESTRO SISTEMA!!!!')
        while (opc<0 or opc>4):
            os.system("cls")
            mod_mm()
            opc = int(input("Ingreso Invalido - reintente ... "))
            match opc:
                case 1: mod_gestionar_usuarios()
                case 2:  mod_gestionar_reportes()
                case 3:  reportes_estadisticos()
                case 0: print('\n\n GRACIAS POR USAR NUESTRO SISTEMA!!!!')

def mod_gestionar_usuarios():
    os.system("cls")
    print("Gestionar usuarios")
    print("\na. Desactivar usuario")
    print("b. Volver")
    opc = str(input("Ingrese su opcion: "))
    match opc:
        case "a": mod_desactivar_ususario()
        case "b": print("Volviendo al menu anterior")
    while (opc!="b"):
        os.system("cls")
        print("Gestionar usuarios")
        print("\na. Desactivar usuario")
        print("b. Volver")
        opc = str(input("Ingreso Invalido - reintente ... "))
        match opc:
            case "a": mod_desactivar_ususario()
            case "b":  print("Volviendo al menu anterior")

def mod_desactivar_ususario():
    os.system("cls")
    print("Desactivar usuario")
    opc=str(input("Ingrese ID o nombre de usuario: "))#esto esta hecho mara comprobar si funciona

def mod_gestionar_reportes():
    os.system("cls")
    print("Gestionar reportes")
    print("\na. Ver reportes")
    print("b. Volver")
    opc = str(input("Ingrese su opcion: "))
    match opc:
        case "a": mod_ver_reportes()
        case "b": print("Volviendo al menu anterior")
    while (opc!="b"):
        os.system("cls")
        print("Gestionar reportes")
        print("\na. Ver reportes")
        print("b. Volver")
        opc = str(input("Ingreso Invalido - reintente ... "))
        match opc:
            case "a": mod_ver_reportes()
            case "b":  print("Volviendo al menu anterior")

reportes=["pooner reportes aca"]#no esta hecho todavia, solo es de relleno para el resto del sistema

def mod_ver_reportes():
    os.system("cls")
    print("Ver reportes")
    print(reportes)
    opc = str(input("Desea volver?: "))#esto esta hecho para comprobar si funciona

def reportes_estadisticos():
    print("3")

def usu_gestionar_mi_perfil():    
    os.system("cls")
    print("Gestionar mi perfil")
    print("\na. Editar mis datos personales")
    print("c. Volver")
    opcion = str(input("Ingrese su opción: "))
    while opcion != "c":
        if opcion == "a": 
            usu_editar_mis_datos_personales()         
        os.system("cls")    
        print("Gestionar mi perfil")
        print("\na. Editar mis datos personales")
        print("c. Volver")
        opcion = str(input("Ingreso Invalido - reintente ... "))

'''
FUN gestionar_candidatos
opcion: str
'''
def usu_gestionar_candidatos():
    os.system("cls")
    print("Gestionar candidatos")
    print("\na. Elegir candidato para matchear")
    print("c. Volver")
    opcion = str(input("Ingrese su opción: "))  
    while opcion != "c":
        if opcion == "a":
            usu_ver_candidatos() 
        os.system("cls")
        print("Gestionar candidatos")
        print("\na. Elegir candidato para matchear")
        print("c. Volver")     
        opcion = str(input("Ingreso Invalido - reintente ... "))

'''
FUN matcheos
opcion: str
'''
def usu_matcheos():
    os.system("cls")
    print("Matcheos")
    print("\nEn construcción")
    print("a. Volver")
    opcion = str(input("Ingrese su opción: "))
    while opcion != "a":
        os.system("cls")
        print("Matcheos")
        print("\nEn construcción")
        print("a. Volver")         
        opcion = str(input("Ingreso Invalido - reintente ... "))

'''
FUN reportes_estadisticos
opcion: str
'''
def reportes_estadisticos():
    os.system("cls")
    print("Reportes estadisticos")
    print("\nEn construcción")
    print("a. Volver")
    opc = str(input("Ingrese su opción: "))
    while opc != "a":
        os.system("cls")
        print("Reportes estadisticos")
        print("\nEn construcción")
        print("a. Volver")  
        opc = str(input("Ingreso Invalido - reintente ... "))

'''
FUN editar_mis_datos_personales
opcion: str
'''       
def usu_editar_mis_datos_personales():
    os.system("cls")
    usu_menu_de_mis_datos()
    print("\nEditar mis datos personales")
    print(" a. Editar mi fecha de nacimiento")
    print(" b. Editar mi biografía")
    print(" c. Editar mis hobbies")
    print(" d. Volver")  
    opcion = str(input("Ingrese su opción: "))
    while opcion != "d":
        if opcion == "a": 
            usu_editar_mi_fecha_de_nacimiento()
        elif opcion == "b":
            usu_editar_mi_biografia()          
        elif opcion == "c":
            usu_editar_mis_hobbies()  
        os.system("cls")
        usu_menu_de_mis_datos()
        print("\nEditar mis datos personales")
        print(" a. Editar mi fecha de nacimiento")
        print(" b. Editar mi biografía")
        print(" c. Editar mis hobbies")  
        print(" d. Volver")  
        opcion = str(input("Ingreso Invalido - reintente ... "))

def usu_ver_candidatos():
    os.system("cls")
    usu_mostrar_todos_los_candidatos()
    print("Gestionar candidatos")
    print("\na. Ingresar el nombre del candidato")
    print("b. Volver")  
    opcion = str(input("Ingrese su opción: "))
    while opcion != "b":
        if opcion == "a": 
            usu_dar_me_gusta_al_candidato()
        print("\nGestionar candidatos")
        print(" a. Ingresar el nombre del candidato")
        print(" b. Volver")  
        opcion = str(input("Ingreso Invalido - reintente ... "))

'''
FUN mostrar_todos_los_candidatos
email_usuario_autenticado, usuario1_email, usuario2_email, usuario3_email, usuario1_nombre, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, usuario2_nombre, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, usuario3_nombre, usuario3_fecha_de_nacimiento, usuario3_biografia, usuario3_hobbies: str
'''
def usu_mostrar_todos_los_candidatos():
    cv = "" #cv = (campo vacio)
    print("Candidatos\n")
    if email_usuario_autenticado == usuario1_email:
        usu_mostrar_datos(cv, cv, usuario2_nombre, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, cv)
        print("\n")
        usu_mostrar_datos(cv, cv, usuario3_nombre, usuario3_fecha_de_nacimiento, usuario3_biografia, usuario3_hobbies, cv)
    elif email_usuario_autenticado == usuario2_email:
        usu_mostrar_datos(cv, cv, usuario1_nombre, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, cv)
        print("\n")
        usu_mostrar_datos(cv, cv, usuario3_nombre, usuario3_fecha_de_nacimiento, usuario3_biografia, usuario3_hobbies, cv)
    elif email_usuario_autenticado == usuario3_email:
        usu_mostrar_datos(cv, cv, usuario1_nombre, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, cv)
        print("\n")
        usu_mostrar_datos(cv, cv, usuario2_nombre, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, cv)

'''
FUN dar_me_gusta_al_candidato
usuario1_me_gusta, usuario2_me_gusta, usuario3_me_gusta, nombre_candidato, email_usuario_autenticado, usuario1_nombre, usuario2_nombre, usuario3_nombre: str
'''
def usu_dar_me_gusta_al_candidato():
    global usuario1_me_gusta, usuario2_me_gusta, usuario3_me_gusta

    nombre_candidato = str(input("Ingrese el nombre su candidato: "))
    while (nombre_candidato != usuario1_nombre and nombre_candidato != usuario2_nombre and nombre_candidato != usuario3_nombre):
        print("El nombre del candidato no es válido")
        nombre_candidato = str(input("Ingrese un nombre válido: "))
    
    if email_usuario_autenticado == usuario1_email:
        usuario1_me_gusta = nombre_candidato
    elif email_usuario_autenticado == usuario2_email:
        usuario2_me_gusta = nombre_candidato
    elif email_usuario_autenticado == usuario3_email:
        usuario3_me_gusta = nombre_candidato
    
    print("El candidato ha sido seleccionado correctamente")

'''
FUN menu_de_mis_datos()
usuario1_email, usuario1_contraseña, usuario1_nombre, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, usuario1_me_gusta, usuario2_email, usuario2_contraseña, usuario2_nombre, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, usuario2_me_gusta, email_usuario_autenticado, usuario3_email, usuario3_contraseña, usuario3_nombre, usuario3_fecha_de_nacimiento, usuario3_biografia, usuario3_hobbies, usuario3_me_gusta: str
''' 
def usu_menu_de_mis_datos():
    os.system("cls")
    print("Mis datos personales")
    if (email_usuario_autenticado == usuario1_email):
        usu_mostrar_datos(usuario1_email, usuario1_contraseña, usuario1_nombre, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, usuario1_me_gusta)
    elif (email_usuario_autenticado == usuario2_email):
        usu_mostrar_datos(usuario2_email, usuario2_contraseña, usuario2_nombre, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, usuario2_me_gusta)
    elif (email_usuario_autenticado == usuario3_email):
        usu_mostrar_datos(usuario3_email, usuario3_contraseña, usuario3_nombre, usuario3_fecha_de_nacimiento, usuario3_biografia, usuario3_hobbies, usuario3_me_gusta)

'''
FUN editar_mi_fecha_de_nacimiento
usuario1_fecha_de_nacimiento, usuario2_fecha_de_nacimiento, usuario3_fecha_de_nacimiento, nueva_fecha_de_nacimiento: str
'''
def usu_editar_mi_fecha_de_nacimiento():
    global usuario1_fecha_de_nacimiento, usuario2_fecha_de_nacimiento, usuario3_fecha_de_nacimiento 

    nueva_fecha_de_nacimiento = str(input("Ingrese su fecha de nacimiento: "))
    if (email_usuario_autenticado == usuario1_email):
        usuario1_fecha_de_nacimiento = nueva_fecha_de_nacimiento
    elif (email_usuario_autenticado == usuario2_email):
        usuario2_fecha_de_nacimiento = nueva_fecha_de_nacimiento
    elif (email_usuario_autenticado == usuario3_email):
        usuario3_fecha_de_nacimiento = nueva_fecha_de_nacimiento
    else:
        print("Error")

'''
FUN editar_mi_biografia
usuario1_biografia, usuario2_biografia, usuario3_biografia, nueva_biografia: str
'''
def usu_editar_mi_biografia():
    global usuario1_biografia, usuario2_biografia, usuario3_biografia

    nueva_biografia = str(input("Ingrese su biografia: "))
    if (email_usuario_autenticado == usuario1_email):
        usuario1_biografia = nueva_biografia
    elif (email_usuario_autenticado == usuario2_email):
        usuario2_biografia = nueva_biografia
    elif (email_usuario_autenticado == usuario3_email):
        usuario3_biografia = nueva_biografia
    else:
        print("El ususario no existe")

'''
FUN editar_mis_hobbies
usuario1_hobbies, usuario2_hobbies, usuario3_hobbies, nuevos_hobbies: str
'''
def usu_editar_mis_hobbies():
    global usuario1_hobbies, usuario2_hobbies, usuario3_hobbies

    nuevos_hobbies = str(input("Ingrese sus hobbies: "))
    if (email_usuario_autenticado == usuario1_email):
        usuario1_hobbies = nuevos_hobbies
    elif (email_usuario_autenticado == usuario2_email):
        usuario2_hobbies = nuevos_hobbies
    elif (email_usuario_autenticado == usuario3_email):
        usuario3_hobbies = nuevos_hobbies
    else:
        print("Error")

'''
FUN mostrar_edad
fecha_nacimiento, fecha_actual: date
edad: int
'''
def usu_mostrar_edad(fecha):
    fecha_nacimiento = datetime.strptime(fecha, '%Y-%m-%d')   #dudoso 
    fecha_actual = datetime.now()
    
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    
    return edad

'''
FUN mostrar_datos
usuario_email, usuario_contraseña, usuario_nombre, usuario_fecha_de_nacimiento, usuario_biografia, usuario_hobbies, usuario_me_gusta: str
'''
def usu_mostrar_datos(usuario_email, usuario_contraseña, usuario_nombre, usuario_fecha_de_nacimiento, usuario_biografia, usuario_hobbies, usuario_me_gusta):
    
    if(usuario_email):
        print("\nEmail: ", usuario_email)
    if(usuario_contraseña):
        print("Contraseña: ", usuario_contraseña)
    if(usuario_nombre):   
        print("Nombre: ", usuario_nombre)
    if(usuario_fecha_de_nacimiento):   
        print("Fecha de nacimiento: ", usuario_fecha_de_nacimiento)
    if(usuario_biografia):   
        print("Biografia: ", usuario_biografia)
    if(usuario_fecha_de_nacimiento):   
        print("Edad: ", usu_mostrar_edad(usuario_fecha_de_nacimiento), "años")
    if(usuario_hobbies):   
        print("Hobbies: ", usuario_hobbies)
    if(usuario_me_gusta):   
        print("Me gusta: ", usuario_me_gusta)

def validar_numero():
    while True:
        try:
            return int(input("Ingrese un número entre 0 y 4: "))
        except ValueError:
            print("Debe ingresar un número")



def declarar_constantes():
    global usuario1_email, usuario1_contraseña, usuario1_nombre, usuario1_me_gusta, usuario2_email, usuario2_contraseña, usuario2_nombre, usuario2_me_gusta, usuario3_email, usuario3_me_gusta, usuario3_contraseña, usuario3_nombre, intentos_restantes, isLoggedIn, intentos_restantes, email_usuario_autenticado, usuario1_fecha_de_nacimiento, usuario1_biografia, usuario1_hobbies, usuario2_fecha_de_nacimiento, usuario2_biografia, usuario2_hobbies, usuario3_fecha_de_nacimiento,usuario3_biografia, usuario3_hobbies

    #Usuario 1 dec vars
    usuario1_email = "estudiante1@ayed.com"
    usuario1_contraseña = "111222"
    usuario1_me_gusta = ""
    usuario1_fecha_de_nacimiento = "1985-02-25"
    usuario1_nombre = "Carlos"
    usuario1_biografia = "Nacido en Rosario"
    usuario1_hobbies = "tocar la guitarra y correr"

    #Usuario2 decl vars
    usuario2_email = "estudiante2@ayed.com"
    usuario2_contraseña = "333444"
    usuario2_me_gusta = ""
    usuario2_fecha_de_nacimiento = "2001-12-06"
    usuario2_nombre = "Ramiro"
    usuario2_biografia = "Nacido en Misiones"
    usuario2_hobbies = "Dibujar y pintar"

    #Usuario3 dec vars
    usuario3_email = "estudiante3@ayed.com"
    usuario3_contraseña = "555666"
    usuario3_me_gusta = ""
    usuario3_fecha_de_nacimiento = "1993-05-25"
    usuario3_nombre = "Sandra"
    usuario3_biografia = "Nacida en San Francisco"
    usuario3_hobbies = "Cocinar y cantar en el coro"

    intentos_restantes = 3
    email_usuario_autenticado = ""



main_mods()
main_usuarios()
