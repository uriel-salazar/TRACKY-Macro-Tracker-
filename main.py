import pandas as pd 
from texts import basic_info
from control import bmr
from saving_data import begin_data

def main():
    year,wg,h,gre,name=basic_info()
    value_bmr=bmr(wg,h,gre,year)
    print(f'Your BMR : {value_bmr}')
    saving=begin_data(name,value_bmr,gre)
    


if __name__ == "__main__":
    main()



    
    
