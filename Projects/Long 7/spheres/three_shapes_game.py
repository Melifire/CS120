"""File: three_shapes_game.py

   Author: Russ Lewis

   Purpose: Defines the Game class, which provides the core mechanisms for the
            Three Shapes family of programs.
"""


import math        # for sqrt

from graphics import graphics



class Game:
    def __init__(self, title, frame_rate, wid,hei,depth, show_top = True):
        """Constructor.  Initializes the game to have zero objets; call
           add_obj() to add objects to the system.

           Parameters: the width and height of the window
        """
        self._wid = wid
        self._hei = hei
        self._depth = depth

        self._frame_rate = frame_rate

        self._win = graphics(wid,hei, title)
        if show_top:
            self._top_view = graphics(wid, self._depth*2, 'top')
        else:
            self._top_view = False

        # this is a configuration setting - it changes how we calculate
        # the distance between objects in do_nearby_calls()
        self._account_for_radii_in_dist = False

        # the user must call add_obj() to add to this set
        self._active_objs = set()

        # see what remove_obj() and perform_moves() do, to understand this
        # variable.
        self._pending_removes = set()

        # I plan to add a feature, where the user can mark the game as "over"
        self._game_over = False

    def get_size(self):
        return (self._wid, self._hei, self._depth)

    def config_set(self, param, val):
        """Function to set various config variables.  Right now, it only
           supports a single parameter; I might add more later.  Give the name
           of the parameter (as a string), then the value.

           Parmeters: config parameter to set, value

           Supported Config Options:
             "account_for_radii_in_dist" -> Boolean
        """
        if param == "account_for_radii_in_dist":
            self._account_for_radii_in_dist = val
        else:
            assert False   # unrecognized config parameter



    def set_game_over(self):
        self._game_over = True
    def is_over(self):
        return self._game_over



    def add_obj(self, new_obj):
        """Adds a new object to the game.  Can be called at any time, although
           if called in the middle of the nearby() or move() loops, may not be
           added to the ongoing loop.  The object must implement the standard
           methods required of any object: get_xy(), get_radius(), nearby(),
           move(), and draw().

           Parameters: the new object
        """
        assert new_obj not in self._active_objs
        self._active_objs.add(new_obj)



    # REMOVE LOGIC 
    #
    # In the do_nearby_calls() and do_move_calls() methods, we loop over
    # lots of objects.  Inside those methods, the user may choose to call
    # remove_obj(); if they do, then ideally we would just remove it
    # immediately.  But we're in the middle of a loop: what if we call
    # nearby() or move() on a recently-removed object, or if we pass it as
    # a parameter to a nearby() call?
    #
    # One option would be to force the remove logic to exclude such objects
    # from the loop as it runs, but that's not the easiest thing in the
    # world.  Instead, remove_obj() will add an object to a set of "pending
    # removes" - none of these removals will take place until the game loop
    # calls execute_removes() - which happens *after* all of the nearby()
    # and move() calls have finished.
    #
    # When the user calls remove_obj(), it *MUST* be in the current set of
    # active objects.  It is *permissible* to call it multiple times in the
    # same game tick.

    def remove_obj(self, bad_obj):
        """Queues up an object to be removed from the game.  It is
           permissible to call this multiple times on the same object during
           one clock tick; all of the removals will take place at once,
           *after* all of the nearby() and move() calls have been completed,
           but *before* any draw() calls.  It is illegal to call this if the
           object is not currently in the game.

           Arguments: object to remove
        """
        assert bad_obj in self._active_objs
        self._pending_removes.add(bad_obj)

    def execute_removes(self):
        """Called by the game loop, after all of the nearby() and move() calls
           have completed; performs all of the pending remove operations.

           Arguments: None
        """
        self._active_objs -= self._pending_removes
        self._pending_removes = set()



    def do_nearby_calls(self):
        """Collisions are significantly simplified as each collision only
            requires a single call rather than one for each object colliding

           Parameters: none
        """

        positions = []
        for o in self._active_objs:
            x,y,z = o.get_xyz()
            positions.append( (o,x,y,z) )


        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                o1,x1,y1,z1 = positions[i]
                o2,x2,y2,z2 = positions[j]

                dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

                if not o1.nearby(o2, dist, self):
                    break




    def do_move_calls(self):
        """Calls move() on every object in the game"""
        for o in self._active_objs:
            o.move(self)



    def do_edge_calls(self):
        """Finds any objects that are close to any edge - defined as within the
           radius of it (that is, touching or overlapping) - and calls edge()
           on them.

           Parameters: none
        """

        for o in self._active_objs:
            x,y,z = o.get_xyz()
            rad = o.get_radius()

            if x < rad:
                o.edge("left", 0)
            if y < rad:
                o.edge("top", 0)

            if x+rad >= self._wid:
                o.edge("right", self._wid)
            if y+rad >= self._hei:
                o.edge("bottom", self._hei)

            #third dimensional wall
            if z-rad < -1*self._depth:
                o.edge("back", 0)
            if z+rad > self._depth:
                o.edge("front", 0)

    # stops the top down view
    def kill_top_view(self):
        self._top_view.is_killed = True


    def draw(self):
        """Calls draw() on every object in the game.  Also does the rest of the
           misc calls necessary to animate the window.
        """

        # if the window has been destroyed, then we will throw an exception when
        # we run clear() below.  So check for this condition first!
        if self._win.is_killed:
            self._game_over = True
            return

        #changes here are made to accomadate a second window for top down view
        self._win.clear()
        if self._top_view and not self._top_view.is_killed:
            self._top_view.clear()

        for o in self._active_objs:
            o.draw(self._win, self._top_view)

        self._win.update_frame(self._frame_rate)
        if self._top_view and not self._top_view.is_killed:
            self._top_view.update_frame(self._frame_rate)


