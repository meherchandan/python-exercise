def febonacci():
    count = int(input("Please enter the number how many fibonacci number you want: "))
    previous = 0
    current = 1
    print(previous)
    print(current)
    for i in range(2,count):
        temp = current + previous
        previous = current
        current = temp
        print(temp)

if(__name__ == "__main__"):
    febonacci()

        
