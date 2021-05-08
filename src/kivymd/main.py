from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from GPButton import GPButton
from CocktailProvider import * 
from PumpProvider import *

RES_PATH = "..\\res\\"

class MainApp(MDApp):
    def build(self):
        cocktails = self.loadCocktails()
        pumps = self.loadPumps()
        print(cocktails[0])
        print(pumps[0])

        screen = Screen(size=(800,480))

        screen.add_widget(
            GPButton(
                25,25,
                text="Pump 1", 
                icon=RES_PATH+"img\\coke.png", 
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                user_font_size="128sp"
            )
        )
        
        return screen

    def loadCocktails(self):
        provider = CocktailDataProvider(RES_PATH+"cocktails.json")
        return provider.load()

    def loadPumps(self):
        provider = PumpDataProvider(RES_PATH+"pump-config.json")
        return provider.load()


MainApp().run()