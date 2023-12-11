import numpy as np
import random
import utilities


# recursion_basic TODO



def generate_recursive(size=(20,20), display=False, display_stepped=False, waitTime=10, scale=3, square_size=6, wall_thickness=1, wall_color=(0,0,0,255), background_color=(255,255,255), verbose=True):

	# empty maze starts with all cells with full walls, aka 0
	maze = np.full((size[1], size[0]), 0, dtype=np.uint8)

	# random empty cell = current
	current = (random.randint(0, size[0]-1),random.randint(0, size[1]-1))
	recursive_function(maze, current, waitTime, square_size, wall_thickness, display_stepped, verbose)

	if display: utilities.display_maze(maze, scale=scale, display=True, waitTime=1000, square_size=square_size, wall_thickness=wall_thickness, wall_color=wall_color, background_color=background_color)	
	return maze


def recursive_function(maze, cell, waitTime, square_size, wall_thickness, display_stepped, verbose):

	neighbors = utilities.get_empty_neighbors(maze, cell)
	# print(f"len: {len(neighbors)}, neighbors: {neighbors}")

	while len(neighbors) > 0:
		# remove wall between current and neighbor
		next = random.choice(neighbors)
		maze = utilities.add_path(maze, [cell, next])
		if display_stepped: utilities.display_maze(maze, scale=6, display=True, waitTime=waitTime, square_size=square_size, wall_thickness=wall_thickness)	

		recursive_function(maze, next, waitTime, square_size, wall_thickness, display_stepped, verbose)
	
		neighbors = utilities.get_empty_neighbors(maze, cell)


				# find all empty cells

		if verbose: 
			empty_cells = utilities.get_empty_cells(maze)
			print(f"Empty: {len(empty_cells): >10}", end='\r')


	# print("leaf")

