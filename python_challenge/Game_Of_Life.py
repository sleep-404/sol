from collections import namedtuple, defaultdict
import time

'''
    Create a tuple named cell with [x,y] in it.
'''
Cell = namedtuple('Cell', ['x', 'y'])

'''
    Generate a board as given in the Config file.
    initial -> Given in the form of config file.
'''
def generate_board(initial):
    board = set()
    for i in range(len(initial)):
        board.add(Cell(int(initial[i][0]),int(initial[i][1])))
    return board

'''
    Check if a cell is a valid cell or not
'''
def valid(x,y,rows,cols):
    if x>=0 and y>=0 and x<cols and y<rows:
        return True
    return False

'''
    Generate all the valid neighbours
'''
def neighbours(cell,rows,cols):
    for x in range(cell.x - 1, cell.x + 2):
        for y in range(cell.y - 1, cell.y + 2):
            if (x, y) != (cell.x, cell.y):
                if valid(x,y,rows,cols):
                    yield Cell(x, y)

'''
    Check to how many cells is the current cell a neighbour.
    Update it's corresponding count by accesing it directly
    from the dictionary using its name.
'''
def count_neighbours(board,rows,cols):
    neighbour_counts = defaultdict(int)
    for cell in board:
        for neighbour in neighbours(cell,rows,cols):
            neighbour_counts[neighbour] += 1
    return neighbour_counts

'''
    If a cell is dead and neighbours_count == 3
        it becomes alive
    else if it is already in board and count == 2
        Alive ;
'''

def isAlive(cell,count,board):
    if count == 3:
        return True
    elif cell in board and count == 2:
        return True
    return False

'''
    Generate new board by updating the older one with new alive neighbours
'''
def update_board(board,rows,cols):
    new_board = set()
    for cell, count in count_neighbours(board,rows,cols).items():
        if isAlive(cell,count,board):
            new_board.add(cell)
    return new_board

'''
    Convert the board to a string so that it can be conviniently printed.
    And also add dead cells to the string.
'''
def board_to_string(board,rows,cols):
    if not board:
        return "empty"
    board_str = ""
    for x in range(0, rows):
        for y in range(0,cols):
            board_str += '1 ' if Cell(x, y) in board else '0 '
        board_str += '\n'
    return board_str.strip()
