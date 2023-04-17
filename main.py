import tkinter as tk
from itertools import cycle
from tkinter import font
from typing import NamedTuple
from ticTacToeGame import TicTacToeGame
from ticTacToeBoard import TicTacToeBoard


    
    
if __name__ == "__main__":
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()
    print("XO Game is running")
    
    
    
    