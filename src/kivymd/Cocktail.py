import json

class CocktailFactory():
    def __init__(self,file):
        self.file = file

    def loadFromFile(self):
        with open(self.file) as data:
            cocktails = json.load(data)["cocktails"]
            data = []
            for cocktail in cocktails:
                name = cocktail["name"]
                ingredients = cocktail["ingredients"]
                data.append(Cocktail(name,ingredients))
            return data

class Cocktail():
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def make(self, pumps):
        for key, value in self.ingredients.items():
            for pump in pumps:
                if pump.ingredient == key:
                    pump.activate(value)
