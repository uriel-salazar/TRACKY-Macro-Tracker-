import os 
from validation import block,fun_m


def clear_console():
    """Clears the console screen, compatible with Windows and Unix-like systems."""
    # Check the operating system and execute the appropriate clear command
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        _ = os.system('clear')

def basic_info():
        while True:
                print("-- Setting up your calories ---")
                year=fun_m("How old are you?? :",13,130)
                wg=block("what is your weigh??: ",20,200)
                gre=input("Are you a women or men ? (woman/man)").upper()
                h=block("What is your heigh??",10,300)
                name=input("What is your name?? (STRING) : ")
    
                
                print("--- Confirming your data ---")
                print(f'''
                Name={name}
                Gender:{gre}
                Years :{year} years old 
                Weight:{wg:.0f}kg
                Heigh :{h} m''')
                confirm=input("Does your data is correct?? (yes/no):")
                if confirm=="yes":
                    clear_console()
                
                    return year,wg,h,gre,name
                
            
    
                
            
def activity_level():
    activity={
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "very": 1.725,
        "extra": 1.9
    }
    for i,each in enumerate(activity.keys(),start=1):
        print(f'-{i} {each}')

    type_act=block("What type of activty you are? (SELECT A NUMBER ) :",0,5)
    return type_act,activity


def option_goal():
    print("Choose an option :")
    print("1. Volumen\n2. Cutting")
    return block("What are you going to choose?:",0,2)


def type_bulking():
    print("""
                1. Agressive bulking 
                2. Normal bulking """)
    return block("What type of bulking are you looking for ?:",1,2)
    
    
def type_cutting():
    print("""
          1. Aggressive cutting
          2. Normal cutting """)
    return block("What type of cutting are you going to do??",1,2)


    
    
    
