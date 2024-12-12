import unittest

from maze import Maze


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0].has_left_wall)
        self.assertFalse(m1._cells[11][9].has_bottom_wall)

    def test_reset_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_walls(0,0)
        self.assertTrue(m1._cells[4][4].visited)
        m1._reset_cells_visited()
        self.assertFalse(m1._cells[4][4].visited)

if __name__ == '__main__':
    unittest.main()
