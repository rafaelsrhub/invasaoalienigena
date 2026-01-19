import pygame
class Settings:
    def __init__(self):
        '''Configurações do jogo'''
        '''tela, largura'''
        self.bg_image = (pygame.image.load('images/bg.jpg'))     
        self.ship_speed = 8
        #configurações do projetil
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = (0,200,0)
        self.bullet_limit= 10
        self.alien_speed=1.0
        self.fleet_drop_speed= 10
        self.fleet_direction = 1# 1 direita -1 esquerda