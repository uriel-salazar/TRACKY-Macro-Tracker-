import pandas as pd 
import os 

def basic_data(nickname, bmr_value, gender):
    """
    Save basic info data in a CSV file using pandas library.

    Creates a Pandas DataFrame and stores the basic user info (name, BMR, and gender)
    in a gender-specific file: 'bmr_man.csv' or 'bmr_woman.csv'.

    Args:
        nickname (str): User's name
        bmr_value (float): BMR value calculated
        gen (str): Gender of the user ("MALE" or "FEMALE")

    Returns:
        pd.DataFrame: DataFrame object containing the saved data
    """
    print("Your data has been saved successfully!")

    nickname = str(nickname)
    bmr_value = float(bmr_value)
    gen = str(gender).upper()

    # Choose file based on gender
    if gen == "MALE":
        file_name = "bmr_man.csv"
    else:
        file_name = "bmr_woman.csv"

    macro_data = pd.DataFrame({
        "Name": [nickname],
        "BMR": [bmr_value],
        "Gender": [gender]
    })

    macro_data.to_csv(file_name, mode="a", index=False, header=not os.path.exists(file_name))

    return macro_data

def save_macro(name,fat_gram,prote_grams,carb_grams,cal_value):
    """ Saves macros of user in a.csv file 

    Args:
        name (str): User's name
        fat_gram (int): User's Fat portion (gr) 
        prote_grams (int): User's Prote portion (gr) 
        carb_grams (int): User's  Carbs  portion (gr)
        cal_value (int): User's Calories portion (gr)

    Returns:
        DataFrame: user's data macros saved in dataframe
    """
    import os
    import pandas as pd

    name=str(name)
    fat_gram=int(fat_gram)
    prote_grams=int(prote_grams)
    carb_grams=int(carb_grams)
    cal_value=int(cal_value)

    macros={
        "Name":[name],
        "Fat":[fat_gram],
        "Protein":[prote_grams],
        "Carbs":[carb_grams],
        "Total Calories":[cal_value]
    }

    user_macro=pd.DataFrame(macros)
    print("Your macros in gr:")
    print(user_macro.iloc[0].to_string()) 
    file_macro="data_macros.csv"
    if not os.path.exists(file_macro):
        user_macro.to_csv(file_macro,index=False,header=True)
    else:
        user_macro.to_csv(file_macro,mode='a',header=False,index=False)

    return user_macro
