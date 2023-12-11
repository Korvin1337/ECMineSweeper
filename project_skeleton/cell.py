import pygame
import random


class Cell:
    """This file contains the cell class representing each square in the game"""

    def __init__(self, x, y, width, height, bomb_chance):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (0, 64, 0)  # RGB color
        self.cell_thickness = 2
        self.neighbouring_bombs = 0
        self.selected = False

        self.cell_center = (
            self.x + self.width // 2,
            self.y + self.width // 2,
        )  # useful for drawing
        self.bomb = (
            random.random() < bomb_chance
        )  # each cell has a chance of being a bomb

    def draw(self, screen):
        """This method is called in the main.py files draw_cells"""
        # Hint: Should draw each cell, i.e something to do with pygame.draw.rect
        # Later on in the assignment it will do more as well such as drawing X for bombs or writing digits
        # Important: Remember that pygame starts with (0,0) coordinate in upper left corner!
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), self.cell_thickness)

        if self.selected:
            font = pygame.font.SysFont(None, 30)
            text = font.render(str(self.neighbouring_bombs), True, (255, 255, 255))

            if self.bomb:
                text = font.render("X", True, (255, 0, 0)) # Display bomb

            screen.blit(text, (self.cell_center[0] - text.get_width() // 2, self.cell_center[1] - text.get_height() // 2))

            #if self.bomb:
                #text = font.render
                #pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x + self.width, self.y + self.height), 2)
                #pygame.draw.line(screen, (255, 255, 255), (self.x + self.width, self.y), (self.x, self.y + self.height), 2)

    def print_me(self):
        print(self.x)
        print(self.y)
        print(self.width)
        print(self.height)
        print(self.bomb)
