from kivy.uix.screenmanager import Screen
from kivymd.uix.carousel import Carousel
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

from GPButton import GPButton

import time

fullscreen = 0
debug = 2

if(debug==1):
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    for p in range (1, 37):
        GPIO.setup(p, GPIO.OUT)
else:
    print(f'\033[93m[WRN] debug variable is set -> no GPIO \033[0m')

class Program(MDApp):

    def build(self):
        screen = Screen(size=(800,480))
        root = GridLayout(cols=2, rows = 3, padding = 10, spacing=10)

        btn1 = GPButton(24,11,icon="cup",user_font_size="148sp")
        btn2 = GPButton(18,23,icon="cup",user_font_size="148sp")
        btn3 = GPButton(19,26,icon="cup",user_font_size="148sp")
        btn4 = GPButton(6,13,icon="cup",user_font_size="148sp")
        btn5 = GPButton(27,22,icon="cup",user_font_size="148sp")
        btn6 = GPButton(4,17,icon="cup",user_font_size="148sp")

        root.add_widget(btn2)
        root.add_widget(btn1)
        root.add_widget(btn4)
        root.add_widget(btn3)
        root.add_widget(btn6)
        root.add_widget(btn5)

        screen.add_widget(root)

        return screen


if __name__ == '__main__':
    if fullscreen==1:
        Window.fullscreen = 'auto'
    Program().run()
