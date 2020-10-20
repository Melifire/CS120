''' File: count_items.py
    Author: Ben Kruse
    Purpose: Prints out processed data from a text file
'''
def main():

    inp = input('File to scan: ').strip()
    #inp = 'test-count_items-01.in'

    file = open(inp)
    lst = file.readlines()
    #remove outside whitespace
    lst = [i.strip() for i in lst if i.strip() and i[0] != '#']
    #breaks it into the string and number as a list
    lst = [[i.split()[0], int(i.split()[1])] for i in lst]

    #converts list into dictionary and adds the value of common keys
    dictionary = {}
    for arr in lst:
        if arr[0] in dictionary:
            dictionary[arr[0]] += arr[1]
        else: dictionary[arr[0]] = arr[1]

    #back to a list and sort it
    lst = list(dictionary.items())
    lst = sorted(lst, key = lambda x: (-x[1], x[0]))

    #print it out
    for dataPoint in lst:
        print('{} {}'.format(dataPoint[0], dataPoint[1]))

main()
