name = "?"

def main():
    global name
    global playagain

    playagain = True


    print("Welcome to rock paper scissors!")


    name = input(str("What is your name?"))

    while playagain == True:
        p1x = userInput()
        p2y = compNum()
        checkWin(p1x, p2y)
        playAgain()

def userInput():

    useranswer = int(input("Type 1 to choose rock, 2 to choose paper, or 3 to choose scissors."))

    return useranswer

def compNum():

    from random import randint

    companswer = int(randint(1,3))

    return companswer

def checkWin(a, b):

    if a == 1:
        print("You chose rock!")

    if a == 2:
        print("You chose paper!")

    if a == 3:
        print("You chose scissors!")


    if b == 1:
        print("The computer chose rock!")

    if b == 2:
        print("The computer chose paper!")

    if b == 3:
        print("The computer chose scissors!")



    if a == b:
        print("There was a tie!")

    if a == 1 and b == 2:
        print("The computer wins!")

    if a == 1 and b == 3:
        print("You win " + name + "!")

    if a == 2 and b == 1:
        print("You win " + name + "!")

    if a == 2 and b == 3:
        print("The computer wins!")

    if a == 3 and b == 1:
        print("The computer wins!")

    if a == 3 and b == 2:
        print("You win " + name + "!")


def playAgain():

    global playagain
    reset = int(input("Would you like to play again? Type 1 for yes or 2 for no."))

    if reset == 1:
        playagain = True
    else:
        playagain = False

main()