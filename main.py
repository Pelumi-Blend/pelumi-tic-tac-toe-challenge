
import numpy as np
#https://www.w3schools.com/python/python_user_input.asp
#game_board
board = []

#Winning Combinations


#Flag to keep track of if user has inputed an INT or not
number_flag= True

user_row_col = 0


def create_board(row_col:int = 3):
    #create count variable to keep track of number to append
    count = 1
    """dynamically creates a board based on user input
        Args:
        row_cow(int): Size of row and column
    """
    for i in range(1,row_col+1):
        row = []
        for j in range(row_col):
            row.append(count)
            count += 1
        board.append(row)

    #print(board)

def show_board(game_board:list):
    for row in game_board:
        print(*row,"\n_____")




#While user input != int ask for a number (int)
while number_flag:
    user_row_input = input("Welcome, Please enter a number > than 0:")
    try:
        user_row_input = int(user_row_input)
        number_flag = False
    except:
        print("Please enter a whole number etc 1,2,3" )

    print("FUNCTION NOT IMPLEMENTED YET DEFAULTING TO 3")
    user_row_col = 3





create_board(user_row_col)
show_board(board)




#x input needed
#y input needed


