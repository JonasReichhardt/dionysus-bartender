from kivymd.uix.carousel import Carousel
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

from pathlib import Path

from GPButton import *
from src.kivymd.model.Cocktail import CocktailFactory

RES_PATH = Path("../res/")

class CocktailCarousel(Carousel):
    def __init__(self, cocktails, pumps, **kwargs):
        super(CocktailCarousel, self).__init__(**kwargs)
        # create a widget for each cocktail
        for cocktail in cocktails:
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
                    pumps,
                    icon = self.getIconPath(cocktail.name),
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    user_font_size="128sp"
                )
            )
            self.add_widget(grid)

    def getIconPath(self, name):
        path = RES_PATH / "img" / (name.lower().replace(' ','-')+".png")
        if path.exists() and path.is_file():
            return str(path)
        else:
            return str(RES_PATH / "img" / "error.png")