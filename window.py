from tkinter import Tk, BOTH, Canvas

from line import Line
from point import Point


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(self.__root, width=width, height=height,   borderwidth=0, highlightthickness=0)
        self.__canvas.pack(padx = 6, pady=6)
        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def create_line(self, x1, x2, y1, y2, fill, width):
        self.draw_line(Line(Point(x1, y1), Point(x2, y2)), fill, width)

    def draw_line(self, line, fill="black", width=2):
        line.draw(self.__canvas, fill, width)