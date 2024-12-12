from line import Line
from point import Point


class Cell:
    def __init__(self, x1, x2, y1, y2, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.window = window
        self.visited = False

    def draw(self):
        if self.window is None:
            return
        bottom_left_point = Point(self._x1, self._y2)
        bottom_right_point = Point(self._x2, self._y2)
        top_left_point =  Point(self._x1, self._y1)
        top_right_point =  Point(self._x2, self._y1)
        left = Line(bottom_left_point, top_left_point)
        right = Line(bottom_right_point, top_right_point)
        top = Line(top_left_point, top_right_point)
        bottom = Line(bottom_left_point, bottom_right_point)
        self._draw_wall(left, self.has_left_wall)
        self._draw_wall(right, self.has_right_wall)
        self._draw_wall(bottom, self.has_bottom_wall)
        self._draw_wall(top, self.has_top_wall)

    def _draw_wall(self, line, exists):
        if exists:
            print("drawing bottom")
            self.window.draw_line(line)
        else:
            self.window.draw_line(line, fill="white")

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        line = Line(self.get_center(), to_cell.get_center())
        self.window.draw_line(line, fill=color)

    def get_center(self):
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

