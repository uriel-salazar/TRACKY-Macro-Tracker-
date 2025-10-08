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
