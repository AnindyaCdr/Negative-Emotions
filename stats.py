import pygame
import time
class Stats:
    def __init__(self,settings,protg:pygame.sprite.Sprite,cloudGroup:pygame.sprite.Group):
        '''Makes The game work'''
        self.settings = settings
        self.protg = protg
        self.cloudGroup = cloudGroup
        self.isProtected =False
        self.sTime=time.time()
        self.timeElasped={'secs':0.0,'minutes':0.0,'hours':0.0}

    def _check_collision_cloud_taken(self) ->bool:
        '''
        Returns true if collision with cloud takes place
        Else return false
        '''

        #To remove redline from vscode
        _temp_group = pygame.sprite.Group()
        _temp_group.add(self.protg)
        self.protg = _temp_group.sprites()[0]

        if pygame.sprite.spritecollideany(self.protg,self.cloudGroup):
            if self.isProtected:
                return False
            else:
                self.isProtected=True
                return True    
        else:
            return False
    def _clock_score(self):
        '''Adds time as scoring system'''

        #stores time
        self.timeElasped['secs'] = time.time()-self.sTime

        #manages the time format
        if self.timeElasped['secs']>=60:
            self.timeElasped['secs'] =0
            self.timeElasped['minutes']+=1
        if self.timeElasped['minutes']>=60:
            self.timeElasped['minutes']=0
            self.timeElasped['hours']+=1
        if self.timeElasped['hours']>=24:
            self.timeElasped['hours']=0
        return self.timeElasped




