from texts import activity_level
from wrap_up import info_and_bmr
from control import TDEE
from wrap_up import info_and_bmr,set_macros
from api_food.wrap_api import calling,show_food
from manual_track.menu_manual import manually_track
from validation import verify

def menu_user():
    """ Shows available options to user 
    """
    completed_info=False
    while True:
        print(" --- TRACKY (Macro Tracker) --- ")
        print("1. Check your Daily Base Fuel 🚀 (BMR): ")
        print("2. Calories your body burns per day based on activity 🏃‍♂️:")
        print("3. Search a food ingredient :")
        print("4. Enter macros manually : ")
        choice=verify(" Select an opcion (1-4) :",minim=1,maxim=4)
        if choice==1:
            value_bmr,wg,name,gre=info_and_bmr()
            completed_info=True
        
        elif choice==2:
            if completed_info:
                type_act,activity = activity_level() #Type of activity 
                show_tdee=TDEE(activity,type_act,value_bmr) #Calculates your TDEE in base of your activity
                set_macros(wg,name,show_tdee) #shows macros 
            else:
                print("First,you must fill your basic information.")
        elif choice==3:
            if completed_info:
                calling()
                show_food()        
            else:
                print("First,you must fill your basic information.")
               
        elif choice==4:
            manually_track()
        else:
            print("Please,Enter a valid number")
            
            
            
        