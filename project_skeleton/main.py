import pygame
import sys
from cell import Cell
from calcs import measure_distance

""" This is the main file you work on for the project"""

pygame.init()

SCREEN_MIN_SIZE = 750  # Can be made to autoadjust after % of ur screen
amount_of_cells = 16  # The amount of cells is equal in rows and columns, 16x16 (LOCKED)
bomb_chance = 0.2  # Change to prefered value or use default 0.25
bomb_counter = 0
amount_of_bombs = 0
amount_of_cells_revealed = 0
cells_in_game = 256

CELL_SIZE = SCREEN_MIN_SIZE // amount_of_cells  # how big can each cell be?
READJUSTED_SIZE = CELL_SIZE * amount_of_cells
CELL_WIDTH = CELL_HEIGHT = CELL_SIZE  # Probably not needed, just use cell_size

SCREEN_WIDTH, SCREEN_HEIGHT = READJUSTED_SIZE, READJUSTED_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("MineSweeper")

cells = []


def create_cells():
    global amount_of_bombs
    y = -46 # Update value for each column, increase by 750 / 16 = 46
    for a_row in range(amount_of_cells):
        row = []
        y += 46
        x = 0
        for a_column in range(amount_of_cells):
            new_cell = Cell(x, y, CELL_WIDTH, CELL_HEIGHT, bomb_chance) # Create the cells by usimg the Cell class constructor
            if new_cell.bomb:
                amount_of_bombs = amount_of_bombs + 1 # Keep track of how many bombs are in the playfield
            row.append(new_cell)
            x += 46
        cells.append(row)
    check_for_bombs_around_cell(cells)
    draw()


def check_for_bombs_around_cell(cells):
    for a_row in range(amount_of_cells):
        for a_column in range(amount_of_cells):
            cell = cells[a_row][a_column]
            if not cell.bomb:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        row = a_row + i
                        col = a_column + j
                        if 0 <= row < len(cells) and 0 <= col < len(cells[row]):
                            if cells[row][col].bomb:
                                cell.neighbouring_bombs += 1


def draw_cells():
    """In this function we want to draw each cell, i.e call upon each cells .draw() method!"""
    # Hint: take inspiration from the forloop in create_cells to loop over all the cells
    for row in cells:
        for cell in row:
            cell.draw(screen)


def draw():
    """This function handles all the drawings to the screen, such as drawing rectangles, objects etc"""
    draw_cells()


def event_handler(event):
    """This function handles all events in the program"""
    if event.type == pygame.QUIT:
        terminate_program()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Make event for left clicking mouse button
        left_mouse_button_click(event.pos)


def left_mouse_button_click(position):
    deadzone = 40

    for row in cells:
        for cell in row:
            if (
                cell.x <= position[0] <= cell.x + cell.width and
                cell.y <= position[1] <= cell.y + cell.height and
                not (
                    cell.x - deadzone > position[0] or
                    position[0] > cell.x + cell.width + deadzone or
                    cell.y + deadzone < position[1] or
                    position[1] > cell.y + cell.height
                )
            ):
                handle_click(cell)

def reset_game():
    global bomb_counter, amount_of_cells_revealed, cells, amount_of_bombs
    bomb_counter = 0
    amount_of_cells_revealed = 0
    amount_of_bombs = 0
    for row in cells:
        for cell in row:
            cell.reset()
    cells.clear()
    print("--------------------------------------------------------")
    print("-------------------New Game Starting--------------------")
    print("--------------------------------------------------------")
    main()


def reveal_bomb(cell):
    global bomb_counter # Keep track of how many times a bomb has been clicked
    bomb_counter += 1
    print("B00M! You clicked a bomb!")
    cell.selected = True
    if(bomb_counter > 3):
        counter = 0
        while(counter < 25):
            print("--------------------------------------------------------")
            print("-------------------You lose!----------------------------")
            counter += 1
        reset_game()
    # End game ? Reveal all bombs ?


def handle_click(cell):
    print("Clicked on cell:", cell.x, cell.y)

    if cell.bomb and not cell.selected:
        reveal_bomb(cell)
    elif not cell.selected:
        cell.selected = True
        reveal_cells_around(cell)



# Reveals the cell that is clicked, if the cell clicked is a 0 it works together with reveal_neighbours to reveal it´s neighbours (non bombs since they are none around it)
def reveal_cells_around(cell):
    print("Reveal non-bomb cells around:", cell.x, cell.y)
    global amount_of_cells_revealed # Keep track of number of cells revealed

    # Calculate grid indices for the selected cell
    cell_row = cell.y // CELL_SIZE
    cell_col = cell.x // CELL_SIZE

    # Count amount of cells revealed
    amount_of_cells_revealed += 1

    # Check for bombs
    if cell.neighbouring_bombs == 0:
        reveal_neighbors(cell_row, cell_col)


def reveal_neighbors(row, col):
    global amount_of_cells_revealed # Keep track of number of cells revealed
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_row, new_col = row + i, col + j

            # Check if the indices are within bounds
            if 0 <= new_row < amount_of_cells and 0 <= new_col < amount_of_cells:
                cell_around = cells[new_row][new_col]

                # Check if the cell is not already selected to avoid infinite recursion
                if not cell_around.selected:
                    cell_around.selected = True
                    amount_of_cells_revealed += 1

                    # If the cell has no neighboring bombs, recursively reveal its neighbors
                    if cell_around.neighbouring_bombs == 0:
                        reveal_neighbors(new_row, new_col)



def reveal_cells(cell):
    print("Revealing cell:", cell.x, cell.y)

    # Check if bomb is around selected cell
    if not cell.selected and not cell.bomb:
        cell.selected = True

        # Check if the current cell has no neighboring bombs
        if cell.neighbouring_bombs == 0:
            # Iterate over neighboring cells
            for a_row in range(-1, 2):
                for a_col in range(-1, 2):
                    row = (cell.x // CELL_SIZE) + a_row
                    col = (cell.y // CELL_SIZE) + a_col
                    print(f"Row: {row}, Col: {col}")
                    # Check if the indices are valid
                    if 0 <= row < amount_of_cells and 0 <= col < amount_of_cells:
                        cell_around = cells[row][col]
                        # Recursively reveal neighboring cells
                        reveal_cells(cell_around)



def run_setup():
    """This function is meant to run all code that is neccesary to setup the app, happends only once"""
    create_cells()


def terminate_program():
    """Functionality to call on whenever you want to terminate the program"""
    pygame.quit()
    sys.exit()


def main():
    run_setup()

    clock = pygame.time.Clock() # Clock to be able to set fps
    running = True
    frame = 0

    while running:
        win = False
        global amount_of_cells_revealed, cells_in_game, amount_of_bombs
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                left_mouse_button_click(event.pos)
                #print(str(amount_of_cells_revealed) + " revealed")
                #print(str(amount_of_cells) + " cells")
                #print(str(amount_of_bombs) + " boms")
                #print(amount_of_cells - amount_of_bombs)
                if(amount_of_cells_revealed == cells_in_game - amount_of_bombs):
                    win = True

        draw_cells()
        pygame.display.flip()

        clock.tick(30)
        frame += 1

        if win:
            counter = 0
            while(counter < 25):
                print("--------------------------------------------------------")
                print("------------C0NGRATULATI0NS, Y0U WIN!!!!----------------")
                counter += 1
            reset_game()

    terminate_program()


if __name__ == "__main__":
    main()
