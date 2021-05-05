from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from GPButton import GPButton

class MainApp(MDApp):
    def build(self):
        screen = Screen(size=(800,480))

        screen.add_widget(
            GPButton(
                25,25,
                text="Pump 1", 
                icon="..\\res\\img\\coke.png", 
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                user_font_size="128sp"
            )
        )
        return screen

MainApp().run()