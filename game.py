import pygame, controls
from gun import Gun
from pygame.sprite import Group


def run():
        
    pygame.init()
    screen = pygame.display.set_mode((700, 800))  #flag=pygame.NOFRAME
    pygame.display.set_caption("Космические защитники") # название игры
    bg_color = (0, 0, 0)
    icon = pygame.image.load('game/images/icon2.png')
    pygame.display.set_icon(icon)
    gun = Gun(screen)
    bullets = Group()

    while True:
        controls.events(screen, gun, bullets)  
        gun.update_gun()
        controls.update(bg_color, screen, gun, bullets)
        controls.update_bullets(bullets)
        
run()