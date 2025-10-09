

def basic_info():
        while True:
                print("-- Setting up your calories ---")
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
                Heigh :{h} m''')
                
                confirm=input("Does your data is correct?? (yes/no):")
                if confirm=="yes":
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

    type_act=int(input("What type of activty you are? (SELECT A NUMBER ) :"))
    return type_act,activity
            