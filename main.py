
#https://www.w3schools.com/python/python_user_input.asp
#https://www.geeksforgeeks.org/python/how-to-replace-values-in-a-list-in-python/
#https://www.geeksforgeeks.org/python/input-validation-in-python/
#https://stackoverflow.com/questions/57420792/check-if-value-exists-in-specific-column-of-2d-list-list-of-lists



#game_board
board = []

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

#Players
player_1 = 'X'
player_2 = 'O'


#keep track of player positions
player_positions = {
    'X': [],
    'O': []
}

#DEFAULT BOARD TO 3
user_row_col = 3
#Create max count for the board
max_count = user_row_col * user_row_col


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
    player_locations[player].append(player_input)


def update_board(player_input:int, game_board:list, player:str):
    """Compares input to board and updates if conditions match"""
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == player_input:
                game_board[i][j] = player

                #update player position
                update_positions(player_positions,player,player_input)
    #print(player_positions)


def check_position(player_num:int,positions:dict):
    """Checks if the position the player inputs is free """

    #New strategy take the input of that user and compare entered location to the dict of stored
    #CONTAINS in python
    valid = True

    if player_num in positions.get(player_1,[]):
        valid = False
        print(player_num, 'is in dict')

    elif player_num in positions.get(player_2,[]):
        valid = False
        print(player_num,'is in dict')

    return valid


def show_board(game_board:list):
    """show game board"""
    for row in game_board:
        print(*row,"\n_____")


#While user input != int ask for a number (int)
def initial_game_start(number_flag):

    while number_flag:

        try:
            user_no_input = input("Welcome, Please enter a number > than 0:")
            number_flag = False
        except Exception as e:
            print("Please enter a whole number etc 1,2,3", e)

        print("FUNCTION NOT IMPLEMENTED YET DEFAULTING TO 3")

        #CREATE BOARD
        print("CREATING BOARD....")
        create_board(user_row_col)

        show_board(board)

def game_loop(player:str):

    try:
        player_input = int(input(f"~~~~~~\nHello you are {player} please choose a number: "))

        if player_input <= max_count:

            valid_placement = check_position(player_input,player_positions)
            print("placement is",valid_placement)

            if valid_placement:
                update_board(player_input,board,player)
                show_board(board)
            else:
                print("Placement invalid")
        else:
            print(f"Please enter a value less than {max_count}")
    except Exception as e:
        raise
    #  has_won = True

if __name__ == "__main__":
    has_won = False
    number_flag = True


    initial_game_start(number_flag)

    while not has_won:
        game_loop(player_1)
        #check win
        game_loop(player_2)
        #check win
