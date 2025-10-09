
from texts import activity_level
from control import TDEE


from wrap_it_up import info_and_bmr

def main():
    value_bmr=info_and_bmr() #This is going to calculate the basic info and the bmr of the user()
    type_act,activity = activity_level()
    show_tdee=TDEE(type_act,value_bmr,activity)
    
    

if __name__ == "__main__":
    main()



    
    
