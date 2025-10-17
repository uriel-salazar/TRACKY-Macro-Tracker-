
from texts import activity_level
from control import TDEE
from wrap_up import info_and_bmr,set_macros
from open_food.wrap_api import calling

def main():
    value_bmr,wg,name=info_and_bmr()  #Calculates basic info and BMR
    type_act,activity = activity_level() #Type of activity 
    show_tdee=TDEE(activity,type_act,value_bmr) #Calculates your TDEE in base of your activity
    set_macros(wg,name,show_tdee) #Shows the processed information in a tab format.
    #and saves it in a .csv file
    #calling api:
    total_cal, total_prote, total_carb, total_fat = calling()
    ###
if __name__ == "__main__":
    main()



    
    
