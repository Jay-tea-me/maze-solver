import time
import random2
from cell import Cell


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_width = cell_size_x
        self.cell_height = cell_size_y
        self._win = win
        self._cells = self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls(0,0)
        self._reset_cells_visited()
        self._draw_cells()
        self._solve_r(0, 0)

    def _create_cells(self):
        cells = []
        for col in range(self.num_cols):
            cell_cols = []
            for row in range(self.num_rows):
                x1 = col * self.cell_width
                x2 = (col + 1) * self.cell_width
                y1 = row * self.cell_height
                y2 = (row + 1) * self.cell_height
                cell = Cell(x1, x2, y1, y2, self._win)
                cell_cols.append(cell)
            cells.append(cell_cols)
        return cells

    def _draw_cells(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].draw()
        self._animate()


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.5)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[len(self._cells) - 1][len(self._cells[0])-1].has_bottom_wall = False

    def _break_walls(self, i, j):
        self._cells[i][j].visited = True
        while True:
            adjacent_cells = []
            if i > 0 and not self._cells[i-1][j].visited:
                adjacent_cells.append((i-1, j))

            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                adjacent_cells.append((i + 1, j))

            if j > 0 and not self._cells[i][j - 1].visited:
                adjacent_cells.append((i, j - 1))

            if j < self.num_rows -1  and not self._cells[i][j + 1].visited:
                adjacent_cells.append((i, j + 1))

            if len(adjacent_cells) == 0:
                return
            next_index = random2.choice(adjacent_cells)


            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False

    # def solve(self, i=0, j=0):
        # self._animate()
        # self._cells[i][j].visited = True
        # print(f"visiting {0}, {1}")
        # if i == self.num_cols-1 and j == self.num_rows - 1:
        #     return True
        #
        # for i_adj in range(i-1, i+1):
        #     if i_adj < 0 or i_adj > len(self._cells) - 1 or i == i_adj:
        #         continue
        #     for j_adj in range(j - 1, j + 1):
        #         if j_adj < 0 or j_adj > len(self._cells[0]) - 1 or j == j_adj:
        #             continue
        #         if self._cells[i_adj][j_adj].visited:
        #             continue
        #         next_cell = self._cells[i_adj][j_adj]
        #         current_cell = self._cells[i][j]
        #         if i_adj < i and next_cell.has_left_wall:
        #             current_cell.draw_move(next_cell, undo=True)
        #             return False
        #         if i_adj > i and next_cell.has_right_wall:
        #             current_cell.draw_move(next_cell, undo=True)
        #             return False
        #         if j_adj < j and next_cell.has_top_wall:
        #             current_cell.draw_move(next_cell, undo=True)
        #             return False
        #         if j_adj > j and next_cell.has_bottom_wall:
        #             current_cell.draw_move(next_cell, undo=True)
        #             return False
        #         self._cells[i][j].draw_move(next_cell)
        #         if self.solve(i_adj, j_adj):
        #             return True
        #
        # return False

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True

        # left
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if i < self.num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if j < self.num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False