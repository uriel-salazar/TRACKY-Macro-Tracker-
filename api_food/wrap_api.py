from api_food.spoon import url_api,search,portion,calculate_gr
from api_food.show_ingr import product_macro,csv_meal,food_added,total_macros
from api_food.actual_macros import fetch_user_macros
from manual_track.manual_functions import remain,dict_macro

def calling():
    """Calls Open Food Facts API
    Contains functions such as  searching user's product,adjust their portion,
    shows products macros and save it in a csv file. 

    Returns:
    float : Macros in gr
    """
    while True:
        url = url_api()
        name,calories, protein_100g, carbs_100g, fat_100g = search(url)
        if name is None:
            print("Not found try again")
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
    """ Wraps functions with  the purpose of showing remaining calories 


    Returns:
        _type_: _description_
    """
    see=food_added()
    food_cal,food_prote,food_carb,food_fat=total_macros(see)
    name_main,fat_main,prote_main,carb_main,calories_main=fetch_user_macros()
    goal,current=dict_macro(fat_main, prote_main, carb_main, calories_main,
              food_fat,food_prote,food_carb,food_cal)
    remain(goal,current)
    return food_cal,food_prote,food_carb,food_fat

    