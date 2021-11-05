from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.uix.banner import MDBanner
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.carousel import Carousel
from kivymd.uix.list import *
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel

Builder.load_string('''
<ExampleBanner@Screen>

    MDBanner:
        id: banner
        text: ["One line string text example without actions."]
        # The widget that is under the banner.
        # It will be shifted down to the height of the banner.
        over_widget: screen
        vertical_pad: toolbar.height

    MDToolbar:
        id: toolbar
        title: "Example Banners"
        elevation: 10
        pos_hint: {'top': 1}

    MDBoxLayout:
        id: screen
        orientation: "vertical"
        size_hint_y: None
        height: Window.height - toolbar.height

        OneLineListItem:
            text: "Banner without actions"
            on_release: banner.show()

        Widget:
''')


class WelcomeCarousel(Carousel):

    def __init__(self, cocktails, pumps, **kwargs):
        super(WelcomeCarousel, self).__init__(**kwargs)
        self.initFirstPage(cocktails, pumps)
        self.initSecPage(cocktails, pumps)
        self.add_widget(MDLabel())

        return Factory.ExampleBanner()

    def initFirstPage(self, cocktails, pumps):
        ingredientList = MDList()
        cocktailList = MDList()

    def initSecPage(self, cocktails, pumps):
        vertLayout = MDGridLayout(cols=1, padding=[100, 0, 100, 0])


