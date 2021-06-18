from kivy.uix.screenmanager import Screen
from kivymd.uix.carousel import Carousel
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivy.clock import Clock
from GPButton import GPButton
from CocktailProvider import * 
from PumpProvider import *

RES_PATH = "..\\res\\"

class MainApp(MDApp):
    def build(self):
        cocktails = self.loadCocktails()
        pumps = self.loadPumps()

        snackbar = Snackbar(
            text="Configuration loaded",
            snackbar_x="10dp",
            snackbar_y="10dp",
            size_hint_x=.5,
            pos_hint={"center_x": .5, "center_y":0.1}
        )
        snackbar.open()

        Clock.schedule_once(snackbar.dismiss,1)

        screen = Screen(size=(800,480))
        carousel = Carousel()
        inting = 1

        for cock in cocktails:
            if inting<=6:
                grid = MDFloatLayout()
                grid.add_widget(
                    MDLabel(
                        text=cock.name,
                        pos_hint={"center_x": .8, "center_y": .26},
                        font_style="H3"
                    )
                )
                grid.add_widget(
                    GPButton(
                        18,23,
                        icon=RES_PATH+"img\\coke"+str(inting)+".png", 
                        pos_hint={"center_x": 0.5, "center_y": 0.5},
                        user_font_size="128sp"
                    )
                )
                inting= inting+1
                carousel.add_widget(grid)

        screen.add_widget(carousel)
        
        return screen

    def loadCocktails(self):
        provider = CocktailDataProvider(RES_PATH+"cocktails.json")
        return provider.load()

    def loadPumps(self):
        provider = PumpDataProvider(RES_PATH+"pump-config.json")
        return provider.load()


MainApp().run()