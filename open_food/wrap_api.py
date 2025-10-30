from open_food.spoon import cal_api,search,portion,calculate_gr
from open_food.show_ingr import product_macro,csv_meal,food_added,total_macros
from open_food.actual_macros import fetch_user_macros,goal_user
from meals_logic.control_meal import goal_macro,remain

def calling():
    url = cal_api()
    name,calories, protein_100g, carbs_100g, fat_100g = search(url)

    if  name and calories is None:
        print("Your food couldn't be calculated")
        return None, None, None, None  # Stop here safely

    # If product found
    grams = portion()
    total_cal, total_prote, total_carb, total_fat = calculate_gr(
        calories, protein_100g, carbs_100g, fat_100g, grams
    )
    m_cal,m_prote,m_carb,m_fat=product_macro(total_cal, total_prote, total_carb, total_fat)
    file,meal_api=csv_meal(name,m_cal,m_prote,m_carb,m_fat)         

    return total_cal, total_prote, total_carb, total_fat

def show_food():
    see=food_added() #
    food_cal,food_prote,food_carb,food_fat=total_macros(see)
    name_main,fat_main,prote_main,carb_main,calories_main=fetch_user_macros()
  #  goal_user(name_main, fat_main, prote_main, carb_main, calories_main,
          #    food_fat,food_prote,food_carb,food_cal)
    goal,current=goal_macro(fat_main, prote_main, carb_main, calories_main,
              food_fat,food_prote,food_carb,food_cal)
    remain(goal,current)
    return food_cal,food_prote,food_carb,food_fat

    