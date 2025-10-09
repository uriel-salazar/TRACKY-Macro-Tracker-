          
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


def TDEE(key,worth,lazy):
    key_list=list(lazy.keys())
    worth=float(worth)
    choosen_key=key_list[key-1]
    multiply = lazy[choosen_key]
    result=worth*multiply
    print(f'Your TDEE : {result:.0f}')
    return result


def prote(weigh):
    rule_prote=2.2
    gr_p=round(rule_prote*weigh)
    cal_p_=4
    calories_p=gr_p*cal_p_
    print(f"Your protein in gr :{gr_p} ")
    print(f'Calories Protein : {calories_p}')
    return gr_p,calories_p
    
    
    