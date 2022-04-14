from kivymd.uix.carousel import Carousel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

from pathlib import Path

RES_PATH = Path("../res/")

class CocktailCarousel(Carousel):
    def __init__(self, cocktails, pumps, **kwargs):
        super(CocktailCarousel, self).__init__(**kwargs)
        # create a widget for each cocktail
        for cocktail in cocktails:
            print(cocktail)

    def getIconPath(self, name):
        path = RES_PATH / "img" / (name.lower().replace(' ','-')+".png")
        if path.exists() and path.is_file():
            return str(path)
        else:
            return str(RES_PATH / "img" / "error.png")