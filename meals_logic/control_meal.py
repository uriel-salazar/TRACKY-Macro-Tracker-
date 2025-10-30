
import pandas as pd
import os 

from open_food.wrap_api import fetch_user_macros
def manual_track():
    """ The user enters their macros in a manual way 

    Returns:
        dict: User's Macros dict
    """
    control_meal = {"meals": {}}

    while True:
        print("--Quick Add---")
        meal_type = input("Type of Meal : ").upper()
        name_food = input("Description: ")
        cal_food = int(input("Energy (cal): ")) 
        prote_food = int(input("Protein (g): "))
        carb_food = int(input("Carb (g): "))
        fat_food = int(input("Enter your fat value (g): "))
        save_it = input("Save it? (yes/no): ")

        if save_it.lower() == "yes":
            control_meal["meals"][meal_type] = {
            "Description": name_food,
            "Calories": cal_food,
            "Protein": prote_food,
            "Carbs": carb_food,
            "Fats": fat_food
            }
            print("Your info :")
            print("-----")
            for meal_type, info in control_meal["meals"].items():
                print(f"{meal_type}")
                print(f"Cal :{info["Calories"]}")
                print(f"Protein :{ info["Protein"]}")
                print(f"Carb:{info["Carbs"]}")
                print(f"Fats : {info["Fats"]}")
        elif save_it.lower()!="yes":
            break
        repeat = input("Do you want to add another meal? (yes/no): ")
        if repeat.lower() != "yes":
            break  
        
    return control_meal
    
    
    

def method_track():
    """ Shows a menu for track your macros 

    Returns:
        dict: Dict manual macros 
    """
    meals={}
    while True:
        print("--- Tracking your macros manually ---")
        print("1.Enter your food manually")
        print("2. Check you food registered food ")
        print("3.Check your total macros  ")
        print("4.Exit ")
        option=int(input("What are you going to choose?:"))
        if option == 1:
            meals = manual_track()
        elif option == 2:
            if meals:
                number_save=track_macro_all(meals)
            else:
                print(" ⚠️ First you have to track your food ⚠️")
        elif option == 3:
            dat_cal,dat_prote,dat_carb,dat_fats=calculate()
            name_main,fat_main,prote_main,carb_main,calories_main=fetch_user_macros()
            goal,current=goal_macro(fat_main,prote_main,carb_main,calories_main,
                       dat_fats,dat_prote,dat_carb,dat_cal)
            remain(goal,current)
        elif option == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
    
    return meals


    
    

def track_macro_all(control_meal):
    """ Saves a csv file according with user's macros

    Args:
        control_meal (dict): _description_

    Returns:
        DataFrame: User's macros file
    """
    rows = []
    for meal_type, info in control_meal["meals"].items():
            rows.append({
            "Meal": meal_type,
            "Description": info["Description"],
            "Calories": info["Calories"],
            "Protein": info["Protein"],
            "Carbs": info["Carbs"],
            "Fats": info["Fats"]
        })

    number_save = pd.DataFrame(rows)
    print("Your macros in gr:")
    print(number_save)

    file_macro = "manually_macros.csv"
    if not os.path.exists(file_macro):
        number_save.to_csv(file_macro, index=False, header=True)
    else:
        number_save.to_csv(file_macro, mode='a', header=False, index=False)
    return number_save

def calculate():
    """ Adds user's macros

    Returns:
        int: Total Macros 
    """
    read_macros=pd.read_csv("manually_macros.csv")
    read_macros.columns = read_macros.columns.str.strip() 
    dat_cal=read_macros['Calories'].sum()
    dat_prote=read_macros["Protein"].sum()
    dat_carb=read_macros["Carbs"].sum()
    dat_fats=read_macros["Fats"].sum()
    
    print(dat_cal,"Calories")
    print("Protein :",dat_prote,"gr")
    print(f'Carbs :{dat_carb} gr')  ##
    print(f'Fats : {dat_fats} gr')
    return dat_cal,dat_prote,dat_carb,dat_fats
    

def food_added():
    """Reads meals searched on food_data.csv
    The user can decide whether conserve them or not 
    """
    print("--- Just added 🔥 ---")
    show=pd.read_csv("manually_macros.csv")
    print(show)
    conserve=input("Are you going to conserve this food? (yes/no)")
    if conserve=="yes":
        pass
    else:
    
        print("Foods eliminated !")  
        os.remove("manually_macros.csv")
    return show


    
def goal_macro(fat_goal, prote_goal, carb_goal, cal_goal, 
               fat_u, prote_u, carb_u, cal_u):
    """Shows the user their remaining calories"""

    # Convert all to integers
    fat_goal = int(fat_goal)
    prote_goal = int(prote_goal)
    carb_goal = int(carb_goal)
    cal_goal = int(cal_goal)
    fat_u = int(fat_u)
    prote_u = int(prote_u)
    carb_u = int(carb_u)
    cal_u = int(cal_u)

    goal = {
        "cal": cal_goal,
        "carb": carb_goal,
        "prote": prote_goal,
        "fat": fat_goal
    }

    current = {
        "cal": cal_u,
        "carb": carb_u,
        "prote": prote_u,
        "fat": fat_u
    }

    return goal, current


def remain(goals, current):
    remaining_user = {}
    print(" ---Macro summary ---")
    
    # Loop through each key (carb, prote, etc.)
    for key in goals:
        diff = goals[key] - current.get(key, 0)
        remaining_user[key] = diff

        if diff < 0:
            print(f"{key.upper()}: Over by {-diff}")
        else:
            print(f"{key.upper()}: Remaining {diff}")

    return remaining_user