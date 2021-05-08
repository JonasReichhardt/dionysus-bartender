import json

class PumpDataProvider():
    def __init__(self,file):
        self.file = file
    
    def load(self):
        with open(self.file) as data:
            pumps = json.load(data)["pumps"]
            data = []
            for pump in pumps:
                name = pump["name"]
                pins = pump["pins"]
                ingredient = pump["ingredient"]
                data.append(Pump(name,pins,ingredient))
            return data

class Pump():
    def __init__(self, name, pins, ingredient):
        self.name = name
        self.ingredient = ingredient
        self.pins = pins