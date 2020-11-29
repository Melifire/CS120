import array

class Checkers:

    def __init__(self, build_list):
        # each 8x8 game board is encoded in 194 bits compared to 392 bits for an empty string
        # 011 is a new line
        # otherwise characters are encoded:
        #   (is there a piece) (is it a king) (is it red)

        # for example, 101 would be a base red piece

        self.board = 2 | (build_list[0] == 'r')

        for letter in build_list[2:]:
            if letter == ' ':  # new line 
                self.board = self.board << 3 | 3
            else:
                self.board = self.board << 3 | ((letter != '.') << 2
                    | ((letter.isupper()) << 1 | (letter.lower() == 'r')))


    def __str__(self):
        bit_rep = format(self.board, '021b')

        out = ['b ', 'r '][bit_rep[1] == '1']        

        for i in range(2, len(bit_rep), 3):
            if bit_rep[i] == '0':
                if bit_rep[i+1] == '1':
                    out += ' '
                else:
                    out += '.'
            else:
                if bit_rep[i+1] == '1':
                    if bit_rep[i+2] == '1':
                        out += 'R'
                    else:
                        out += 'B'
                else:
                    if bit_rep[i+2] == '1':
                        out += 'r'
                    else:
                        out += 'b'

        return out

    def get_square(self, x, y):
        pos = ((8-x) + (8-y) * 9) * 3
        val = (self.board >> pos) & 7
        if val == 0:
            print('.')
        elif val == 4:
            print('b')
        elif val == 5:
            print('r')
        elif val == 6:
            print('B')
        elif val == 7:
            print('R')
        else:
            print('Character offset')


    def get_cur_player(self):
        return ['black', 'red'][format(self.board, '021b')[1] == '1']
        

test = Checkers(
    'b r.r.r.r. .r.r.r.r r.r.r.r. ........ ........ b.b.b.b. .b.b.b.b b.b.b.b.')

print(test)
print(test.get_cur_player())
test.get_square(7,6)
