from Classes import *
import tkinter as tk
from tkinter import filedialog
import os
import time

def initialize():
    print('Welcome to the EasyShare digital recipe recording/sharing tool!')

def retrieve_available_recipes():
    current_recipes = []
    with open('Available_recipes.txt', 'r') as recipes:
        recipes_string = recipes.read()
        for line in recipes_string.split('\n'):
            try:
                temp = line.split('\t')
                current_recipes.append(Recipe(temp[0], recipe_file = temp[1]))
            except:
                add_recipe = input('There are no recipes currently logged. Would you like to add one? Y/N \n')
                if add_recipe.upper() in ['Y','YES']:
                    enter_recipe()
                else:
                    menu()
    return current_recipes

def display_available_recipes(menu_return = True):
    current_recipes = retrieve_available_recipes()
    iter = 1
    for recipe in current_recipes:
        print(str(iter) + '. ' + recipe.name)
        iter += 1
    if menu_return == True:
        wait()

def enter_recipe():
    name = input('Enter a name for the recipe.\n')
    print('Select the recipe reference text file. \n')
    time.sleep(.5)
    recipe_filename = filedialog.askopenfilename(initialdir=os.getcwd())
    with open('Available_recipes.txt', 'r+') as current_recipes:
        if current_recipes.read() == '':
            current_recipes.write(name + '\t' + recipe_filename)
        else:
            current_recipes.write('\n'+ name + '\t' + recipe_filename)
    wait()
    
def open_recipe():
    display_available_recipes(False)
    my_recipe = input('\nWhat recipe would you like to look at?\n')
    with open('Available_recipes.txt', 'r') as recipes:
        for line in recipes.read().split('\n'):
            temp = line.split('\t')
            if my_recipe in temp[0]:
                with open(temp[1], 'r') as temp_2:
                    print(temp_2.read())
                    wait()
    print('Recipe not found')
    wait()

def edit_recipe():
    display_available_recipes(False)
    my_recipe = input('What recipe would you like to edit?\n')
    with open('Available_recipes.txt', 'r') as recipes:
        for line in recipes.read().split('\n'):
            temp = line.split('\t')
            if my_recipe in temp[0]:
                oscommand = 'notepad.exe ' + temp[1]
                os.system(oscommand)
                wait()
    print('Recipe not found')
    wait()

def check_for_ingredient():
    display_available_recipes(False)
    current_recipes = retrieve_available_recipes()
    choice = input('What recipe would you like to check for ingredients?\n')
    for recipe in current_recipes:
        if recipe.name == choice:
            recipe.has_ingredients()
    wait()

def delete_recipe():
    display_available_recipes(False)
    temp = input('What recipe would you like to delete?\n')
    with open('Available_recipes.txt', 'r') as recipes:
        recipes = recipes.read().split('\n')
        for item in recipes:
            recipe_name_file = item.split('\t')
            if temp in recipe_name_file[0]:
                delete = input(f'Delete recipe {recipe_name_file[0]}? Y/N \n').upper()
                if delete in ['Y', 'YES']:
                    delete_line = item
                else:
                    wait()
    with open('Available_recipes.txt', 'r+') as recipes_2:
        temp = recipes_2.read().split('\n')
        recipes_2.seek(0)
        for line in temp:
            if line != delete_line:
                recipes_2.write(line)
        recipes_2.truncate()
    wait()

def wait():
    input('continue?')
    menu()          

def menu():
    choice = int(input('''What would you like to do?
    
    1. Enter a new recipe
    2. Edit an existing recipe
    3. Delete an existing recipe
    4. Display available recipes
    5. Open Recipe
    6. Check for ingredient in recipe
    7. Close program

    '''))

    actions = {1: enter_recipe,2: edit_recipe, 3: delete_recipe, 4: display_available_recipes, 5: open_recipe, 6: check_for_ingredient, 7: exit_program}
    actions[choice]()

def exit_program():
    print('Thanks for coming! Come back soon to log more recipes and do some more cooking!')
    quit()