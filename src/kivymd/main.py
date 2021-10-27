from kivy.uix.screenmanager import *
from kivymd.app import MDApp
from kivy.core.window import Window

from Cocktail import *
from Pump import *
from WelcomeCarousel import *
from CocktailCarousel import *

# setup screen depending on OS
import platform
platformInfo = platform.uname()
if platformInfo.system == 'Linux' and platformInfo.machine.find('64') == -1:
    Window.fullscreen = 'auto'

class DionysusApp(MDApp):

    # change to main view
    def change_to_main(self, instance, value):
        if value == 2:
            self.screenmanager.current = 'main'

    def build(self):
        self.cocktails = self.loadCocktails()
        self.pumps = self.loadPumps()

        self.screenmanager = ScreenManager(transition=FadeTransition(duration=0.5))
        self.screenmanager.transition.direction = 'right'

        # create scenes
        welcomeScreen = Screen(name='intro',size=(800,480))
        appScreen = Screen(name='main',size=(800,480))

        # create carousels
        welcomeCarousel = WelcomeCarousel(self.cocktails,self.pumps)
        welcomeCarousel.bind(index=self.change_to_main)
        cocktailCarousel = CocktailCarousel(self.cocktails, self.pumps)

        welcomeScreen.add_widget(welcomeCarousel)
        appScreen.add_widget(cocktailCarousel)
        self.screenmanager.add_widget(welcomeScreen)
        self.screenmanager.add_widget(appScreen)
        
        return self.screenmanager

    def loadCocktails(self):
        provider = CocktailFactory(str(RES_PATH / "cocktails.json"))
        return provider.loadCocktails(self.loadIngredients())

    def loadPumps(self):
        provider = PumpFactory(str(RES_PATH / "pump-config.json"))
        return provider.loadFromFile()

    def loadIngredients(self):
        pumps = self.loadPumps()
        ingredients = []
        for pump in pumps:
            ingredients.append(pump.ingredient)
        return ingredients


DionysusApp().run()
