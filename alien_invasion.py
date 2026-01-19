import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''classe geral para gerencia ativos do jogo'''

    def __init__(self):
        '''Inicializa o jogo e cria recursos do jogo'''
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings = Settings()

        self.screen= pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        #ajusta o bg e a resolução do jogo!
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        #ajusta exclusivamente o bg com a resolução disponivel!
        self.settings.bg_image = pygame.transform.scale(self.settings.bg_image, 
        (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        '''importa a nave para acessar os conteudos do jogo '''
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()# usamos o metodo sprite.group pois queremos administrar mais de um item simultaneamente
        self.aliens= pygame.sprite.Group()
        self.create_fleet()# usamos creat flit para criar e administrar uma frota

    
    def run_game(self):        
        '''inicia o loop principal do jogo'''
        while True:
            '''checa os comandos a serem executados na janela do jogo'''
            self.check_events() #verifica eventos de teclado e mouse
            self.ship.update() #atualiza a posição da nave
            self.bullets.update() #atualiza a posição das balas
            self.update_bullets()
            #atualiza a posição dos aliens
            self.update_aliens()
            #descarta os projeteis quando nao são mais utilizados
            
                #pode ser usado a função print aqui para saber se as balas estão sendo deletadas da tela
                #print(len(self.bullets))
                

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
                self.check_keydown_events(event)
                #transfere o loop para uma lista de eventos que serão checkados
            #corta o loop quando a tecla para de ser pressionada
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
                #transfere o loop para uma lista de eventos que serão checkados
            #mover para a esquerda    
    
    #checa eventos de pressionar tecla
    def check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()    

    #checa eventos de soltar teclas    
    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def create_alien(self, x_position, y_position):
        #Cria um alienigena e o posiciona na fileira    
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def create_fleet(self):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        #agora vamos trabalhar em mais alienigenas na frota
        alien_width = alien.rect.width

        current_x,current_y = alien_width,alien_height
        while current_y < (self.settings.screen_height - 3* alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self.create_alien(current_x, current_y)
                current_x += 2*alien_width
            current_x = alien_width
            current_y += 2*alien_height

    #função que ativa a movimentação dos aliens na tela
    def update_aliens(self):
        self.aliens.update()
        self.check_fleet_edges()
    
    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break
    
    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    #cria o tiro na tela
    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_limit:    
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    #atualiza cada posição do tiro!
    def update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                    self.bullets.remove(bullet)

    #atualiza a imagem de fundo sempre que necessario!
    def update_screen(self):   
        self.screen.blit(self.settings.bg_image, (0, 0))
        '''Coloca a espaçonave na tela com o blitme'''
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        
        pygame.display.flip() 

if __name__ == '__main__':
    '''Cria uma instância do jogo e executa ele'''
    ai=AlienInvasion()
    ai.run_game() 