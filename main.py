import pygame

pygame.init()

# game window
window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("welcome to snakey")

# surfaces (player)
player = pygame.surface.Surface((100, 100))
player.fill((255, 255, 255))
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

# loop to make the window running
while True:
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
    #output
    
    window.fill((255, 255, 255))
    
    window.blit(player, (player_x, player_y))
    
    pygame.display.flip()

window.blit(falling_object, (falling_object_x, falling_object_y))
