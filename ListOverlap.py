def listoverlap():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    result = set(item for item in a if item in b )
    print(result)


if(__name__=="__main__"):
    listoverlap()