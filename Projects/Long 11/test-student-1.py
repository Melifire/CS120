import battleship

game = battleship.Board(12)

#must testcases be in a method

ship_list = [
    (battleship.Ship('Nina', [(0,0), (1, 0), (2, 0), (3, 0)]), (3, 4), 0),
    (battleship.Ship('Pinta', [(0,0), (1, 0), (2, 0), (3, 0)]), (0, 0), 0),
    (battleship.Ship('Santa Maria', [(0,0), (1, 0), (2, 0), (3, 0)]), (0, 5), 1)
]

for ship in ship_list:
    ship[0].rotate(ship[2])
    game.add_ship(ship[0], ship[1])

fail_ship_collide = battleship.Ship('Collide', [(0, 0)])
try:
    game.add_ship(fail_ship_collide, (3, 4))
except:
    print('Caught ship collision error')

fail_ship_bounds = battleship.Ship('Bounds', [(0, 0)])
try:
    game.add_ship(fail_ship_bounds, (100, 100))
except:
    print('Caught ship bounds error')

for ship in game.get_ships():
    ship.print()

game.print()

game.attempt_move((5, 5))

game.print()

game.attempt_move((3, 4))
game.attempt_move((4, 4))
game.attempt_move((5, 4))

game.print()

game.attempt_move((6, 4))

game.print()