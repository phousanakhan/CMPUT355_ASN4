import numpy as np
import instruction as instruction


boardWidth = 7 #col
boardHeight = 6 #row
quit = False

def get_open_row(board, col):
    for i in range(boardHeight):
        if board[i][col] == 0:
            return i

def board_strip_print(board):
    print("---------BOARD---------")
    for i in np.flip(board,0):
        i = str(i).lstrip('[').rstrip(']')
        print(" ", i)
    

def legal_move(board, col):
    #print(board[boardHeight-1][col])
    if (board[boardHeight-1][col] == 0):
        return True
    else:
        return False

def show_col_num():
    print("---------COLUMN---------")
    arr = np.zeros(7)
    starter_col = 0
    for k in range(len(arr)):
        arr[k] = starter_col
        starter_col += 1
    arr = str(arr).lstrip('[').rstrip(']')
    print(" ", arr, "\n")


def validate_input(input):
    pass1 = False
    if input == "quit":
        print("Quitting!")
        exit(0)
    if input == "man":
        instruction.show_manual()
        return False
    if input == "hist":
        instruction.history()
        return False
    if input == "strat":
        instruction.strat()
        return False
    try:
        input = int(input)
        pass1 = True
    except:
        print("\n")
        print("ERROR!  -->  input must be an integer from 0-7!\n")
        pass1 = False
        return False
    
    if pass1 == True:
        if int(input) < 0:
            print("\n")
            print("ERROR!  -->  input less than 0!\n")
            return False
        if int(input) > 6:
            print("\n")
            print("ERROR!  -->  input greater than 6!\n")
            return False
    return True

def check_for_win(board, player_numb):
    #4 (try and except)
    # if 1 of the (try and except) pass --> win
    for row in range(boardHeight):
        for col in range(boardWidth):
            try: #horizontal check
                count = 0
                for i in range(4):
                    if board[row][col+i] == player_numb:
                        count += 1
                    if count == 4:
                        print("Horizontal Win!")
                        return True  
            except:
                pass

            try: #vertical check
                count = 0
                for i in range(4):
                    if board[row+i][col] == player_numb:
                        count += 1
                    if count == 4:
                        print("Vertical Win!")
                        return True
            except:
                pass

            try: #right diagonal
                count = 0
                for i in range(4):
                    if board[row+i][col+i] == player_numb:
                        count += 1
                    if count == 4:
                        print("Diagonal Win!")
                        return True
            except:
                pass

            try: #left diagonal
                count = 0
                for i in range(4):
                    if board[row-i][col+i] == player_numb:
                        count += 1
                    if count == 4:
                        print("Diagonal Win!")
                        return True
            except:
                pass
    return False
