import pygame

class Ship:
    '''espaço para configurar a espaçonave'''
    def __init__ (self, ai_game):
        '''inicia a nave na tela e define sua posição inicial'''
        self.screen = ai_game.screen
        self.setting=ai_game.settings
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
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1
    def blitme(self):
        '''vai mostra a espaçonave emsua localização atual'''
        self.screen.blit(self.image,self.rect)
