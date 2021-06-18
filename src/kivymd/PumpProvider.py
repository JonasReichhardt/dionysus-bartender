import json

class PumpDataProvider():
    def __init__(self,file):
        self.file = file
    
    def load(self):
        with open(self.file) as data:
            pumps = json.load(data)["pumps"]
            data = []
            for pump in pumps:
                pins = pump["pins"]
                ingredient = pump["ingredient"]
                flowrate = pump["flowrate"]
                data.append(Pump(pins,ingredient,flowrate))
            return data

class Pump():
    def __init__(self, pins, ingredient, flowrate):
        self.ingredient = ingredient
        self.pins = pins
        self.flowrate = flowrate