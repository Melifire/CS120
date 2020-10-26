''' Weclome TA and or whoever else is reading this.

    Author: Ben Kruse
    Purpose: Recreates the drawing effect from 3 Blue 1 Brown's youtube video:
        https://www.youtube.com/watch?v=r6sGWTCMz2k&t=1315s
    In essense it uses a bunch of straight lines rotating at fixed speeds to trace out a
    predefined path
    It does this through a series of functions that create factors, make vector lists, 
    and prints them out on a canvas

'''


from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, Close, parse_path
from graphics import graphics
import math
math_i = 0 + 1j

class Vector():
    ''' The basic vector for the project. Each has a value:
    (x, y initial cords given as x+yj)
    and an exponent. The exponent detemines the rate of rotation. 1 makes one full 
    rotation, 2 makes 2 rotations, etc. 0 doesnt rotate and is the base vector
    '''
    def __init__(self, val, exp):
        self.val = val
        self.exp = exp
        self.next = None

def general_formula(path, offset, samples):
    # based on the formula in the video, generates the inital position for a given vector
    return sum(path.point(i/samples)*math.e**(offset*-2*math.pi*math_i*i/samples) 
        for i in range(samples))/samples

def generate_facts(path, depth, samples):
    # calls the general formula on a number of vectors determined by the user. each 
    # vector is a different integer increment and come in +- pairs
    facts = [general_formula(path, 0, samples)]
    for i in range(1, depth//2):
        facts.append(general_formula(path, i, samples))
        facts.append(general_formula(path, -i, samples))
    return facts

def print_svg(window, path, samples):
    # gets the cords of a bunch of points on the svg then draws lines between them
    coords = [path.point(i/samples) for i in range(samples)]
    points_split = [(coord.real, coord.imag) for coord in coords]
    for i in range(samples-1):
        window.line(*points_split[i], *points_split[i+1], 'black', 1)
    window.line(*points_split[0], *points_split[-1], 'black', 1)
    

    window.update()

def make_vector_list(facts, exp = 0):
    # recursivly makes a vector list with the factors previously calcuated
    if not facts:
        # ends the list with None if there are no more factors
        return None
    elif facts and exp > 0:
        # for all factors but the first the +- pairs are added at the same time
        positive = Vector(facts[0], exp)
        negative = Vector(facts[1], -exp)
        positive.next = negative
        negative.next = make_vector_list(facts[2:], exp+1)
        return positive
    else:
        base = Vector(facts[0], 0)
        base.next = make_vector_list(facts[1:], 1)
        return base

def print_vectors(window, tail, vector, t):
    if not vector:
        window.ellipse(tail.real, tail.imag, 10, 10, 'red')
        return None
    else:
        tip = tail + vector.val*math.e**(2*math.pi*t*math_i*vector.exp)
        window.line(tail.real, tail.imag, tip.real, tip.imag, 'black', 1)
        print_vectors(window, tip, vector.next, t)

def main():
    # These are the svg 'd strings'. You can make your own by using whatever vector art tool you want
    svg_string = 'M273.47 457.43C358.61 457.43 414.39 409.24 440.79 312.87C329.9 382.84 274.13 382.84 273.47 312.87C272.81 242.9 216.7 242.9 105.15 312.87C132.21 409.24 188.32 457.43 273.47 457.43Z'
    hey_svg = 'M12.08 246.47C17.03 271.23 320.99 254.39 357.62 246.47C394.26 238.55 396.24 144.49 328.91 193.01C261.58 241.52 237.82 300.93 283.37 291.23C313.73 284.76 320.66 230.9 304.16 129.64C302.84 171.89 291.29 193.01 269.5 193.01C247.72 193.01 239.47 171.89 244.75 129.64C242.77 171.23 228.25 192.35 201.19 193.01C160.59 194 157.62 129.64 185.35 129.64C213.07 129.64 209.11 190.04 185.35 191.03C161.58 192.02 150.69 194.99 129.9 191.03C109.11 187.07 130.89 113.8 92.28 113.8C66.53 113.8 53 140.2 51.68 193.01C45.74 74.2 45.74 14.79 51.68 14.79C60.59 14.79 71.49 59.34 71.49 107.86C71.49 140.2 54.32 168.59 20 193.01C11.42 212.15 8.78 229.97 12.08 246.47Z'
    pi_svg = 'M 10.499686,177.03840 L 31.174931,178.56990 C 52.615925,154.32116 61.039171,82.595924 187.38789,96.634671 C 182.79339,403.95560 48.021426,436.37234 56.444675,499.41907 C 59.507674,535.15406 87.840417,557.10556 118.47041,558.38181 C 215.21014,555.06356 210.87089,424.63084 240.99038,95.868921 L 365.80760,95.868921 C 359.17110,211.75239 341.04836,327.63586 339.00636,441.22208 C 340.53786,516.77606 386.48285,557.10556 446.97708,557.61606 C 546.52456,560.93431 577.92030,444.79558 577.92030,395.27709 L 556.47931,395.27710 C 554.43731,436.11709 534.78306,465.47083 492.92207,467.25758 C 378.82535,468.78908 441.61683,266.63113 442.38258,97.400421 L 577.92030,98.166171 L 577.15455,11.636437 C 13.807491,8.9075799 85.312284,-2.1366151 10.499686,177.03840 z'
    path = parse_path(pi_svg) # put the svg of your choice in this field

    window_width = 600
    window_height = 600
    frames_per_loop = 200  # higher means slower animation
    frames_per_second = 30  # higher means faster assuming your computer can take it
    depth = 100  # number of vectors, use lower if your computer needs but less accurate
    samples = 200  # how acurate the shape reading is, higher numbers is better but 
    # takes longer to set up



    window = graphics(window_width, window_height, 'main')

    factors = generate_facts(path, depth, samples)  #generates initail positions of vectors
    vectors = make_vector_list(factors)  # makes the vectors from the given initials

    frame = 1
    while True:
        # loops the animation
        if frame > frames_per_loop:
            frame = 0
        frame += 1
        window.clear()
        print_svg(window, path, frames_per_loop-1)
        print_vectors(window, vectors.val, vectors.next, frame/frames_per_loop)
        window.update_frame(frames_per_second)

if __name__ == '__main__':
    main()

