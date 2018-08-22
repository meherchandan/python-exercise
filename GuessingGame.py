import random
def guessinggame():
    guessnumber = random.randint(1,9)
    gamechecker = True
    count = 0
    while(gamechecker):
        userinput = int(input("Guess the number between 1 and 9:"))
        if(userinput>9):
            print("Nooo. You have yo choose number between 1 and 9")
            continue
        if(userinput == guessnumber):
            count +=1
            msg = "Congratulations!! you guess the correct number in {} attempts".format(count)
            print(msg)
            exit()
        elif( abs(guessnumber-userinput)<3):
            count += 1
            print("Wow !! You'r closer")
        else:
            count +=1
            print("Sorry, your guess is too far")


if(__name__ == "__main__"):
    guessinggame()