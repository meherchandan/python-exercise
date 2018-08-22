def devisior():
    n = int(input("Please enter the number to get the devisors: "))
    possibledivisors = list(range(2,(n//2)+1))
    divisors = list(filter(lambda x: n%x==0, possibledivisors))
    msg = None
    if(len(divisors)==0):
        msg = "{} is a prime number ".format(n)
    else:
        msg = "divisors are {}".format(divisors)
    print(msg)

if(__name__=="__main__"):
    devisior()