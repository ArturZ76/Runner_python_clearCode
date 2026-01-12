import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font( "font/Pixeltype.ttf", 50 )

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render("My game", False, "Black")

snail_surface = pygame.image.load("graphics/snail/snail1.png")
snail_x_pos = 800

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))    #(blit)block image transfer
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 50))
    snail_x_pos -= 2
    if snail_x_pos <= -70:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 270))

    pygame.display.update()
    clock.tick(60) #maxk is 60fps