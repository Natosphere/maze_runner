# Generate unique maze

from PIL import Image
from generation_algorithms.wilson_algo import generate_wilson
from generation_algorithms.aldous_broder import generate_aldous_broder
from generation_algorithms.recursive import generate_recursive
from utilities import display_maze
import sys




wall_color = (0,0,0,255)
background_color = (255,255,255)

# number of squares in maze



# # maze = generateMaze(square_size, wall_thickness, maze_size, wall_color, background_color)
# maze_array, maze_img = generate_wilson(size=(100,50), 
# 									   display=True, 
# 									   display_stepped=False, 
# 									   waitTime=10, 
# 									   scale=3, 
# 									   square_size=6, 
# 									   wall_thickness=1,
# 									   wall_color=(0,0,0,255), 
# 									   background_color=(255,255,255))



# aldous_broder_maze = generate_aldous_broder(size=(50,50))
# display_maze(aldous_broder_maze, display=True, waitTime=0)



sys.setrecursionlimit(1500)
recursive_maze = generate_recursive(size=(10,10))
display_maze(recursive_maze, display=True, waitTime=0)