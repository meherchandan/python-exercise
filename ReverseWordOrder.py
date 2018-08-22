def reversewordorder():
    inputstr = input("Please enter the string to reverse: ")
    inputlist = list(inputstr.split(" "))
    print(' '.join(reversed(inputlist)))


if(__name__ == "__main__"):
    reversewordorder()