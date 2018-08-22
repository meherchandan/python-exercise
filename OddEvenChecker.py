import math

def evenoddchecker():
    n = int(input("Please enter the number:"))
    msg ="Given number {} is ".format(str(n))
    if(n%4==0):
        msg += "even number and also divisble by 4"
    elif(n%2==0):
        msg += "even number"
    else:
        msg += "odd number"
    print(msg)
    msg ="Given number {} is divisble by ".format(n)
    divider = input("Please enter the number to divide by:")
    if(n%int(divider)==0):
        msg = "Given number {} is divisble by {}".format(n, str(divider)) 
    else:
        msg = "Given number {} is not divisble by {}".format(n, str(divider)) 
    print(msg)

if(__name__=="__main__"):
    evenoddchecker()

