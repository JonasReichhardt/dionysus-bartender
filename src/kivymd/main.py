from kivy.uix.screenmanager import *
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.swiper import MDSwiperItem

from Model.Pump import *
from WelcomeCarousel import *
from CocktailCarousel import *

# setup screen depending on OS
import platform

from theming import colors

platformInfo = platform.uname()
if platformInfo.system == 'Linux' and platformInfo.machine.find('64') == -1:
    Window.fullscreen = 'auto'

RES_PATH = Path("../res/")


# main screen
class WelcomeScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# main screen
class MainScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# class representation of swiper
class CocktailScreen(MDScreen):

    def on_enter(self):
        for c in self.loadCocktails():
            self.ids.swiper.add_widget(CocktailItem())

    def loadCocktails(self):
        provider = CocktailFactory(str(RES_PATH / "cocktails.json"))
        return provider.loadCocktails(self.loadIngredients())

    def loadIngredients(self):
        pumps = self.loadPumps()
        ingredients = []
        for pump in pumps:
            ingredients.append(pump.ingredient)
        return ingredients

    def loadPumps(self):
        provider = PumpFactory(str(RES_PATH / "pump-config.json"))
        return provider.loadFromFile()

    def getIconPath(self):
        name = "coke4"
        path = RES_PATH / "img" / (name.lower().replace(' ', '-') + ".png")
        if path.exists() and path.is_file():
            return str(path)
        else:
            return str(RES_PATH / "img" / "error.png")


# normal cocktail
class CocktailItem(MDSwiperItem):
    pass


class DionysusApp(MDApp):

    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "500"

        kv = Builder.load_file("View/CocktailScreen.kv")
        kv = Builder.load_file("View/WelcomeScreen.kv")
        kv = Builder.load_file("View/MainScreen.kv")
        sm = ScreenManager(transition=FadeTransition(duration=0.5))
        # register all pages
        screens = [WelcomeScreen(name="welcome"), MainScreen(name="main"), CocktailScreen(name='cocktail')]
        for screen in screens:
            sm.add_widget(screen)
        sm.current = "welcome"

        return sm

    # change to main view
    def change_to_main(self, instance, value):
        if value == 2:
            sm.current = 'main'


DionysusApp().run()
