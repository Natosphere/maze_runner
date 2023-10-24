import generation_algorithms.wilson_algo as wilson_algo
import pieces
import utilities
import numpy as np


### utilities tests

def test_get_cell_wall_status():

	# FULL WALL
	cell1 = 0
	north_wall, east_wall, south_wall, west_wall = utilities.get_cell_wall_status(cell1)
	assert north_wall == True
	assert east_wall == True
	assert south_wall == True
	assert west_wall == True

	# NORTH WALL
	cell2 = 1
	north_wall, east_wall, south_wall, west_wall = utilities.get_cell_wall_status(cell2)
	assert north_wall == False
	assert east_wall == True
	assert south_wall == True
	assert west_wall == True

	# EAST WALL
	cell3 = 2
	north_wall, east_wall, south_wall, west_wall = utilities.get_cell_wall_status(cell3)
	assert north_wall == True
	assert east_wall == False
	assert south_wall == True
	assert west_wall == True

	# SOUTH WALL
	cell4 = 4
	north_wall, east_wall, south_wall, west_wall = utilities.get_cell_wall_status(cell4)
	assert north_wall == True
	assert east_wall == True
	assert south_wall == False
	assert west_wall == True

	# WEST WALL
	cell5 = 8
	north_wall, east_wall, south_wall, west_wall = utilities.get_cell_wall_status(cell5)
	assert north_wall == True
	assert east_wall == True
	assert south_wall == True
	assert west_wall == False

	# NO WALL
	cell6 = 15
	north_wall, east_wall, south_wall, west_wall = utilities.get_cell_wall_status(cell6)
	assert north_wall == False
	assert east_wall == False
	assert south_wall == False
	assert west_wall == False

	# NORTH EAST WALL
	cell7 = 3
	north_wall, east_wall, south_wall, west_wall = utilities.get_cell_wall_status(cell7)
	assert north_wall == False
	assert east_wall == False
	assert south_wall == True
	assert west_wall == True

	# NORTH SOUTH WALL
	cell8 = 5
	north_wall, east_wall, south_wall, west_wall = utilities.get_cell_wall_status(cell8)
	assert north_wall == False
	assert east_wall == True
	assert south_wall == False
	assert west_wall == True

	# SOUTH WEST WALL
	cell9 = 12
	north_wall, east_wall, south_wall, west_wall = utilities.get_cell_wall_status(cell9)
	assert north_wall == True
	assert east_wall == True
	assert south_wall == False
	assert west_wall == False


def test_remove_walls():

	# start with all walls
	cell1 = 0
	# remove north wall
	cell1 = utilities.remove_walls(cell1, north=True)
	north_wall, east_wall, south_wall, west_wall = utilities.get_cell_wall_status(cell1)

	assert north_wall == False
	assert east_wall == True
	assert south_wall == True
	assert west_wall == True

	# start with west and east walls
	cell2 = 5
	# remove east wall
	cell2 = utilities.remove_walls(cell2, east=True)
	north_wall, east_wall, south_wall, west_wall = utilities.get_cell_wall_status(cell2)
	assert north_wall == False
	assert east_wall == False
	assert south_wall == False
	assert west_wall == True


def test_cell_img_creator_WALLS():

	# FULL WALL TEST
	cell1_value = 0
	size = 10

	cell1_img = utilities.cell_img_creator(cell1_value, size=size)

	assert cell1_img.width == cell1_img.height
	assert cell1_img.size == (size,size)
	
	w = cell1_img.width-1
	h = cell1_img.height-1

	assert cell1_img.mode == "RGBA"
	assert cell1_img.getpixel((0,0)) == (0,0,0,255)
	assert cell1_img.getpixel((w/2,h/2)) == (0,0,0,255)
	# check top wall
	assert cell1_img.getpixel((w/2,0)) == (0,0,0,255)
	# check right wall
	assert cell1_img.getpixel((w,h/2)) == (0,0,0,255)
	# check bottom wall
	assert cell1_img.getpixel((w/2,h)) == (0,0,0,255)
	# check left wall
	assert cell1_img.getpixel((0,h/2)) == (0,0,0,255)


	# NORTH WALL TEST
	cell2_value = 14
	size = 10

	cell2_img = utilities.cell_img_creator(cell2_value, size=size)
	assert cell2_img.width == cell2_img.height
	assert cell2_img.size == (size,size)
	
	w = cell2_img.width-1
	h = cell2_img.height-1

	assert cell2_img.mode == "RGBA"
	assert cell2_img.getpixel((w/2,h/2)) == (0,0,0,0)
	# check north wall
	assert cell2_img.getpixel((w/2,0)) == (0,0,0,255)
	# check east wall
	assert cell2_img.getpixel((w,h/2)) == (0,0,0,0)
	# check south wall
	assert cell2_img.getpixel((w/2,h)) == (0,0,0,0)
	# check west wall
	assert cell2_img.getpixel((0,h/2)) == (0,0,0,0)



	# EAST WALL TEST
	cell3_value = 13
	size = 10

	cell3_img = utilities.cell_img_creator(cell3_value, size=size)
	assert cell3_img.width == cell3_img.height
	assert cell3_img.size == (size,size)
	
	w = cell3_img.width-1
	h = cell3_img.height-1

	assert cell3_img.mode == "RGBA"
	assert cell3_img.getpixel((w/2,h/2)) == (0,0,0,0)
	# check north wall
	assert cell3_img.getpixel((w/2,0)) == (0,0,0,0)
	# check east wall
	assert cell3_img.getpixel((w,h/2)) == (0,0,0,255)
	# check south wall
	assert cell3_img.getpixel((w/2,h)) == (0,0,0,0)
	# check west wall
	assert cell3_img.getpixel((0,h/2)) == (0,0,0,0)


	
	# SOUTH WALL TEST
	cell3_value = 11
	size = 10

	cell3_img = utilities.cell_img_creator(cell3_value, size=size)
	assert cell3_img.width == cell3_img.height
	assert cell3_img.size == (size,size)
	
	w = cell3_img.width-1
	h = cell3_img.height-1

	assert cell3_img.mode == "RGBA"
	assert cell3_img.getpixel((w/2,h/2)) == (0,0,0,0)
	# check north wall
	assert cell3_img.getpixel((w/2,0)) == (0,0,0,0)
	# check east wall
	assert cell3_img.getpixel((w,h/2)) == (0,0,0,0)
	# check south wall
	assert cell3_img.getpixel((w/2,h)) == (0,0,0,255)
	# check west wall
	assert cell3_img.getpixel((0,h/2)) == (0,0,0,0)	


	# WEST WALL TEST
	cell3_value = 7
	size = 10

	cell3_img = utilities.cell_img_creator(cell3_value, size=size)
	assert cell3_img.width == cell3_img.height
	assert cell3_img.size == (size,size)
	
	w = cell3_img.width-1
	h = cell3_img.height-1

	assert cell3_img.mode == "RGBA"
	assert cell3_img.getpixel((w/2,h/2)) == (0,0,0,0)
	# check north wall
	assert cell3_img.getpixel((w/2,0)) == (0,0,0,0)
	# check east wall
	assert cell3_img.getpixel((w,h/2)) == (0,0,0,0)
	# check south wall
	assert cell3_img.getpixel((w/2,h)) == (0,0,0,0)
	# check west wall
	assert cell3_img.getpixel((0,h/2)) == (0,0,0,255)

	
def test_cell_img_creator_COLOR():
	
	cell3_value = 11
	size = 10
	color = (255,0,0,255)

	cell3_img = utilities.cell_img_creator(cell3_value, size=size, color=color)
	assert cell3_img.width == cell3_img.height
	assert cell3_img.size == (size,size)
	
	w = cell3_img.width-1
	h = cell3_img.height-1

	assert cell3_img.mode == "RGBA"
	assert cell3_img.getpixel((w/2,h/2)) == (0,0,0,0)
	# check north wall
	assert cell3_img.getpixel((w/2,0)) == (0,0,0,0)
	# check east wall
	assert cell3_img.getpixel((w,h/2)) == (0,0,0,0)
	# check south wall
	assert cell3_img.getpixel((w/2,h)) == color
	# check west wall
	assert cell3_img.getpixel((0,h/2)) == (0,0,0,0)	


def test_cell_img_creator_THICKNESS():
	
	# average wall thinckness test
	cell3_value = 7
	size = 10
	wall_thickness = 4

	cell3_img = utilities.cell_img_creator(cell3_value, size=size, wall_thickness=wall_thickness)
	assert cell3_img.width == cell3_img.height
	assert cell3_img.size == (size,size)
	
	w = cell3_img.width-1
	h = cell3_img.height-1


	assert cell3_img.mode == "RGBA"
	assert cell3_img.getpixel((w/2,h/2)) == (0,0,0,0)
	# check north wall
	assert cell3_img.getpixel((w/2,0)) == (0,0,0,0)
	assert cell3_img.getpixel((w/2,0+wall_thickness-1)) == (0,0,0,0)
	# check east wall
	assert cell3_img.getpixel((w,h/2)) == (0,0,0,0)
	assert cell3_img.getpixel((w-wall_thickness+1,h/2)) == (0,0,0,0)
	# check south wall
	assert cell3_img.getpixel((w/2,h)) == (0,0,0,0)
	assert cell3_img.getpixel((w/2,h-wall_thickness+1)) == (0,0,0,0)
	# check west wall
	assert cell3_img.getpixel((0,h/2)) == (0,0,0,255)
	assert cell3_img.getpixel((0+wall_thickness-1,h/2)) == (0,0,0,255)


	# extreme wall thickness test
	cell_value = 1
	size = 100
	wall_thickness = 49

	cell_img = utilities.cell_img_creator(cell_value, size=size, wall_thickness=wall_thickness)
	assert cell_img.width == cell_img.height
	assert cell_img.size == (size,size)
	
	w = cell_img.width-1
	h = cell_img.height-1


	assert cell_img.mode == "RGBA"
	assert cell_img.getpixel((w/2,h/2)) == (0,0,0,0)
	# check north wall
	assert cell_img.getpixel((w/2,0)) == (0,0,0,0)
	assert cell_img.getpixel((w/2,0+wall_thickness-1)) == (0,0,0,0)
	# check east wall
	assert cell_img.getpixel((w,h/2)) == (0,0,0,255)
	assert cell_img.getpixel((w-wall_thickness+1,h/2)) == (0,0,0,255)
	# check south wall
	assert cell_img.getpixel((w/2,h)) == (0,0,0,255)
	assert cell_img.getpixel((w/2,h-wall_thickness+1)) == (0,0,0,255)
	# check west wall
	assert cell_img.getpixel((0,h/2)) == (0,0,0,255)
	assert cell_img.getpixel((0+wall_thickness-1,h/2)) == (0,0,0,255)


def test_add_path():



	# SIMPLE PATH TEST1
	maze1 = np.array([
		[[0],[0],[0]],
		[[0],[0],[0]],
		[[0],[0],[0]]
	])
	path1 = ([0,1],[1,1],[2,1])
	result1 = utilities.add_path(maze1, path1)
	expected_result1 = np.array([
		[[0],[0],[0]],
		[[2],[10],[8]],
		[[0],[0],[0]]
	])
	assert np.array_equal(result1, expected_result1)



	# SIMPLE PATH TEST2
	maze3 = np.array([
		[[0],[0],[0]],
		[[0],[0],[0]],
		[[0],[0],[0]]
	])
	path3 = ([0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0],[1,1])
	result3 = utilities.add_path(maze3, path3)
	expected_result3 = np.array([
		[[4],[6],[12]],
		[[5],[1],[5]],
		[[3],[10],[9]]
	])
	assert np.array_equal(result3, expected_result3)



	# COMPLEX PATH TEST
	maze2 = np.array([
		[[0],[0],[0],[0],[0]],
		[[0],[0],[0],[0],[0]],
		[[0],[0],[0],[0],[0]],
		[[0],[0],[0],[0],[0]],
		[[0],[0],[0],[0],[0]]
	])
	path2 = ([4,1],[4,0],[3,0],[2,0],[2,1],[2,2],[2,3],[3,3],[4,3],[4,4])
	result2 = utilities.add_path(maze2, path2)
	expected_result2 = np.array([
		[[0],[0],[6],[10],[12]],
		[[0],[0],[5],[0],[1]],
		[[0],[0],[5],[0],[0]],
		[[0],[0],[3],[10],[12]],
		[[0],[0],[0],[0],[1]]
	])
	assert np.array_equal(result2, expected_result2)


def test_add_path_EXISTNG_CELL_CONNECTION():

	# EXISTING CELL CONNECTION TEST
	maze4 = np.array([
		[[0],[2],[12]],
		[[0],[0],[1]],
		[[0],[0],[0]]
	])
	path4 = ([0,2],[1,2],[2,2],[2,1])
	result4 = utilities.add_path(maze4, path4)
	expected_result4 = np.array([
		[[0],[2],[12]],
		[[0],[0],[5]],
		[[2],[10],[9]]
	])
	assert np.array_equal(result4, expected_result4)



def test_get_empty_neighbors():


	maze = np.array([
		[0,2,0],
		[0,1,1],
		[0,0,0]
	])

	result = utilities.get_empty_neighbors(maze, (1,1))
	expected_result = [(1,2),(0,1)]
	assert result == expected_result


	result2 = utilities.get_empty_neighbors(maze, (1,2))
	expected_result2 = [(2,2),(0,2)]
	assert result2 == expected_result2


	maze2 = np.array([
		[0,2,0],
		[7,1,1],
		[0,5,0]
	])

	result3 = utilities.get_empty_neighbors(maze2, (1,1))
	expected_result3 = []
	assert result3 == expected_result3


	result4 = utilities.get_empty_neighbors(maze2, (1,2))
	expected_result4 = [(2,2),(0,2)]
	assert result4 == expected_result4

	maze3 = np.array([
		[0,2,0,3,1,4],
		[7,1,1,9,0,5],
		[0,5,0,1,0,0]
	])

	result5 = utilities.get_empty_neighbors(maze3, (5,1))
	expected_result5 = [(5,2),(4,1)]
	assert result5 == expected_result5


	result6 = utilities.get_empty_neighbors(maze3, (1,2))
	expected_result6 = [(2,2),(0,2)]
	assert result6 == expected_result6

# def test_display_maze():
# 	pass



### wilson algorithm test

# def test_wilson_algorithm():
# 	size = [5,5]
# 	seed = 1
