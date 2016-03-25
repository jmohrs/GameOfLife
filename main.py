#!/usr/bin/python


from Tkinter      import *
from game_of_life import GameOfLife
import time


def _clicked_(event):
     global width
     global game
     global master
     canvas  = event.widget
     x       = canvas.canvasx(event.x)
     y       = canvas.canvasy(event.y)
     cell    = canvas.find_closest(x,y)
     coord   = canvas.coords(cell)
     coloumn = int(coord[0] / 10)
     row     = int(coord[3] / 10) - 1
     game._adjust_start_configuration_((coloumn,row))
     master.update()

#-------- Enter Main Loop ---------#
def _on_start():
     try:
          while True:
               time.sleep(0.1)
               game._evolution_()
               master.update_idletasks()
               master.update()
     except TclError:
          pass



master         = Tk()
canvas         = Canvas(master, width=800, height=800)
canvas.pack()
canvas.bind("<Button 1>", _clicked_)
button = Button(master, text='Start', width=25, command=_on_start)
button.pack()



num_rows       = 100
num_cols       = 100
width          = 8
game           = GameOfLife(canvas, num_rows, num_cols, width, None)

start_configuration = [(4,3), (4,4), (3,4), (3,3), (20,20), (21,20), (22,20), (22,21), (21,22)]
game._start_configuration_(start_configuration)

mainloop()







