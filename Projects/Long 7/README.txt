Hello Ta, This file provides some basic information about my programs

While both three_shapes.py and spheres.py are included with three_shapes_game.py and graphics.py files, three_shapes.py still uses the base versions of those files. 
spheres.py however uses a modified version to accomidate a third dimension so it must be used with the three_shapes_game.py that comes with it.

Both programs require python as well as numpy to run (for easier vector math)

three_shapes.py:
	Creates three classes: Circle, Triangle, Square, each with their own way of moving and colliding

	Circle: The circle bounces off walls and eachother. Is killed by squares and kills triangles. Move in 2d. in this simulation the bouncing is not quite as desired 
        because each collion is called twice (once on each obj). This problem is fixed in my spheres program but creates some interesting effects so it was left unchanged 
	here

	Square: Squares only move down in an almost tetris fashion where they jump thier height downwards every 10 frames, They stop once they either reach the
    	bottom or touch another square. Are killed by triangles and kill circles

	Triangle: Triangles only move right at a random speed. Once they hit the wall, they instantly jump to the left side and continue on the same path. 
  	Killed by circles and kills squares.

spheres.py:
	Creates spheres that collide in 3d space, the output window is a 2d cross section of the volume. A top down view can also be shown by changing 
   	the False in the games constructor to True. Collisions are by no means perfect but work well enough I think