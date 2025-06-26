import pygame 
import os


WIDTH, HEIGHT = 1000, 800
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 70, 50
SPACESHIP_VELOCITY = 5
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Galaxy Fighter")
BG_COLOR = (255, 255, 255)
FPS = 120

SPACESHIP_YELLOW_IMAGE = pygame.image.load(os.path.join("Assets", "Images", "spaceship_yellow.png"))
SPACESHIP_RED_IMAGE = pygame.image.load(os.path.join("Assets", "Images", "spaceship_red.png"))
SPACESHIP_YELLOW = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_YELLOW_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)
SPACESHIP_RED = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_RED_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)


def main():
	clock = pygame.time.Clock()
	red_spaceship = pygame.Rect(50, (HEIGHT - SPACESHIP_HEIGHT) / 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	yellow_spaceship = pygame.Rect(WIDTH - SPACESHIP_WIDTH - 50, (HEIGHT - SPACESHIP_HEIGHT) / 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

	running = True
	while running:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_w] and red_spaceship.y > 0:
			red_spaceship.y -= SPACESHIP_VELOCITY
		if keys_pressed[pygame.K_s] and red_spaceship.y < HEIGHT - SPACESHIP_WIDTH:
			red_spaceship.y += SPACESHIP_VELOCITY

		draw_window(red_spaceship, yellow_spaceship)

	pygame.quit()


def draw_window(red, yellow):
	WINDOW.fill(BG_COLOR)
	WINDOW.blit(SPACESHIP_RED, (red.x, red.y))
	WINDOW.blit(SPACESHIP_YELLOW, (yellow.x, yellow.y))
	pygame.display.update()	




if __name__ == '__main__':
	main()