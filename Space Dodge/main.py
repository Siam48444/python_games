import pygame
import time
import random
import math
pygame.font.init()


WIDTH, HEIGHT = 1000, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
STAR_WIDTH, STAR_HEIGHT = 10, 30

PLAYER_VELOCITY = 5
STAR_VELOCITY = 7

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Space Dodge")
FONT = pygame.font.SysFont("Inter", 20)


def main():
    player = pygame.Rect(
        (WIDTH - PLAYER_WIDTH) / 2, HEIGHT - PLAYER_HEIGHT, 
        PLAYER_WIDTH, PLAYER_HEIGHT
    )
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add = 2000
    star_next = 0
    stars = []
    
    hit = False
    running = True
    
    while running:
        star_next += clock.tick(120)
        elapsed_time = time.time() - start_time

        if star_next > star_add:
            for _ in range(3):
                start_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(start_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add = max(200, star_add - 50 )
            star_next = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x <= WIDTH - PLAYER_WIDTH:
            player.x += PLAYER_VELOCITY

        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y > player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        draw(player, elapsed_time, stars)
    
    pygame.quit()


def draw(player, elapsed_time, stars):
    WINDOW.fill("black")

    time_text = FONT.render(f"Time: {math.floor(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_text, (0, 0))

    pygame.draw.rect(WINDOW, "red", player)

    for star in stars:
        pygame.draw.rect(WINDOW, "white", star)

    pygame.display.update()





if __name__ == "__main__":
    main()
