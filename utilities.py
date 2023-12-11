import numpy as np
import cv2
from PIL import Image



def get_empty_cells(maze):
		# find all empty cells
		empty_cells = [(location[1], location[0]) for location in np.argwhere(maze == 0)]
		empty_cells = sorted(empty_cells, key=lambda loc: (loc[0], loc[1]))
		return empty_cells


def get_empty_neighbors(maze, cell):
	size = (maze.shape[1], maze.shape[0])


	north_n = (cell[0], cell[1]-1)
	east_n = (cell[0]+1, cell[1])
	south_n = (cell[0], cell[1]+1)
	west_n = (cell[0]-1, cell[1])
	neighbors = [north_n, east_n, south_n, west_n]
	


	result = []
	for neighbor in neighbors:
		# prevent out of bounds
		if 0 <= neighbor[0] < size[0] and 0 <= neighbor[1] < size[1]:
			if maze[neighbor[1], neighbor[0]] == 0:
				result.append(neighbor)

	return result


# returns a list of bools of walls the cell has. True == has_wall
def get_cell_wall_status(cell_value):
	north_wall = cell_value % 2 == 0
	east_wall = (cell_value // 2) % 2 == 0
	south_wall = (cell_value // 4) % 2 == 0
	west_wall = (cell_value // 8) % 2 == 0

	return north_wall, east_wall, south_wall, west_wall


# generates the cell image
def cell_img_creator(cell_value, size=3, color=(0,0,0,255), wall_thickness=1, background_color=(0, 0, 0, 0)):
	north_wall, east_wall, south_wall, west_wall = get_cell_wall_status(cell_value)

	# if cell is empty, return blacked out cell
	if cell_value == 0:
		return Image.new("RGBA", (size, size), color)
	
	# blank canvas
	base = Image.new("RGBA", (size, size), background_color)

	# add walls as needed
	if north_wall:
		wall = Image.new("RGBA", (size, wall_thickness), color)
		base.alpha_composite(wall, (0, 0), (0,0))
	if east_wall:
		wall = Image.new("RGBA", (wall_thickness, size), color)
		base.alpha_composite(wall, (size-wall_thickness, 0))
	if south_wall:
		wall = Image.new("RGBA", (size, wall_thickness), color)
		base.alpha_composite(wall, (0, size-wall_thickness))
	if west_wall:
		wall = Image.new("RGBA", (wall_thickness, size), color)
		base.alpha_composite(wall, (0, 0))
	
	return base


# adds a path to the maze, aka removes walls between cells in the path list
def add_path(maze, path):
	# print(f"path: {path}")

	for i in range(len(path)):
		# skip first loop, skip last loop
		if i == 0: continue

		previous = path[i-1]
		current = path[i]

		# check path direction between previous and current, then remove walls between them
	
		# check if north
		if previous[1] > current[1]:
			maze[previous[1]][previous[0]] = remove_walls(maze[previous[1]][previous[0]], north=True)
			maze[current[1]][current[0]] = remove_walls(maze[current[1]][current[0]], south=True)
		# check if east
		if previous[0] < current[0]:
			maze[previous[1]][previous[0]] = remove_walls(maze[previous[1]][previous[0]], east=True)
			maze[current[1]][current[0]] = remove_walls(maze[current[1]][current[0]], west=True)
		# check if south
		if previous[1] < current[1]:
			maze[previous[1]][previous[0]] = remove_walls(maze[previous[1]][previous[0]], south=True)
			maze[current[1]][current[0]] = remove_walls(maze[current[1]][current[0]], north=True)
		# check if west
		if previous[0] > current[0]:
			maze[previous[1]][previous[0]] = remove_walls(maze[previous[1]][previous[0]], west=True)
			maze[current[1]][current[0]] = remove_walls(maze[current[1]][current[0]], east=True)


	return maze


# modifies the the cell value to remove the walls, then returns the new cell value
def remove_walls(cell_value, west=False, east=False, north=False, south=False):

	if north:
		cell_value += 1
	if east:
		cell_value += 2
	if south:
		cell_value += 4
	if west:
		cell_value += 8

	return cell_value




def display_image(img, title, scale, waitTime):
	img = cv2.resize(img, (img.shape[1]*scale, img.shape[0]*scale), interpolation = cv2.INTER_NEAREST)
	cv2.imshow(title, img)
	cv2.waitKey(waitTime)



def display_maze(maze, wall_color=(0,0,0,255), background_color=(255,255,255,255), wall_thickness=1, square_size=6, title="maze", scale=3, display=False, waitTime=500, dest_cell=(-1,-1)):
	maze_x = (maze.shape[0] * square_size) - ((maze.shape[0] * wall_thickness) - 1)
	maze_y = (maze.shape[1] * square_size) - ((maze.shape[1] * wall_thickness) - 1)
	maze_img = Image.new("RGBA", (maze_y, maze_x), background_color)

	# display the base maze
	for row in range(maze.shape[0]):
		for col in range(maze.shape[1]):

			# calculates where the current square should go
			if col != 0:
				current_x = (col * square_size) - wall_thickness * col
			else:
				current_x = col * square_size
			if row != 0:
				current_y = (row * square_size) - wall_thickness * row
			else:
				current_y = row * square_size



			# generate the square, display the destination cell
			if row == dest_cell[1] and col == dest_cell[0]:
				current_cell = cell_img_creator(maze[row][col], size=square_size, color=background_color, wall_thickness=wall_thickness)
			else:
				current_cell = cell_img_creator(maze[row][col], size=square_size, color=wall_color, wall_thickness=wall_thickness)

			# slice and replace the squares of the maze
			maze_img.alpha_composite(current_cell, (current_x, current_y))
			# print(row, col)
	
	if display:
		# maze_img.resize((maze_img.size[1]*scale, maze_img.size[0]*scale), resample=Image.NEAREST)
		opencvImage = cv2.cvtColor(np.array(maze_img), cv2.COLOR_RGB2BGR)
		opencvImage = cv2.resize(opencvImage, (opencvImage.shape[1]*scale, opencvImage.shape[0]*scale), interpolation = cv2.INTER_NEAREST)
		cv2.imshow(title, opencvImage)
		cv2.waitKey(waitTime)

	return maze_img



def display_path(img_base, path, color=(127,127,127,255), background_color=(127,127,127,255), wall_thickness=1, square_size=6, title="maze", scale=4,  waitTime=100, display=False, display_stepped=False):
	img_copy = img_base.copy()


	for col,row in path:
		# generate the square
		current_cell = cell_img_creator(0, size=square_size, color=color, wall_thickness=wall_thickness, background_color=background_color)

		# calculates where the current square should go
		if col != 0:
			current_x = (col * square_size) - wall_thickness * col
		else:
			current_x = col * square_size
		if row != 0:
			current_y = (row * square_size) - wall_thickness * row
		else:
			current_y = row * square_size

	
		
		# slice and replace the squares of the maze
		img_copy.alpha_composite(current_cell, (current_x, current_y))

		if display and display_stepped:
			opencvImage = cv2.cvtColor(np.array(img_copy), cv2.COLOR_RGB2BGR)
			opencvImage = cv2.resize(opencvImage, (opencvImage.shape[1]*scale, opencvImage.shape[0]*scale), interpolation = cv2.INTER_NEAREST)
			cv2.imshow(title, opencvImage)
			cv2.waitKey(waitTime)

	if display and not display_stepped:
			opencvImage = cv2.cvtColor(np.array(img_copy), cv2.COLOR_RGB2BGR)
			opencvImage = cv2.resize(opencvImage, (opencvImage.shape[1]*scale, opencvImage.shape[0]*scale), interpolation = cv2.INTER_NEAREST)
			cv2.imshow(title, opencvImage)
			cv2.waitKey(waitTime)
	return opencvImage