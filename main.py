import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple
from ticTacToeGame import TicTacToeGame
from ticTacToeBoard import TicTacToeBoard

def main():
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()
if __name__ == "__main__":
    main()
    
    
    