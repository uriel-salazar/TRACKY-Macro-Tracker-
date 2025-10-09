
from texts import activity_level,option_goal,type_bulking,type_cutting
from control import TDEE


from wrap_it_up import info_and_bmr,two_options

def main():
    value_bmr=info_and_bmr() #This is going to calculate the basic info and the bmr of the user()
    type_act,activity = activity_level()
    show_tdee=TDEE(type_act,value_bmr,activity) #it'll calculate your TDEE
    preference=option_goal()
    if preference==1:
        sub_option=type_bulking()
    else:
        sub_option=type_cutting()
        
    cal=two_options(show_tdee,preference,sub_option)
    print("Your total of calories :{cal:.0f}")

    

    
if __name__ == "__main__":
    main()



    
    
