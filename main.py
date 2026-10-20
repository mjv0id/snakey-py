import pygame
import random

pygame.init()

# game window
window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("蛇 snakey")

# surfaces (player)
player = pygame.surface.Surface((100, 100))
player.fill((255, 255, 255))
player = pygame.image.load("img/snake.png").convert_alpha()
player = pygame.transform.scale(player, (100, 100))

player_x = 0 
player_y = 0
player_vel_x = 0
player_vel_y = 0

# falling objects
falling_object = pygame.surface.Surface((50, 50))
falling_object.fill((255, 255, 255))
falling_object_x = 0
falling_object_y = 0
falling_object_vel_x = 0
falling_object_vel_y = 0.3

while True:
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_vel_x = -0.2
            if event.key == pygame.K_RIGHT:
                player_vel_x = 0.2
        else:
            player_vel_x = 0
            player_vel_x = 0
    if falling_object_y >= window.get_height():
        falling_object_y = 0
        falling_object_x = random.randint(0, window.get_width() - 50)

    #output
    
    window.fill((255, 255, 255))
    player_x += player_vel_x 
    player_y += player_vel_y

    window.blit(player, (player_x, player_y))
    
    pygame.display.flip()

    falling_object_x += falling_object_vel_x
    falling_object_y += falling_object_vel_y
    window.blit(falling_object, (falling_object_x, falling_object_y))

window.blit(falling_object, (falling_object_x, falling_object_y))
