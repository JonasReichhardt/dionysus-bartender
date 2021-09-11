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

# setup screen and gpio depending on OS
import platform
platformInfo = platform.uname()
if platformInfo.system == 'Linux' and platformInfo.machine.find('64') == -1:
    Window.fullscreen = 'auto'
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    for p in range (1, 37):
        GPIO.setup(p, GPIO.OUT)
else:
    print(f'\033[93m[WRN] not running on linux -> no GPIO \033[0m')

RES_PATH = Path("../res/")

class MainApp(MDApp):
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

        inting = 1
        for cocktail in self.cocktails:
            if inting<=6:
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
                        icon= str(RES_PATH / "img" / ("coke"+str(inting)+".png")),
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                        user_font_size="128sp"
                    )
                )
                inting= inting+1
                carousel.add_widget(grid)

        screen.add_widget(carousel)

        return screen

    def loadCocktails(self):
        provider = CocktailFactory(str(RES_PATH / "cocktails.json"))
        return provider.loadFromFile()

    def loadPumps(self):
        provider = PumpFactory(str(RES_PATH / "pump-config.json"))
        return provider.loadFromFile()


MainApp().run()
