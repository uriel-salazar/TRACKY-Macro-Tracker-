import os
import pandas as pd



def data():
    while True:
                print("Setting up your calories :")
                year=int(input("How old are you?? :"))
                wg=float(input("what is your weigh??: "))
                gre=input("Are you a women or men ? (woman/man)").lower()
                h=float(input(("What is your heigh??")))
                
                print("--- Confirming your data ---")
                check=print(f'''
                Years :{year} years old 
                Weight:{wg}kg
                Heigh :{h} m
                Gender:{gre} 
                            ''')
                confirm=input("Does your data is correct?? (yes/no):").lower()
                if confirm=="yes":
                    return year,wg,h,gre
                
                

          
def bmr(year,wg,h,gre):
    
    if gre=="man":
       value=10 *(wg) +6.25 *(h)-5*year+5
    else:
        value=10*(wg)+6.25*(h)-5*year-161
    return value
    
    
 
 
def write(value,gre):
    print("Your data has been saved succesfully!") 
    if  gre=="man":
        m_dat=pd.DataFrame({
                    "BMR":[value],
                    "Genre":[gre]
        })
        m_dat.to_csv("bmr_man.csv",mode="a",index=False,header=not os.path.exists("bmr_man.csv"))
    else:
        w_dat=pd.DataFrame({
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

    type_act=input("What type of activty you are? (SELECT A NUMBER ) :")
    print("Choose an opcion :")
    print("""
          1.Volumen
          2.Cutting""")
    ask=input("What are you going to choose??")
    return type_act,activity,ask,


def cutting(type_act,value,activity):
    multiply=activity[type_act]
    x=value
    result=x*multiply
    print(result)
    
    
    
      
year,wg,h,gre=data()
value=bmr(year,wg,h,gre)
bmr(year,wg,h,gre)
write(value,gre)
activity_level()
type_act,actvity=cutting(value)
cutting(type_act)
 




 
 
    



