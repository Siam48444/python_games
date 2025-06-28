import pygame
import random
import os
import time
pygame.font.init()



WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Space Shooter")

PLAYER_VELOCITY = 5
PLAYER_WIDTH, PLAYER_HEIGHT = 70, 70

RED_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACESHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
YELLOW_SPACESHIP = pygame.transform.scale(
	pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png")), (PLAYER_WIDTH, PLAYER_HEIGHT)
)

RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

BG_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
MAIN_FONT = pygame.font.SysFont("Arial", 30)
FPS = 90


class Ship():
	def __init__(self, x, y, health=100):
		self.x = x
		self.y = y
		self.health = health
		self.ship_img = None
		self.laser_img = None
		self.lasers = []
		self.cool_down_counter = 0

	def draw(self, window):
		window.blit(self.ship_img, (self.x, self.y))


class Player(Ship):
	def __init__(self, x, y, health=100):
		super().__init__(x, y, health)
		self.ship_img = YELLOW_SPACESHIP
		self.laser_img = YELLOW_LASER
		self.mask = pygame.mask.from_surface(self.ship_img)
		self.max_health = health


class Enemy(Ship):
	COLOR_MAP = {
		"red": (RED_SPACESHIP, RED_LASER),
		"green": (GREEN_SPACESHIP, GREEN_LASER),
		"blue": (BLUE_SPACESHIP, BLUE_LASER),
	}

	def __init__(self, x, y, color, health=100):
		super().__init__(x, y, health)
		self.ship_img, self.laser_img = self.COLOR_MAP[color]
		self.mask = pygame.mask.from_surface(self.ship_img)

	def move(self, vel):
		self.y += vel


def main():
	clock = pygame.time.Clock()
	lives = 5
	level = 1
	player_ship = Player((WIDTH - PLAYER_WIDTH) / 2, HEIGHT - PLAYER_HEIGHT - 50)
	enemies = []
	wave_length = 5
	enemy_velocity = 1


	def draw_window():
		WINDOW.fill(BG_COLOR)
		lives_label = MAIN_FONT.render(f"Life: {lives}", True, TEXT_COLOR)
		level_label = MAIN_FONT.render(f"Level: {level}", True, TEXT_COLOR)
		WINDOW.blit(lives_label, (10, 10))
		WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

		for enemy in enemies:
			enemy.draw(WINDOW)

		player_ship.draw(WINDOW)
		pygame.display.update()


	run = True
	while run:
		clock.tick(FPS)

		if len(enemies) == 0:
			level += 1
			wave_length += 5
			enemy_velocity += 2
			for i in range(wave_length):
				enemy = Enemy(
					random.randrange(50, WIDTH - 50), 
					random.randrange(-1500, -150), 
					random.choice(["red", "blue", "green"])
				)
				enemies.append(enemy)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()
		if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player_ship.x > 0:
			player_ship.x -= PLAYER_VELOCITY
		if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player_ship.x < WIDTH - PLAYER_WIDTH:
			player_ship.x += PLAYER_VELOCITY
		if (keys[pygame.K_w] or keys[pygame.K_UP]) and player_ship.y > 0:
			player_ship.y -= PLAYER_VELOCITY
		if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player_ship.y < HEIGHT - PLAYER_HEIGHT:
			player_ship.y += PLAYER_VELOCITY

		for enemy in enemies:
			enemy.y += enemy_velocity

		draw_window()
	pygame.quit()	





if __name__ == '__main__':
	main()