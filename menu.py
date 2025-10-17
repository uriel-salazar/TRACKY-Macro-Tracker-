from texts import activity_level
from wrap_up import info_and_bmr
from control import TDEE
from wrap_up import info_and_bmr,set_macros
from open_food.wrap_api import calling


def menu_user():
    while True:
        print("1.Calculate your BMR ")
        print(" 2 .Calculate your TDEE and show your TDEE")
        choice=int(input("Choice a number"))
        if choice==1:
            value_bmr,wg,name=info_and_bmr()
        elif choice==2:
            type_act,activity = activity_level() #Type of activity 
            show_tdee=TDEE(activity,type_act,value_bmr) #Calculates your TDEE in base of your activity
        elif choice==3:
            set_macros(wg,name,show_tdee)
        else:
            print("Please enter a number ")
                
            
        