from kivymd.uix.button import MDIconButton

class GPButton(MDIconButton):
    def __init__(self,cocktail,pumps,**kwargs):
        super(GPButton, self).__init__(**kwargs)
        self.cocktail = cocktail
        self.pumps = pumps

    def get_cocktail(self):
        return self.cocktail
    
    def set_cocktail(self, value):
        self.cocktail = value
    
    _cocktail = property(get_cocktail, set_cocktail)

    def on_press(self):
        self.disabled = True
        self.cocktail.make(self.pumps)
