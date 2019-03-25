'''
    Import the required modules
'''
import json
import time
from Game_Of_Life import *

'''
    Load the config file
'''
config = json.loads(open('config.json').read())

'''
    Generate the required board from the config file
'''

board = generate_board(config['Initial'])
print(config['Initial'])
'''
    Clear the output screen and print the initial state of the cells
'''
print("\033[2J\033[1;1H")
print(board_to_string(board,int(config['rows']),int(config['coloumns'])))

'''
    Keep computing the states of the cells using the Game_Of_Life constraints
    and stop when there are no cells alive.
    With a time gap of 0.5 seconds between consecutive iterations
'''
while True:
    board = update_board(board,int(config['rows']),int(config['coloumns']))
    print("\033[2J\033[1;1H")
    print(board_to_string(board,int(config['rows']),int(config['coloumns'])))
    if not len(board):
        print("Oooops,everyone is dead !!!")
        break
    time.sleep(0.5)
