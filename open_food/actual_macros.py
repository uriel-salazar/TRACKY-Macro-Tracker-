import pandas as pd
from saving_data import basic_data


def remaining(group):
    if group=="MALE":
        user_data=pd.read_csv("bmr_man.csv")
    else:
        user_data=pd.read_csv("bmr_woman.csv")
    print(group)