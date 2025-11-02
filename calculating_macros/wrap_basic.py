from calculating_macros.show_text import basic_info,option_goal,type_bulking,type_cutting
from basic_data.data_functions import basic_data,save_macro
from calculating_macros.calculate import bmr,prote,fat,carb


def info_and_bmr():
    """ Calls basic data functions for the user

    Returns:
        value_bmr: User's bmr value 
        wg:user's weigh 
        name:name's user
        gre:gender 
    """
    year,wg,h,gre,name=basic_info()
    value_bmr=bmr(wg,h,gre,year)
    basic_data(name,value_bmr,gre)
    return value_bmr,wg,name,gre
  

def type_diet(preference,tdee,sub_option,):
    """ Increase or decrease calories 
    in base of user's option 

    Args:
        preference (int): User's activity option chosen 
        tdee (float): TDEE value
        sub_option (int): Option between normal type of diet or harder 

    Returns:
        float: TDEE calculation
    """
    if preference==1:
        if sub_option==1:
            return tdee+500
        elif sub_option==2:
            return tdee+300
    elif preference==2:
        if sub_option==1:
            return tdee-700
        elif sub_option==2:
            return tdee-500
        

def decision(show_tdee):
    """ Prints whether is calories for bulking or cutting 

    Args:
        show_tdee (int): Total Daily Energy Expenditure Value

    Returns:
        float: Calories based on user's activity 
    """
    preference=option_goal() 
    if preference==1: 
        sub_option=type_bulking()
    else:
        sub_option=type_cutting()

    cal=type_diet(preference,show_tdee,sub_option)#
    print(f"Your total of calories :{cal:.0f} cal")
    return cal


def set_macros(wg,name,show_tdee):
    """Calls functions for printing macros and save them 

    Args:
        wg (int): User's Weight 
        name (str): User's Name
        show_tdee (int): Total Daily Energy Expenditure Value
    """
    user_decision=decision(show_tdee)
    prote_cal,prote_grams=prote(wg) #Returning protein 
    calories_fats,fats_gr=fat(user_decision)
    carb_grams,carb_calories=carb(user_decision,calories_fats,prote_cal)  
    save_macro(name,fats_gr,prote_grams,carb_grams,user_decision)
    