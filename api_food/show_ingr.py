import os
from calculating_macros.show_text import clear_console
from calculating_macros.verify.verify_input import valid_word
import pandas as pd
def product_macro(m_cal:int ,m_prote:int,m_carb:int,m_fat:int):
    """ Prints user's macros 

    Args:
        m_cal (float): Calories_grams 
        m_prote (float): Protein grams
        m_carb (float): Carb grams
        m_fat (float): Fat grams 

    Returns:
        int: Personalized user's macros 
    """
    print(f"Calories :{m_cal}kcal")
    print(f"Protein :{m_prote}")
    print(f"Carbs :{m_carb}")
    print(f"Fats:{m_fat}")
    return m_cal,m_prote,m_carb,m_fat
     
    
def csv_meal(name_food,calories,protein,carb,fat):
    """ Creates a csv file for each meal searched on Open Food Facts

    Args:
        name_food (srt): name of the food (gr)
        calories (int): calories of the food  (gr)
        protein (int): protein of the food (gr)
        carb (int): carbs of the food (gr)
        fat (int): fats of the food 

    Returns:
        DataFrame: Panda's Data Frame from Open Food Facts API
    """
    name_food=str(name_food)
    calories=int(calories)
    protein=int(protein)
    carb=int(carb)
    fat=int(fat)
    meal_api=pd.DataFrame([{
        "Name Meal":name_food,
        "Calories Meal":calories,
        "Prote Meal":protein,
        "Carb Meal":carb,
        "Fat Meal":fat
    }])
    print("Your food : ")
    print(meal_api.to_string(index=False))
    file="food_data.csv"
    if not os.path.exists(file):
        meal_api.to_csv(file,index=False,header=True)
    else:
        meal_api.to_csv(file,mode='a',header=False,index=False)

    return meal_api,file


def food_added(): 
    """Reads meals searched on food_data.csv
    The user can decide whether conserve their meals or not. 
    You can eliminate your meals data if you want
    
    Returns:
    (DataFrame):csv readable about macros
     
    """
    print("--- Just added 🍛---")
    see=pd.read_csv("food_data.csv")
    print(see)
    conserve=valid_word("Are you going to conserve this food? (yes/no)",["yes","no"]).lower()
    if conserve=="yes":
        pass
    else:
        clear_console()
        print("Foods eliminated !")  
        os.remove("food_data.csv")
    return see
        

def total_macros(read):
    """ Adds all the user macros and shows them to the user.

    Args:
        read (DataFrame):csv readable about macros

    Returns:
        food_cal,food_prote,food_carb,food_fat : Macros in total 
    """
    print("-Summary- ")
    food_cal=read["Calories Meal"].sum()
    food_prote=read["Prote Meal"].sum()
    food_carb=read["Carb Meal"].sum()
    food_fat=read["Fat Meal"].sum()
    
    print(f"Calories :{food_cal:.0f} gr")
    print(f"Protein  :{food_prote:.0f}gr")
    print(f'Carbs    :{food_carb:.0f} gr')
    print(f'Fats     :{food_fat:.0f} gr')
    return food_cal,food_prote,food_carb,food_fat

    
    

