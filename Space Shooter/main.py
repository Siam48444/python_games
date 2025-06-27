import pygame
import random
import os
import time
pygame.font.init()



WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Space Shooter")

# Load the images
RED_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
YELLOW_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")) # Player

RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

BG_COLOR = (0, 0, 0)


def main():
	FPS = 90
	clock = pygame.time.Clock()

	level = 1
	lives = 5

	def draw_window():
		WINDOW.fill(BG_COLOR)
		pygame.display.update()

	run = True
	while run:
		clock.tick(FPS)
		draw_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

	pygame.quit()	





if __name__ == '__main__':
	main()