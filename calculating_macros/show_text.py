import os 
from calculating_macros.verify.verify_input import verify,fun_text ,valid_word,get_letters


def clear_console():
    if os.name == 'nt': 
        _ = os.system('cls')

def basic_info():
    """ Ask user basic information 

    Returns:
         - year (int): User's year of birth.
            - wg (float): User's weight in kilograms. (kg).
            - h (float): User's height in centimeters.(cm).
            - gre (str): User's gender ("FEMALE" or "MALE").
            - name (str): User's name.
  
    """
  
  
    while True:
                print("-- Setting up your calories ---")
                year=fun_text("How old are you?? :",min_age=13,max_age=130)
                wg=verify("what is your weigh?? (kg): ",minim=20,maxim=300)
                gre=valid_word("Are you a female or male ? (female/male) :",["female","male"]).upper()
                h=verify("What is your heigh?? (cm) :",minim=90,maxim=300)
                name=get_letters("What is your name?? (STRING) : ").upper()
    
                
                print("--- Confirming your data ✔ ---")
                print(f'''
                Name={name}
                Gender:{gre}
                Years :{year} years old 
                Weight:{wg:.0f} kg
                Heigh :{h} cm''')
                confirm=valid_word("Does your data is correct?? ('yes'/'no'):",['yes','no']).lower()
                if confirm=="yes":
                    clear_console()
                
                    return year,wg,h,gre,name
                            
def activity_level():
    """ Shows a dictionary and iterates each activity to the user 

    Returns:
        type_act (int)  : User's activity chosen
        activity(dict):Type of activities with key as value of each one.
    """
    activity={
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "very": 1.725,
        "extra": 1.9
    }
    for i,each in enumerate(activity.keys(),start=1):
        print(f'-{i} {each}')

    type_act=verify("What type of activty you are? (SELECT A NUMBER ) :",minim=0,maxim=5)
    return type_act,activity


def option_goal():
    """ Option between Volumen or cutting 

    Returns:
        int: User's option ( Volumen / Cutting )
    """
    print("Choose an option :")
    print("1. Volumen\n2. Cutting")
    return verify("What are you going to choose?:",minim=0,maxim=2)


def type_bulking():
    """ Option type of bulking 
    """
    print("""
                1. Agressive bulking 
                2. Normal bulking """)
    return verify("What type of bulking are you looking for ?:",minim=1,maxim=2)
    
    
def type_cutting():
    """ Option type of cutting
    """
    print("""
          1. Aggressive cutting
          2. Normal cutting """)
    return verify("What type of cutting are you going to do??",minim=1,maxim=2)


    
    
    
