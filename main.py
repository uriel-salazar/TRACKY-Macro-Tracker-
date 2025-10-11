
from texts import activity_level
from control import TDEE,prote,fat,carb
from saving_data import save_macro
from wrap_it_up import info_and_bmr,decision



def main():
    value_bmr,wg,name=info_and_bmr() #This is going to calculate the basic info and the bmr of the user()
    type_act,activity = activity_level() #Type of activity 
    show_tdee=TDEE(activity,type_act,value_bmr) #it'll calculate your TDEE
    user_decision=decision(show_tdee) #jsu the calories
    prote_cal,prote_grams=prote(wg) #Returning protein 
    calories_fats,fats_gr=fat(user_decision)
    carb_grams,carb_calories= carb(user_decision,calories_fats,prote_cal)
    save_macro(name,fats_gr,prote_grams,carb_grams)
       
    
if __name__ == "__main__":
    main()



    
    
