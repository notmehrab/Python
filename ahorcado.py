#elegir palabra
palabra_secreta = "manzana"

letras_correctas = []
letras_incorrectas = []
seguir_jugando = True

#pintar guion
while seguir_jugando:
    for letra in palabra_secreta:
        if letra in letras_correctas:
            print(letra, end =" ")
        else:
            print("_ ", end =" ") #end elimina el salto de linea

    #pedir letra
    letra_pedida = input("\n dime una letra: ")

#determinar la palabra

    if letra_pedida in palabra_secreta:
        letras_correctas.append(letra_pedida)
    else:
        letras_incorrectas.append(letra_pedida)

    print ("incorrectas: ", letras_incorrectas)

    #ganar el juego
    if set(letras_correctas) == set(palabra_secreta):
        seguir_jugando = False
        print("Has ganado!")
    if len(letras_incorrectas) == 6:
        seguir_jugando = False
        print("Has perdido!")
        print("la palabra era: ", palabra_secreta)
