""" File: prob1.py
    Author: Ben Kruse
    Purpose: Three simple classes used to learn classes
"""

class Simplest():
    '''
    a simple class with 3 public variables, no functions rather than init
    '''
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class Rotate():
    '''
    Has three private variables first second and third
    4 functions:
        get_first, get_second, get_third return first, second, and third values
        rotate moves each value the position before it, the first goes to last
    '''
    def __init__(self, first, second, third):
        self._first = first
        self._second = second
        self._third = third

    def get_first(self):
        return self._first

    def get_second(self):
        return self._second

    def get_third(self):
        return self._third

    def rotate(self):
        temp = self._first
        self._first = self._second
        self._second = self._third
        self._third = temp

class Band():
    '''
    Simulates a band
    '''
    def __init__(self, singer):
        self.singer = singer
        self.drummer = None
        self.guitarists = []

    def get_singer(self):
        return self.singer

    def set_singer(self, new_singer):
        self.singer = new_singer

    def get_drummer(self):
        return self.drummer

    def set_drummer(self, new_drummer):
        self.drummer = new_drummer

    def add_guitar_player(self, new_guitar_player):
        self.guitarists += [new_guitar_player]

    def fire_all_guitar_players(self):
        self.guitarists = []

    def get_guitar_players(self):
        return self.guitarists[:]

    def play_music(self):
        if self.singer == "Frank Sinatra":
            print("Do be do be do")
        elif self.singer == "Kurt Cobain":
            print("bargle nawdle zouss")
        else:
            print("La la la")

        if self.drummer:
            print("Bang bang bang!")

        for _ in self.guitarists:  # we dont need the name of each so _ is used
            print("Strum!")

        
