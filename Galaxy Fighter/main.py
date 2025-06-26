import pygame 
import os


WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Galaxy Fighter")

BG_COLOR = (255, 255, 255)
FPS = 60

SPACESHIP_YELLOW = pygame.image.load(os.path.join("Assets", "Images", "spaceship_yellow.png"))
SPACESHIP_RED = pygame.image.load(os.path.join("Assets", "Images", "spaceship_red.png"))


def main():
	clock = pygame.time.Clock()

	running = True
	while running:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		draw_window()

	pygame.quit()


def draw_window():
	WINDOW.fill(BG_COLOR)
	pygame.display.update()	




if __name__ == '__main__':
	main()