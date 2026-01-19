import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        #defini a posição inicial do alien
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #carrega a imagem do alien
        self.image = pygame.image.load('images/alien1.png')
        self.rect = self.image.get_rect()

        # inicia cada alien novo perto do canto esquerdo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #armazena a posição horizontal do alien
        self.x= float (self.rect.x)# esse formato permite que haja um posicionamento - 
        #"quebrado(float)" caso a velocidade seja 1.5 ou 2.5 pixels , etc

     #faremos uma ação de retorno para True quando o alienigena chegar na borda da tela
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    #move os aliens para a direita
    def update(self):
        self.x += self.settings.alien_speed *self.settings.fleet_direction#desloca a frota para a direita ou para a esquerda
        self.rect.x = self.x
