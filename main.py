import pygame
import random

pygame.init()

# game window
window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("ghost ride")

# surfaces (player)
player = pygame.surface.Surface((100, 100))
player.fill((255, 255, 255))
player = pygame.image.load("img/ghost.png").convert_alpha()
player = pygame.transform.scale(player, (75, 75))

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

game_state = 1

font = pygame.font.SysFont(None, 72)
game_over = font.render("game over", True, (0, 0, 0))


while True:
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        keys = pygame.key.get_pressed()
        player_vel_x = 0
        player_vel_y = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_vel_x = -2
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_vel_x = 2
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            player_vel_y = -2
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            player_vel_y = 2
        
        player_x += player_vel_x
        player_y += player_vel_y

        #keep player inside the window
        player_x = max(0, min(player_x, window.get_width() - player.get_width()))
        player_y = max(0, min((player_y, window.get_height() - player.get_height())))

        #draw
        window.fill((10, 10, 25))
        window.blit(player, (player_x, player_y))
        pygame.display.flip()

    #output
    pygame.display.flip()
    
    if game_state == 1:
        window.fill((255, 255, 255))
        player_x += player_vel_x 
        player_y += player_vel_y
        window.blit(player, (player_x, player_y))

        falling_object_x += falling_object_vel_x
        falling_object_y += falling_object_vel_y
        window.blit(falling_object, (falling_object_x, falling_object_y))
    elif game_state == 2:
        pass


window.blit(falling_object, (falling_object_x, falling_object_y))

def collision_detection():
    return (
            player_x <= (falling_object_x + falling_object.get_width()) and
            (player_x + player.get_width()) >= falling_object_x and 
            player_y <= (falling_object_y + falling_object.get_height() + 5) and
            (player_y + player.get_height() >= falling_object_y)
            )

