import numpy as np
import random
import utilities

#region encoding notes
# A note about encoding the maze:
# Method 1: bitshifts
	# bool1 = True
	# bool2 = False
	# encoded_number = 0
	# if bool1:
	#     encoded_number |= (1 << 0)
	# if bool2:
	#     encoded_number |= (1 << 1)

	# decoded_bool1 = (encoded_number & (1 << 0)) != 0
	# decoded_bool2 = (encoded_number & (1 << 1)) != 0
	

# Method 2: modulo --- this method gets exponentially less efficient the more bools you encode
	# bool1 = True
	# bool2 = False
	# bool3 = False
	# encoded_number = 0
	# if bool1:
	#     encoded_number += 1
	# if bool2:
	#     encoded_number += 2
	# if bool3:
	#     encoded_number += 4
	# decoded_bool1 = encoded_number % 2 == 1
	# decoded_bool2 = (encoded_number // 2) % 2 == 1
	# decoded_bool3 = (encoded_number // 4) % 2 == 1
#endregion



# Wilson's Algorithm --- Loop-erased random walk
	# "https://en.wikipedia.org/wiki/Maze_generation_algorithm#Wilson's_algorithm"
	# "https://en.wikipedia.org/wiki/Loop-erased_random_walk"
	# "https://www.cs.cmu.edu/~15859n/RelatedWork/RandomTrees-Wilson.pdf"


def generate_wilson(size=(50,50), seed=None, display=False, waitTime=500, display_stepped=False, scale=2, background_color=(255,255,255,255), wall_color=(0,0,0,255), square_size=6, wall_thickness=1, verbose=True):
# create numpy array of zeros
# empty maze starts with all cells with full walls, aka 0
	maze = np.full((size[1], size[0]), 0, dtype=np.uint8)

	# set seed
	if seed:
		random.seed(seed)


	# get empty cells
	empty_cells = utilities.get_empty_cells(maze)

	while len(empty_cells) > 0:

		# Choose random cell to start a random walk through the grid.
		start_cell_loc = random.choice(empty_cells)

		# Choose random cell as destination
		dest_cell_loc = random.choice(empty_cells)
		# only use destination cell on the first path.
		if len(empty_cells) == size[0] * size[1]:
			dest_cell_loc = random.choice(empty_cells)
		else: dest_cell_loc = [-1,-1]

		if display and display_stepped:
			base_img = utilities.display_maze(maze, scale=scale, display=False, waitTime=waitTime, square_size=square_size, wall_thickness=wall_thickness)
			path_img = base_img.copy()

		
		# random walk
		path = [(start_cell_loc)]
		if display and display_stepped:
			utilities.display_path(img_base=path_img, path=path[-1:], scale=scale, waitTime=waitTime, display=True, square_size=square_size, wall_thickness=wall_thickness)
		while(True):

			current = path[-1]

			
			possible_directions = ['west', 'east', 'north', 'south']
			# prevent stepping backwards
			if len(path) >= 2:
				previous = path[-2]
				if current[1] == previous[1]+1: # restrict north if previous
					possible_directions.remove('north')
				elif current[0] == previous[0]-1: # restrict east if previous
					possible_directions.remove('east')
				elif current[1] == previous[1]-1: # restrict south if previous
					possible_directions.remove('south')
				elif current[0] == previous[0]+1: # restrict west if previous
					possible_directions.remove('west')
			
			# prevent out of bounds
			if 'north' in possible_directions and current[1]-1 < 0: # restrict up if out of bounds
				possible_directions.remove('north')
			if 'east' in possible_directions and current[0]+1 >= size[0]: # restrict right if out of bounds
				possible_directions.remove('east')
			if 'south' in possible_directions and current[1]+1 >= size[1]: # restrict down if out of bounds
				possible_directions.remove('south')
			if 'west' in possible_directions and current[0]-1 < 0: # restrict left if out of bounds
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


			# add next to path
			path.append(next)

			if display and display_stepped:
				utilities.display_path(img_base=path_img, path=path, scale=scale, waitTime=waitTime, display=True, square_size=square_size, wall_thickness=wall_thickness)


			# if the random walk ever touches it's own path, erase the entire loop it created. 
			for i, x in enumerate(path[:-1]):
				if next == x:
					path = path[:i+1]
					if display and display_stepped:
						utilities.display_path(img_base=path_img, path=path, scale=scale, waitTime=1, display=True, square_size=square_size, wall_thickness=wall_thickness)

					break


			# check if next is dest_cell_loc or existing path, if so, add path to maze
			if dest_cell_loc == next or maze[next[1]][next[0]] != 0:
				maze = utilities.add_path(maze, path)

				if display and display_stepped:
					base_img = utilities.display_maze(maze, scale=scale, display=display, waitTime=waitTime, square_size=square_size, wall_thickness=wall_thickness)	
					path_img = base_img.copy()


				break
		
		# find all empty cells
		empty_cells = utilities.get_empty_cells(maze)

		if verbose: print(f"Empty: {len(empty_cells): >10}", end='\r')

	if verbose: print("Maze Generated Successfully")
	if display:
		utilities.display_maze(maze, wall_color=wall_color, background_color=background_color, waitTime=0, display=display, scale=scale, square_size=square_size, wall_thickness=wall_thickness)
	return maze, utilities.display_maze(maze, wall_color=wall_color, background_color=background_color)


