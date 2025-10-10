import pandas as pd 
import os 


def begin_data(nickname,rate,gen):
    print("Your data has been saved succesfully!") 
    nickname=str(nickname)
    rate=float(rate)
    gen=str(gen)
    if  gen=="MAN":
        m_dat=pd.DataFrame({
                    "Name":[nickname],
                    "BMR":[rate],
                    "Genre":[gen]
                
        })
        m_dat.to_csv("bmr_man.csv",mode="a",index=False,header=not os.path.exists("bmr_man.csv"))
    else:
        w_dat=pd.DataFrame({
                  "Name":[nickname],
                  "BMR":[rate],
                  "Genre":[gen]
        
    })
        w_dat.to_csv("bmr_woman.csv",mode="a",index=False,header=not os.path.exists("bmr_woman.csv"))




def save_data():
    macros={
     "Name":[name],
      "Fat":[fat_grams],
   "Protein":[prote_grams],
     "Carbs":[grams]
    }
    
    macro_save=pd.DataFrame(macros)
    print(macro_save)
  
  #  file_macros="data_macros.csv"
 #   if not os.path.exists(file_macros):
        macro_save.to_csv(file_macros,index=False,header=True)
#    else:
 #      macro_save.to_csv(file_macros,mode='a',header=False,index=False)