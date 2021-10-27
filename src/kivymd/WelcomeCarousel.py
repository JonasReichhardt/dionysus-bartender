from kivymd.uix.carousel import Carousel
from kivymd.uix.list import *
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel

class WelcomeCarousel(Carousel):

    def __init__(self, cocktails, pumps, **kwargs):
        super(WelcomeCarousel, self).__init__(**kwargs)
        self.initFirstPage(cocktails, pumps)
        self.initSecPage(cocktails, pumps)
        self.add_widget(MDLabel())

    def initFirstPage(self, cocktails, pumps):
        ingredientList = MDList()
        cocktailList = MDList()

        for pump in pumps:
            ingredientList.add_widget(OneLineListItem(text=pump.ingredient))
        for cocktail in cocktails:
            cocktailList.add_widget(OneLineListItem(text=cocktail.name))

        vertLayout = MDBoxLayout(orientation='vertical')
        vertLayout.add_widget(
            MDLabel(
                    text="Welcome to DionysusOS",
                    font_style="H3",
                    halign="center"
            )
        )
        vertLayout.add_widget(
            MDLabel(
                    text="Please check available drinks",
                    font_style="H6",
                    halign="center"
            )
        )

        horLayout = MDBoxLayout(orientation='horizontal')
        horLayout.add_widget(ingredientList)
        horLayout.add_widget(MDLabel(
                    text="=>",
                    font_style="H1",
                    halign="center"
            ))
        horLayout.add_widget(cocktailList)

        pageLayout = MDBoxLayout(orientation='vertical', padding=[50,0,50,25])
        pageLayout.add_widget(vertLayout)
        pageLayout.add_widget(horLayout)

        self.add_widget(pageLayout)
    
    def initSecPage(self, cocktails, pumps):
        vertLayout = MDGridLayout(cols=1,padding=[100,0,100,0])

        additional = set()
        for cocktail in cocktails:
            for item in cocktail.additional:
                additional.add(item)

        vertLayout.add_widget(
            MDLabel(
                    text="Additional ingredients required",
                    font_style="H4",
                    halign="center",
                    size_hint=(1, 0.5)
            )
        )
        
        for item in additional:
            vertLayout.add_widget(MDLabel(
                    text=item,
                    font_style="H6",
                    halign="center"
            ))

        self.add_widget(vertLayout)

        
        

