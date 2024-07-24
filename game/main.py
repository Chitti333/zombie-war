import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):

        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('ZOMBIE WAR')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE * 2)
        self.state = "menu"
        self.level = Level()


        self.background_image = pygame.image.load("graphics/menu/start_menu.jpg").convert()
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))
    
    def draw_text(self, text, font, color, surface, x, y):
        textobj = font.render(text, True, color)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        surface.blit(textobj, textrect)
    

    def main_menu(self):
        while self.state == "menu":
            # self.screen.fill("white") #add a good picture

            self.screen.blit(self.background_image, (0,0))

            # self.draw_text("Play", self.font, "white", self.screen, WIDTH/2, HEIGHT/2)
            # self.draw_text("How to Play", self.font, "white", self.screen, WIDTH/2, HEIGHT/2 + UI_FONT_SIZE * 2 + 50)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_play = pygame.Rect(500, 315, 200, 50)
            button_how_to_play = pygame.Rect(400, 315 + UI_FONT_SIZE * 2 + 50, 400, 50)


            if button_play.collidepoint((mouse_x, mouse_y)):
                if pygame.mouse.get_pressed()[0]:
                    self.state = "game"
            
            if button_how_to_play.collidepoint((mouse_x, mouse_y)):
                if pygame.mouse.get_pressed()[0]:
                    self.state = "how_to_play"
            

            # pygame.draw.rect(self.screen, "green", button_play)
            # pygame.draw.rect(self.screen, "orange", button_how_to_play)

            self.draw_text("Play", self.font, "white", self.screen, WIDTH/2, HEIGHT/2)
            self.draw_text("How to Play", self.font, "white", self.screen, WIDTH/2, HEIGHT/2 + UI_FONT_SIZE * 2 + 50)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            self.clock.tick(FPS)
    

    def how_to_play(self):
        while self.state == 'how_to_play':
            self.screen.fill('white')
            self.draw_text('How to Play', self.font, 'black', self.screen, WIDTH/2, HEIGHT/7)
            self.draw_text('1. Use arrow keys to move', self.font, 'black', self.screen, WIDTH/2, HEIGHT/7 + UI_FONT_SIZE * 6)
            self.draw_text('2. "SPACEBAR" to attack, "Q" key to change weapons', self.font, 'black', self.screen, 100, 300)
            self.draw_text('2. "SPACEBAR" to attack, "Q" key to change weapons', self.font, 'black', self.screen, 100, 300)

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.state = 'menu'
            
            pygame.display.update()
            self.clock.tick(FPS)



            





    def run(self):
        while True:
                if self.state == "menu":
                    self.main_menu()
                
                elif self.state == "how_to_play":
                    self.how_to_play()
                
                elif self.state == "game":
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                                self.level.toggle_menu()

                    self.screen.fill('black')
                    self.level.run()
                    pygame.display.update()
                    self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()