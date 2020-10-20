""" File: prob3.py
    Author: Ben Kruse
    Purpose: Created a room similar to what would be seen in a MUD. Also has a 
    funtion for building an array of rooms
"""

class Room():
    '''Each room has a name as well as 4 possible exits to another room. If the 
    next room is None, than there is no room in that direction
    '''
    def __init__(self, name = 'gen_room', nesw = (None, None, None, None)):
        self._name = name
        self.n, self.e, self.s, self.w = nesw

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def collapse_room(self):
        # nesw is repeated twice so that every direction has its oposite 
        # two spaces later
        dirs = "neswnesw"  
        # circles around n, e, s, w and closes the link to and from each room
        for i in range(4): 
            exec('self.{}.{} = None'.format(dirs[i], dirs[i+2]))
            exec('self.{} = None'.format(dirs[i]))

def build_grid(w, h):
    '''builds a grid using the room objects defined in this program
    '''
    # for debugging, each room is named its x, y position in the grid 
    # "base" at 0, 0
    base = Room('Base')
    cur = base      # cur is used to hold what room the program is on while 
    cury = base     # cury is used to hold what row its on
    for j in range(h):
        for i in range(w):

            # for the bottom row, creates a new room to the east and links up
            if i != w-1 and j == 0:
                cur.e = Room('{}, {}'.format(i+1, j))
                cur.e.w = cur
            
            # for every row but the bottom, links this node to the one to the 
            # east. This node is found by going south, east, north
            if j != 0 and i != w-1 : 
                cur.e = cur.s.e.n
                cur.e.w = cur

            #for every row but the top, create a new room north of this one 
            # and link them up
            if j != h-1:
                cur.n = Room('{}, {}'.format(i, j+1))
                cur.n.s = cur

            cur = cur.e  #advances the room to the right

        cury = cury.n  # moves the row pointer up and 
        cur = cury     # resets the room pointer to the first of the row
    return base




