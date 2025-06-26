import pygame 
import os


WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Galaxy Fighter")

BG_COLOR = (255, 255, 255)
FPS = 60

SPACESHIP_YELLOW_IMAGE = pygame.image.load(os.path.join("Assets", "Images", "spaceship_yellow.png"))
SPACESHIP_RED_IMAGE = pygame.image.load(os.path.join("Assets", "Images", "spaceship_red.png"))

SPACESHIP_YELLOW = pygame.transform.scale(SPACESHIP_YELLOW_IMAGE, (55, 50))
SPACESHIP_RED = pygame.transform.scale(SPACESHIP_RED_IMAGE, (55, 50))


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
	WINDOW.blit(SPACESHIP_RED, (0, 0))
	pygame.display.update()	




if __name__ == '__main__':
	main()