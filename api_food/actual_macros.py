import pandas as pd

def fetch_user_macros():
    """ Searchs  fot the latest input of  user macros 

    Returns:
        np.int64: User macros (fats,prote,carbs,calories)
    """
    user_data = pd.read_csv("data_macros.csv")
      

    print("Your macros in gr:")
    print(user_data.iloc[-1].to_string(index=True))
    name_main=str(user_data.iloc[-1]["Name"])
    fat_main=int(user_data.iloc[-1]["Fat"])
    prote_main=int(user_data.iloc[-1]["Protein"])
    carb_main=int(user_data.iloc[-1]["Carbs"])
    calories_main=int(user_data.iloc[-1]["Total Calories"])
    return name_main,fat_main,prote_main,carb_main,calories_main


    
    