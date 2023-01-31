#Elegir opciones
user = input("elige X o O: ").upper()

#Crear la tabla
#casillas =[0,   1,  2, 3,  4,  5,   6, 7,  8]
table = ["", "", "", "", "", "", "", "", "",]

print(
"| "+table[0]+"| "+table[1]+"| "+table[2]+"|\n"
"| "+table[3]+"| "+table[4]+"| "+table[5]+"|\n"
"| "+table[6]+"| "+table[7]+"| "+table[8]+"|\n"
)

#Pedir Casilla
position =int(input("elige una posición entre 0 a 8: "))



#Guardar valor
#Comprobar el ganador
#Compronbar que no ha termindo los turnos