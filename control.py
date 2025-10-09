          
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