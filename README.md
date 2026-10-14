### Task: Create a Terminal-Based Tic-Tac-Toe Game in Python

#### Objective:
Develop a simple Tic-Tac-Toe game that can be played in the terminal by two players. This exercise will help you practice basic Python concepts such as loops, conditionals, functions, and lists.

#### Requirements:

1. **Game Board**:
   - Create a 3x3 grid that represents the Tic-Tac-Toe board.
   - Each cell of the grid should be represented by a number (1-9) corresponding to its position.

2. **Players**:
   - There should be two players, one using 'X' and the other 'O'.
   - Players should take turns to place their symbol (X or O) in an empty cell.

3. **Input**:
   - Players should be prompted to input a number between 1 and 9 to place their symbol in the corresponding cell.
   - Validate the input to ensure that the chosen cell is not already occupied and that the input is within the valid range.

4. **Game Flow**:
   - Display the current state of the board after each move.
   - Check for a win or a draw after each move:
     - A player wins if they have three of their symbols in a row, column, or diagonal.
     - The game ends in a draw if all cells are filled and no player has won.

5. **Winning the Game**:
   - If a player wins, display a congratulatory message and end the game.
   - If the game ends in a draw, display a message indicating the draw.

6. **Restart Option**:
   - After the game ends, ask the players if they want to play again.
   - If they choose to play again, reset the board and start a new game.

#### Example Output:
```
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 

Player 1, enter a number (1-9): 5

 X | 2 | 3 
-----------
 4 | X | 6 
-----------
 7 | 8 | 9 

Player 2, enter a number (1-9): 1

 O | 2 | 3 
-----------
 4 | X | 6 
-----------
 7 | 8 | 9 

... (continue game) ...

Player 1 wins!
```

#### Hints:
- Use a list of length 9 to represent the board.
- Use a loop to keep the game running until there’s a win or a draw.
- Define functions for each major part of the game (e.g., displaying the board, checking for a win, etc.).
- Consider edge cases, such as invalid input or trying to place a symbol in an occupied cell.

#### Bonus:
- Implement an AI opponent that players can compete against.
- Allow players to choose their symbols.

#### Submission:
Submit your Python code in a `.py` file and include comments explaining your logic.