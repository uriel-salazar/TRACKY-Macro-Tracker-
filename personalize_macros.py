import os
import pandas as pd




def clear_console():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # macOS / Linux
    else:
        os.system('clear')

def data():
    while True:
                print("Setting up your calories :")
                year=int(input("How old are you?? :"))
                wg=float(input("what is your weigh??: "))
                gre=input("Are you a women or men ? (woman/man)").upper()
                h=float(input(("What is your heigh??")))
                name=input("What is your name?? (STRING) : ")
                
                print("--- Confirming your data ---")
                print(f'''
                Name={name}
                Gender:{gre}
                Years :{year} years old 
                Weight:{wg}kg
                Heigh :{h} m

                 
                            ''')
                confirm=input("Does your data is correct?? (yes/no):")
                if confirm=="yes":
                    return year,wg,h,gre,name
                
         # data ()
         # in this section we know the name , gender , 
         # years, weight and the heigh from the user 
                

          
def bmr(weight,height,group,birth):
    # Ensure data types are correct
    weight = float(weight)
    height = float(height)
    birth = int(birth)

    if group.upper() == "MAN":
        value = 10 * weight + 6.25 * height - 5 * birth + 5
    else:
        value = 10 * weight + 6.25 * height - 5 * birth - 161

    print(f"\nYour BMR is: {value:.2f} kcal/day")
    return value

    
    #is going to return the bmr() from each user 

    
 
 
def write(value,gre,name):
    print("Your data has been saved succesfully!")
    if  gre=="MAN":
        m_dat=pd.DataFrame({
                    "Name":[name],
                    "BMR":[value],
                    "Genre":[gre]
                
        })
        m_dat.to_csv("bmr_man.csv",mode="a",index=False,header=not os.path.exists("bmr_man.csv"))
    else:
        w_dat=pd.DataFrame({
                  "Name":[name],
                  "BMR":[value],
                  "Genre":[gre]
        
    })
        w_dat.to_csv("bmr_woman.csv",mode="a",index=False,header=not os.path.exists("bmr_woman.csv"))


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

    type_act=int(input("What type of activty you are? (SELECT A NUMBER ) :"))
    return type_act,activity


def TDEE(type_act_key, bmr_value, activity_dict):
    multiply=activity_dict[type_act_key]
    result=bmr_value*multiply
    print(f'Your TDEE : {result:.0f}')
    return result
    
    

      




 
 
    



