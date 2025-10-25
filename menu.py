from texts import activity_level
from wrap_up import info_and_bmr
from control import TDEE
from wrap_up import info_and_bmr,set_macros
from open_food.wrap_api import calling
from meals_logic.control_meal import method_track
from open_food.actual_macros import remaining
def menu_user():
    """ Prints a menu that shows the available options to the user
    """
    completed_info=False
    while True:
        print(" --- Macro Tracker --- ")
        print("1.Calculate your BMR : ")
        print(" 2 .Calculate your TDEE ")
        print("3. Search ingredient ")
        print("4. Calculate your daily macros (manual/api)")
        choice=int(input("Choice a number (1/2/3/4):"))
        if choice==1:
            value_bmr,wg,name,gre=info_and_bmr()
            completed_info=True
        
        elif choice==2:
            if completed_info:
                type_act,activity = activity_level() #Type of activity 
                show_tdee=TDEE(activity,type_act,value_bmr) #Calculates your TDEE in base of your activity
                set_macros(wg,name,show_tdee)
            else:
                print("First,you must fill your basic information.")
        elif choice==3:
            calling()
            remaining(gre)
            
            
        elif choice==4:
            method_track()
            
        else:
            print("Please,Enter a valid number")
            
            
            
        