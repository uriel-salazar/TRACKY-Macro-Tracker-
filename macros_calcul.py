from personalize_macros import tdee_value
import pandas as pd
from personalize_macros import wg
import os
from personalize_macros import name


def calories(tdee_value):
    
        print("Choose an opcion :")
        print("""
        #      1.Volumen
        #     2.Cutting """)
        ask=int(input("What are you going to choose??:"))
        
        
        if ask==1:
                print("""
                1. Agressive bulking 
                2. Normal bulking """)
                bulk_type=int(input("What type of bulking are you looking for ?:"))
                if bulk_type==1:  
                      cal=tdee_value+500
                      print(f"Your total of calories for your bulking are : {cal:.0f} cal     ")
                elif bulk_type==2:
    
                     cal=tdee_value+300
                    
                     print(f' {cal:.0f} cal ')
                return cal
        elif ask==2:
            print(""" 1. Agressive cutting
              2. Normal cutting  """)
            cutting_type=int(input("What type of cutting are you looking for :  "))
            if cutting_type==1:
                print("Welcome to aggressive cutting")
                
                cal=tdee_value-700
                print(f'{cal:.0f} cal ')
                
            elif cutting_type==2:
                print("Welcome to normal cutting")
                cal=tdee_value-500
                print(f'{cal:.0f} cal ')
            return cal,ask
                
                
    #defining two functions for setting up the daily protein 
            
def prote(wg):
  rule_prote=2.2
  calcul=round(rule_prote*wg)
  gram_p=4
  cal_prote=calcul*gram_p
  
  
  print(f'Your daily ingest of protein : {calcul} gr  ({cal_prote:.0f}cal )')
  return cal_prote,calcul
  
  """" this is goin"""

def fats(cal):
      intake_f=0.25
      cal=int(cal)
      fat_sum=round(cal*intake_f/9)
      gram_f=9
      cal_fat=fat_sum*gram_f
      
      print(f"Your daily fat intake is : {fat_sum} gr equals : {cal_fat} cal")
      return cal_fat,fat_sum

    
  
def carb(cal,cal_fat,cal_prote):
        v_carb=cal-cal_prote-cal_fat
        grams=round(v_carb/4)
        print(f"You carbs :{grams} gr")
        return grams
      

            

#total_cal=calories(tdee_value)

#prote_cals,prote_grams=prote(wg)

#fat_cals,fat_grams=((fats(total_cal)))
#grams = carb(total_cal, fat_cals, prote_cals)


#### saving data 
#def save_data():
   # macros={
  #  "Name":[name],
#    "Fat":[fat_grams],
 #  "Protein":[prote_grams],
 #   "Carbs":[grams]
    
    
 #   macro_save=pd.DataFrame(macros)
  #  print(macro_save)
  
  #  file_macros="data_macros.csv"
  #  if not os.path.exists(file_macros):
  #     macro_save.to_csv(file_macros,index=False,header=True)
  #  else:
  #   macro_save.to_csv(file_macros,mode='a',header=False,index=False)
      
#save_data()







    

    
    

