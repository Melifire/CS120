''' File: strings_and_input.py
    Author: Ben Kruse
    Purpose: Take and input string and do a bunch of stuff with it
'''

def main():
    inp = input('input string: ')
    print(len(inp))
    print(inp[1])
    try:
        print(inp[:10])
    except IndexError:
        print(inp)
    try:
        print(inp[-5:])
    except IndexError:
        print(inp)
    print(inp.upper())

    #the fist letter of the input string; lowecase;
    first_letter = inp[0]
    qwerty = ['q', 'w', 'e', 'r', 't', 'y']
    uiop = ['u', 'i', 'o', 'p']
    if first_letter.lower() in qwerty: print('QWERTY')
    elif first_letter in uiop: print('UIOP')
    #check for it being a letter
    elif 97 <= ord(first_letter.lower()) <= 122:
        print('LETTER')
    elif 48 <= ord(first_letter) <= 57:
        print('DIGIT')
    else:
        print('OTHER')

    number1 = int(input())
    number2 = int(input())

    print(number1*number2)

main()
