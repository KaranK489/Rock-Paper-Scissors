name = "?"

keepvalues = 2

wins = 0

p1score = 0
p2score = 0

p1wins = 0
p2wins = 0

def main():
    from random import randint
    global name
    global playagain
    global players
    global name2
    global whogoesfirst
    global wins
    global p1score
    global p2score
    global keepvalues


    playagain = True

    print("Welcome to rock paper scissors!")
    print(" ")
    print("Type 1 for a one player game.")
    players = int(input("Type 2 for a two player game."))
    print(" ")

    wins = int(input("What score would you like to play to?"))
    print(" ")

    if players == 1:
        name = input(str("What is your name?"))

    if players == 2:
        name = input(str("What is your name Player 1?"))
        name2 = input(str("What is your name Player 2?"))
        print(" ")

    while playagain == True:
        if players == 1:
            while playagain == True:
                p1x = userInput()
                p2y = compNum()
                checkWin(p1x, p2y)

        if players == 2:
            whogoesfirst = randint(1, 2)
            if whogoesfirst == 1:
                print(name + " gets to go first!")
            else:
                print(name2 + " gets to go first!")

            while playagain:

                if whogoesfirst == 1:
                    p1x = userInput()
                    p2y = userInput2()
                    checkWin(p1x, p2y)

                else:
                    p2y = userInput2()
                    p1x = userInput()
                    checkWin(p1x, p2y)

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
    global p1score
    global p2score
    global p1wins
    global p2wins
    global keepvalues

    print(" ")

    if keepvalues == 2:
        p1score = 0
        p2score = 0
        keepvalues = 1

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
        print("There was a tie, so no points for anyone!")

    if a == 1 and b == 2:
        if players == 1:
            print("The computer wins the round!")
        else:
            print(name2 + " wins the round!")
        p2score += 1

    if a == 1 and b == 3:
        if players == 1:
            print("You win the round " + name + "!")
        else:
            print(name + " wins the round!")
        p1score += 1

    if a == 2 and b == 1:
        if players == 1:
            print("You win the round " + name + "!")
        else:
            print(name + " wins the round!")
        p1score += 1

    if a == 2 and b == 3:
        if players == 1:
            print("The computer wins the round!")
        else:
            print(name2 + " wins the round!")
        p2score += 1

    if a == 3 and b == 1:
        if players == 1:
            print("The computer wins the round!")
        else:
            print(name2 + " wins the round!")
        p2score += 1

    if a == 3 and b == 2:
        if players == 1:
            print("You win the round " + name + "!")
        else:
            print(name + " wins the round!")
        p1score += 1

    print(" ")
    if players == 1:
        print(name + ", you have a score of " + str(p1score))
        print("The computer has a score of " + str(p2score))
    else:
        print(name + ", you have a score of " + str(p1score))
        print(name2 + ", you have a score of " + str(p2score))

    if int(p1score) == int(wins) or int(p2score) == int(wins):
        print(" ")

        if players == 1:
            if p1score == wins:
                print(name + ", you won the game with  " + str(wins) + " wins!")
                p1wins += 1
            if p2score == wins:
                print("The computer won the game with " + str(wins) + " wins!")
                p2wins += 1

            print(" ")
            print(name + ", your total number of games won is now " + str(p1wins) + ".")
            print("The computer's total number of games won is now " + str(p2wins) + ".")

        if players == 2:
            if p1score == wins:
                print(name + ", you won the game with  " + str(wins) + " wins!")
                p1wins += 1
            if p2score == wins:
                print(name2 + ", you won the game with  " + str(wins) + " wins!")
                p2wins += 1

            print(" ")
            print(name + ", your total number of games won is now " + str(p1wins) + ".")
            print(name2 + ", your total number of games won is now " + str(p2wins) + ".")

        p1score = 0
        p2score = 0
        playAgain()


def playAgain():
    global playagain
    global p1wins
    global p2wins

    print(" ")
    print("Type 1 to play again.")
    reset = int(input("Type 2 to quit."))

    if reset == 1:
        playagain = True
        print(" ")
        print("Type 1 to continue the game.")
        keepvalues = int(input("Type 2 to restart the game."))
        print(" ")

        if keepvalues == 2:
            p1wins = 0
            p2wins = 0
            main()

    else:
        print(" ")
        print("Thank you for playing!")
        playagain = False


main()
