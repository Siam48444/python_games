import pygame 
import os


WIDTH, HEIGHT = 1000, 800
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 50
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Galaxy Fighter")

SPACESHIP_YELLOW_IMAGE = pygame.image.load(os.path.join("Assets", "Images", "spaceship_yellow.png"))
SPACESHIP_RED_IMAGE = pygame.image.load(os.path.join("Assets", "Images", "spaceship_red.png"))

SPACESHIP_YELLOW = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_YELLOW_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
SPACESHIP_RED = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_RED_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)

BG_COLOR = (255, 255, 255)
FPS = 60


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
	WINDOW.blit(SPACESHIP_YELLOW, (0, 0))
	WINDOW.blit(SPACESHIP_RED, (WIDTH - 100, 0))
	pygame.display.update()	




if __name__ == '__main__':
	main()