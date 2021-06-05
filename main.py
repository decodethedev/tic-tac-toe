from board import Board
import os
import time
import random
from random import randint
if __name__ == '__main__':
    while True:

        print("Welcome to simple tictactoe made by Decode!")
        print("#"*20)
        print("#"+"[ 'q' ] to quit   #")
        print("#"+"[ 'p' ] to play   #")
        print("#"*20)
        inp = input(">")
        if(inp == "q"):
            break
        elif(inp == "p"):
            pass
        else:
            continue
        new_board = Board()
        current_player = "X"
        random_number = randint(0, 1)
        if(random_number == 1):
            current_player = "X"
        else:
            current_player = "O"
        while True:

            if(new_board.checkWin() != None):
                print(new_board.checkWin() + "\nRestarting...")
                time.sleep(3)
                clear = os.system('cls')
                break
            if(new_board.checkTie() == "Tie!"):
                print(new_board.checkTie() + "\nRestarting...")
                time.sleep(3)
                clear = os.system('cls')
                break
            new_board.print_Board()
            print(f"{current_player}'s turn!")
            while True:
                try:
                    inp = int(
                        input(f"Please give us where to put the {current_player}, from 0-8 \n->"))
                    if(inp == "q"): break
                    break
                except Exception as E:
                    continue
            put = new_board.putInSlot(inp, current_player)
            if(put != 200):
                clear = os.system('cls')
                print(put)
                continue
            if(current_player == "X"):
                current_player = "O"
            else:
                current_player = "X"

            clear = os.system('cls')
