import random

#Elegir opciones
user = "X"
pc = "O"

while True:
    #Crear la tabla
    table = ["", "", "", "", "", "", "", "", "",]
    lista =[0,1,2,3,4,5,6,7,8,9]

    #Pedir Casilla al usuario
    position = int(input("elige uno: "))
    table[position] = "x"

    print(
    "| "+table[0]+"| "+table[1]+"| "+table[2]+"|\n"
    "| "+table[3]+"| "+table[4]+"| "+table[5]+"|\n"
    "| "+table[6]+"| "+table[7]+"| "+table[8]+"|\n"
    )

    if position == lista:
        remove.postion(lista)

    #Eleccion del ordenador
  
    pc_position = random.choice(lista)
    table[pc_position] = "O"

    print(
    "| "+table[0]+"| "+table[1]+"| "+table[2]+"|\n"
    "| "+table[3]+"| "+table[4]+"| "+table[5]+"|\n"
    "| "+table[6]+"| "+table[7]+"| "+table[8]+"|\n"
    )
    if pc_position == lista:
        remove.postion(lista)
