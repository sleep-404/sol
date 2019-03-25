'''
    Tests to verify the validity of the module 
'''

from Game_Of_Life import *
import unittest

class Test(unittest.TestCase):

    '''
        Test to check if generate_board() works fine or not .
    '''
    def test_generate_board(self):
        initial = [[0,0],[1,1]]
        actual = generate_board(initial)
        expected = set([Cell(0, 0), Cell(1, 1)])
        self.assertEqual(expected, actual)

    '''
        Test to check if valid() works fine or not.
    '''
    def test_valid(self):
        rows,cols = 5,5
        actual = set([
            valid(1,1,rows,cols),valid(7,1,rows,cols) ])
        expected = set([True,False])
        self.assertEqual(expected, actual)

    '''
        Test to check whether neighbours() returns
        correct value on contrained cell.
    '''
    def test_constrained_neighbours(self):
        cell = Cell(0, 0)
        rows,cols=5,5
        expected = set([
            Cell(1, 0), Cell(0, 1), Cell(1, 1) ])
        actual = set(neighbours(cell,rows,cols))
        self.assertEqual(expected, actual)

    '''
        Test to check whether neighbours() returns
        correct value on normal cell.
    '''
    def test_complete_neighbours(self):
        cell = Cell(1, 1)
        rows,cols=5,5
        expected = set([
            Cell(0, 0), Cell(0, 1), Cell(0, 2),
            Cell(2, 0), Cell(2, 1), Cell(2, 2),
            Cell(1, 0), Cell(1, 2) ])
        actual = set(neighbours(cell,rows,cols))
        self.assertEqual(expected, actual)

    '''
        Test to check if count_neighbours() works fine or not.
    '''
    def test_count_neighbours(self):
        alive = set([Cell(0, 0), Cell(1, 1)])
        rows,cols=3,3
        expected = {
            Cell(0, 0): 1,
            Cell(1, 0): 2,
            Cell(2, 0): 1,
            Cell(0, 1): 2,
            Cell(1, 1): 1,
            Cell(2, 1): 1,
            Cell(0, 2): 1,
            Cell(1, 2): 1,
            Cell(2, 2): 1,
        }
        actual = count_neighbours(alive,rows,cols)
        self.assertEqual(expected, actual)

    '''
        Test to verify isAlive() works fine on new cells : Positive example
    '''
    def test_isAlive(self):
        cell,count = Cell(0,0),3
        board = set([
            Cell(0, 0),Cell(0,1),
            Cell(1, 0),Cell(1,1)
            ])
        expected = isAlive(cell,count,board)
        actual = True
        self.assertEqual(expected, actual)

    '''
        Test to verify isAlive() works fine on new cells : Negative example
    '''
    def test_is_not_Alive(self):
        cell,count = Cell(1,1),4
        board = set([
            Cell(0, 0),Cell(0,1),
            Cell(1, 0),Cell(1,1),Cell(1,2)
            ])
        expected = isAlive(cell,count,board)
        actual = False
        self.assertEqual(expected, actual)

    '''
        Test to verify isAlive() works fine on existing cells : Positive example
    '''
    def test_isAlive_contraint(self):
        cell,count = Cell(1,1),2
        board = set([
            Cell(0, 0),Cell(0,1),
            Cell(1,1)
            ])
        expected = isAlive(cell,count,board)
        actual = True
        self.assertEqual(expected, actual)

    '''
        Test to verify isAlive() works fine on existing cells : Negative example
    '''
    def test_is_not_Alive_contraint(self):
        cell,count = Cell(1,1),2
        board = set([
            Cell(0, 0),Cell(0,1),
            ])
        expected = isAlive(cell,count,board)
        actual = False
        self.assertEqual(expected, actual)

    '''
        Test to check whether update_board() works fine on empty sets
    '''
    def test_update_empty_board(self):
        alive = set()
        rows,cols=3,3
        self.assertEqual(alive, update_board(alive,rows,cols))

    '''
        Test to check whether update_board() works fine on usual cells
    '''
    def test_update_board(self):
        initial = [[0,0],[1,1],[2,2]]
        rows,cols=3,3
        board = generate_board(initial)
        actual = update_board(board,rows,cols)
        expected = set([Cell(1,1)])
        self.assertEqual(expected, actual)

    '''
        Test to check the validity of board_to_string()
    '''
    def test_board_to_string(self):
        initial = [[0,0],[0,1],[1,1],[2,2]]
        rows,cols=3,3
        board = generate_board(initial)
        new_board = update_board(board,rows,cols)
        actual = board_to_string(new_board,rows,cols)
        expected = "1 1 0 \n1 1 1 \n0 0 0"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
