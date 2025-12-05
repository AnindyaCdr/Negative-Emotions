import pygame,sys
from settings import Settings
from protagonist import Protagonist
from background import Background
from falling_objects import FallingObjects
from stats import Stats
from end_screen import EndScreen


class NegativeEmotions:


    def __init__(self):
        '''Initializing the game'''
        pygame.init()

        #Flag for running Game
        self.isRunning=True

        
        #Setting screen
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.screen)
        pygame.display.set_caption(self.settings.name)

        #setting Bg
        self.background =Background(self.screen)

        #Setting Clock
        self.clock = pygame.time.Clock()
        self.FPS=30
        
        #Setting protg
        self.protg = Protagonist(self,self.settings.protagonistType,self.background.groundRect,self.settings,self.isRunning)

        #Setting Falling Objects
        self.fallObj = FallingObjects(self.screen,self.settings,self.background.groundRect,self.isRunning)
        #Making Stats
        self.stats = Stats(self.settings,self.protg.protagonist,self.fallObj.cloudGroup)

        #Setting endscreen for endgame
        self.endScreen=EndScreen(self.screen)

        #playing background music
        #pygame.mixer.init()
        #pygame.mixer.music.load('assets/pianovol.mp3')
        #pygame.mixer.music.play(-1,0)

        

    def _event_handler(self):
        """Handles The User Event"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.protg.movingLeft=True
                elif event.key == pygame.K_RIGHT:
                    self.protg.movingRight=True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.protg.movingLeft=False
                elif event.key ==pygame.K_RIGHT:
                    self.protg.movingRight=False

    def _check_endGame(self):
        '''Ends the game when contition met'''
        if self.stats._check_collision_cloud_taken()==True:
            self.isRunning=False
            #Reset cloud
            self.fallObj.__init__(self.screen,self.settings,self.background.groundRect,self.isRunning)

            #Reset Player
            self.protg.__init__(self,self.settings.protagonistType,self.background.groundRect,self.settings,self.isRunning)

            #Reset stats
            self.stats.__init__(self.settings,self.protg.protagonist,self.fallObj.cloudGroup)
        elif  (self.isRunning==False) and (self.endScreen._restart_clicked()==True):
            self._restart_game()

    def _restart_game(self):
        '''Restarts the game'''
        #Reruns the game
        self.isRunning=True

        #Reset cloud
        self.fallObj.__init__(self.screen,self.settings,self.background.groundRect,self.isRunning)

        #Reset Player
        self.protg.__init__(self,self.settings.protagonistType,self.background.groundRect,self.settings,self.isRunning)

        #Reset stats
        self.stats.__init__(self.settings,self.protg.protagonist,self.fallObj.cloudGroup)

        


    def runGame(self):
        '''Running the game'''

        #Game loop
        while True:
            self._event_handler()

            self.background._display_bg()

            self.protg._display()

            self.fallObj._display_fallingObjects()

            self._check_endGame()

            self.endScreen._run_end_screen_when_needed(self.isRunning)

            pygame.display.update()
            self.clock.tick(30)


if __name__=='__main__':
    game = NegativeEmotions()
    game.runGame()
