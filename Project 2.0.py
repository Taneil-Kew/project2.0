import pygame
(width,height)=(600,500)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
b
while True:
    pass
running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False