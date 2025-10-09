from texts import basic_info
from saving_data import begin_data
from control import bmr


def info_and_bmr():
    year,wg,h,gre,name=basic_info()
    value_bmr=bmr(wg,h,gre,year)
    print(f'Your BMR : {value_bmr}')
    begin_data(name,value_bmr,gre)
    return value_bmr
