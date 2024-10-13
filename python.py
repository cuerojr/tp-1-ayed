import os.path
import pickle

class contacto:
    def __init__(self):
        self.codigo = 0
        self.nombreApellido = ""
        self.telefono = ""
        self.mail = ""
        self.baja = ""

class Moderador:
    def __init__(self):
        self.id = 0             #int
        self.email = ""         #string 32
        self.contraseña = ""    #string 32
        self.estado = False     #boolean
        self.ignorado = 0       #int
        self.aceptado = 0       #int

class Reportes:
    def __init__(self):
        self.id_reportante = 0      #int
        self.id_reportado = 0       #int
        self.motivo = ""            #string 255
        self.estado = 0             #int 0 reportado por ver, 1 usuario baneado, 2 omitido

def abrir_Archivos():
    global arFiCon, arFiMod, arFiRep
    global arLoCon, arLoMod, arLoRep
    arFiCon = "contacto.dat"
    arFiMod = "registroMods.dat"
    arFiRep = "registroReportes.dat"
    if os.path.exists(arFiCon):
        print(f"El archivo {arFiCon} ya existe")
        arLoCon = open(arFiCon,"r+b")
    else:
        print("El archivo " + arFiCon + " NO existia y fue creado")
        arLoCon = open(arFiCon, "w+b")
    if os.path.exists(arFiRep):
        print(f"El archivo {arFiRep} ya existe")
        arLoRep = open(arFiRep,"r+b")
    else:
        print("El archivo " + arFiRep + " NO existia y fue creado")
        arLoRep = open(arFiRep, "w+b")
    if os.path.exists(arFiMod):
        print(f"El archivo {arFiMod} ya existe")
        arLoMod = open(arFiMod,"r+b")
    else:
        print("El archivo " + arFiMod + " NO existia y fue creado")
        arLoMod = open(arFiMod, "w+b")


def cerrar_Archivos():
    print("Se cerró el archivo")
    arLoCon.close()

def mostrar_Menu():
    print("1- Crear contacto")
    print("2- Mostrar un contacto")
    print("3- Modificar un contacto")
    print("4- Eliminar contacto")
    print("5- Mostrar toda la libreta de contactos")
    print("0- Salir")

def ordenarContactosPorNombre():
    global arFiCon
    global arLoCon
    con1 = contacto()
    con2 = contacto()
    arLoCon.seek(0,0)
    con1 = pickle.load(arLoCon)
    tamReg = arLoCon.tell()
    tamArch = os.path.getsize(arFiCon)
    cantReg = tamArch//tamReg
    for i in range(cantReg-1):
        for j in range(i+1,cantReg):
            arLoCon.seek(i*tamReg,0)
            con1 = pickle.load(arLoCon)
            arLoCon.seek(j*tamReg,0)
            con2 = pickle.load(arLoCon)
            if con1.nombreApellido > con2.nombreApellido:
                arLoCon.seek(i*tamReg,0)
                pickle.dump(con2,arLoCon)
                arLoCon.flush
                arLoCon.seek(j*tamReg,0)
                pickle.dump(con1,arLoCon)
                arLoCon.flush

def crear_Contacto():
    global arFiCon
    global arLoCon
    con = contacto()
    continuar="S"
    while continuar == "S":
        if os.path.getsize(arFiCon) == 0:
            con.codigo = 1
        
        else:
            arLoCon.seek(0,0)
            con = pickle.load(arLoCon)
            tamReg = arLoCon.tell()
            tamArch = os.path.getsize(arFiCon)
            cantReg = tamArch//tamReg
            con.codigo = cantReg + 1
        
        nomYape = input("Ingrese el Nonmbre y Apellido (Máximo 30 caracteres): ")
        while len(nomYape) > 30:
            print("Solo 30 caracteres")
            nomYape = str(input("Ingrese el Nonmbre y Apellido (Máximo 30 caracteres): "))
        if len(nomYape) < 30:
            con.nombreApellido = nomYape.ljust(30," ")
        elif len(nomYape) == 30:
            con.nombreApellido = nomYape

        tel = input("Ingrese el n° de telefono de la persona (Máximo 15 caracteres): ")
        while len(tel) > 15:
            print("Solo 15 caracteres")
            tel = str(input("Ingrese el n° de telefono de la persona (Máximo 15 caracteres): "))
        if len(tel) < 15:
            con.telefono = tel.ljust(15," ")
        elif len(tel) == 15:
            con.telefono = tel

        mail = input("Ingrese el mail (Máximo 30 caracteres): ")
        while len(mail) > 30:
            print("Solo 30 caracteres")
            mail = str(input("Ingrese el mail (Máximo 30 caracteres): "))
        if len(mail) < 30:
            con.mail = mail.ljust(30," ")
        elif len(mail) == 30:
            con.mail = mail
        con.baja = "N"
        arLoCon.seek(0,2)
        u = arLoCon.tell()
        pickle.dump(con,arLoCon)
        arLoCon.flush
        arLoCon.seek(u,0)
        con = pickle.load(arLoCon)
        print(con.codigo,"     ",con.nombreApellido,"     ",con.telefono,"     ",con.mail)
        continuar = "L"
        while continuar != "S" and continuar != "N":
            continuar = input("¿Desea continuar creando contactos?(Ingrese S (Sí) o N (No)): ")
            continuar = continuar.upper()
    
    ordenarContactosPorNombre()
    arLoCon.flush
    arLoCon.seek(0,0)
    print("Código    Nombre y Apelldio                     Teléfono                Mail")
    while arLoCon.tell() < os.path.getsize(arFiCon):
        con = pickle.load(arLoCon)
        print(con.codigo,"       ",con.nombreApellido,"      ",con.telefono,"     ",con.mail)

def busquedaDico(ref):
    global arFiCon
    global arLoCon
    arLoCon.seek(0,0)
    con = pickle.load(arLoCon)
    tamReg = arLoCon.tell()
    tamArch = os.path.getsize(arFiCon)
    cantReg = tamArch//tamReg
    prim = 0
    ult = cantReg
    med = (ult+prim)//2
    arLoCon.seek(med*tamReg,0)
    p = arLoCon.tell()
    con = pickle.load(arLoCon)
    nomYape = con.nombreApellido.rstrip()
    while nomYape != ref and prim < ult:
        if nomYape > ref:
            ult = med - 1
        else:
            prim = med + 1
        med = (ult+prim)//2
        arLoCon.seek(med*tamReg,0)
        p = arLoCon.tell()
        con = pickle.load(arLoCon)
        nomYape = con.nombreApellido.rstrip()
    if nomYape == ref:
        return p
    else:
        return -1

def mostrar_Contacto():
    global arFiCon
    global arLoCon
    con = contacto()
    nomYape = str(input("Ingrese el nombre de la persona que está buscando: "))
    pos = busquedaDico(nomYape)
    if pos != -1:
        arLoCon.seek(pos,0)
        con = pickle.load(arLoCon)
        print(f"El nombre es {con.nombreApellido}")
        print(f"El telefono es {con.telefono}")
    else:
        print("El contacto no fue encontrado")

def modificar_Contacto():
    global arFiCon
    global arLoCon
    con = contacto()
    nomYape = str(input("Ingrese el nombre de la persona que está buscando: " ))
    pos = busquedaDico(nomYape)
    if pos != -1:
        arLoCon.seek(pos,0)
        con = pickle.load(arLoCon)
        if con.baja == "N":
            opc = -1
            while opc != 0:
                print(f"1- Nombre y Apellido - Actual: {con.nombreApellido}")
                print(f"2- Teléfono - Actual: {con.telefono}")
                print(f"3- Mail - Actual: {con.mail}")
                print("0- Dejar de editar")
                opc = int(input("¿Qué atributo desea modificar? "))
                while opc > 3 and opc < 0:
                    print("Opción incorrecta")
                    opc = int(input("¿Qué atributo desea modificar? "))
                match opc:
                    case 1:
                        nomYape = str(input("Ingrese nombre y apellido (Máximo de 30 caractéres): "))
                        while len(nomYape) > 30:
                            print("Hasta 30 caracttéres solo")
                            nomYape = str(input("Ingrese nombre y apellido (Máximo de 30 caractéres): "))
                        if len(nomYape) < 30:
                            con.nombreApellido = nomYape.ljust(30," ")
                        elif len(nomYape) == 30:
                            con.nombreApellido = nomYape
                        print("Los nuevos datos son:")
                        print(f"Nombre y Apellido: {con.nombreApellido}")
                        print(f"Teléfono: {con.telefono}")
                        print(f"Mail: {con.mail}")
                    case 2:
                        tel = str(input("Ingrese el nuevo numero de telefono: "))
                        while len(tel) > 15:
                            print("Hasta 30 caracttéres solo")
                            tel = str(input("Ingrese nombre y apellido (Máximo de 15 caractéres): "))
                        if len(tel) < 30:
                            con.telefono = tel.ljust(15," ")
                        elif len(tel) == 15:
                            con.telefono = tel
                        print("Los nuevos datos son:")
                        print(f"Nombre y Apellido: {con.nombreApellido}")
                        print(f"Teléfono: {con.telefono}")
                        print(f"Mail: {con.mail}")
                    case 3:
                        mail = str(input("Ingrese el nuevo mail: "))
                        while len(mail) > 30:
                            print("Hasta 30 caracttéres solo")
                            mail = str(input("Ingrese nombre y apellido (Máximo de 30 caractéres): "))
                        if len(nomYape) < 30:
                            con.mail = mail.ljust(30," ")
                        elif len(mail) == 30:
                            con.mail = mail
                        print("Los nuevos datos son:")
                        print(f"Nombre y Apellido: {con.nombreApellido}")
                        print(f"Teléfono: {con.telefono}")
                        print(f"Mail: {con.mail}")
                arLoCon.seek(pos,0)
                pickle.dump(con,arLoCon)
                arLoCon.flush()
        else:
            print("El contacto fue eliminado")
    else:
        print("El contacto no fue encontrado")

def eliminar_Contacto():
    global arFiCon
    global arLoCon
    con=contacto()
    nYa = str(input('Ingrese el nombre del usuario: '))
    pos = busquedaDico(nYa)
    if pos != -1:
        arLoCon.seek(pos,0)
        con = pickle.load(arLoCon)
        if con.baja == "N":
            con.baja = "S"
            arLoCon.seek(pos,0)
            pickle.dump(con,arLoCon)
            arLoCon.flush()
            print(f'El contacto {con.nombreApellido} fue eliminado')
        else:
            print('El contacto ya se encontraba eliminado')
    else:
        print("El contacto no se encuentra")

def mostrar_Todo():
    global arLoCon, arFiCon
    con = contacto()
    arLoCon.seek(0,0)
    while os.path.getsize(arFiCon) > arLoCon.tell():
        con = pickle.load(arLoCon)
        if con.baja == "N":
            nomYape = con.nombreApellido.rstrip()
            tel = con.telefono.rstrip()
            mail = con.mail.rstrip()
            print(f'\nUsuario N°: {con.codigo}')
            print(f"Nombre y Apellido: {nomYape}")
            print(f"Teléfono: {tel}")
            print(f"Mail: {mail}\n")

def buscar_moderadores(param, busqueda):
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

def reportes_estadisticos():
    global arFiMod, arFiRep
    global arLoRep, arLoMod
    rep = Reportes()
    mod = Moderador()
    arLoRep.seek(0,0)
    tamArch = os.path.getsize(arFiRep)
    rep = pickle.load(arLoRep)
    tamReg = arLoRep.tell()
    cant = tamArch//tamReg
    cont1 = 0
    cont2 = 0
    while arLoRep.tell() <= os.path.getssize(arFiRep):
        if rep.estado == 1:
            cont1 += 1
        elif rep.estado == 2:
            cont2 += 1
        rep = pickle.load(arLoRep)
    print(f'La cantidad de reportes hechos es: {cant}')
    print(f'El porcentaje de reportes ignorados es: {(cont2*100)/cant}')
    print(f'El porcentaje de reportes aceptados es: {(cont1*100)/cant}')
    mod_pos = buscar_moderadores("estado",True)
    arLoMod.seek(mod_pos,0)
    mod = pickle.load(arLoMod)


def case(opc):
    match opc:
        case 1:
            crear_Contacto()
        case 2:
            mostrar_Contacto()
        case 3:
            modificar_Contacto()
        case 4:
            eliminar_Contacto()
        case 5:
            mostrar_Todo()
        case 6:
            reportes_estadisticos()

def menu():
    opc = -1
    while opc != 0:
        mostrar_Menu()
        opc = int(input("Eliga una opción: "))
        while not (opc>=0 and opc<=6):
            opc = print(int(input("Eliga una opción: ")))
        case(opc)



# Aca empieza el programa principal
global arFiCon
global arLoCon

abrir_Archivos()
menu()
cerrar_Archivos()