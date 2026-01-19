import pygame
class Settings:
    def __init__(self):
        '''Configurações do jogo'''
        '''tela, largura'''
        self.bg_image = (pygame.image.load('images/bg.jpg'))     
        self.ship_speed = 10