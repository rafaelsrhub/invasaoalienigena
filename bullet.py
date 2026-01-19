import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #Classe que gerencia os projétei da nave
    def __init__(self,ai_game):
    #cria um objeto bullet na posição atual da espaçonave
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)


    def update (self):
        #desloca o projetil verticalmente 
        self.y -= self.settings.bullet_speed
        #atualiza a posição de rect
        self.rect.y= self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

