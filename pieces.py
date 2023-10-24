from PIL import Image
from utilities import get_cell_wall_status

# create each of the squares





# '   ' no walls
def wall_id15(size=3, color=(0,0,0,255), wallThickness=1):
	blank = Image.new("RGBA", (size, size), (255, 255, 255, 0))
	return blank


# '▔▔' top wall
def wall_id14(size=3, color=(0,0,0,255), wallThickness=1):
	wall = Image.new("RGBA", (size, wallThickness), color)
	base = wall_id15(size)
	base.alpha_composite(wall, (0, 0), (0,0))
	return base


# '  |' right wall
def wall_id13(size=3, color=(0,0,0,255), wallThickness=1):
	wall = Image.new("RGBA", (wallThickness, size), color)
	base = wall_id15(size)
	base.alpha_composite(wall, (size-wallThickness, 0))
	return base



# '▔▔|' top and right wall
def wall_id12(size=3, color=(0,0,0,255), wallThickness=1):
	top = wall_id14(size, color, wallThickness)
	right = wall_id13(size, color, wallThickness)
	img = Image.alpha_composite(top, right)
	return img


# '___' bottom wall
def wall_id11(size=3, color=(0,0,0,255), wallThickness=1):
	wall = Image.new("RGBA", (size, wallThickness), color)
	base = wall_id15(size)
	base.alpha_composite(wall, (0, size-wallThickness))
	return base


# 'ニニ' top and bottom wall
def wall_id10(size=3, color=(0,0,0,255), wallThickness=1):
	top = wall_id14(size, color, wallThickness)
	bottom = wall_id11(size, color, wallThickness)
	img = Image.alpha_composite(top, bottom)
	return img


# '__│' right and bottom wall
def wall_id9(size=3, color=(0,0,0,255), wallThickness=1):
	right = wall_id13(size, color, wallThickness)
	bottom = wall_id11(size, color, wallThickness)
	img = Image.alpha_composite(right, bottom)
	return img


# 'ニニ|' top, right, and bottom wall
def wall_id8(size=3, color=(0,0,0,255), wallThickness=1):
	top = wall_id14(size, color, wallThickness)
	right = wall_id13(size, color, wallThickness)
	bottom = wall_id11(size, color, wallThickness)
	img = Image.alpha_composite(top, right)
	img = Image.alpha_composite(img, bottom)
	return img


# '|  ' left wall
def wall_id7(size=3, color=(0,0,0,255), wallThickness=1):
	wall = Image.new("RGBA", (wallThickness, size), color)
	base = wall_id15(size)
	base.alpha_composite(wall, (0, 0))
	return base


# '|▔▔' top and left wall
def wall_id6(size=3, color=(0,0,0,255), wallThickness=1):
	top = wall_id14(size, color, wallThickness)
	left = wall_id7(size, color, wallThickness)
	img = Image.alpha_composite(top, left)
	return img

# '| |' left and right wall
def wall_id5(size=3, color=(0,0,0,255), wallThickness=1):
	left = wall_id7(size, color, wallThickness)
	right = wall_id13(size, color, wallThickness)
	img = Image.alpha_composite(left, right)
	return img


# '|▔|' left, top, and right wall
def wall_id4(size=3, color=(0,0,0,255), wallThickness=1):
	left = wall_id7(size, color, wallThickness)
	top = wall_id14(size, color, wallThickness)
	right = wall_id13(size, color, wallThickness)
	img = Image.alpha_composite(left, top)
	img = Image.alpha_composite(img, right)
	return img


# '|__' left and bottom wall
def wall_id3(size=3, color=(0,0,0,255), wallThickness=1):
	left = wall_id7(size, color, wallThickness)
	bottom = wall_id11(size, color, wallThickness)
	img = Image.alpha_composite(left, bottom)
	return img


# '|ニニ' left, top, and bottom wall
def wall_id2(size=3, color=(0,0,0,255), wallThickness=1):
	left = wall_id7(size, color, wallThickness)
	top = wall_id14(size, color, wallThickness)
	bottom = wall_id11(size, color, wallThickness)
	img = Image.alpha_composite(left, top)
	img = Image.alpha_composite(img, bottom)
	return img


# '|_|' left, bottom, and right wall
def wall_id1(size=3, color=(0,0,0,255), wallThickness=1):
	left = wall_id7(size, color, wallThickness)
	bottom = wall_id11(size, color, wallThickness)
	right = wall_id13(size, color, wallThickness)
	img = Image.alpha_composite(left, bottom)
	img = Image.alpha_composite(img, right)
	return img

# solid walls, aka filled in
def wall_id0(size=3, color=(0,0,0,255), wallThickness=1):
	wall = Image.new("RGBA", (size, size), (0, 0, 0, 255))
	return wall



