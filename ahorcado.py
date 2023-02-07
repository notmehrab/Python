#elegir palabra

palabra_secreta = "aprobar"

letras_correctas = []
letras_incorrectas = []

#pintar guion
while True:
    for letra in palabra_secreta:
        if letra in letras_correctas:
            print(letra, end =" ")
        else:
            print("_ ", end =" ") #end elimina el salto de linea

    #pedir letra
    letra_pedida = input("\n dime una letra: ")

    if letra_pedida in palabra_secreta:
        letras_correctas.append(letra_pedida)
    else:
        letras_incorrectas.append(letra_pedida)

    print ("corrctas: ", letras_correctas)
    print ("incorrectas: ", letras_incorrectas)

