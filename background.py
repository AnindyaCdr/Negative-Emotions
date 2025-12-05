import pygame
class Background:
    def __init__(self,screen:pygame.Surface):
        '''Intializes the background'''
        self.screen = screen
        self.screenRect = self.screen.get_rect()

        self.ground = pygame.image.load("assets/ground.png")
        self.groundRect=self.ground.get_rect()
        self.groundRect.midbottom = self.screenRect.midbottom

        self.skies = []
        self.currentSky=0
        self.skies.append(pygame.image.load('assets/sky/sky0.png'))
        self.skies.append(pygame.image.load('assets/sky/sky1.png'))
        self.skies.append(pygame.image.load('assets/sky/sky2.png'))
        self.skies.append(pygame.image.load('assets/sky/sky3.png'))
        self.skies.append(pygame.image.load('assets/sky/sky4.png'))
        self.sky = self.skies[self.currentSky]

    def _animate_sky(self):
        '''animates the sky'''
        #Updates the sky
        if self.currentSky<len(self.skies):
            
            self.sky = self.skies[int(self.currentSky)]
            self.currentSky +=0.2
        else:
            self.currentSky=0

    def _display_bg(self):
        '''Displays Ground in specified position'''
        self.screen.blit(self.sky,(0,0))
        self.screen.blit(self.ground,self.groundRect)
        self._animate_sky()

        
