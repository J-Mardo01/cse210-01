def main():
    print('Welcome to Tic Tac Toe!')
    i = 1
    players = player_input()
    board = ['#'] * 10
   
    while True:
        game_on = full_board_check(b)
        
        while not game_on:
            position = player_choice()

            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]

            place_marker()

            display_board()

            i += 1
            if win_check():
                print('You won!')
                break
            game_on = full_board_check()
        if not replay():
            break
        else:
            i = 1
            players = player_input()
            board = ['#'] * 10


def display_board(board):
    blankboard="""
____________________
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
            print("You've chosen" + player1 + ". Player 2 will be " + player2)
            return player1.upper(),player2
        elif player1.upper() == 'O':
            player2='X'
            print("You've chosen" + player1 + ". Player 2 will be " + player2)
            return player1.upper(),player2
        else:
            player1 = input("Please pick a marker: 'X' or 'O' ")


            