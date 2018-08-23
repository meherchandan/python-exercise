def binarysearch(ordered_list, number_to_find,start=0):
    mid = len(ordered_list)//2
    if(len(ordered_list) == 0):
        print("Number not found in the list")
        return
    if(number_to_find == ordered_list[mid]):
        print("Number found on the index: ",mid + start)
        return
    elif(number_to_find < ordered_list[mid]):
        return binarysearch(ordered_list[:mid], number_to_find,start)
    elif(number_to_find >= ordered_list[mid]):
        return binarysearch(ordered_list[mid + 1:], number_to_find,start + mid + 1)

if(__name__ == "__main__"):
    ordered_list  = input("Please enter the ordered list(comma seperated): ")
    ordered_list = [int(x) for x in ordered_list.split(',')]
    number_to_find = int(input("Please enter the number to find: "))
    binarysearch(ordered_list, number_to_find)