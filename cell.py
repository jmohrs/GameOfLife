"""
" This class is used to represent a cell in the game of life
"""

from Tkinter import Canvas


class Cell:
     def __init__(self, canvas, x, y, width, alive, key):
          self.key            = key
          self.x              = x
          self.y              = y
          self.width          = width
          self.canvas         = canvas
          self.alive          = alive
          self.left           = None
          self.topleft        = None
          self.right          = None
          self.topright       = None
          self.top            = None
          self.bottom         = None
          self.bottomleft     = None
          self.bottomright    = None
          self.alive          = alive
          if (self.alive):
               self.rect = canvas.create_rectangle(x, y, x + width, y + width, fill="black")
          else:
               self.rect = canvas.create_rectangle(x, y, x + width, y + width, fill="white")

     def __kill__(self):
          self.canvas.itemconfig(self.rect, fill="white")
          self.alive = False

     def __live__(self):
          self.canvas.itemconfig(self.rect, fill="black")
          self.alive = True

     def __get_living_neighbours__(self):
          living_neighbours = 0
          if (self.left.alive)       :  living_neighbours += 1
          if (self.right.alive)      :  living_neighbours += 1
          if (self.top.alive)        :  living_neighbours += 1
          if (self.bottom.alive)     :  living_neighbours += 1
          if (self.topleft.alive)    :  living_neighbours += 1
          if (self.topright.alive)   :  living_neighbours += 1
          if (self.bottomleft.alive) :  living_neighbours += 1
          if (self.bottomright.alive):  living_neighbours += 1
          return living_neighbours 

     def __get_neighbours__(self):
          neighbours	= []
          neighbours.append(self.left)
          neighbours.append(self.right)
          neighbours.append(self.topleft)
          neighbours.append(self.bottomleft)
          neighbours.append(self.topright)
          neighbours.append(self.bottomright)
          neighbours.append(self.top)
          neighbours.append(self.bottom)
          return neighbours		
