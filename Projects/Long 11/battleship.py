import math

class Board():
    def __init__(self, size):
        assert size > 0  # even though the spec says for >= 0, 0 doesn't work
        self._size = size
        # a 2d array that represents the board. square with '.' in each position
        self._grid = [['.' for i in range(size)] for j in range(size)]
        self._ships = []  # an array that holds all the ships
        self._taken_spaces = []  # used to check for collisions

    def get_ships(self):
        # returns the ship list
        return self._ships

    def add_ship(self, ship, position):
        '''adds previously created Ship objects to the board class'''
        ship.set_position(position)
        for bit in ship.get_offset_shape():
            # checks to make sure that each space in the new ship is not colliding with
            # another ship and not off the board
            assert bit not in self._taken_spaces, 'Invalid Position'
            assert 0 <= bit[0] < self._size and 0 <= bit[1] < self._size
            self._grid[bit[1]][bit[0]] = ship.get_name()[0]  # to show ship on grid
            self._taken_spaces.append(bit)  # for checking later collisions
        self._ships.append(ship)  # adds the ship to the ship list

    def print(self):
        '''using the boards '._grid', draw it out on the consol'''
        num_len = int(math.log10(self._size))  # the character length of the size
        # prints the top bound
        print(' ' * (num_len+2) + '+' + '-' * (self._size*2 + 1) + '+') 
        # prints each line of the board starting with the row number
        for i in range(self._size-1, -1, -1):
            print(' ' * (num_len - len(str(i)) + 1) + str(i) + ' | ', end='')
            for j in self._grid[i]:
                print(j, end=' ')
            print('|')
        print(' ' * (num_len+2) + '+' + '-' * (self._size*2 + 1) + '+') # bottom bound
        # all of this is just used to correctly space the collumn numbers no matter how 
        # many there are
        for i in range(num_len+1): 
            print(' ' * (num_len+4), end='')
            for j in range(self._size):
                if j < 10 ** (num_len - i) and i < num_len:
                    print('  ', end='')
                else:
                    print((j % 10 ** (num_len + 1 - i)) // 10 ** (num_len - i),
                            end=' ')
            print()
            
    def has_been_used(self, position):
        '''checks the board at a position to see if it has been used already'''
        # if the board at any point is '*' 'o' or 'X' then the player has already shot 
        try_point = self._grid[position[1]][position[0]]
        if try_point == '*' or try_point == 'o' or try_point == 'X':
            return True
        return False

    def attempt_move(self, position):
        '''attempts to make a move, assertion error if already tried. 
        Returns 'Miss' 'Hit' or 'Sunk :(ship)' depending on the outcome
        '''
        assert not self.has_been_used(position), 'Spot already chosen'
        shot_point = self._grid[position[1]][position[0]]
        if shot_point == '.':  # no ships
            self._grid[position[1]][position[0]] = 'o'
            return 'Miss'
        for ship in self._ships:  # assumes that if it doesnt hit nothing, it hits a ship
            if position in ship.get_offset_shape():  # if it hit this ship
                hit_pos = ship.hit(position)
                self._grid[hit_pos[1]][hit_pos[0]] = '*'
                if ship.is_sunk():  # checks it that was the final blow
                    for bit in ship.get_offset_shape():
                        self._grid[bit[1]][bit[0]] = 'X'
                    return f"Sunk ({ship.get_name()})"
                return 'Hit'
        return 'Something went worng' # This is for debugging and should never occur


class Ship():
    def __init__(self, name, shape):
        assert len(name) > 0  # later, name is indexed at 0 with no checks
        self._name = name
        self._shape = shape
        self._hits = [False for i in range(len(self._shape))]
        self._position = None

    def get_name(self):
        return self._name

    def print(self):
        ''' prints the ship represented as a string of its components with a * for each
        hit part. This is followed by the name of the ship
        '''
        for i in range(len(self._shape)):
            if self._hits[i]:
                print('*', end='')
            else:
                print(self._name[0], end='')

        print(' ' * (10 - len(self._shape)) + self._name)

    def get_shape(self):
        return self._shape

    def get_offset_shape(self):
        '''Returns the offset shape which is the shape of the ship summed with the offet 
            vector. Usefull for checking actual prosition on the board'''
        
        assert self._position, 'This piece has not yet been given a position'
        return ((self._position[0] + bit[0], self._position[1] + bit[1]) 
            for bit in self._shape)

    def set_position(self, position):
        self._position = position

    def hit(self, position):
        ''' hits the ship at given position. 
            The position is taken relative to the board'''
        un_offset_hit = (position[0] - self._position[0],
                         position[1] - self._position[1])
        # makes sure that the hit point is valid
        assert un_offset_hit in self._shape, f"{un_offset_hit} - {self._shape}"
        i = self._shape.index(un_offset_hit)
        self._hits[i] = True
        bit = self._shape[i]
        return [self._position[0] + bit[0], self._position[1] + bit[1]] 

    def is_sunk(self):
        return all(self._hits)

    def rotate(self, amount):
        '''rotates the ship by dotting each part with a 2d rotation matrix'''
        assert 0 <= amount <= 3
        if amount == 0:
            return None
        elif amount == 1:
            rotation_matrix = [[0, 1], [-1, 0]] # 90 degree rotation matrix
        elif amount == 2:
            rotation_matrix = [[-1, 0], [0, -1]] # 180 degree rotation matrix
        elif amount == 3:
            rotation_matrix = [[0, -1], [1, 0]] # 270 degree rotation matrix
        for i, shape in enumerate(self._shape):
            self._shape[i] = self._math_dot_product(rotation_matrix, shape)

    def _math_dot_product(self, matrix, vector):
        ''' does a dot product between a matrix and a vector '''
        assert matrix and vector, 'empty'
        assert len(vector) == len(matrix), 'dif len'
        out_vector = [0 for i in range(len(vector))]

        for i, row in enumerate(matrix):
            for col_num in range(len(row)):
                out_vector[i] += vector[col_num] * row[col_num]

        return tuple(out_vector)
