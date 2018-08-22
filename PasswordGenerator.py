import random
import string
def passwordgenerator():
    print("Available password Complexities \n1. Easy \n2. Medium \n3. Complex")
    complexity = int(input("Please enter your choice(1,2 or 3): "))
    size =0
    if(complexity==1):
        size = 5
    elif(complexity==2):
        size = 8
    else:
        size = 15
    password = ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(size))
    print("PASSWORD IS:",password)


if(__name__ == "__main__"):
    passwordgenerator()