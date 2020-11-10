import math

class Board():
    def __init__(self, size):
        assert size > 0  # even though the spec says for >= 0, 0 wouldn't work
        self._size = size
        self._grid = [['.' for i in range(size)] for j in range(size)]
        self._ships = []
        self._taken_spaces = []

    def get_ships(self):
        return self._ships

    def add_ship(self, ship, position):
        ship.set_position(position)
        for bit in ship.get_offset_shape():
            assert bit not in self._taken_spaces, 'Invalid Position'
            assert 0 <= bit[0] < self._size and 0 <= bit[1] < self._size
            self._grid[bit[1]][bit[0]] = ship.get_name()[0]
            self._taken_spaces.append(bit)
        self._ships.append(ship)

    def print(self):
        num_len = int(math.log10(self._size))
        print(' ' * (num_len+2) + '+' + '-' * (self._size*2 + 1) + '+')
        for i in range(self._size-1, -1, -1):
            print(' ' * (num_len - len(str(i)) + 1) + str(i) + ' | ', end='')
            for j in self._grid[i]:
                print(j, end=' ')
            print('|')
        print(' ' * (num_len+2) + '+' + '-' * (self._size*2 + 1) + '+')
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
        try_point = self._grid[position[1]][position[0]]
        if try_point == '*' or try_point == 'o' or try_point == 'X':
            return True
        return False

    def attempt_move(self, position):
        assert not self.has_been_used(position), 'Spot already chosen'
        shot_point = self._grid[position[1]][position[0]]
        if shot_point == '.':
            self._grid[position[1]][position[0]] = 'o'
            return 'Miss'
        for ship in self._ships:
            if position in ship.get_offset_shape():
                hit_pos = ship.hit(position)
                self._grid[hit_pos[1]][hit_pos[0]] = '*'
                if ship.is_sunk():
                    for bit in ship.get_offset_shape():
                        self._grid[bit[1]][bit[0]] = 'X'
                    return f"Sunk ({ship.get_name()})"
                return 'Hit'
        return 'Something went worng'


class Ship():
    def __init__(self, name, shape):
        assert len(name) > 0
        self._name = name
        self._shape = shape
        self._hits = [False for i in range(len(self._shape))]
        self._position = None

    def get_name(self):
        return self._name

    def print(self):
        for i in range(len(self._shape)):
            if self._hits[i]:
                print('*', end='')
            else:
                print(self._name[0], end='')

        print(' ' * (10 - len(self._shape)) + self._name)

    def get_shape(self):
        return self._shape

    def get_offset_shape(self):
        
        assert self._position, 'This piece has not yet been given a position'
        return ((self._position[0] + bit[0], self._position[1] + bit[1]) 
            for bit in self._shape)

    def set_position(self, position):
        self._position = position

    def hit(self, position):
        un_offset_hit = (position[0] - self._position[0],
                         position[1] - self._position[1])
        assert un_offset_hit in self._shape, f"{un_offset_hit} - {self._shape}"
        i = self._shape.index(un_offset_hit)
        self._hits[i] = True
        bit = self._shape[i]
        return [self._position[0] + bit[0], self._position[1] + bit[1]]

    def is_sunk(self):
        return all(self._hits)

    def rotate(self, amount):
        assert 0 <= amount <= 3
        if amount == 0:
            return None
        elif amount == 1:
            rotation_matrix = [[0, 1], [-1, 0]]
        elif amount == 2:
            rotation_matrix = [[-1, 0], [0, -1]]
        elif amount == 3:
            rotation_matrix = [[0, -1], [1, 0]]
        for i, shape in enumerate(self._shape):
            self._shape[i] = self._math_dot_product(rotation_matrix, shape)

    def _math_dot_product(self, matrix, vector):
        assert matrix and vector, 'empty'
        assert len(vector) == len(matrix), 'dif len'
        out_vector = [0 for i in range(len(vector))]

        for i, row in enumerate(matrix):
            for col_num in range(len(row)):
                out_vector[i] += vector[col_num] * row[col_num]

        return tuple(out_vector)
