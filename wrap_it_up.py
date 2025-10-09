from texts import basic_info,option_goal,type_bulking,type_cutting
from saving_data import begin_data
from control import bmr


def info_and_bmr():
    year,wg,h,gre,name=basic_info()
    value_bmr=bmr(wg,h,gre,year)
    print(f'Your BMR : {value_bmr}')
    begin_data(name,value_bmr,gre)
    return value_bmr

def two_options(preference,tdee,sub_option,):
    if preference==1:
        if sub_option==1:
            return tdee+500
        elif sub_option==2:
            return tdee+300
    elif preference==2:
        if sub_option==1:
            return tdee-700
        elif sub_option==2:
            return tdee-500
        

def decision(show_tdee):
    preference=option_goal() #Whether the user is going to choose volumen or cutting 
    if preference==1: #if the user chose 1 means that he want the bulking's calories 
        sub_option=type_bulking()
    else:
        sub_option=type_cutting()
        #if is nnot 1 this mean the answer is 2 which this means that the user 
        #is going to see their calories for cutting !
    cal=two_options(preference,show_tdee,sub_option)#
    print(f"Your total of calories :{cal:.0f}")

        

