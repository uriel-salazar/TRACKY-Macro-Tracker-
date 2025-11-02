from api_food.wrap_api import fetch_user_macros
from manual_track.manual_functions import track,save_meal,calculate_macros,dict_macro,remain
from calculating_macros.verify.verify_input import verify
 
def manually_track():
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
        option=verify("What are you going to choose?:",minim=1,maxim=4)
        if option == 1:
            meals = track()
        elif option == 2:
            if meals: 
                number_save=save_meal(meals)
            else:
                print(" ⚠️ First you have to track your food ⚠️")
        elif option == 3:
            dat_cal,dat_prote,dat_carb,dat_fats=calculate_macros()
            name_main ,fat_main,prote_main,carb_main,calories_main=fetch_user_macros()
            goal,current=dict_macro(fat_main,prote_main,carb_main,calories_main,
                       dat_fats,dat_prote,dat_carb,dat_cal)
            remain(goal,current)
        elif option == 4:
            print("Goodbye!")
            break
    
    return meals


    
    

