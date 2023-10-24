import numpy as np
import random
import utilities


# recursion_basic TODO



def generate_recursive(size=(50,50)):

	# empty maze starts with all cells with full walls, aka 0
	maze = np.full((size[1], size[0]), 0, dtype=np.uint8)

	# random empty cell = current
	current = (random.randint(0, size[0]-1),random.randint(0, size[1]-1))
	recursive_function(maze, current)

	return maze


def recursive_function(maze, cell):

	neighbors = utilities.get_empty_neighbors(maze, cell)
	print(f"len: {len(neighbors)}, neighbors: {neighbors}")

	while len(neighbors) > 0:
		# remove wall between current and neighbor
		maze = utilities.add_path(maze, [cell, random.choice(neighbors)])
		print("path added")
		utilities.display_maze(maze, scale=6, display=True, waitTime=100, square_size=6, wall_thickness=1)	

		recursive_function(maze, random.choice(neighbors))
	
		neighbors = utilities.get_empty_neighbors(maze, cell)


	print("leaf")

