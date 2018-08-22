import datetime

def evenitemfilter():
    data = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    result = list(filter(lambda x : x%2==0, data))
    print("even filtered list is: ",result)

def currentage():
    years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
    age = list(map(lambda x: datetime.datetime.now().year - x,years_of_birth))
    print("current age is" ,age)

if(__name__ == "__main__"):
    evenitemfilter()
    currentage()
