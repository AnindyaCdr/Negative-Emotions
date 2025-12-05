import pygame
import random

class FallingObjects:
    class NegCloudSprite(pygame.sprite.Sprite):
        def __init__(self,xCord,yCord,gCord):
            '''Creates A negative cloud'''
            super().__init__()
            self.image = pygame.image.load("assets/negativeCloud.png")
            self.rect = self.image.get_rect()
            self.rect.topleft = (xCord,yCord)
            self.gCord = gCord
        def update(self):
            if self.rect.bottom >=self.gCord:
                self.kill()
            

    class HeartSprite(pygame.sprite.Sprite):
        def __init__(self,xCord,yCord):
            '''Creates a heart'''
            super().__init__()
            self.hearts = []
            self.hearts.append(pygame.image.load("assets/careHeart.png"))
            self.hearts.append(pygame.image.load("assets/loveHeart.png"))

            self.image = self.hearts[random.randint(0,1)]
            self.rect = self.image.get_rect()
            self.rect.topleft = (xCord,yCord)
            


    def create_wave(self):
        '''Creates an position of a wave of clouds'''

        _wavePos = [] #Stores position of each cloud temporarily

        #Generates clouds of a wave with each x_pos unique but may have same offset
        for _x_pos in random.sample(range(0,self.screenRect.width//100),k=self.cloudsInWave):
            x_offset = random.randint(-5,5)*10
            _wavePos.append((_x_pos*100+x_offset,0))
        
        for postion in _wavePos:
            self.cloudGroup.add(self.NegCloudSprite(postion[0],postion[1],self.ground.top))



    def __init__(self,screen:pygame.Surface,settings,groundRect:pygame.Rect,isRunning:bool):
        '''Initializing falling objects'''

        self.screen = screen
        self.screenRect = self.screen.get_rect()

        self.fallingSpeed = settings.initialFallSpeed
        self.fallingSppedIncrement = settings.fallAcceleration


        self.cloudGroup = pygame.sprite.Group()
        
        self.ground = groundRect
        self.started=False
        self.selectedCloudInWave =0 #Should contain the first cloud of the latest wave
        self.cloudsInWave=settings.cloudInWave

        #Gamerun flag
        self.isRunning = isRunning


    def wave_mover(self):
        '''Moves each wave of cloud'''
        if self.isRunning:
            for cloud in self.cloudGroup.sprites():
                cloud.rect.centery += self.fallingSpeed
                self.fallingSpeed += self.fallingSppedIncrement

    def wave_manager(self):
        '''Manages each wave of game'''

        
        #While In game ->New wave 
        if self.started:
            '''
            Note: 
              using 0 as index because it will always contain the first cloud of the wave that 
              had spwan the earliest because we are removing the one which are more down than ground 
              So naturally it will be most down so we will only check that rather than checking all because 
              it is the wave which will reach the ground the earliest
            '''
            #Destroying old wave
            if self.cloudGroup.sprites()[0].rect.bottom>=self.ground.top:
                self.cloudGroup.update()
                self.selectedCloudInWave-=self.cloudsInWave
                '''
                As a wave is destroyed the first n(self.cloudsInWave number) elemnts will be gone so 
                we will move the pointer n backwards to point to the latest wave's first cloud again as sprite group 
                is updated 
                '''
            #Creating new wave
            elif self.cloudGroup.sprites()[self.selectedCloudInWave].rect.top >=300:
                self.create_wave()
                self.selectedCloudInWave+=self.cloudsInWave
                '''
                Once we create a wave based on another now we don't want to track that wave becuase
                it is already down the line. so we will move the pointer n(self.cloudsInWave number)
                number forward to point the latest wave's first cloud
                We are generating new wave based on latest wave's postion so we need the pointer
                pointing to latest wave's any cloud ,but its easier to manage with the endpoints(Start,end)
                '''

        #Starting Game ->New wave
        else:
            self.create_wave()
            self.started=True

        #moving waves

        self.wave_mover()

    def _display_fallingObjects(self):
        '''Displays Falling Object'''
        self.wave_manager()
        self.cloudGroup.draw(self.screen)
        pass
