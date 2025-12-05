import pygame
class EndScreen:
    def __init__(self,screen:pygame.Surface):
        '''Initializes the end screen for use'''
        self.screen=screen
        self.screenRect = self.screen.get_rect()

        self.endImage = pygame.image.load("assets/endScreen.png")
        self.endImageRect = self.endImage.get_rect()

        self.restartImages=[]
        self.restartImages.append(pygame.image.load("assets/restartBut.png"))
        self.restartImages.append(pygame.image.load("assets/restartButPressed.png"))
        self.restartImage = self.restartImages[0]
        self.restartRect = self.restartImage.get_rect()


        self.endImageRect.center = self.screenRect.center

        self.restartRect.centerx = self.endImageRect.centerx
        self.restartRect.bottom = self.endImageRect.bottom -100

    def _run_end_screen_when_needed(self,isRunning:bool):
        '''Runs The endscreen when running is false'''
        #Runs endscreen
        
        if isRunning:
            pass
        else:
            self.screen.blit(self.endImage,self.endImageRect)
            self.screen.blit(self.restartImage,self.restartRect)
        #manages hover
        self._restart_but_hover()

    def _restart_but_hover(self):
        '''Changes image based on hover state of button'''
        if self.restartRect.collidepoint(pygame.mouse.get_pos()):
            self.restartImage=self.restartImages[1]
        else:
            self.restartImage=self.restartImages[0]

    def _restart_clicked(self) ->bool:
        '''Checks if restart button has been pressed or not'''
        if self.restartRect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
            else:
                return False
        else:
            return False

        