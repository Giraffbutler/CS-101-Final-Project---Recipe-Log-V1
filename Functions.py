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
            temp = line.split('\t')
            current_recipes.append(Recipe(temp[0], recipe_file = temp[1]))
    return current_recipes

def display_available_recipes(menu_return = True):
    current_recipes = retrieve_available_recipes()
    iter = 1
    for recipe in current_recipes:
        print(str(iter) + '. ' + recipe.name)
        iter += 1
    if menu_return == True:
        menu()

def enter_recipe():
    name = input('Enter a name for the recipe.\n')
    print('Select the recipe reference text file. \n')
    time.sleep(.5)
    recipe_filename = filedialog.askopenfilename(initialdir=os.getcwd())
    with open('Available_recipes.txt', 'a') as current_recipes:
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

def wait():
    input()
    menu()
                

def menu():
    choice = int(input('''What would you like to do?
    
    1. Enter a new recipe
    2. Delete an existing recipe
    3. Display available recipes
    4. Open Recipe
    5. Close program
    '''))

    actions = {1: enter_recipe, 2: '', 3: display_available_recipes, 4: open_recipe, 5: exit_program}
    actions[choice]()

def exit_program():
    print('Thanks for coming! Come back soon to log more recipes and do some more cooking!')
    quit()