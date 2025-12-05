from typing import Any
import pygame

class Protagonist():

    class ProtagonistSprite(pygame.sprite.Sprite):
        def __init__(self,type):
            '''Creates the sprite for player'''

            #initializing
            super().__init__()
            #loading character
            self.standing_image = pygame.image.load(f'assets/{type}.png')

            self.movingImages=[]
            self.movingImages.append(pygame.image.load(f"assets/{type}/{type}_run1.png"))
            self.movingImages.append(pygame.image.load(f"assets/{type}/{type}_run2.png"))
            self.currentImage=0

            self.image = self.standing_image
            self.rect = self.image.get_rect()

            #Is moving flag
            self.isMoving=False


        def update(self):
            '''Updates the protagonist'''

            #If is moving
            if self.isMoving:
                if self.currentImage<len(self.movingImages):
                    self.image = self.movingImages[int(self.currentImage)]
                    self.currentImage+=0.18
                else:
                    self.currentImage=0
            #If not moving
            else:
                self.image=self.standing_image
            
            

    def __init__(self,gameClass,protagonistType,ground:pygame.Rect,settings,isRunning:bool):
        '''Creates the protagonist and places it'''

        #Initializing
        self.screen =gameClass.screen
        self.groundRect = ground
        self.type = protagonistType
        self.settings = settings

        #Getting Protagonist
        self.protagonist = self.ProtagonistSprite(protagonistType)
        self.protagonistSpriteGroup = pygame.sprite.Group()
        self.protagonistSpriteGroup.add(self.protagonist)

        #Setting intial location
        self.protagonist.rect.midbottom = self.groundRect.midtop

        #Motion of Protagoinst
        self.movingRight=False
        self.movingLeft=False

        #Flag for game running
        self.isRunning = isRunning
        
    def _update_protg(self):
        '''Moves The Protagonist according to movement flag'''
        #Sets the moving animation flag
        if self.movingLeft and self.movingRight:
            self.protagonist.isMoving=False

        elif self.movingLeft or self.movingRight:
            self.protagonist.isMoving=True
        else:
            self.protagonist.isMoving=False
            

        if self.movingLeft:
            self._go_left()
        if self.movingRight:
            self._go_right()
        else:
            pass

    def _display(self):
        '''Puts the charcter to position'''
        self._update_protg()
        self.protagonistSpriteGroup.draw(self.screen)
        self.protagonistSpriteGroup.update()
        
        
            
    
    def _go_right(self):
        '''Makes The Protagonist go Right'''
        if self.isRunning:
            if self.protagonist.rect.right<= self.groundRect.right:
                self.protagonist.rect.centerx += self.settings.protgSpeed

    def _go_left(self):
        '''Makes The Protagonist go Left'''
        if self.isRunning:
            if self.protagonist.rect.left >=self.groundRect.left:
                self.protagonist.rect.centerx -= self.settings.protgSpeed