import os 
import time


def clear_console():
    """Clears the console """
    
    if os.name == 'nt':  
        _ = os.system('cls')
 
def bmr(weight,height,group,birth):
    """ Calculate User's  Basal Metabolic Rate (BMR)

    Args:
        weight (float): User's weight in kg 
        height (float): User's height
        group (string): User's gender (FEMALE/MALE) 
        birth (int): User's age

    Returns:
        float : BMR in kcal/day
    """
    weight = float(weight)
    height = float(height)
    birth = int(birth)

    if group.upper() == "MALE":
        value = 10 * weight + 6.25 * height - 5 * birth + 5
    else:
        value = 10 * weight + 6.25 * height - 5 * birth - 161

    print(f"\nYour BMR is: {value:.0f} kcal/day")
    return value


def TDEE(user_activity,key,bmr):
    """Calculates how many calories you burn per day (TDEE)

    Args:
        user_activity(dict): Dict Activities
        key (int ):Index of User's activity 
        bmr (float): Value of BMR (calories/day)

    Returns:
        float : BMR value  according to user's activity.
    """
    print("Lets calculate your TDEE ! (Total Daily Energy Expenditure)")
    key_list=list(user_activity.keys())
    bmr =int(bmr)    
    choosen_key=key_list[key-1]
    multiply =user_activity[choosen_key]
    result=bmr*multiply
    return result


def prote(weight):
    """Calculates your daily protein intake with output of grams and cal

    Args:
        weight (int): User's weigh (kg)

    Returns:
        float:Protein calculated in grams and calories 
    """
    time.sleep(1)
    print("Setting up your protein ..🥩🍗 ")
    rule_prote=2.2
    gr_p=round((rule_prote)*weight)
    cal_p_=4
    calories_p=gr_p*cal_p_
    return calories_p,gr_p
    

def fat(kcal_tde,fat_number=0.25):
    """Calculates your daily fat intake 

    Args:
        kcal_tde (float):Calories per day based on activity
        fat_number (float): Percentage of fat recomended  (0.25)

    Returns:
        float :Grams of fats,Calories of fats
    """
    time.sleep(1)
    print("Let's create your fat intake ..🔥🥑")
    kcal_tde=int(kcal_tde)
    cal_fat=kcal_tde*fat_number
    gr_fat=cal_fat/9
    return cal_fat,gr_fat

  
def carb(calories,cal_protein,cal_fat):
    """ Calculates your carbs 

    Args:
        calories (float): Calories based on TDEE's user
        cal_protein (float): Value of protein in calories 
        cal_fat (float): Value of fats  in calories 

    Returns:
        float:Grams of carbs,calories of carbs
    """
    time.sleep(1)
    print("Checking your carbs .. 🍚🫘")
    cal_carb=calories-cal_protein-cal_fat
    gr_carb=round(cal_carb/4)
    return gr_carb,cal_carb
    
    