import random

#crear 3 variables
while True:
    r ="rock"
    p ="paper"
    s ="scissor"

    option = [r, p, s]

    #elección del ordenador y del usario

    pc = random.choice(option)
    user = input("rock, paper or scissor?: ").lower()

    #Rock
    if pc == r and user == r:
        print("Draw")
    elif pc == r and user == p:
        print("Win")
    elif pc == r and user == s:
        print("Loose")
    #paper
    if pc == p and user == p:
        print("Draw")
    elif pc == p and user == s:
        print("Win")
    elif pc == p and user == r:
        print("Loose")
    #Scissor
    if pc == s and user == s:
        print("Draw")
    elif pc == s and user == r:
        print("Win")
    elif pc == s and user == p:
        print("Loose")