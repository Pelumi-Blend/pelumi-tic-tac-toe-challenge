
import numpy as np
#https://www.w3schools.com/python/python_user_input.asp
#https://www.geeksforgeeks.org/python/how-to-replace-values-in-a-list-in-python/
#https://www.geeksforgeeks.org/python/input-validation-in-python/

#players
player_1 = 'X'
player_2 = 'O'
#game_board
board = []
#
#Winning Combinations only for 3
winning_combinations = (
    #across
    [1,2,3],
    [4,5,6],
    [7,8,9],
    #downwards
    [1,4,7],
    [2,5,8],
    [3,6,9],
    #Diagonal
    [1,5,9],
    [3,5,7]
)

#keep track of player positions
player_positions = {
    'X': [],
    'O': []
}

#FLAGS
number_flag = True
has_won = False

user_row_col = 0


def create_board(row_col:int):
    """Creates board based on user input"""
    count = 1

    for i in range(1,row_col+1):
        row = []
        for j in range(row_col):
            row.append(count)
            count += 1
        board.append(row)

    #print(board)

def update_positions(player_locations:dict,player:str, player_input:int):
    """updates player position tracker in player_position"""
    player_locations.update({player:player_input})




def update_board(player_input:int, game_board:list, player:str):
    """Compares input to board and updates if conditions match"""
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == player_input:
                game_board[i][j] = player

                #update player position
                update_positions(player_positions,player,player_input)
    #print(player_positions)


def check_position(game_board:list,player:str):
    """Checks if the position the player inputs is free """
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == player_1:
                print(f'{player} is unable to fit as spot taken by {player_1}')
            elif game_board[i][i] == player_2:
                print(f'{player} is unable to fit as Spot taken by {player_2}')


def show_board(game_board:list):
    """show game board"""
    for row in game_board:
        print(*row,"\n_____")


#While user input != int ask for a number (int)
while number_flag:
    user_no_input = input("Welcome, Please enter a number > than 0:")
    try:
        user_no_input = int(user_no_input)
        number_flag = False
    except:
        print("Please enter a whole number etc 1,2,3" )

    print("FUNCTION NOT IMPLEMENTED YET DEFAULTING TO 3")

    #DEFAULT BOARD TO 3
    user_row_col = 3

    #CREATE BOARD
    print("CREATING BOARD....")
    create_board(user_row_col)

    show_board(board)

max_count = user_row_col * user_row_col

while not has_won:
    player_1_input = 0
    player_2_input = 0

    while True:
        try:
            player_1_input = int(input("~~~~~~\nHello player 1 you are X please choose a number: "))

            if player_1_input <= max_count:
                update_board(player_1_input,board,player_1)
                show_board(board)
                break
            else:
                print(f"Please enter a value less than {max_count}")
        except:
            print("Please enter a number")


    while True:
        try:
            player_2_input = int(input("~~~~~~\nHello player 2 you are O please choose a number: "))

            if player_2_input <= max_count:
                update_board(player_2_input,board,player_2)
                show_board(board)
                break
            else:
                print(f"Please enter a value less than {max_count}")
            break
        except:
            print("Please enter a number")




    # has_won = True



