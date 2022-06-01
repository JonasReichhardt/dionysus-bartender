from pathlib import Path

from kivy.graphics import Rectangle
from kivy.lang import Builder
from kivy.uix.screenmanager import *
from kivy.core.window import Window
from kivymd.uix.fitimage import FitImage
from kivymd.uix.screen import MDScreen
from kivymd.uix.swiper import MDSwiperItem
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from playsound import playsound

# setup screen depending on OS
import platform
import requests
import json

from theming import colors

platformInfo = platform.uname()
if platformInfo.system == 'Linux' and platformInfo.machine.find('64') == -1:
    Window.fullscreen = 'auto'

RES_PATH = Path("../res/")
SERVER_IP = '192.168.56.1'
SERVER_PORT = '8081'

sm = ScreenManager(transition=FadeTransition(duration=0.5))


# welcome screen
class WelcomeScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# main screen
class MainScreen(MDScreen):
    ingredients = json.loads(requests.get('http://' + SERVER_IP + ':' + SERVER_PORT + '/ingredients').content)
    raisedBtn = None
    initial = 0
    ingredientsSavedMsg = 'Save'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # initialize ingredient list by calling ingredient endpoint
        menu_items = self.getMenuItems(self.getIngredients())
        self.menu = MDDropdownMenu(
            caller=self.ids.buttonLayout,
            items=menu_items,
            position="center",
            width_mult=4,
            height=70
        )
        self.menu.bind()

    def getIngredients(self):
        return json.loads(requests.get('http://' + SERVER_IP + ':' + SERVER_PORT + '/ingredients').content)

    def postIngredients(self):
        requests.post('http://' + SERVER_IP + ':' + SERVER_PORT + '/ingredients', json=self.ingredients)
        self.ids['btnSave'].text = 'Config saved!'

    def getMenuItems(self, ing):
        return [
            {
                "viewclass": "OneLineListItem",
                "text": ing[i],
                "on_release": lambda x=i: self.setIngredient(ing[x], self.raisedBtn),
            } for i in range(len(ing))
        ]

    def onRelease(self, btn):
        self.raisedBtn = btn
        self.menu.open()

    def setIngredient(self, item, index):
        self.ingredients[index] = item
        # change btn text
        self.ids['btn' + str(index)].text = item
        self.menu.dismiss()

    def returnToCocktailView(self):
        sm.transition.direction = 'up'
        sm.current = 'cocktail'


class CocktailImage(FitImage):
    initial = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


# class representation of swiper
class CocktailScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_pre_enter(self):
        for widget in self.ids.swiper.get_items():
            self.ids.swiper.remove_widget(widget)
        for c in self.loadCocktails():
            self.ids.swiper.add_widget(CocktailItem(cocktail=c))

    def loadCocktails(self):
        return json.loads(requests.get('http://' + SERVER_IP + ':' + SERVER_PORT + '/cocktails').content)


# normal cocktail
class CocktailItem(MDSwiperItem):
    cocktail = {}

    def __init__(self, **kwargs):
        self.cocktail = kwargs["cocktail"]
        super().__init__()

    def getIconPath(self):
        path = RES_PATH / "img" / (self.cocktail['name'].lower().replace(' ', '-') + ".png")
        if path.exists() and path.is_file():
            return str(path)
        else:
            return str(RES_PATH / "img" / "error.png")

    def getCocktailName(self):
        return self.cocktail['name']

    def makeCocktail(self):
        name = str.lower(self.cocktail['name']).replace(" ", "")
        requests.post('http://' + SERVER_IP + ':' + SERVER_PORT + '/cocktails/standard/' + name)
        playsound(str(RES_PATH / 'TestSound.mp3'), block=False)

    def on_touch_down(self, touch):
        self.initial = touch.y

    def on_touch_up(self, touch):
        if self.ids.btn.collide_point(*touch.pos):
            self.makeCocktail()
        if self.initial - touch.y > 50:
            sm.transition.direction = 'down'
            sm.current = 'main'


class DionysusApp(MDApp):

    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "200"

        kv = Builder.load_file("View/CocktailScreen.kv")
        kv = Builder.load_file("View/WelcomeScreen.kv")
        kv = Builder.load_file("View/MainScreen.kv")
        # register all pages
        screens = [WelcomeScreen(name="welcome"), MainScreen(name="main"), CocktailScreen(name='cocktail')]
        for screen in screens:
            sm.add_widget(screen)
        sm.current = "cocktail"

        return sm

    # change to main view
    def change_to_main(self, instance, value):
        if value == 2:
            sm.current = 'main'


DionysusApp().run()
