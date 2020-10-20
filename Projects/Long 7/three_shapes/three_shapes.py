"""File: three_shapes.py

   Author: Ben Kruse

   Purpose: Creates three classes: Circle, Triangle, Square, each with their
   own way of moving and colliding
"""

from three_shapes_game import Game
import numpy as np
import random as rn

class Circle:
    '''
    The circle bounces off walls and eachother. Is killed by squares and kills
    triangles. Move in 2d
    '''
    def __init__(self, pos, vel, radius = 20, color = 'black'):
        # np arrays are used for their ability to add as vectors and dot prods
        self.pos = np.array(pos, 'float64')
        self.vel = np.array(vel, 'float64')
        self.radius = radius
        self.color = color


    def get_xy(self):
        return tuple(self.pos)

    def get_radius(self):
        return self.radius

    def nearby(self, other, dist, game):
        min_distance = self.get_radius() + other.get_radius()
        if dist <= min_distance:
            if type(other) == Square:
                game.remove_obj(self)

            if type(other) == Circle:
                # these equations are based on the wiki article for collisions.
                #  in this simulation the effect is not quite as desired 
                # because each collion is called twice (once on each obj). 
                # This problem is fixed in my spheres program but creates some 
                # interesting effects so it was left unchanged here
                new_vel_1 = self.vel -\
                    ((np.dot(self.vel-other.vel, self.pos-other.pos))/\
                    (np.linalg.norm(self.pos - other.pos))**2) *\
                    (self.pos-other.pos)

                new_vel_2 = other.vel -\
                    ((np.dot(other.vel-self.vel, other.pos-self.pos)) /\
                    (np.linalg.norm(other.pos - self.pos))**2) *\
                    (other.pos-self.pos)

                self.vel = new_vel_1 * .9
                other.vel = new_vel_2 * .9

                self.pos += self.vel
                other.pos += other.vel


    def edge(self, dir, position):
        # flips the velocity bouncing it off the wall
        if dir == 'top' or dir == 'bottom':
            self.vel[1] *= -1
        if dir == 'left' or dir == 'right':
            self.vel[0] *= -1

    def move(self, game):
        # moves in the dir of velocity by the lenght of the velocity vector
        self.pos += self.vel

    def draw(self, win):
        win.ellipse(self.pos[0], self.pos[1], self.radius*2, self.radius*2, 
            self.color)


class Triangle:
    '''Triangles only move right at a random speed. Once they hit the wall, 
    they instantly jump to the left side and continue on the same path. 
    Killed by circles and kills squares.
    '''
    def __init__(self, pos, h_vel, side_len=20, color='black'):
        self._pos = np.array(pos, 'float64')
        self._vel = np.array((h_vel, 0), 'float64')
        self._side_len = side_len
        self._color = color

    def get_xy(self):
        return tuple(self._pos)

    def get_radius(self):
        return self._side_len * .7

    def nearby(self, other, dist, game):
        min_distance = self.get_radius() + other.get_radius()
        if dist <= min_distance:
            if type(other) == Circle:
                game.remove_obj(self)

    def edge(self, dir, position):
        # triangles should only ever hir the right side
        assert not (dir == 'top' or dir == 'bottom' or dir == 'left'), \
            'This should never occur, Triangle bounds error'
        if dir == 'right':
            self._pos[0] = self._side_len

    def move(self, game):
        # moves in the dir of velocity by the lenght of the velocity vector
        self._pos += self._vel

    def draw(self, win):
        x, y = self._pos
        l = self._side_len
        win.triangle(x-l/2, y-l/2, x+l/2, y-l/2, x, y+l/2, self._color)


class Square:
    '''
    Squares only move down in an almost tetris fashion where they jump thier
    height downwards every 10 frames, They stop once they either reach the
    bottom or touch another square.
    '''
    def __init__(self, h_pos, color='black'):
        self._pos = np.array((h_pos*20 + 10, 10), 'int32')
        self._length = 20
        self._color = color
        # a frame counter is used to make the square move every 10 frames
        self._frame_counter = 0
        # stopped means it has touched the bottom or another block, no longer 
        # moves
        self._stopped = False

    def get_xy(self):
        return tuple(self._pos)

    def get_radius(self):
        return 19

    def nearby(self, other, dist, game):
        min_distance = self.get_radius() + other.get_radius()
        if dist <= min_distance:
            if type(other) == Triangle:
                game.remove_obj(self)

            if type(other) == Square and other._stopped == True:
                self._stopped = True

    def edge(self, dir, position):
        # squares only move down so they should only touch the bottom
        if dir == 'bottom':
            self._stopped = True


    def move(self, game):
        # only moves on every 10th frame
        if not self._stopped:
            self._frame_counter += 1
            if self._frame_counter == 10:
                self._pos[1] += 20
                self._frame_counter = 0


    def draw(self, win):
        x, y = self._pos
        win.rectangle(x-10, y-10, 20, 20, self._color)


def spawn(game_obj):
    # shape picker picks a random digit 0: circle, 1: triangle, 2: square
    shape_picker = rn.randrange(0, 3)
    # picks a random number between hex 000000 and hex ffffff, converted later
    color = rn.randrange(0, 16777215)
    if shape_picker == 0:
        radius = rn.randrange(10, 50)
        obj = Circle((rn.randrange(radius, 800-radius),
                      rn.randrange(radius, 800-radius)), 
                     (rn.randrange(-30, 30), 
                      rn.randrange(-30, 30)), 
                      radius, '#{:06X}'.format(color))
    if shape_picker == 1:
        side_length = rn.randrange(10, 50)
        obj = Triangle((rn.randrange(side_length, 800-side_length),
                        rn.randrange(side_length, 800-side_length)),
                        rn.randrange(1, 50),
                        side_length, '#{:06X}'.format(color))
    if shape_picker == 2:
        obj = Square(rn.randrange(0, 39),
                     '#{:06X}'.format(color))    
    #adds the shape
    game_obj.add_obj(obj)
                
        

def main():
    wid = 800
    hei = 800

    game = Game("Three Shapes", 20, wid, hei)

    # some starting shapes, there are input manually at the start
    test_shapes = [
        Circle((100, 100), (10, 5), 20, 'red'),
        Circle((300, 400), (-10, -10), 30, 'black'),
        Square(5, 'green'),
        Square(2, 'blue'),
        Square(10, 'blue'),
        Square(0, 'blue'),
        Triangle((300, 100), 10, 20, 'purple'),
        Triangle((600, 400), 10, 20, 'yellow'),
    ]

    # adds the test shapes
    for obj in test_shapes:
        game.add_obj(obj)

    # frame counter is used to add a new shape every 5 frames
    frame_counter = 0
    while not game.is_over():
        frame_counter += 1
        if frame_counter == 5:
            spawn(game)
            frame_counter = 0

        game.do_nearby_calls()
        game.do_move_calls()
        game.do_edge_calls()
        game.execute_removes()
        game.draw()



if __name__ == "__main__":
    main()



