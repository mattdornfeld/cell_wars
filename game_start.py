import pygame
import sys
from pygame.locals import *
from math import sqrt, ceil
from hex_board import *
import numpy as np
from IPython import embed
import cProfile


WIN_WIDTH = 800
WIN_HEIGHT = 640
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
 
# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

HEX_SIZE = 50
HEX_WIDTH = 2 * HEX_SIZE
HEX_HEIGHT = sqrt(3) * HEX_SIZE
BOARD_SIZE = (30, 30) #(rows, columns)
BOARD_WIDTH  = HEX_WIDTH * 0.75 * (BOARD_SIZE[1] - 1)
BOARD_HEIGHT = HEX_HEIGHT * BOARD_SIZE[0]  

def quit_checker(event):
	if event.type == QUIT:
		pygame.quit()
		sys.exit()

def key_scroll_checker(event):
	x_vel = 0
	y_vel = 0
	if event.type == KEYDOWN and event.key == K_UP:
		y_vel = -BOARD_HEIGHT / 20			
	if event.type == KEYDOWN and event.key == K_DOWN:
		y_vel = BOARD_HEIGHT / 20			
	if event.type == KEYDOWN and event.key == K_LEFT:
		x_vel = -BOARD_WIDTH / 20		
	if event.type == KEYDOWN and event.key == K_RIGHT:
		x_vel = BOARD_WIDTH / 20

	return x_vel, y_vel

def update_origin(origin, x_vel, y_vel, window_size):

	origin[0] += x_vel
	origin[1] += y_vel
	if origin[0] < 0: origin[0] = 0
	if origin[1] < 0: origin[1] = 0
	if origin[0] > BOARD_WIDTH - window_size[0]:
		origin[0] = BOARD_WIDTH - window_size[0]
	if origin[1] > BOARD_HEIGHT - window_size[1]: 
		origin[1] = BOARD_HEIGHT - window_size[1]
	
	return origin

def draw_board(surface, hex_board, origin, window_size):
	surface.fill(BLACK)
	for _, tile in hex_board.iteritems():
		intersects = tile.intersects_display(origin, window_size)
		if intersects:
			pygame.draw.polygon(surface, GREEN, tile.vertices - origin , 2)


def main():
	hex_board = gen_board(BOARD_SIZE, HEX_SIZE)
	origin = [0, 0]
	pygame.init()
	surface = pygame.display.set_mode((0,0), 0, 32)
	window_size = surface.get_size()
	draw_board(surface, hex_board, origin, window_size)
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			quit_checker(event)
			x_vel, y_vel = key_scroll_checker(event)

		origin = update_origin(origin, x_vel, y_vel, window_size)
		draw_board(surface, hex_board, origin, window_size)
		pygame.display.update()

if __name__ == '__main__':
	cProfile.run('main()')

