import pygame 
import os
pygame.font.init()


WIDTH, HEIGHT = 1000, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Galaxy Fighter")

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 70, 50
SPACESHIP_VELOCITY = 5

SPACESHIP_YELLOW_IMAGE = pygame.image.load(os.path.join("Assets", "Images", "spaceship_yellow.png"))
SPACESHIP_RED_IMAGE = pygame.image.load(os.path.join("Assets", "Images", "spaceship_red.png"))
SPACESHIP_YELLOW = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_YELLOW_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), -90)
SPACESHIP_RED = pygame.transform.rotate(pygame.transform.scale(SPACESHIP_RED_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

MIDDLE_BAR_COLOR = (0, 0, 0)
MIDDLE_BAR_THICKNESS = 3
MIDDLE_BAR = pygame.Rect((WIDTH - MIDDLE_BAR_THICKNESS) // 2, 0, MIDDLE_BAR_THICKNESS, HEIGHT)

BULLET_WIDTH, BULLET_HEIGHT = 20, 10
BULLET_VELOCITY = 10
MAX_BULLETS = 3

BG_COLOR = (255, 255, 255)
RED_COLOR = (255, 0, 0)
YELLOW_COLOR = (222, 255, 0)
FPS = 120
MAX_HEALTH = 5

SCORE_FONT = pygame.font.SysFont('Arial', 30)
LOST_FONT = pygame.font.SysFont('Arial', 80)


def main():
	clock = pygame.time.Clock()
	red_spaceship = pygame.Rect(50, (HEIGHT - SPACESHIP_HEIGHT) / 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	yellow_spaceship = pygame.Rect(WIDTH - SPACESHIP_WIDTH - 50, (HEIGHT - SPACESHIP_HEIGHT) / 2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
	red_bullets = []
	yellow_bullets = []
	red_health = MAX_HEALTH
	yellow_health = MAX_HEALTH
	
	running = True
	while running:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
					bullet = pygame.Rect(
						yellow_spaceship.x, 
						yellow_spaceship.y + yellow_spaceship.height / 2 + BULLET_HEIGHT / 2, 
						BULLET_WIDTH, BULLET_HEIGHT
					)
					yellow_bullets.append(bullet)
				if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
					bullet = pygame.Rect(
						red_spaceship.x + red_spaceship.width - BULLET_WIDTH * 2, 
						red_spaceship.y + red_spaceship.height / 2 + BULLET_HEIGHT / 2, 
						BULLET_WIDTH, BULLET_HEIGHT
					)
					red_bullets.append(bullet)

		keys_pressed = pygame.key.get_pressed()
		red_movement(keys_pressed, red_spaceship)
		yellow_movement(keys_pressed, yellow_spaceship)

		red_health, yellow_health = handle_bullets(
			red_bullets, yellow_bullets, red_spaceship, yellow_spaceship, red_health, yellow_health
		)

		draw_window(red_spaceship, yellow_spaceship, red_bullets, yellow_bullets, red_health, yellow_health)

		if red_health <= 0:
			draw_winner("Yellow Wins!")
			break
		elif yellow_health <= 0:
			draw_winner("Red Wins!")
			break

	pygame.quit()


def red_movement(keys_pressed, red):
	if keys_pressed[pygame.K_w] and red.y > 0:
		red.y -= SPACESHIP_VELOCITY
	if keys_pressed[pygame.K_s] and red.y < HEIGHT - SPACESHIP_WIDTH:
		red.y += SPACESHIP_VELOCITY
	if keys_pressed[pygame.K_a] and red.x > 0:
		red.x -= SPACESHIP_VELOCITY
	if keys_pressed[pygame.K_d] and red.x < (WIDTH / 2) - SPACESHIP_HEIGHT:
		red.x += SPACESHIP_VELOCITY


def yellow_movement(keys_pressed, yellow):
	if keys_pressed[pygame.K_UP] and yellow.y > 0:
		yellow.y -= SPACESHIP_VELOCITY
	if keys_pressed[pygame.K_DOWN] and yellow.y < HEIGHT - SPACESHIP_WIDTH:
		yellow.y += SPACESHIP_VELOCITY
	if keys_pressed[pygame.K_LEFT] and yellow.x > WIDTH / 2:
		yellow.x -= SPACESHIP_VELOCITY
	if keys_pressed[pygame.K_RIGHT] and yellow.x < WIDTH - SPACESHIP_HEIGHT:
		yellow.x += SPACESHIP_VELOCITY


def handle_bullets(red_bullets, yellow_bullets, red, yellow, red_health, yellow_health):
	for bullet in red_bullets[:]:
		bullet.x += BULLET_VELOCITY
		if yellow.colliderect(bullet):
			red_bullets.remove(bullet)
			yellow_health -= 1
		elif bullet.x > WIDTH:
			red_bullets.remove(bullet)

	for bullet in yellow_bullets[:]:
		bullet.x -= BULLET_VELOCITY
		if red.colliderect(bullet):
			yellow_bullets.remove(bullet)
			red_health -= 1
		elif bullet.x < 0:
			yellow_bullets.remove(bullet)

	return red_health, yellow_health


def draw_winner(text):
	win_text = LOST_FONT.render(text, True, (0, 0, 0))
	WINDOW.blit(win_text, ((WIDTH - win_text.get_width()) / 2, (HEIGHT - win_text.get_height()) / 2))
	pygame.display.update()
	pygame.time.delay(3000)


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
	WINDOW.fill(BG_COLOR)
	WINDOW.blit(SPACESHIP_RED, (red.x, red.y))
	WINDOW.blit(SPACESHIP_YELLOW, (yellow.x, yellow.y))
	pygame.draw.rect(WINDOW, MIDDLE_BAR_COLOR, MIDDLE_BAR)

	for bullet in red_bullets:
		pygame.draw.rect(WINDOW, RED_COLOR, bullet)
	for bullet in yellow_bullets:
		pygame.draw.rect(WINDOW, YELLOW_COLOR, bullet)

	red_health_text = SCORE_FONT.render(f"Health: {red_health}", True, RED_COLOR)
	yellow_health_text = SCORE_FONT.render(f"Health: {yellow_health}", True, YELLOW_COLOR)
	WINDOW.blit(red_health_text, (10, 10))
	WINDOW.blit(yellow_health_text, (WIDTH - yellow_health_text.get_width() - 10, 10))

	pygame.display.update()	




if __name__ == '__main__':
	main()