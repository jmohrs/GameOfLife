#!/usr/bin/python

"""
" This class represnts the game of life, which is made up of individual cells
"""
import Tkinter 
from cell import Cell

class GameOfLife:
     def __init__(self, canvas, number_of_rows, number_of_coloumns, width, start_positions):
          self.canvas             = canvas
          self.number_of_rows     = number_of_rows
          self.number_of_coloumns = number_of_coloumns
          self.width		    = 10
          self.cells              = []                 # <- Used to represent the cells, inner lists represent rows
          self.living_cells	    = []                   # <- Represents the living cells in each step
          self.dying_cells	    = []			       # <- Cells that are going to die in this step
          self.checked_cells	    = []                   # <- Cells that already sentenced to death or life

          key = 0
          for i in range(0, self.number_of_rows):
               row = []
               for j in range(0, self.number_of_coloumns):
                    cell = Cell(self.canvas, j * self.width, i * self.width, self.width, False, key)
                    row.append(cell)
                    key += 1	
               self.cells.append(row)

          for i in range(0, self.number_of_rows):					# <- Set up the neighbours of a cell
               for j in range(0, self.number_of_coloumns):
                    cell 			= self.cells[i][j]
                    cell.left 		= self.cells[i][(j-1) % self.number_of_coloumns]
                    cell.right 		= self.cells[i][(j+1) % self.number_of_coloumns]
                    cell.top 			= self.cells[(i-1) % number_of_rows][j]
                    cell.bottom 		= self.cells[(i+1) % number_of_rows][j]
                    cell.topleft 		= self.cells[(i-1) % number_of_rows][(j-1) % self.number_of_coloumns]
                    cell.topright 		= self.cells[(i-1) % number_of_rows][(j+1) % self.number_of_coloumns]
                    cell.bottomleft 	= self.cells[(i+1) % number_of_rows][(j-1) % self.number_of_coloumns]
                    cell.bottomright 	= self.cells[(i+1) % number_of_rows][(j+1) % self.number_of_coloumns]			
	


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Defines whether a cell lives or dies in the next step
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
     def _evolution_(self):
          self.dying_cells    = []									 
          self.checked_cells	= []                   		
          jesus_cells		= []
          for i in self.living_cells:
               living_neighbours = i.__get_living_neighbours__()
               if (living_neighbours < 2): 
                    self.dying_cells.append(i)
                    self.living_cells.remove(i)
               elif (living_neighbours == 2 or living_neighbours == 3): continue
               else : 
                    self.dying_cells.append(i)
                    self.living_cells.remove(i)
               for j in i.__get_neighbours__():
                    if (j.alive): continue
                    if (j.key in self.checked_cells): continue
                    ngbh = j.__get_living_neighbours__()
                    if (ngbh == 3): jesus_cells.append(j)
                    self.checked_cells.append(j.key)
          for i in self.dying_cells:
               i.__kill__()
          for i in jesus_cells:
               i.__live__()
               self.living_cells.append(i)


     def _start_configuration_(self, start_places):
          for (x,y) in start_places:
               cell = self.cells[y][x]
               self.living_cells.append(cell)
          for cell in self.living_cells: cell.__live__()
          



















