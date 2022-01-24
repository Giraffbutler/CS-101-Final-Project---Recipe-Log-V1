class recipe:
    def __init__(self, name, ingredients = [], recipe_file = None):
        self.name = name
        self.ingredients = ingredients
        self.recipe_file = recipe_file

    def __repr__(self):
        return f'This recipe contains infomation on how to make {self.name}.'

    def has_ingredient(self,ingredients):
        if type(ingredients) is str:
            if ingredients in self.ingredients:
                print(f'The recipe does contain {ingredients}')
            else:
                print(f'The recipe does not contain {ingredients}')
        elif type(ingredients) is list:
            contained_ingredients = []
            for ingredient in ingredients:
                for item in self.ingredients:
                    if ingredient in item:
                        contained_ingredients.append(ingredient)
            print('The recipe contains the following ingredients:')
            for element in contained_ingredients:
                print(element)