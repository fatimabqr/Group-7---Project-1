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
                  "instructions", "difficulty", "recipe_rating", "category", "times_cooked", "last_cooked"]

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

def load_random_recipe():
    """Returns a random recipe suggestion."""
    recipes_df = load_recipes()
    if recipes_df.empty:
        print("No recipes found. Please add a recipe first!")
    else:
        random_recipe = recipes_df.sample(n=1).iloc[0]
        print("Here is your random recipe suggestion:")
        print(f"Name: {random_recipe['name']}")
        print(f"Category: {random_recipe['category']}")
        print(f"Difficulty: {random_recipe['difficulty']}")
        print(f"Prep-time: {random_recipe['prep_time']} minutes")
        print(f"Ingredients: {random_recipe['ingredients']}")
        print(f"Instructions: {random_recipe['instructions']}")

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

    def category():
        """
        This function will allow the user to categorize the recipe into the following categories: 
        ('Breakfast', 'Lunch', 'Dinner', 'Snack', 'Drink', 'Dessert')
        -Fatima
        """
        category_list = ['Breakfast', 'Lunch', 'Dinner', 'Snack', 'Drink', 'Dessert']
        while True:
            print("What would you categorize this recipe as? Please pick one of the following:\n('Breakfast', 'Lunch', 'Dinner', 'Snack', 'Drink')")
            category_input = input().strip().capitalize()
            if category_input in category_list:
                return category_input
            else:
                print("Oops! That's not a valid category. Please try again.")

    category_input = category()

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
        Returns: return cooking instructions
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
        Done By: Zahra Ali Hasan, edited by fatooma <3
        """
        difficulty_catg = ['easy', 'medium', 'hard']
        
        while True:
            print('Enter difficulty level (Easy, Medium, Hard): ')
            difficulty_input = input().strip().lower()
            if difficulty_input in difficulty_catg:
                return difficulty_input  
            else:
                print("Invalid difficulty level. Please try again!")

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
            try:
                the_rate = float(input())
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
        "category": category_input,
        "ingredients": ", ".join(ingredients_str),
        "prep_time": prep_time_input,
        "instructions": instructions,
        "difficulty": difficulty,
        "recipe_rating": the_rate,
        "times_cooked": 0,
        "last_cooked": ""
    }

    recipes_df = load_recipes()
    recipes_df = pd.concat([recipes_df, pd.DataFrame([new_recipe_data])], ignore_index=True)
    recipes_df.to_csv(recipes_location, index=False)
    print(f"\nRecipe '{name}' added successfully!")

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


def view_category_recipe():
    """
    This function returns a list of all the recipes under a specific food category. The categories are as follows:
    ('Breakfast', 'Lunch', 'Dinner', 'Snack', 'Drink', 'Dessert')
    -fatooma
    """
    df = load_recipes()
    if df.empty:
        print("Uh Oh! No recipes found. Please add a recipe first.")
        return pd.DataFrame()
    
    category_list = ['Breakfast', 'Lunch', 'Dinner', 'Snack', 'Drink', 'Dessert']
    print("Which category would you like to view? Here are the categories:\n('Breakfast', 'Lunch', 'Dinner', 'Snack', 'Drink', 'Dessert')")
    
    while True:
        category_search_input = input("Enter category: ").strip().capitalize()
        if category_search_input in category_list:
            break
        else:
            print("LOL thats not a valid category. I know you're hangry but please try again.")
            continue  
            
    result = df[df['category'].str.capitalize() == category_search_input]
    
    if result.empty:
        print(f"\nNo recipes found under '{category_search_input}'. Sorry!")
        return pd.DataFrame()
    else:
        print(f"\n{category_search_input} recipes:")
        return result


# Menu 


def display_menu():
    """Display the main menu options."""
    print("\n=== Ctrl + Eat: Recipe Manager ===")
    print("1. Add a new recipe.")
    print("2. Search for recipe by ingredient.")
    print("3. View all recipes.")
    print("4. View recipe sorted by rating")
    print("5. In the mood for a certain category?")
    print("6. View a random recipe.")
    # print("leave a rating?")
    print("7. Exit")
    return input("Enter your choice (1-7): ")

def main():
    """Main application function."""
    print("Welcome to your all-inclusive recipe tracker, Ctrl + Eat!")
    print("This app helps you add your favorite recipes and search through them. Ready to eat?")
    while True:
        choice = display_menu()
        if choice == '1':
            add_new_recipe()

            print("\nWhat would you like to do next?")
            print("\n Press 'Enter' to return to the main menu or '7' to exit.")
            follow_up_input = input("Your choice, we wont get mad: ").strip()

            if follow_up_input == '7':
                print("Thank you for using Ctrl + Eat, hope you're no longer hungry!")
                break
                  
        elif choice == '2':
            result = search_by_ingredient()
            if result is not None and not result.empty:
                display(result)

            print("\nWhat would you like to do next?")
            print("\n Press 'Enter' to return to the main menu or '7' to exit.")
            follow_up_input = input("Your choice, we wont get mad: ").strip()

            if follow_up_input == '7':
                print("Thank you for using Ctrl + Eat, hope you're no longer hungry!")
                break
                
        elif choice == '3':
            view_all_recipes()

            print("\nWhat would you like to do next?")
            print("\n Press 'Enter' to return to the main menu or '7' to exit.")
            follow_up_input = input("Your choice, we wont get mad: ").strip()

            if follow_up_input == '7':
                print("Thank you for using Ctrl + Eat, hope you're no longer hungry!")
                break
                
        elif choice == '4':
            view_recipes_sorted_by_rating()

            print("\nWhat would you like to do next?")
            print("\n Press 'Enter' to return to the main menu or '7' to exit.")
            follow_up_input = input("Your choice, we wont get mad: ").strip()

            if follow_up_input == '7':
                print("Thank you for using Ctrl + Eat, hope you're no longer hungry!")
                break

        elif choice == '5':
            result = view_category_recipe()
            if result is not None and not result.empty:
                display(result)

            print("\nWhat would you like to do next?")
            print("\n Press 'Enter' to return to the main menu or '7' to exit.")
            follow_up_input = input("Your choice, we wont get mad: ").strip()
        
            if follow_up_input == '7':
                print("Thank you for using Ctrl + Eat, hope you're no longer hungry!")
                break
                
        elif choice == '6':
            load_random_recipe()

            print("\nWhat would you like to do next?")
            print("\n Press 'Enter' to return to the main menu or '7' to exit.")
            follow_up_input = input("Your choice, we wont get mad: ").strip()

            if follow_up_input == '7':
                print("Thank you for using Ctrl + Eat, hope you're no longer hungry!")
                break
                
        elif choice == '7':
            print("Thank you for using Ctrl + Eat, hope you're no longer hungry!")
            break
                
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
