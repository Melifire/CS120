import array

class Checkers:

    def __init__(self, build_list):
        board = array.array('b', [build_list[0] == 'r'])

        for letter in build_list[1:]:
            if letter == ' ':
                continue
            board.extend([letter != '.', letter.isupper(), letter.lower() == 'r'])

        print(board)

        


test = Checkers('b r.r.r.r .b.b.b.')