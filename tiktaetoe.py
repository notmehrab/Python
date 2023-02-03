import random


#Crear la tabla
table = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]
lista =[0,1,2,3,4,5,6,7,8]

while True:
    #Pedir Casilla al usuario
    userp = int(input("elige una posición entre 0 a 8: "))

    #user 
    if table[userp] == " " :
        table[userp] = "X"
        lista.remove(userp)
    
    if table[0] and table[1] and table[2] == "X":
        print("has ganado")
        break
    if table[3] and table[4] and table[5] == "X":
        print("has ganado")
        break
    if table[6] and table[7] and table[8] == "X":
        print("has ganado")
        break

    if table[0] and table[3] and table[6] == "X":
        print("has ganado")
        break
    if table[1] and table[4] and table[7] == "X":
        print("has ganado")
        break
    if table[2] and table[5] and table[8] == "X":
        print("has ganado")
        break
    
    if table[0] and table[4] and table[8] == "X":
        print("has ganado")
        break

    print(
    "| "+table[0]+"| "+table[1]+"| "+table[2]+"|\n"
    "| "+table[3]+"| "+table[4]+"| "+table[5]+"|\n"
    "| "+table[6]+"| "+table[7]+"| "+table[8]+"|\n"
    )

    #ordenador
    pcp = random.choice(lista)
    table[pcp] = "O"
    lista.remove(pcp)

    print(lista)

    print(
    "| "+table[0]+"| "+table[1]+"| "+table[2]+"|\n"
    "| "+table[3]+"| "+table[4]+"| "+table[5]+"|\n"
    "| "+table[6]+"| "+table[7]+"| "+table[8]+"|\n"
    )