import random
def cowandbulls():
    correctNumber = list(str(random.randint(1000,9999)))
    print("correct number is ",correctNumber)
    count = 0
    gamecheck = True
    while(gamecheck):
        userNumber = list(input("Please enter your guess of 4 digit number: "))
        cows = 0
        bulls = 0
        count += 1
        if(userNumber == correctNumber):
            gamecheck = False
            msg = "You guessed the correct number in {} attempts".format(count)
        else:
            for i in range(0,len(correctNumber)):
                if( userNumber[i] == correctNumber[i]):
                    cows += 1
                elif(userNumber[i] in correctNumber):
                    bulls += 1
            msg = "your choice has {} cows and {} bulls".format(cows,bulls)
        print(msg)

if(__name__ == "__main__"):
    cowandbulls()