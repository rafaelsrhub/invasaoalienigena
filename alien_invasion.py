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
            '''checa primeiro se a algum comando para fechar a janela'''
            self.check_events()
            self.ship.update()
            #olha eventos de teclado e mouse
            self.update_screen()
            self.clock.tick(60)

    '''Função definida para controlar eventos'''        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #mover para a direita   
            #inicia o loop para que a nave fique indo para a direita ou para a esquerda
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            #corta o loop quando a tecla para de ser pressionada
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT: 
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
            #mover para a esquerda
            

                    
    def update_screen(self):   
        self.screen.fill(self.settings.bg_color)
        '''Coloca a espaçonave na tela com o blitme'''
        self.ship.blitme()

        pygame.display.flip() 


if __name__ == '__main__':
    '''Cria uma instância do jogo e executa ele'''
    ai=AlienInvasion()
    ai.run_game() 