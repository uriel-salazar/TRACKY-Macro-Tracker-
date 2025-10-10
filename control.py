          
def bmr(weight,height,group,birth):
    # Ensure data types are correct
    weight = float(weight)
    height = float(height)
    birth = int(birth)

    if group.upper() == "MAN":
        value = 10 * weight + 6.25 * height - 5 * birth + 5
    else:
        value = 10 * weight + 6.25 * height - 5 * birth - 161

    print(f"\nYour BMR is: {value:.2f} kcal/day")
    return value


def TDEE(lazy,key,worth):
    key_list=list(lazy.keys())
    worth=int(worth)
    choosen_key=key_list[key-1]
    multiply = lazy[choosen_key]
    result=worth*multiply
    print(f'Your TDEE : {result:.0f}')
    return result


def prote(weight):
    rule_prote=2.2
    gr_p=round((rule_prote)*weight)
    cal_p_=4
    calories_p=gr_p*cal_p_
    print(f"Your protein in  :{gr_p} gr  ")
    print(f'Calories Protein : {calories_p} kcal ')
    return calories_p,gr_p
    

def fat(kcal_tde,fat_number=0.25):
    kcal_tde=int(kcal_tde)
    cal_fat=kcal_tde*fat_number
    gr_fat=cal_fat/9
    print(f' Your gr of fat are {gr_fat:.0f}gr, Your cal of fats per day : {cal_fat:.0f}')
    return cal_fat,gr_fat

  
def carb(calories,cal_protein,cal_fat):
        cal_carb=calories-cal_protein-cal_fat
        gr_carb=round(cal_carb/4)
        
        print(f"Your calories from carbs  :{cal_carb} cal , grams of carbs :{gr_carb} ")
        return cal_carb,gr_carb
    
    