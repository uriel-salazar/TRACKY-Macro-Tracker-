
from texts import activity_level,option_goal,type_bulking,type_cutting
from control import TDEE,prote


from wrap_it_up import info_and_bmr,two_options,decision

def main():
    value_bmr=info_and_bmr() #This is going to calculate the basic info and the bmr of the user()
    type_act,activity = activity_level()  #Type of activity 
    show_tdee=TDEE(type_act,value_bmr,activity) #it'll calculate your TDEE
    user_decision=decision(show_tdee)
    protein_user=prote(value_bmr)

    

    
if __name__ == "__main__":
    main()



    
    
