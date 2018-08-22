import random
def rockpaperscissor():
    gameinput = { 1: 'rock', 2: 'paper', 3: 'scissor'}
    gamecontinue = True
    while(gamecontinue):
        print("1. Rock \n2. Paper\n3. Scissor")
        selection = int(input("Select Your Choice: "))
        if(selection in [1,2,3]):
            selection = gameinput[selection]
        else:
            print("Incorrect choice!! Please try Again..")
            rockpaperscissor()
            exit()
        systemchoice = gameinput[random.randint(1,3)]
        print("System selection: ",systemchoice)
        if((selection == "rock" and systemchoice == "scissor") or (selection == "scissor" and systemchoice == "paper") or (selection == "paper" and systemchoice == "rock") ):
            msg = "{} bets {}".format(selection.title(),systemchoice.title())
            print("You Won !!",msg)
        else:
            msg = "{} bets {}".format(systemchoice.title(),selection.title())
            print("You Lose !!",msg)
        gamestatus = input("Come On. Let's Play Again!!..(y/n): ")
        if(not gamestatus.lower() == "y"):
            gamecontinue = False
        

if(__name__ == "__main__"):
    rockpaperscissor()
    




