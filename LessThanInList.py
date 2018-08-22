def lessthaninlist():
    inputList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    numberchecker = int(input("Please enter the number to get the less than list: "))
    lessthannumber = list(filter(lambda x: x<numberchecker,inputList ))
    print(lessthannumber)

if(__name__=="__main__"):
    lessthaninlist()