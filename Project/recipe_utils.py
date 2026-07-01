"""
Trial Recipes Module
Trial functions for the Recipe Manager project. Yippe!
"""
import pandas as pd
import uuid
import os
from datetime import date, datetime, timedelta

recipes_location = "./data/recipes.csv"
recipe_columns = ["recipe_id", "name", "ingredients", "prep_time", 
                  "instructions", "difficulty",  "rating"]

def load_recipes():
    """Loads all the recipes in the dataframe."""
    file_exists = os.path.exists(recipes_location)
    if file_exists:
        recipes_df = pd.read_csv(recipes_location)
        print("\nThe dataframe recipes.csv exists. Here are the available recipes:")
    else:
        recipes_df = pd.DataFrame(columns=recipe_columns)
        recipes_df.to_csv(recipes_location, header=True, index=False)
        print("\nA new recipes.csv has been created")
    return recipes_df

def view_all_recipes():
    """Displays all recipes with key details."""
    recipes_df = load_recipes()
    if recipes_df.empty:
        print("No recipes found. Please add one first!")
    else:
        print("\n=== All Recipes ===")
        print(recipes_df[['name', 'prep_time', 'difficulty']].to_string(index=False))
        input("\nPress 'Enter' to return to the main menu")
        # Shouldnt there be an option to just exittttttttt IM SO DONE W THIS 
        
def load_random_recipe():
    """Returns a random recipe suggestion."""
    recipes_df = load_recipes()
    if recipes_df.empty:
        print("No recipes found. Please add a recipe first!")
    else:
        random_recipe = recipes_df.sample(n=1).iloc[0]
        print("Here is your random recipe suggestion:")
        print(f"Name: {random_recipe['name']}")
        print(f"Difficulty: {random_recipe['difficulty']}")
        print(f"Prep-time: {random_recipe['prep_time']} minutes")
        print(f"Ingredients: {random_recipe['ingredients']}")
        print(f"Instructions: {random_recipe['instructions']}")

# Zahra 

def add_new_recipe():
    """
    This function will let user add new recipe
    Args: None
    Returns: name of the recipe
    Done By: Zahra Ali Hasan
    """

    print('Enter the recipe name:')
    recipe_id = str(uuid.uuid4())[:8]
    name = input().strip().capitalize()


    def ingrediantss():
            """
            This function will let user add list of ingredients
            Args: None
            Returns: list of ingredients
            Done By: Zahra Ali Hasan
            """
            while True:
                ingredients = []
                print('Add list of ingredients & write "stop" when u are done:')
    
                while True:
                    user_input = input(' ')
                    if user_input.lower().strip() == "stop":
                        break
                    if user_input.strip() != "":
                        ingredients.append(user_input.strip())
    
                if len(ingredients) == 0:
                    print(' Error: You must enter at least one ingredient! Please try again')
                else:
                    return ingredients
    
    ingredients_str = ingrediantss()


    def timing():
            """
            This function will let user add preparation time
            Args: None
            Returns: return preparation time
            Done By: Zahra Ali Hasan
            """
            while True:
                print('Enter preparation time (in minutes):')
                try:
                    prep_time_input = int(input())
    
                    if prep_time_input >= 0:
                        return prep_time_input
                    else:
                        print("Invalid input! Time cannot be negative. Please try again.")
                except ValueError:
                    print("Invalid input! It is not an integer. Please try again.")
    
    prep_time_input = timing()


    def instructionss():
            """
            This function will let user enter cooking instructions
            Args: None
            Returns: return  cooking instructions
            Done By: Zahra Ali Hasan
            """
            print('Enter cooking instructions: ')
            instructions = input().strip()
            return instructions
    
    instructions = instructionss()


    def difficulty_level():
            """
            This function will let user enter difficulty level
            Args: None
            Returns: return difficulty level
            Done By: Zahra Ali Hasan
            """
            print('Enter difficulty level (Easy, Medium, Hard): ')
            difficulty = input().strip().lower()
            return difficulty
    
    difficulty = difficulty_level()

    def rating():
            """
            This function will let user Rate the recipe from 1-5
            Args: None
            Returns: return recipe rate
            Done By: Zahra Ali Hasan
            """
            while True:
                print('Rate the recipe from 1-5:')
                the_rate = float(input())
    
                try:    
                    if 1 <= the_rate <= 5:
                        return the_rate
                    else:
                        print('Oops! Please rate again in the range (1 to 5).')
                except ValueError:
                    print('Invalid input! Please enter a number between 1 and 5.')
    
    the_rate = rating()
    
    new_recipe_data = {
            "recipe_id": recipe_id,
            "name": name,
            "ingredients": [ingredients_str],
            "prep_time": [prep_time_input],
            "instructions": [instructions],
            "difficulty": [difficulty],
            "recipe_rating": the_rate
        }
    
    df = pd.DataFrame(new_recipe_data)
    
    file_exists = os.path.exists(recipes_location)
    df.to_csv(recipes_location, mode='a', index=False, header=not file_exists)


# Ohood

def search_by_ingredient():
    """
    This function searches the database and filters all recipes containing the requested ingredient.
    Args:ingredient (str): The name of the ingredient to look for.
    Returns:DataFrame: A pandas DataFrame containing the filtered recipe names.
    Done By: Ohood Majed Ahmed
    """
    df = load_recipes()

    search_ing = input("\nPlease write your preferred ingredient below:").strip().lower()
    
    result = df[df['ingredients'].str.lower().str.contains(search_ing, na = False)]

    if result.empty:
        print("No recipe with such ingredient :(")
        return pd.DataFrame()  
    else:
        result_filtered_by_ing = result[['name', 'ingredients', 'instructions', 'prep_time']].reset_index(drop=True)
        return result_filtered_by_ing
    

def view_all_recipes():
    """
    This function returns the complete list of recipes loaded from the CSV database as a DataFrame.

    Args: None
    Returns:DataFrame: A pandas DataFrame containing all recipe details from the database.
    Done By: Ohood Majed Ahmed
    """
    recipes = load_recipes()

    if recipes.empty:
        print("\n Oh no! Your recipe book is currently empty, add a recipe first.")
    
    else:
        print("\n--- All Recipes ---")
        df_filtered = recipes[['name', 'ingredients','prep_time']]
        display(df_filtered)



def view_recipes_sorted_by_rating():
    """
    This function loads all recipes and returns them sorted by their existing rating.
    Args: None
    Returns:
        DataFrame: A pandas DataFrame containing recipe names and ratings sorted.
    Done By: Ohood Majed Ahmed
    """
    df = load_recipes()

    df['recipe_rating'] = pd.to_numeric(df['recipe_rating'], errors='coerce')
    df_sorted = df.sort_values(by='recipe_rating', ascending=False)

    df_filtered_sorted = df_sorted[['name', 'recipe_rating']]
    df_filtered_sorted.columns = ['Recipe Name', 'Rating']
    
    if df_filtered_sorted.empty:
        print("\n Your recipe book is currently empty, please add a new recipe!.")
    else:
        display(df_filtered_sorted)





# Menu 


def display_menu():
    """Display the main menu options."""
    print("\n=== Ctrl + Eat: Recipe Manager ===")
    print("1. Add a new recipe.")
    print("2. Search for recipe by ingredient.")
    print("3. View all recipes.")
    print("4. View recipe sorted by rating")
    print("5. View a random recipe.")
    print("6. Exit")
    return input("Enter your choice (1-6): ")

def main():
    """Main application function."""
    print("Welcome to your all-inclusive recipe tracker, Ctrl + Eat!")
    print("This app helps you add your favorite recipes and search through them. Ready to eat?")
    while True:
        choice = display_menu()
        if choice == '1':
            add_new_recipe()
            
        elif choice == '2':
            search_by_ingredient()
            
        elif choice == '3':
            view_all_recipes()
            
        elif choice == '4':
             view_recipes_sorted_by_rating()
            
        elif choice == '5':
            load_random_recipe()
            
        elif choice == '6':
            print("Thank you for using Ctrl + Eat, hope you're no longer hungry!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
