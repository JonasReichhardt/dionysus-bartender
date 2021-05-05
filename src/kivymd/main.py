from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.gridlayout import MDGridLayout


class MainApp(MDApp):
    def build(self):
        screen = Screen(size=(800,480))
        layout = MDGridLayout(cols=2, rows = 3, padding = 10, spacing=10)

        layout.add_widget(
            MDRectangleFlatButton(
                text="Pump 1"
            )
        )
        layout.add_widget(
            MDRectangleFlatButton(
                text="Pump 2"
            )
        )
        layout.add_widget(
            MDRectangleFlatButton(
                text="Pump 3"
            )
        )
        layout.add_widget(
            MDRectangleFlatButton(
                text="Pump 4"
            )
        )
        layout.add_widget(
            MDRectangleFlatButton(
                text="Pump 5"
            )
        )
        layout.add_widget(
            MDRectangleFlatButton(
                text="Pump 6"
            )
        )
        screen.add_widget(layout)
        return screen


MainApp().run()