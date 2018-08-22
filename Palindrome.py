def palindrome():
    data = input("Please enter the string to check palindrome: ")
    reverse = ''.join(reversed(data))
    msg = ''
    if(data == reverse):
        msg = "String {} is a palindrome".format(data)
    else:
        msg = "String {} is not a palindrome".format(data) 
    print(msg)

if(__name__ == '__main__'):
    palindrome()