import os 
import time


def clear_console():
    """Clears the console screen, compatible with Windows and Unix-like systems."""
    # Check the operating system and execute the appropriate clear command
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        _ = os.system('clear')

 
def bmr(weight,height,group,birth):
    # Ensure data types are correct
    weight = float(weight)
    height = float(height)
    birth = int(birth)

    if group.upper() == "MAN":
        value = 10 * weight + 6.25 * height - 5 * birth + 5
    else:
        value = 10 * weight + 6.25 * height - 5 * birth - 161

    print(f"\nYour BMR is: {value:.0f} kcal/day")
    return value


def TDEE(lazy,key,worth):
    print("Lets calculate your TDEE ! (Total Daily Energy Expenditure)")
    key_list=list(lazy.keys())
    worth=int(worth)
    choosen_key=key_list[key-1]
    multiply = lazy[choosen_key]
    result=worth*multiply
    return result


def prote(weight):
    time.sleep(1)
    print("Setting up your protein ..🥩🍗 ")
    rule_prote=2.2
    gr_p=round((rule_prote)*weight)
    cal_p_=4
    calories_p=gr_p*cal_p_
    return calories_p,gr_p
    

def fat(kcal_tde,fat_number=0.25):
    time.sleep(1)
    print("Let's create your fat intake ..🔥🥑")
    kcal_tde=int(kcal_tde)
    cal_fat=kcal_tde*fat_number
    gr_fat=cal_fat/9
    return cal_fat,gr_fat

  
def carb(calories,cal_protein,cal_fat):
    time.sleep(1)
    print("Checking your carbs .. 🍚🫘")
    cal_carb=calories-cal_protein-cal_fat
    gr_carb=round(cal_carb/4)
    return gr_carb,cal_carb
    
    