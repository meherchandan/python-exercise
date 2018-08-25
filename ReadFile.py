def readfile():
    open_file = open('Training_01.txt','r')
    categories_count={}
    for line in open_file:
        category = line.split("/")[2] 
        if(category in categories_count):
            categories_count[category] += 1
        else:
            categories_count[category] = 1
    print(categories_count)



if(__name__ == "__main__"):
    readfile()