from start_screen import StartScreen
class Settings:
    def __init__(self):
        '''Initial Settings'''
        #Display settings
        self.screen = (800,600)
        self.name="Negative Emotions"


        #Character settings
        self.protagonistType= 'she'
        self.protgSpeed = 5

        #Falling Objects Settings
        self.initialFallSpeed = 4
        self.fallAcceleration=0.2**7
        self.cloudInWave = 6

        #Getting info from Start screen
        self.startScreen = StartScreen()

        self.protagonistType = self.startScreen._run_start_screen()