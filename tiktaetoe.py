import random

#Choose option

user_option = input("elige X o O: ").capitalize()  #user decision

if user_option == "X":
    pc_option = "O"   #pc decision
elif user_option == "O":
    pc_option = "X"  #pc decision

#Crear la tabla

table = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]
lista =[0,1,2,3,4,5,6,7,8]

game = True


#Reglas


while game:
#Pedir Casilla al usuario

    userp = int(input("elige una posición entre 0 a 8: "))

#user 

    if table[userp] == " " :
        table[userp] = user_option
        lista.remove(userp)
        turn + 1
    else:
        print("¡La casilla está seleccionada. Por favor, elige otra!")
        userp = int(input("elige una posición entre 0 a 8: "))

#Display decision
    print(
    "| "+table[0]+"| "+table[1]+"| "+table[2]+"|\n"
    "| "+table[3]+"| "+table[4]+"| "+table[5]+"|\n"
    "| "+table[6]+"| "+table[7]+"| "+table[8]+"|\n"
    )

#User rules

    if table[0] == table[1] == table[2] == user_option:
        print("has ganado")
        break
    if table[3] == table[4] == table[5] == user_option:
        print("has ganado")
        break
    if table[6] == table[7] == table[8] == user_option:
        print("has ganado")
        break

    if table[0] == table[3] == table[6] == user_option:
        print("has ganado")
        break
    if table[1] == table[4] == table[7] == user_option:
        print("has ganado")
        break
    if table[2] == table[5] == table[8] == user_option:
        print("has ganado")
        break
    
    if table[0] == table[4] == table[8] == user_option:
        print("has ganado")
        break



#bot

    pcp = random.choice(lista)
    table[pcp] = pc_option
    lista.remove(pcp)


#display decision
    print(
    "| "+table[0]+"| "+table[1]+"| "+table[2]+"|\n"
    "| "+table[3]+"| "+table[4]+"| "+table[5]+"|\n"
    "| "+table[6]+"| "+table[7]+"| "+table[8]+"|\n"
    )

#bot rules
    if table[0] == table[1] == table[2] == pc_option:
        print("Has perdido")
        break
    if table[3] == table[4] == table[5] == pc_option:
        print("Has perdido")
        break
    if table[6] == table[7] == table[8] == pc_option:
        print("Has perdido")
        break

    if table[0] == table[3] == table[6] == pc_option:
        print("Has perdido")
        break
    if table[1] == table[4] == table[7] == pc_option:
        print("Has perdido")
        break
    if table[2] == table[5] == table[8] == pc_option:
        print("Has perdido")
        break
    
    if table[0] == table[4] == table[8] == pc_option:
        print("Has perdido")
        break
    
    print("Turn left: ", turn)

    