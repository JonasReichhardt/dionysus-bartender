import json

class CocktailDataProvider():
    def __init__(self,file):
        self.file = file
    
    def load(self):
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