import pygame
import time
import random
import math
pygame.font.init()


WIDTH, HEIGHT = 1000, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
STAR_WIDTH, STAR_HEIGHT = 5, 10
PLAYER_VELOCITY = 5
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Space Dodge")
FONT = pygame.font.SysFont("Inter", 20)


def main():
    player = pygame.Rect(
        (WIDTH - PLAYER_WIDTH) / 2, HEIGHT - PLAYER_HEIGHT - 20, 
        PLAYER_WIDTH, PLAYER_HEIGHT
    )
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add = 2000
    star_next = 0
    stars = []
    
    running = True
    while running:
        star_next += clock.tick(120)
        elapsed_time = time.time() - start_time

        if star_next > star_add:
            for _ in range(3):
                start_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(start_x, 0, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x <= WIDTH - PLAYER_WIDTH:
            player.x += PLAYER_VELOCITY

        draw(player, elapsed_time)
    
    pygame.quit()


def draw(player, elapsed_time):
    WINDOW.fill("black")

    time_text = FONT.render(f"Time: {math.floor(elapsed_time)}s", 2, "white")
    WINDOW.blit(time_text, (0, 0))

    pygame.draw.rect(WINDOW, "red", player)
    pygame.display.update()





if __name__ == "__main__":
    main()
