""" File: grid_drawing.py
    Author: Ben Kruse
    Purpose: Allows the user to create a board and 'draw' on it by setting 
    values through a variety of functions
"""

import sys

# for this project I used a global board, normally I would use a class in 
# this case but for sake of us not having learned them yet this is my solution
board = []


def b_init(vars):
    # checks for a valid number of inputs, input type in guaranteed as int
    if not len(vars) == 2:
        print('Input error: Invalid number of inputs. Sorry')
        return
    # splits up input array into variables
    i, j = vars
    global board
    # sets the board to be 0s in the size of the inputs
    board =  [[0 for i in range(vars[0])] for j in range(vars[1])]

def b_print(_):
    global board
    trans_board = list(zip(*board))
    for i in range(len(trans_board)-1, -1,-1):
        print(''.join(str(num) for num in trans_board[i]))
    print()

def b_print_raw(_):
    print(board)
    return None

def b_set(vars):
    if not len(vars) == 3:
        print('Input error: Invalid number of inputs. Sorry')
        return
    global board
    try:
        board[vars[1]][vars[2]] = vars[0]
    except IndexError:
        print('Input error: Sorry, that index is out of range')
    return None

def b_horiz_line(vars):
    if not len(vars) == 5:
        print('Input error: Invalid number of inputs. Sorry')
        return
    global board
    c, x1, y1, x2, y2 = vars
    if not y1 == y2:
        print('Input error: Both y values must be the same: y1 = {}, y2 = {}'
        .format(y1, y2))
    for i in range(x1, x2+1):
        try:
            board[i][y1] = c
        except IndexError:
            print('Input error: Sorry, that index is out of range')
    return None

def b_vert_line(vars):
    if not len(vars) == 5:
        print('Input error: Invalid number of inputs. Sorry')
        return
    global board
    c, x1, y1, x2, y2 = vars
    if not x1 == x2:
        print('Input error: Both x values must be the same: x1 = {}, x2 = {}'
        .format(x1, x2))
    for j in range(y1, y2+1):
        try:
            board[x1][j] = c
        except IndexError:
            print('Input error: Sorry, that index is out of range')
    return None

def b_filled_rect(vars):
    if not len(vars) == 5:
        print('Input error: Invalid number of inputs. Sorry')
        return
    global board
    c, x1, y1, x2, y2 = vars
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            try:
                board[i][j] = c
            except IndexError:
                print('Input error: Sorry, that index is out of range')
    return None

def b_hollow_rect(vars):
    if not len(vars) == 5:
        print('Input error: Invalid number of inputs. Sorry')
        return
    global board
    c, x1, y1, x2, y2 = vars
    # uses the other funtions to draw the rectangle's lines
    b_horiz_line([c, x1, y1, x2, y1])
    b_horiz_line([c, x1, y2, x2, y2])
    b_vert_line([c, x1, y1+1, x1, y2-1])
    b_vert_line([c, x2, y1+1, x2, y2-1])
    return None

def main():
    functions = ['init', 'print', 'print_raw', 'set',
    'horiz_line', 'vert_line', 'filled_rect', 'hollow_rect']
    # Used to throw input error if there is no inputs
    hasInput = False
    for line in sys.stdin:
        # clean the input and remove unwanted lines (blank/comment)
        line = line.strip().split()
        if not line:
            continue
        function = line[0]
        if function[0] == '#':
            continue
        hasInput = True
        # trows error if there is no board yet user wants to draw
        if not board and not function == 'init':
            print('Input error: You must first set up a board')
            break
        # puts all inputs into a variables array thats used in the functions
        try:
            variables = [int(i) for i in line[1:]]
        except ValueError:
            print('Input error: Sorry, wrong input type')
            continue
        # makes sure user inputs a valid function
        if function in functions:
            eval('b_' + function + '(variables)')
        else:
            print('Input error: Not a valid function')

    # trows error if no inputs
    if not hasInput:
        print('Input error: There are no inputs!')

main()
