''' File: median.py
    Author: Ben Kruse
    Purpose: Finds the middle letter (or middle two letters if even len)
        of a given input
'''

def main():
    inp = input('input: ')
    length = len(inp) - 1
    #print out the range from our adusted length / 2 rounded down, to our adjusted length / 2 rounded to the nearest whole number
    #the +.1 is used because python rounds .5 to 0 rather than one, the floating-point representation error has many solutions, this is just the simpleist that works for the problem
    #the +1 is used to offset the exclusive nature of substringing
    print(inp[length // 2: round(length / 2 + .1) + 1])
