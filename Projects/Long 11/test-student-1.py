import battleship


def main():
    game = battleship.Board(12)

    # list of all ships to add
    ship_list = [
        (battleship.Ship('Nina', [(0,0), (1, 0), (2, 0), (3, 0)]), (3, 4), 0),
        (battleship.Ship('Pinta', [(0,0), (1, 0), (2, 0), (3, 0)]), (0, 0), 0),
        (battleship.Ship('Santa Maria', [(0,0), (1, 0), (2, 0), (3, 0)]), (0, 5), 1)
    ]

    # checks to makes sure rotation works
    for ship in ship_list:
        ship[0].rotate(ship[2])
        game.add_ship(ship[0], ship[1])

    # check colliding ships
    fail_ship_collide = battleship.Ship('Collide', [(0, 0)])
    try:
        game.add_ship(fail_ship_collide, (3, 4))
    except:
        print('Caught ship collision error')

    # check for out of bounds ship
    fail_ship_bounds = battleship.Ship('Bounds', [(0, 0)])
    try:
        game.add_ship(fail_ship_bounds, (100, 100))
    except:
        print('Caught ship bounds error')

    # checks ship printing
    for ship in game.get_ships():
        ship.print()

    # checks game printing and proper placement of ships
    game.print()

    # checks miss
    game.attempt_move((5, 5))

    game.print()

    # checks hitting ship
    game.attempt_move((3, 4))
    game.attempt_move((4, 4))
    game.attempt_move((5, 4))

    game.print()

    #checks sinking ship
    game.attempt_move((6, 4))

    game.print()

if __name__ == '__main__':
    main()