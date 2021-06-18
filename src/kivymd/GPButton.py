from kivymd.uix.button import MDIconButton
from kivymd.uix.behaviors import MagicBehavior

debug = 0

class GPButton(MDIconButton, MagicBehavior):
    def __init__(self,pin1,pin2,**kwargs):
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
        self.grow()
        if(debug==1):
            GPIO.output(self.pin1, GPIO.HIGH)
        else:
            print(f'\033[93m[INF] gpio {self.pin1} | high\033[0m')
    

    def on_release(self):
        self.shrink()
        if(debug==1):
            GPIO.output(self.pin1, GPIO.LOW)
        else:
            print(f'\033[93m[INF] gpio {self.pin1} | low\033[0m')