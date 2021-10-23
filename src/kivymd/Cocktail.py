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

    def loadCocktails(self, ingredients):
        cocktails = self.loadFromFile()
        makeableCocktails = []

        # only return cocktail if every ingredient is connected to a pump
        for c in cocktails:
            makeable = all(elem in ingredients for elem in c.ingredients)
            if makeable:
                makeableCocktails.append(c)

        return makeableCocktails


class Cocktail():
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def make(self, pumps):
        for key, value in self.ingredients.items():
            for pump in pumps:
                if pump.ingredient == key:
                    pump.activate(value)
