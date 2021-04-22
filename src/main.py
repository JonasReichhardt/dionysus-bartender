from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.carousel import Carousel
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.carousel import Carousel
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout


import time

fullscreen = 1
debug = 2

if(debug==1):
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM) 
    for p in range (1, 37):
        GPIO.setup(p, GPIO.OUT)
else:
    print(f'\033[93m[WRN] debug variable is set -> no GPIO \033[0m')        

Builder.load_string('''
''')

class GPButton(Button):

    def __init__(self,pin1,pin2, **kwargs):
        super(GPButton, self).__init__(**kwargs)
        self.pin1=pin1
        self.pin2=pin2
    
    def get_pin1(self):
        return self.pin1

    def get_pin2(self):
        return self.pin2
    
    def set_pin1(self, value):
        self.pin1 = value

    def set_pin2(self, value):
        self.pin2 = value
    
    _pin1 = property(get_pin1, set_pin1)
    _pin2 = property(get_pin2, set_pin2)

    def on_press(self):
        if(debug==1):
            GPIO.output(self.pin1, GPIO.HIGH)
        else:
            print(f'\033[93m[INF] gpio {self.pin1} | high\033[0m')
    

    def on_release(self):
        if(debug==1):
            GPIO.output(self.pin1, GPIO.LOW)
        else:
            print(f'\033[93m[INF] gpio {self.pin1} | low\033[0m')

class Program(App):

    def build(self):
        root = Carousel()
        page1 = GridLayout(cols=2, rows = 3, padding = 10, spacing=10)

        btn1 = GPButton(24,11,text='Pump 2',size=(75,50),size_hint=(.5,.25))
        btn2 = GPButton(18,23,text='Pump 1')
        btn3 = GPButton(19,26,text='Pump 4')
        btn4 = GPButton(6,13,text='Pump 3')
        btn5 = GPButton(27,22,text='Pump 6')
        btn6 = GPButton(4,17,text='Pump 5')

        page1.add_widget(btn2)
        page1.add_widget(btn1)
        page1.add_widget(btn4)
        page1.add_widget(btn3)
        page1.add_widget(btn6)
        page1.add_widget(btn5)

        page2 = AnchorLayout()
        img = Image(source='res\\img\\coke.png')
        page2.add_widget(img)

        page3 = AnchorLayout()
        img = Image(source='res\\img\\martini.png')
        page3.add_widget(img)

        page4 = AnchorLayout()
        img = Image(source='res\\img\\dik.png')
        page4.add_widget(img)
        
        # add pages to carousel
        root.add_widget(page1)
        root.add_widget(page2)
        root.add_widget(page3)
        root.add_widget(page4)
        
        return root


if __name__ == '__main__':
    Window.clearcolor = (1,1,1,1)
    if fullscreen==1:
        Window.fullscreen = 'auto'
    Program().run()
