import pygame
import sys
from cell import Cell
from calcs import measure_distance
"""Use this file as you want to run testcode and play around"""

SCREEN_MIN_SIZE = 750  # Can be made to autoadjust after % of ur screen
amount_of_cells = 16  # The amount of cells is equal in rows and columns, 16x16 (LOCKED)
bomb_chance = 0.25  # Change to prefered value or use default 0.25

CELL_SIZE = SCREEN_MIN_SIZE // amount_of_cells  # how large can each cell be?
READJUSTED_SIZE = CELL_SIZE * amount_of_cells
CELL_WIDTH = CELL_HEIGHT = CELL_SIZE  # Probably not needed, just use cell_size

SCREEN_WIDTH, SCREEN_HEIGHT = READJUSTED_SIZE, READJUSTED_SIZE


a = 750 // 16

new_cell = Cell(0, 0, CELL_WIDTH, CELL_HEIGHT, bomb_chance)

print(a * 16)

print(new_cell.print_me())
