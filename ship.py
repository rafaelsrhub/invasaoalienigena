import pygame

class Ship:
    '''espaço para configurar a espaçonave'''
    def __init__ (self, ai_game):
        '''inicia a nave na tela e define sua posição inicial'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        '''sobe a imagem da espaçonave e obtem suas dimensoes'''
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        ''' define o aparecimento da espaçonave no centro da tela e em baixo'''
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''vai mostra a espaçonave emsua localização atual'''
        self.screen.blit(self.image,self.rect)