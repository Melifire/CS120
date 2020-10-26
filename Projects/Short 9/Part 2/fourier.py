from svg.path import Path, Line, Arc, CubicBezier, QuadraticBezier, Close, parse_path
from graphics import graphics
import math
math_i = 0 + 1j

class Vector():
    def __init__(self, val, exp):
        self.val = val
        self.exp = exp
        self.next = None

def general_formula(path, offset, samples):
    return sum(path.point(i/samples)*math.e**(offset*-2*math.pi*math_i*i/samples) for i in range(samples))/samples

def generate_facts(path, depth, samples):
    facts = [general_formula(path, 0, samples)]
    for i in range(1, depth//2):
        facts.append(general_formula(path, i, samples))
        facts.append(general_formula(path, -i, samples))
    return facts

def print_svg(window, path, samples):
    coords = [path.point(i/samples) for i in range(samples)]
    points_split = [(coord.real, coord.imag) for coord in coords]
    for i in range(samples-1):
        window.line(*points_split[i], *points_split[i+1], 'black', 1)
    window.line(*points_split[0], *points_split[-1], 'black', 1)
    

    window.update()

def make_vector_list(facts, exp = 0):
    if not facts:
        return None
    elif facts and exp > 0:
        positive = Vector(facts[0], exp)
        negative = Vector(facts[1], -exp)
        positive.next = negative
        negative.next = make_vector_list(facts[2:], exp+1)
        return positive
    else:
        base = Vector(factors[0], 0)
        base.next = make_vector_list(facts[1:], 1)
        return base

def print_vectors(window, tail, vector, t):
    if not vector:
        return None
    else:
        tip = tail + vector.val*math.e**(2*math.pi*t*math_i*vector.exp)
        window.line(tail.real, tail.imag, tip.real, tip.imag, 'black', 1)
        print_vectors(window, tip, vector.next, t)


svg_string = 'M273.47 457.43C358.61 457.43 414.39 409.24 440.79 312.87C329.9 382.84 274.13 382.84 273.47 312.87C272.81 242.9 216.7 242.9 105.15 312.87C132.21 409.24 188.32 457.43 273.47 457.43Z'
hey_svg = 'M12.08 246.47C17.03 271.23 320.99 254.39 357.62 246.47C394.26 238.55 396.24 144.49 328.91 193.01C261.58 241.52 237.82 300.93 283.37 291.23C313.73 284.76 320.66 230.9 304.16 129.64C302.84 171.89 291.29 193.01 269.5 193.01C247.72 193.01 239.47 171.89 244.75 129.64C242.77 171.23 228.25 192.35 201.19 193.01C160.59 194 157.62 129.64 185.35 129.64C213.07 129.64 209.11 190.04 185.35 191.03C161.58 192.02 150.69 194.99 129.9 191.03C109.11 187.07 130.89 113.8 92.28 113.8C66.53 113.8 53 140.2 51.68 193.01C45.74 74.2 45.74 14.79 51.68 14.79C60.59 14.79 71.49 59.34 71.49 107.86C71.49 140.2 54.32 168.59 20 193.01C11.42 212.15 8.78 229.97 12.08 246.47Z'
path = parse_path(svg_string)

window = graphics(500, 500, 'main')

factors = generate_facts(path, 70, 100)
#print(factors)

vectors = make_vector_list(factors)



i = 100
while True:
    if i > 100:
        i = 0
    i += 1
    window.clear()
    print_svg(window, path, 99)
    print_vectors(window, 0+0j, vectors, i/100)
    window.update_frame(60)




