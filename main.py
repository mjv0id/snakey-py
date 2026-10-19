import pygame

pygame.init()

# game window
window = pygame.display.set_mode((800, 600))
window.fill((0, 0, 0))
pygame.display.set_caption("welcome to snakey")

# surfaces (player)
player = pygame.surface.Surface((100, 100))
player.fill((255, 255, 255))

# loop to make the window running
while True:
    #take input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
    #output

    window.fill((255, 255, 255))
    pygame.display.flip()


