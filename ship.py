import pygame

class Ship:
    '''espaço para configurar a espaçonave'''
    def __init__ (self, ai_game):
        '''inicia a nave na tela e define sua posição inicial'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        '''sobe a imagem da espaçonave e obtem suas dimensoes'''
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        ''' define o aparecimento da espaçonave no centro da tela e em baixo'''
        self.rect.midbottom = self.screen_rect.midbottom
        #armazena um float para a posi;'ao horizontal exata da espaçonave
        self.x=float(self.rect.x)
        #flags de movimento no eixo x
        self.moving_right = False
        self.moving_left = False
        
    '''atualiza a posição da nave com base na flag de movimento'''
    def update(self):
        if self.moving_right and self.rect.right< self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left>0:
            self.x -= self.settings.ship_speed
        self.rect.x=self.x
    def blitme(self):
        '''vai mostra a espaçonave emsua localização atual'''
        self.screen.blit(self.image,self.rect)
