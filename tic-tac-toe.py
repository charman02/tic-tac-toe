'''
player_input
Purpose: Accepts Player 1 input for desired marker as string and returns it
'''
def player_input():
    # accept player input
    player_1 = input("Player 1: Do you want to be X or O? ")
    # if input is invalid, continue to prompt player for valid input
    while player_1 != "X" and player_1 != "O":
        player_1 = input("Sorry, I don't understand. Player 1: Do you want to "
                         "be X or O? ")
    return player_1


'''
display_game
Purpose: Given the board elements represented as a list, print 3 by 3 board
representation with list elements in appropriate positions
'''
def display_game(board):
    print('   |   |   ')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('   |   |   ')


'''
player_choice
Purpose: Accept input for player's choice for next position as a string, return
as int
'''
def player_choice():
    # Prompt user for next position
    choice = input("Choose your next position (1-9): ")
    # Validate input if necessary
    while not choice.isdigit() or int(choice) not in range(0,10):
        choice = input("Sorry, I don't understand. Choose your next position "
                       "(1-9): ")
    return int(choice)


'''
three_in_a_row
Purpose: Given list representation of board, returns True if there are three
X's or O's in a row, returns False otherwise
'''
def three_in_a_row(board):
    # Return false if there are three empty spaces in a row
    if board[0] == board[1] == board[2] == " " or\
    board[3] == board[4] == board[5] == " " or\
    board[6] == board[7] == board[8] == " " or\
    board[0] == board[3] == board[6] == " " or\
    board[1] == board[4] == board[7] == " " or\
    board[2] == board[5] == board[8] == " " or\
    board[0] == board[4] == board[8] == " " or\
    board[2] == board[4] == board[6] == " " :
        return False
    # Return true if there are three X's or O's in a row. Otherwise, return
    # false
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or\
    board[6] == board[7] == board[8] or\
    board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or\
    board[2] == board[5] == board[8] or\
    board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True
    else:
        return False
    

'''
ready_to_play
Purpose: Returns True if player is ready to play, otherwise returns False
'''
def ready_to_play():
    # Ask player if they are ready to play
    play_ready = input("Are you ready to play? Enter Yes or No: ")
    # Validate input if necessary
    while play_ready != "Yes" and play_ready != "No":
        play_ready = input("Sorry, I don't understand. Are you ready to play? "
                           "Enter Yes or No: ")
    # If yes, return True. If no, return False
    if play_ready == "Yes":
        return True
    else:
        return False
    

'''
play_again
Purpose: Returns "Yes" if users want to play again, otherwise returns "No"
'''
def play_again():
    replay = input("Would you like to play again? Enter Yes or No: ")\
        .capitalize()
    while replay != "Yes" and replay != "No":
        replay = input("Sorry, I don't understand. Would you like to play "
                       "again? Enter Yes or No: ")
    return replay


'''
update_board
Purpose: Given list representation of board and index, updates and returns
board list, uses given counter to determine if marker should be "X" or "O"
'''
def update_board(counter, index, board):
    if counter % 2 == 0:
        board[index - 1] = "X"
    else:
        board[index - 1] = "O"
    return board


# Run the program
if __name__ == '__main__':
    play = True
    while play:
        print("Welcome to Tic Tac Toe!")
        # Player 1 input
        p1 = player_input()
        # Player 2 input
        if p1 == "X":
            print("Player 1 will go first.")
            p2 = "O"
        else:
            print("Player 2 will go first.")
            p2 = "X"
        # Ask player if they are ready to play
        if ready_to_play():
            # Initialize counter and game board
            counter = 0
            board = [" "," "," "," "," "," "," "," "," "]
            # Run the game until there is a three-in-a-row
            while not three_in_a_row(board) and " " in board:
                print("\n"*100)
                display_game(board)
                index = player_choice()
                while board[index - 1] != " ":
                    print("Sorry, that position is taken.")              
                    index = player_choice()
                board = update_board(counter, index, board)
                counter += 1
            print("\n"*100)
            display_game(board)
            # If there is a three-in-a-row, print congratulation statement 
            if three_in_a_row(board):
                print("Congratulations! You have won the game!")
            # Otherwise, print notify player that they are out of moves
            else:
                print("It's a tie!")
            # Ask user if they would like to play again. If yes, the loop will continue. If no, the program will exit
            # the loop
            if play_again() == "Yes":
                print("\n"*100)
            else:
                play = False
        else:
            play = False