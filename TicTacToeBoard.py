def tictactoe_board(row,column):
    for x in range(0,row):
        print(" ---"*(row))
        print("|   "*(column+1))
    print(" ---"*(row))
    





if(__name__ == "__main__"):
    row = int(input("Please enter board row count: "))
    column = int(input("Please enter board column count: "))
    tictactoe_board(row,column)
