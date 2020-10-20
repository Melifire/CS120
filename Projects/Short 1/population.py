''' File: population.py
    Author: Ben Kruse
    Purpose: Prints out processed data from a text file
'''

def main():
    inp = input('file: ').strip()
    file = open(inp)
    list = file.readlines()
    #remove outside whitespace
    list = [i.strip() for i in list if i.strip() and i[0] != '#']
    #seperate into names and numbers [name, number]
    list = [[' '.join(i.split()[:-1]), i.split()[-1]] for i in list]

    for dataPoint in list:
        print('State/Territory: {}\nPopulation:      {}\n'
            .format(dataPoint[0], dataPoint[1]))

    print('# of States/Territories: {}\nTotal Population:        {}'
        .format(len(list), sum(int(val[1]) for val in list)))

main()
