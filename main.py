#!/usr/bin/python


from Tkinter      import *
from game_of_life import GameOfLife



master 			= Tk()
canvas 		= Canvas(master, width=1000, height=1000)
canvas.pack()
num_rows	= 100
num_cols	= 100
width			= 10
game			= GameOfLife(canvas, num_rows, num_cols, width, None)


mainloop()







