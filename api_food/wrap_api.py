from api_food.spoon import url_api,search,portion,calculate_gr
from api_food.show_ingr import product_macro,csv_meal,food_added,total_macros
from api_food.actual_macros import fetch_user_macros
from manual_track.manual_functions import remain,dict_macro

def calling():
    """Calls Open Food Facts API
    This function :
    - Ask the user for a food item and return an OpenFoodFacts API search URL.
    - Search food with API.
    - If the food is not founded will return None.
    - Personalized user macros in based on food selected.
    - Shows to user macros.
    - Food saved in a csv file.

    Returns:
    float : Macros in gr 
    """
    while True:
        url = url_api()
        name,calories, protein_100g, carbs_100g, fat_100g = search(url)
        if name is None: 
            print(" Food not found,try again")
            continue  
        break


    grams = portion()
    total_cal, total_prote, total_carb, total_fat = calculate_gr(
        calories, protein_100g, carbs_100g, fat_100g, grams
    )
    m_cal,m_prote,m_carb,m_fat=product_macro(total_cal, total_prote, total_carb, total_fat)
    file,meal_api=csv_meal(name,m_cal,m_prote,m_carb,m_fat)         

    return total_cal, total_prote, total_carb, total_fat


def show_food():
    """
     Calculate and display the user's remaining calories and macros based on logged food.

    This function:
    - Retrieves the list of foods added by the user.
    - Computes total macros and calories from the logged food.
    - Fetches the user's daily macro goals.
    - Compares goals vs current intake.
    - Displays the remaining macros/calories.
    
    Returns:
        tuple: (total_calories, total_protein, total_carbs, total_fat)
        - total_calories (float): Sum of calories consumed.
        - total_protein (float): Sum of protein consumed.
        - total_carbs (float): Sum of carbohydrates consumed.
        - total_fat (float): Sum of fats consumed.
    """
    see=food_added()
    food_cal,food_prote,food_carb,food_fat=total_macros(see)
    name_main,fat_main,prote_main,carb_main,calories_main=fetch_user_macros()
    goal,current=dict_macro(fat_main, prote_main, carb_main, calories_main,
              food_fat,food_prote,food_carb,food_cal)
    remain(goal,current)
    return food_cal,food_prote,food_carb,food_fat

    