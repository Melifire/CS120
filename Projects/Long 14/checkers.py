import array
import sys

class Checkers:

    def __init__(self, build_list):
        # each 8x8 game board is encoded in 194 bits, compared to 392 bits for 
        # an empty python string
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

    def get_piece_count(self, color):
        return str(self).lower().count(color)

    def is_game_over(self):
        return not (self.get_piece_count('r') and self.get_piece_count('b'))

    def do_move(self, start, to):
        cur_decoded = list(str(self))

        player = cur_decoded[0]
        start_x, start_y = ord(start[0])-97, int(start[1]) - 1
        to_x, to_y = ord(to[0])-97, int(to[1]) - 1
        star_piece = cur_decoded[2 + start_x + start_y * 9]
        end_piece = cur_decoded[2 + to_x + to_y * 9]

        if start_x > 7 or to_x > 7 or start_x < 0 or to_x < 0 or start_y > 7 or to_y > 7 or start_y < 0 or to_y < 0:
            print('invalid range')
            return None
        if star_piece.lower() != player:
            print('invalid start')
            return None
        if end_piece != '.':
            print('spot full')
            return None
        if star_piece == 'r':
            if abs(to_x - start_x) != 1 or to_y - start_y != 1:  # not up one and to left or right by one
                if to_y - start_y == 2 and abs(to_x - start_x) == 2:  # jumping
                    if cur_decoded[2 + (to_x + start_x)//2 + (to_y + start_y)//2 * 9].lower() != 'b':  # if valid token to jump
                        print('no token to jump')
                        return None
                    else:
                        cur_decoded[2 + (to_x + start_x)//2 + (to_y + start_y)//2 * 9] = '.'
                else:
                    print('cant move to this spot')
                    return None
        elif star_piece == 'b':
            if abs(to_x - start_x) != 1 or to_y - start_y != -1: # not up one and to left or right by one

                print(to_y - start_y, abs(to_x - start_x))
                if to_y - start_y == -2 and abs(to_x - start_x) == 2:  # jumping
                    if cur_decoded[2 + (to_x + start_x)//2 + (to_y + start_y)//2 * 9].lower() != 'r':  # if valid token to jump
                        print('no token to jump')
                        return None
                    else:
                        cur_decoded[2 + (to_x + start_x)//2 + (to_y + start_y)//2 * 9] = '.'
                else:
                    print('cant move to this spot')
                    return None
        elif star_piece == 'R':
            # not up one and to left or right by one
            if abs(to_x - start_x) != 1 or abs(to_y - start_y) != 1:
                if abs(to_y - start_y) == 2 and abs(to_x - start_x) == 2:  # jumping
                    # if valid token to jump
                    if cur_decoded[2 + (to_x + start_x)//2 + (to_y + start_y)//2 * 9].lower() != 'b':
                        print('no token to jump')
                        return None
                    else:
                        cur_decoded[2 + (to_x + start_x)//2 +
                                    (to_y + start_y)//2 * 9] = '.'
                else:
                    print('cant move to this spot')
                    return None
        else:
            # not up one and to left or right by one
            if abs(to_x - start_x) != 1 or abs(to_y - start_y) != 1:
                if abs(to_y - start_y) == 2 and abs(to_x - start_x) == 2:  # jumping
                    # if valid token to jump
                    if cur_decoded[2 + (to_x + start_x)//2 + (to_y + start_y)//2 * 9].lower() != 'r':
                        print('no token to jump')
                        return None
                    else:
                        cur_decoded[2 + (to_x + start_x)//2 +
                                    (to_y + start_y)//2 * 9] = '.'
                else:
                    print('cant move to this spot')
                    return None

        print('valid move')

        if to_y == 0 or to_y == 7:
            cur_decoded[2 + to_x + to_y *
                        9] = cur_decoded[2 + start_x + start_y * 9].upper()
        else:
            cur_decoded[2 + to_x + to_y * 9] = cur_decoded[2 + start_x + start_y * 9]

        cur_decoded[2 + start_x + start_y * 9] = '.'
        cur_decoded[0] = ['r', 'b'][cur_decoded[0] == 'r']

        return Checkers(cur_decoded)
            
        

    def get_cur_player(self):
        return ['black', 'red'][format(self.board, '021b')[1] == '1']
        

test = Checkers(
    'r r.r.r.r. .r.r.r.r r.r.r.r. ........ ........ .b.b.b.b b.b.b.b. .b.b.b.b')



for line in sys.stdin:
    line = line.strip().split()
    test = test.do_move(*line)
    print(test)
