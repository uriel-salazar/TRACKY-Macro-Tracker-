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
        
        

