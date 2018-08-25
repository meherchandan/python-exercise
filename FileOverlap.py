def fileoverlap():
    prime_numbers = open("PrimeNumbers.txt", "r")
    happy_numbers = open("HappyNumbers.txt", "r")
    prime_numbers_list = [int(x) for x in prime_numbers]
    happy_numbers_list = [int(x) for x in happy_numbers]
    for i in  range(0,len(happy_numbers_list)):
        if(prime_numbers_list[i] in happy_numbers_list):
            print(happy_numbers_list[i])

if(__name__ == "__main__"):
    fileoverlap()