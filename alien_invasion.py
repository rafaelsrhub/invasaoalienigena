import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''classe geral para gerencia ativos do jogo'''

    def __init__(self):
        '''Inicializa o jogo e cria recursos do jogo'''
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings = Settings()

        self.screen= pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("Alien Invasion")
        '''importa a nave para acessar os conteudos do jogo '''
        self.ship= Ship(self)
    
    def run_game(self):
        '''inicia o loop principal do jogo'''
        while True:
            #olha eventos de teclado e mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            '''Coloca a espaçonave na tela com o blitme'''
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    '''Cria uma instância do jogo e executa ele'''
    ai=AlienInvasion()
    ai.run_game() 