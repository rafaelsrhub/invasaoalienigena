import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        #defini a posição inicial do alien
        super().__init__()
        self.screen = ai_game.screen

        #carrega a imagem do alien
        self.image = pygame.image.load('images/alien1.png')
        self.rect = self.image.get_rect()

        # inicia cada alien novo perto do canto esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #armazena a posição horizontal do alien
        self.x= float (self.rect.x)# esse formato permite que haja um posicionamento - 
        #"quebrado(float)" caso a velocidade seja 1.5 ou 2.5 pixels , etc

