name = "?"

keepvalues = 2

def main():
    from random import randint
    global name
    global playagain
    global players
    global name2
    global whogoesfirst

    playagain = True

    print("Welcome to rock paper scissors!")
    print(" ")
    print("Type 1 for a one player game.")
    players = int(input("Type 2 for a two player game."))
    print(" ")



    if players == 1:
        name = input(str("What is your name?"))
        while playagain:
            p1x = userInput()
            p2y = compNum()
            checkWin(p1x, p2y)
            playAgain()

    if players == 2:
        name = input(str("What is your name Player 1?"))
        name2 = input(str("What is your name Player 2?"))
        print(" ")
        whogoesfirst = randint(1,2)

        if whogoesfirst == 1:
            print(name + " gets to go first!")
        else:
            print(name2 + " gets to go first!")

        while playagain:
            if whogoesfirst == 1:
                p1x = userInput()
                p2y = userInput2()
                checkWin(p1x, p2y)
                playAgain()
            else:
                p2y = userInput2()
                p1x = userInput()
                checkWin(p1x, p2y)
                playAgain()


def userInput():
    print(" ")
    if players == 1:
        print("Type 1 to choose rock.")
        print("Type 2 to choose paper.")
        useranswer = int(input("Type 3 to choose scissors."))
    else:
        print(name + ",")
        print("Type 1 to choose rock.")
        print("Type 2 to choose paper.")
        useranswer = int(input("Type 3 to choose scissors."))

    return useranswer


def compNum():
    from random import randint

    companswer = int(randint(1, 3))

    return companswer


def userInput2():
    print(" ")
    if players == 1:
        print("Type 1 to choose rock.")
        print("Type 2 to choose paper.")
        useranswer2 = int(input("Type 3 to choose scissors."))
    else:
        print(name2 + ",")
        print("Type 1 to choose rock.")
        print("Type 2 to choose paper.")
        useranswer2 = int(input("Type 3 to choose scissors."))

    return useranswer2


def checkWin(a, b):

    print(" ")


    if a == 1:
        if players == 1:
            print("You chose rock!")
        else:
            print(name + " chose rock!")

    if a == 2:
        if players == 1:
            print("You chose paper!")
        else:
            print(name + " chose paper!")

    if a == 3:
        if players == 1:
            print("You chose scissors!")
        else:
            print(name + " chose scissors!")

    if b == 1:
        if players == 1:
            print("The computer chose rock!")
        else:
            print(name2 + " chose rock!")

    if b == 2:
        if players == 1:
            print("The computer chose paper!")
        else:
            print(name2 + " chose paper!")

    if b == 3:
        if players == 1:
            print("The computer chose scissors!")
        else:
            print(name2 + " chose scissors!")

    print(" ")

    if a == b:
        print("There was a tie!")

    if a == 1 and b == 2:
        if players == 1:
            print("The computer wins!")
        else:
            print(name2 + " wins!")

    if a == 1 and b == 3:
        if players == 1:
            print("You win " + name + "!")
        else:
            print(name + " wins!")

    if a == 2 and b == 1:
        if players == 1:
            print("You win " + name + "!")
        else:
            print(name + " wins!")

    if a == 2 and b == 3:
        if players == 1:
            print("The computer wins!")
        else:
            print(name2 + " wins!")

    if a == 3 and b == 1:
        if players == 1:
            print("The computer wins!")
        else:
            print(name2 + " wins!")

    if a == 3 and b == 2:
        if players == 1:
            print("You win " + name + "!")
        else:
            print(name + " wins!")


def playAgain():
    global playagain
    print(" ")
    print("Type 1 to play again.")
    reset = int(input("Type 2 to quit."))

    if reset == 1:
        playagain = True

    else:
        print(" ")
        print("Thank you for playing!")
        playagain = False


main()
