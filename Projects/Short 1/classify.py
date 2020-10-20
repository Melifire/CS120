''' File: classify.py
    Author: Ben Kruse
    Purpose: Classify the first letter in a given input as
        vowel, consonant, or neither (not a letter)
'''


def main():
    #the fist letter of the input string; lowecase; taken as a decimal
    first_letter_decimal = ord(input("input: ")[0].lower())
    #the lower case vowels as decimals
    vowels = [97, 101, 105, 111, 117, 121]

    #check for it not being a letter
    if not (97 <= first_letter_decimal <= 122):
        print('neither')
    elif first_letter_decimal in vowels:
        print('vowel')
    else:
        print('consonant')
