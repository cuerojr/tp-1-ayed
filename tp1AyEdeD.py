user1 = {
    "name": "usuario_1",
    "password": "111111"
}
user2 = {
    "name": "usuario_2",
    "password": "222222"
}
user3 = {
    "name": "usuario_3",
    "password": "333333"
}

def ingresos():
    count = 0
    for count in range(3):
        userName = input("Enter nombre de usuario: ")
        password = input("Enter contraseña: ")
        if (userName == user1["name"] and password == user1["password"]) or (userName == user2["name"] and password == user2["password"]) or (userName == user3["name"] and password == user3["password"]):
            print(userName, " bienvenido")            
        else:
            count += 1
            
    print("Usuario o contraseña incorrectos")

ingresos()