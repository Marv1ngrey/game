import pygame
from pygame.sprite import AbstractGroup

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, screan, gun):
        super(Bullet, self).__init__()
        self.screen = screan
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 139, 195, 74
        self.speed = 1.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)
        
    def update(self):
        self.y -= self.speed
        self.rect.y = self.y
        
        
    def drow_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        
        
        