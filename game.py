import pygame
import sys

def run():
    
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))  #flag=pygame.NOFRAME
    pygame.display.set_caption("Космические защитники") # название игры
    bg_color = (0, 0, 0)
    icon = pygame.image.load('images/icon2.png')
    pygame.display.set_icon(icon)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        screen.fill(bg_color)
        pygame.display.flip()


run()