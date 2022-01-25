class Recipe:
    def __init__(self, name, recipe_file = None):
        self.name = name
        self.recipe_file = recipe_file

    def __repr__(self):
        return f'This recipe contains infomation on how to make {self.name}.'

    def edit_name(self,new_name):
        self.name = new_name

    def get_ingredients(self):
        pass

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