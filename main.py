from cell import Cell
from line import Line
from maze import Maze
from point import Point
from window import Window

WIDTH = 800
HEIGHT = 600

def create_cells(columns, rows, width, height):
    cell_height = height / rows
    cell_width = width / columns
    cells = []
    for col in range(columns):
        for row in range(rows):
            x1 = col * cell_width
            x2 = (col + 1) * cell_width
            y1 = row * cell_height
            y2 = (row + 1) * cell_height
            cell = Cell(x1, x2, y1, y2)
            cells.append(cell)
    return cells


def main():
    WIDTH = 800
    HEIGHT = 600
    win = Window(WIDTH, HEIGHT)
    #win.draw_line(Line(Point(0, 0), Point(200, 200)), "red", 2)
    # cells = create_cells(5, 5, 800, 600)
    # for c in cells:
    #     c.draw(win)
    maze = Maze(0,0, 5,5, WIDTH/5, HEIGHT/5, win)

    win.wait_for_close()

if __name__ == "__main__":
    main()