from kivy.uix.screenmanager import Screen
from kivymd.uix.carousel import Carousel
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivy.clock import Clock
from GPButton import GPButton
from kivy.core.window import Window

from pathlib import Path

from Cocktail import *
from Pump import *

# setup screen depending on OS
import platform
platformInfo = platform.uname()
if platformInfo.system == 'Linux' and platformInfo.machine.find('64') == -1:
    Window.fullscreen = 'auto'

RES_PATH = Path("../res/")

class DionysusApp(MDApp):
    def build(self):
        self.cocktails = self.loadCocktails()
        self.pumps = self.loadPumps()

        # snackbar = Snackbar(
        #     text="Configuration loaded",
        #     snackbar_x="10dp",
        #     snackbar_y="10dp",
        #     size_hint_x=.5,
        #     pos_hint={"center_x": .5, "center_y":0.1}
        # )
        # snackbar.open()

        # Clock.schedule_once(snackbar.dismiss,1)

        screen = Screen(size=(800,480))
        carousel = Carousel()

        # create a widget for each cocktail
        for cocktail in self.cocktails:
            grid = MDFloatLayout()
            grid.add_widget(
                MDLabel(
                    text=cocktail.name,
                    pos_hint={"center_x": .8, "center_y": .26},
                    font_style="H3"
                )
            )
            grid.add_widget(
                GPButton(
                    cocktail,
                    self.pumps,
                    icon = self.getIconPath(cocktail.name),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    user_font_size="128sp"
                )
            )
            carousel.add_widget(grid)

        screen.add_widget(carousel)
        return screen

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

    def getIconPath(self, name):
         path = RES_PATH / "img" / (name.lower().replace(' ','-')+".png")
         if path.exists() and path.is_file():
             return str(path)
         else:
             return str(RES_PATH / "img" / "error.png")


DionysusApp().run()
