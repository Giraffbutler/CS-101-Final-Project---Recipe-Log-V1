class Recipe:
    def __init__(self, name, recipe_file = None):
        self.name = name
        self.recipe_file = recipe_file

    def __repr__(self):
        return f'This recipe contains infomation on how to make {self.name}.'

    def get_ingredients(self):
        pass

    def has_ingredients(self):
        ingredients = input('Input any ingredients you want to search for separated by a space\n').split()
        with open(self.recipe_file, 'r') as current:
            current = current.read().upper()
            for ingredient in ingredients:
                if ingredient.upper() in current:
                    print(f'The recipe does contain {ingredient}')
                else:
                    print(f'The recipe does not contain {ingredient}')
        return