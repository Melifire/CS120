''' File: swap.py
    Author: Ben Kruse
    Purpose: Swap the first half and second half of an input,
        leaves the middle character if applicable
'''

import math

def main():
    inp = input('Please give a string to swap: ')
    length = len(inp)

    print(inp[math.ceil(length / 2) : ] +  #takes the last chars
          inp[length//2 : math.ceil(length/2)] +  #takes mid char (if appl.)
          inp[ : length//2])  #takes the starting chars

main()
