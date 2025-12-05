import pygame,sys
from background import Background

class StartScreen:
    def __init__(self):
        '''Initializes the start screen'''

        pygame.init()

        #Setting the clock
        self.clock = pygame.time.Clock()
        self.FPS=30

        #Settings the screen
        self.stScreen = pygame.display.set_mode((800,600))
        self.stScreenRect = self.stScreen.get_rect()
        pygame.display.set_caption("Negative Emotions")

        #Setting the background
        self.background = Background(self.stScreen)
        
        #Setting title
        self.title = pygame.image.load('assets/negEmTitle.png')
        self.titleRect = self.title.get_rect()

        self.titleRect.centerx = self.stScreenRect.centerx
        self.titleRect.top = self.stScreenRect.top +80

        #Setting startButton -> umbrella
        self.umbrellaStart = pygame.image.load('assets/umbrella.png')
        self.umbrellaRect = self.umbrellaStart.get_rect()
        self.umbrellaRect.midbottom = self.background.groundRect.midtop

        #Setting char select text
        self.charSelectText = pygame.image.load('assets/char_select_text.png')
        self.charSelectTextRect = self.charSelectText.get_rect()
        self.charSelectTextRect.topleft = self.titleRect.bottomleft

        #He choice
        self.heChoice = pygame.image.load('assets/heChoice.png')
        self.heChoiceRect = self.heChoice.get_rect()
        self.heChoiceRect.left = self.umbrellaRect.centerx
        self.heChoiceRect.bottom = self.background.groundRect.top


        #She choice
        self.sheChoice = pygame.image.load('assets/sheChoice.png')
        self.sheChoiceRect = self.sheChoice.get_rect()
        self.sheChoiceRect.right = self.umbrellaRect.centerx
        self.sheChoiceRect.bottom = self.background.groundRect.top

        #Mainatining offset for choices
        self.x_offset = -4
        self.sheChoiceRect.centerx += self.x_offset
        self.heChoiceRect.centerx += self.x_offset

        #Setting Section
        self.isCharSelected =False
        self.charSelectedIcons = []
        self.charSelectedLiterals=[None,'she','he']
        self.charSelectedIcons.append(pygame.image.load('assets/charSelectEmpty.png'))
        self.charSelectedIcons.append(pygame.image.load("assets/charSelectFemale.png"))
        self.charSelectedIcons.append(pygame.image.load("assets/charSelectMale.png"))
        self.charSelectedIndex = 0
        self.charSelected = self.charSelectedIcons[self.charSelectedIndex]
        self.charSelectedRect = self.charSelected.get_rect() 

        #Setting the icon at position with offsets
        self.charSelectedRect.left = self.charSelectTextRect.right+20
        self.charSelectedRect.centery = self.charSelectTextRect.centery+15



        #Start screen running flag
        self.startScreenRunning = False


    def _run_start_screen(self):
        '''Runs The Start Screen 
        Returns gender of protoganist when start screen ends'''
        self.startScreenRunning = True
        while self.startScreenRunning:
            
            #Event handler
            self._event_handler_start_screen()

            
            #Drawing Objects
            self._draw_objects()
            

            self.clock.tick(self.FPS)
            pygame.display.flip()
        pygame.quit()
        return self.charSelectedLiterals[self.charSelectedIndex]
    def _draw_objects(self):
        '''Draws all the required objects for start screen'''

        #Draws background
        self.background._display_bg()

        #Draws title
        self.stScreen.blit(self.title,self.titleRect)
        #Draws chars elect text
        self.stScreen.blit(self.charSelectText,self.charSelectTextRect)
        
        #Draws umbrella
        self.stScreen.blit(self.umbrellaStart,self.umbrellaRect)

        #Draws he choice

        self.stScreen.blit(self.heChoice,self.heChoiceRect)

        #Draws she choice

        self.stScreen.blit(self.sheChoice,self.sheChoiceRect)

        #Draws Selected character
        self.stScreen.blit(self.charSelected,self.charSelectedRect)



    def _event_handler_start_screen(self):
        '''Handle events for start screen'''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.startScreenRunning=False
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                    self._select_character()

    def _select_character(self):
        '''Let user to select charcter'''
        _mousePos = pygame.mouse.get_pos()
        _leftButState = pygame.mouse.get_pressed()[0]
        if _leftButState:
            if self.heChoiceRect.collidepoint(_mousePos):
                self.charSelectedIndex = 2
                self.charSelected = self.charSelectedIcons[self.charSelectedIndex]
                self.isCharSelected=True

            elif self.sheChoiceRect.collidepoint(_mousePos):
                self.charSelectedIndex = 1
                self.charSelected = self.charSelectedIcons[self.charSelectedIndex]
                self.isCharSelected=True


            elif self.umbrellaRect.collidepoint(_mousePos):
                if self.isCharSelected:
                    self._start_game()
        else:
            pass
    
    def _start_game(self):
        self.startScreenRunning =False
        