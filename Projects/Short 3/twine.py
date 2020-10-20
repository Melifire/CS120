import sys

# Once we learn classes ill stop with the global variables
obstacles = []

def ranges(player):
    # min x, max x, min y, max y
    range = [0, 0, 0, 0]
    by_x = sorted(player, key=lambda item: item[0])
    by_y = sorted(player, key=lambda item: item[1])
    range[0] = by_x[0][0]
    range[1] = by_x[-1][0]
    range[2] = by_y[0][1]
    range[3] = by_y[-1][1]

    return range

def map(player):
    minx, maxx, miny, maxy = ranges(player)
    # double for loop goes through all values in range and checks
    # if anything is at that cord, else it puts a .
    for j in range(maxy, miny-1, -1):
        for i in range(minx, maxx+1):
            item = (i, j)
            if item in player:
                if item == player[-1]:
                    print('+', end='')
                elif item == (0,0):
                    print('*', end='')
                else:
                    print('X', end='')
            elif item in obstacles:
                print(' ', end='')
            else: 
                print('.', end='')
        # puts a new line after every row
        print()


def act(action, path):
    # standard nese movements, calls move function
    if action in ('n', 'e', 's', 'w'):
        new_location = move(action, path[-1])
        # checks for obstacles
        if new_location in obstacles:
            print('You could not move in that direction,\
 because there is an obstacle in the way.\n\
 You stay where you are.')
        else:
            path.append(new_location)
    # moving back one spot
    elif action == 'back':
        # checks if player can move back
        if len(path) > 1:
            print('You retrace your steps by one space')
            path.pop(-1)
        else:
            print("Cannot move back, as you're at the start!")

    # user input for map, just calls map function
    elif action == 'map':
        map(path)

    # user input for ranges function
    elif action == 'ranges':
        # turns out I already sorted them in the right way so this was simple
        print('''The furthest West you have ever walked is {}
The furthest East you have ever walked is {}
The furthest South you have ever walked is {}
The furthest North you have ever walked is {}'''
        .format(*ranges(path))) 

    # user input for crossings function
    elif action == 'crossings':
        print(
            'There have been {} times in the history\
             when you were at this point.'
        .format(path.count(path[-1])))

    # Catches invalid commands
    else:
        print('ERROR: That is not a valid command')


def move(dir, player):
    # maps input to a tuple that, when summed with the last position, 
    # returns the new position
    moves = {'n': (0, 1), 's': (0, -1), 'e': (1, 0), 'w': (-1, 0)}
    move = moves[dir]
    return (player[0] + move[0] , player[1] + move[1])

def main():
    # global variables, like I said up top
    global obstacles
    print('Please give the name of the obstacles filename, or - for none:')
    validFile = False
    # allows for many tries to get valid file input
    while not validFile:
        ob_file_path = input()
        if ob_file_path and not ob_file_path[0] == '-':
            try:
                ob_file = open(ob_file_path, 'r')
                validFile = True
                # enumerate used for getting line number for debugging
                for number, line in enumerate(ob_file):
                    if line:
                        try:
                            obstacles.append(
                                tuple(int(i) for i in line.split()))
                        except:
                            print(
                                "ERROR: there was an error with line {} in {}"
                                .format(number, ob_file_path))
            except:
                print('ERROR: That is not a valid file name')
        else: 
            # found a valid file, now continues program
            validFile = True            

    twine = [(0, 0)]
    while True:
        print('''
Current position: {}
Your history:     {}
What is your next command?'''
            .format(twine[-1], twine))
        try:
            input_string = input()
        except:
            break
        action = input_string.strip()
        if action == 'break':
            break
        if action:
            act(action, twine)
        else:
            print('You do nothing.')


main()

