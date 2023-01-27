#While
import random

number1 = random.randint(1,100 ) #el programador elige un número aleatorio
number2= None #Esto para evitar que en lína 7 no de un Error porque el número 2 aún no está definido y el jugador lo tiene que introducir

while number1 != number2: #si el número 1 no es igual número 2
    number2= int(input("Give me a number: ")) #pide poner el número 
    if number2 > number1:
        print("Your number is greater than the NUMBER")
    elif number2<number1:
        print("Your number is less than the NUMBER")
print("Good Job!")
