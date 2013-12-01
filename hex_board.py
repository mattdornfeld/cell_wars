from math import pi, cos, sin, sqrt
import numpy as np

class HexTile:
	def __init__(self, terrain, axial_coord, center, vertices,
		hex_size):
		
		self.terrain = terrain
		self.axial_coord = axial_coord
		self.center = center 
		self.vertices = vertices
		self.hex_size = hex_size

	def intersects_display(self, origin, window_size):
		self.intersects = False
		for i in range(5):
			v1 = [self.vertices[i, 0], self.vertices[i+1, 1]]
			v2 = [self.vertices[i+1, 0], self.vertices[i, 1]]
			if (v1[0] > origin[0] and v1[0] < origin[0] + window_size[0] and 
				v1[1] > origin[1] and v1[1] < origin[1] + window_size[1]): 
				self.intersects = True
				break
			if (v2[0] > origin[0] and v2[0] < origin[0] + window_size[0] and 
				v2[1] > origin[1] and v2[1] < origin[1] + window_size[1]):
				self.intersects = True
				break

		return self.intersects

def gen_axial_coords(board_size):
	num_rows = board_size[0]
	num_cols = board_size[1]
	axial_coords = []
	for hex_row in range(num_rows):
		for hex_col in range(num_cols):
			axial_coords.append((hex_row, hex_col))

	return axial_coords

def axial_to_pixel(hex_coord, hex_size):
	hex_row = hex_coord[0]
	hex_col = hex_coord[1]
	center_x = hex_size * 1.5 * hex_col
	center_y = hex_size * sqrt(3) * (hex_row + 0.5 * (hex_col%2))

	return [center_x, center_y]

def calc_vertices(center, hex_size):		
	center_x = center[0]
	center_y = center[1]
	vertices = []
	for i in range(0,6):
		theta = 2 * pi / 6 * i
		x_i = center_x + hex_size * cos(theta)
		y_i = center_y + hex_size * sin(theta)
		vertices.append([x_i, y_i])

	return vertices

def gen_board(board_size, hex_size):
	axial_coords = gen_axial_coords(board_size)
	centers = [axial_to_pixel(h, hex_size) for h in axial_coords]
	vertices = [calc_vertices(c, hex_size) for c in centers]

	hex_board = {}
	for h, p, v in zip(axial_coords, centers, vertices):
		hex_board[h] = HexTile('grass', h, p, np.array(v), hex_size)

	return hex_board

if __name__ == '__main__':
	hex_board = gen_board((20,10), 1)





