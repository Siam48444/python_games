import pygame
import time
import random


WIDTH, HEIGHT = 1000, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
PLAYER_VELOCITY = 3
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE = pygame.display.set_caption("Space Dodge")


def main():
    player = pygame.Rect(
        (WIDTH - PLAYER_WIDTH) / 2, HEIGHT - PLAYER_HEIGHT - 20, 
        PLAYER_WIDTH, PLAYER_HEIGHT
    )
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break        

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT]:
            player.x += PLAYER_VELOCITY

        draw(player)
    
    pygame.quit()


def draw(player):
    WINDOW.fill("black")
    pygame.draw.rect(WINDOW, "red", player)
    pygame.display.update()





if __name__ == "__main__":
    main()
