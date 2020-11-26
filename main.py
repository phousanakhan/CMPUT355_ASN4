import numpy as np
import connect4 as c4 
import os



boardWidth = 7 #col
boardHeight = 6 #row
quit = False

def main():
    print("Welcome to the Connect4 game!\n")
    print("Type 'quit' if you want to quit\n")
    print("Type 'man' if you want to see the manual\n")
    print("Type 'hist' if you want to see the a brief history of the game\n")
    print("Type 'strat' for strategy\n")
    os.system("afplay -v 0.5 beat.mp3&")

    board = np.zeros((boardHeight,boardWidth))
    player_turn = 1
    c4.board_strip_print(board)
    c4.show_col_num()
    
    while not quit:
        #--player 1
        if player_turn == 1:
            player_one(board, player_turn)
        else: #player2 
            player_two(board, player_turn)

        c4.board_strip_print(board)
        c4.show_col_num()
        player_turn += 1
        player_turn = player_turn % 2  #so that turn switch


def player_one(board, player_turn):
    usr_input_col = input("Player 1: Enter a column number between 0-6: ")
    while c4.validate_input(usr_input_col) == False:
        c4.board_strip_print(board)
        c4.show_col_num()
        usr_input_col = input("Player 1: Enter a column number between 0-6: ")
        
    usr_input_col = int(usr_input_col)
    if c4.legal_move(board, usr_input_col) == True:
        row = c4.get_open_row(board, usr_input_col)
        board[row][usr_input_col] = 1 #dropping the piece
        if c4.check_for_win(board, 1) == True:
            c4.board_strip_print(board)
            c4.show_col_num()
            print("Player 1 Win!")
            print("Player 2 Lose!")
            again = input("Do you want to play again y/n ? ")
            if again == "y" or again == "Y":
                main()
            else:
                print("Quitting!")
                exit(0)
    else:
        print("ILLEGAL MOVE!!")

def player_two(board, player_turn):
    usr_input_col = input("Player 2: Enter a column number between 0-6: ")
    while c4.validate_input(usr_input_col) == False:
        c4.board_strip_print(board)
        c4.show_col_num()
        usr_input_col = input("Player 2: Enter a column number between 0-6: ")

    usr_input_col = int(usr_input_col)
    if c4.legal_move(board, usr_input_col) == True:
        row = c4.get_open_row(board, usr_input_col)
        board[row][usr_input_col] = 2 #dropping the piece
        if c4.check_for_win(board, 2) == True:
            c4.board_strip_print(board)
            c4.show_col_num()
            print("Player 2 Win!")
            print("Player 1 Lose!\n")
            again = input("Do you want to play again y/n ? ")
            if again == "y" or again == "Y":
                main()
            else:
                print("Quitting!")
                exit(0)
    else:
        print("ILLEGAL MOVE!!")

if __name__ == '__main__':
    main()
