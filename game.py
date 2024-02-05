import pygame, controls
from gun import Gun


def run():
        
    pygame.init()
    screen = pygame.display.set_mode((700, 800))  #flag=pygame.NOFRAME
    pygame.display.set_caption("Космические защитники") # название игры
    bg_color = (0, 0, 0)
    icon = pygame.image.load('game/images/icon2.png')
    pygame.display.set_icon(icon)
    gun = Gun(screen)

    while True:
        controls.events(gun)  
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()
        
        
run()