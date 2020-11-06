"""File: spheres.py

   Author: Ben Kruse

   Purpose: Creates spheres that collide in 3d space, the output window is a 2d
   cross section of the volume. A top down view can also be shown by changing 
   the False in the games constructor to True. Collisions are by no means 
   perfect but work well enough I think
"""

from three_shapes_game import Game
import numpy as np
import math
from graphics import graphics


#all positions, scales, velocities are done (x,y,z)
class Sphere:
    '''
    The sphere class is very similar to a circle class for a 2d environment, 
    differences show in collisions and rendering. Collisions are done in 3d 
    and rendering is done by cross section
    '''
    def __init__(self, pos, rad, vel, color, mass):
        self.pos = np.array(pos, dtype='float64')  # (f, f, f)
        self.rad = rad  # f
        self.vel = np.array(vel, dtype='float64')  # (f, f, f)
        self.color = color
        self.mass = mass * 1.0

    def get_xyz(self):
        return self.pos

    def get_radius(self):
        return self.rad

    def nearby(self, other, dist, game):

        min_distance = self.rad + other.rad
        if dist <= min_distance:
            # collision equations based on the wiki article for collisions
            # the vast majority of this project was trying to get collisions to
            # work in 3d
            new_vel_1 = self.vel - ((2*other.mass)/(self.mass+other.mass))*\
                ((np.dot(self.vel-other.vel, self.pos-other.pos))/\
                    (np.linalg.norm(self.pos - other.pos))**2)*\
                (self.pos-other.pos)

            new_vel_2 = other.vel - ((2*self.mass)/(other.mass+self.mass))*\
                ((np.dot(other.vel-self.vel, other.pos-self.pos))/\
                    (np.linalg.norm(other.pos - self.pos))**2)*\
                (other.pos-self.pos)

            self.vel = new_vel_1 * .9
            other.vel = new_vel_2 * .9

            self.pos += self.vel
            other.pos += other.vel


    def add_force(self, force):
        self.vel += force

    def edge(self, dir, position):
        # inverts velocity to bounce off wall
        if dir == 'top' or dir == 'bottom':
            self.vel[1] *= -.9  # -.9 adds dampening to bottom and top
        if dir == 'left' or dir == 'right':
            self.vel[0] *= -1
        if dir == 'front' or dir == 'back':
            self.vel[2] *= -1
        self.pos += self.vel

    def move(self, game):
        self.pos += self.vel
        self.vel[1] += 5

    def draw(self, win, top):
        x, y, z = self.pos
        # equation finds what the radius of the circle is at z from the center
        new_rad = np.sqrt(max(self.rad**2 - z**2, 0)) 
        if new_rad != 0:  # do not show if not in the cross sections
            win.ellipse(x, y, new_rad*2, new_rad*2, self.color)
        if top and not top.is_killed:
            top.ellipse(x, z+300, self.rad*2, self.rad*2, self.color)
            top.line(0, win.canvas.winfo_height()/2,
                     win.canvas.winfo_width(), win.canvas.winfo_height()/2)



def main():

    wid = 800
    hei = 800
    # the depth is given as the distance both walls are from the center
    # a depth of 300 would mean the room has a total depth of 600
    dep = 300 

    #change the False to True to see a top down view
    game = Game("Three Shapes", 20, wid, hei, dep, True)

    # add your own spheres here, if you want to simply view a 2d simulation, do
    # not add any z to the posion or velocity

    # (position x, y, z), radius, (velocity x, y, z), color, mass
    obj_list = [
        Sphere((200, 200, 0), 100, (0, 0, 0), 'black', 1),
        Sphere((400, 600, 100), 100, (0, 0, 0), 'black', 1),
        Sphere((500, 100, 0), 100, (0, 0, 0), 'black', 1),
        Sphere((600, 600, -20), 100, (0, 0, 0), 'black', 1)
    ]
    for obj in obj_list:
        game.add_obj(obj)

    #game.kill_top_view()


    while not game.is_over():

        game.do_nearby_calls()
        game.do_move_calls()
        game.do_edge_calls()
        game.execute_removes()
        game.draw()


if __name__ == "__main__":
    main()



