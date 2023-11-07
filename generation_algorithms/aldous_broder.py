import numpy as np
import utilities
import random

# Aldous_Broder algorithm
def generate_aldous_broder(size=(50,50), verbose=True):

	# empty maze starts with all cells with full walls, aka 0
	maze = np.full((size[1], size[0]), 0, dtype=np.uint8)



	# while empty cells
	empty_cells = utilities.get_empty_cells(maze)

	# random cell = current
	current = random.choice(empty_cells)

	while len(empty_cells) > 0:


	# pick random neighbor
	
		possible_directions = ['west', 'east', 'north', 'south']
		# prevent out of bounds
		if current[1]-1 < 0: # restrict up if out of bounds
			possible_directions.remove('north')
		if current[0]+1 >= size[0]: # restrict right if out of bounds
			possible_directions.remove('east')
		if current[1]+1 >= size[1]: # restrict down if out of bounds
			possible_directions.remove('south')
		if current[0]-1 < 0: # restrict left if out of bounds
			possible_directions.remove('west')


		random_direction = random.choice(possible_directions)
		if random_direction == 'west': # left
			next = (current[0]-1, current[1])
		elif random_direction == 'east': # right
			next = (current[0]+1, current[1])
		elif random_direction == 'north': # up
			next = (current[0], current[1]-1)
		elif random_direction == 'south': # down
			next = (current[0], current[1]+1)


		# if neighbor empty
		if(maze[next[1],next[0]] == 0):
			
			# remove wall between current and neighbor
			maze = utilities.add_path(maze, [current, next])
			# print(f"Path added: {current, next}")


		# chosen neighbor = current
		current = next



		# find all empty cells
		empty_cells = utilities.get_empty_cells(maze)
		if verbose: print(f"\r Empty: {len(empty_cells): >10}", end='')
	
	return maze