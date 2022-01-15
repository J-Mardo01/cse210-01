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


            
