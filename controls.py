import pygame, sys


def events(gun):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_d:
                gun.mright = True  
            elif event.key == pygame.K_a:
                gun.mleft = True          
        elif event.type == pygame.KEYUP:            
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False
