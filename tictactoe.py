def main():
    print('Welcome to Tic Tac Toe!')
    i = 1
    players = player_input()
    board = ['#'] * 10
   
    while True:
        game_on = full_board_check(board)
        
        while not game_on:
            position = player_choice(board)

            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]

            place_marker(board, marker, int(position))

            display_board(board)

            i += 1
            if win_check(board, marker):
                print('You won!')
                break
            game_on = full_board_check(board)
        if not replay():
            break
        else:
            i = 1
            players = player_input()
            board = ['#'] * 10


def display_board(board):
    blankboard="""
___________________
|     |     |     |
|  1  |  2  |  3  |            
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
"""
    for i in range(1,10):
        if (board[i] == '0' or board[i] == 'X'):
            blankboard = blankboard.replace(str(i), board[i])
        else:
            blankboard = blankboard.replace(str(i), ' ')
    print(blankboard)

def player_input():
    player1 = input("Please pick a marker: 'X' or 'O' ")
    while True:
        if player1.upper() == 'X':
            player2='O'
            print("You've chosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(),player2
        elif player1.upper() == 'O':
            player2='X'
            print("You've chosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(),player2
        else:
            player1 = input("Please pick a marker: 'X' or 'O' ")

def place_marker(board, marker, position):
    board[position] = marker
    return board

def space_check(board, position):
    return board[position] == '#'

def full_board_check(board):
    return len([x for x in board if x =='#']) == 1

def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
    else:
        return False

def player_choice(board):
    choice = input("Please select an empty space between 1 and 9 : ")
    while not space_check(board, int(choice)):
        choice = input("This space isn't valid. Please choose a space between 1 and 9 : ")
    return choice

def replay():
    playagain = input("Do you want to play again (Yes or no)? ")
    if playagain.lower() == "yes":
        return True
    if playagain.lower() == "no":
        return False


main()
            