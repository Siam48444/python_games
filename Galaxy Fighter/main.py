import pygame 


WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Galaxy Fighter")

BLACK = (0, 0, 0)
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
	WINDOW.fill(BLACK)
	pygame.display.update()	




if __name__ == '__main__':
	main()