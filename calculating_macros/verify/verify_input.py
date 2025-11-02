def verify(answer, minim=None, maxim=None):
    """ Verify if is a a valid number
    if not, is going to ask the question again 

    Args:
        answer (int) User's input 
        minim (_type_, optional): Min number Defaults to None.
        maxim (_type_, optional): Max number  Defaults to None.

    Returns:
        int:   User's input validated 
    """
    while True:
        user_input = input(answer).strip()  
        try:
            num = int(user_input)
            
        except ValueError:
            print("Please enter a valid number")
            continue
        
        if minim is not None and num < minim:
            print(f"Number must be at least {minim}.")
            continue
        if maxim is not None and num > maxim:
            print(f"Number must be at most {maxim}.")
            continue
        
        return num 
    
    
def fun_text(prompt, min_age=None, max_age=None):
    """Verifies if the age is valid
    if not, is going to ask it again 

    Returns:
        int: User's age validated 
    """
    
    while True:
        user_input = input(prompt).strip()
        try:
            num = int(user_input)
        except ValueError:
            print("Please enter a valid number")
            continue
        
        if min_age is not None and num < min_age:
            print(f"You have to at least have {min_age} years old for using this app")
            continue
        if max_age is not None and num > max_age:
            print("Are you an alien? 👽")
            continue
        
        return num

def valid_word(word,valid_words):
    """ Forces to enter yes or no answer 

    Args:
        word (str): user's answer 
        valid_words (str): valid words (example :(yes/no))

    Returns:
        str: Answer validated 
    """
    while True: 
        option=input(word).strip()
        
        if option in valid_words:
            return option
        else:
            print('You have to enter a valid word.')
        

def get_letters(prompt):
    """
    Forces user to enter only letters and spaces

    Args:
        prompt (str): message shown to the user

    Returns:
        str: validated text containing only letters and spaces
    """
    while True:
        text = input(prompt).strip()
        
        if all(word.isalpha() for word in text.split()):
            return text
        else:
            print("❌ Only letters allowed.Please try again.")
            

def check_float(answer, minim=None, maxim=None):
    """ Verify if is a a valid number
    if not, is going to ask the question again 

    Args:
        answer (int) User's input 
        minim (_type_, optional): Min number Defaults to None.
        maxim (_type_, optional): Max number  Defaults to None.

    Returns:
        int:   User's input validated 
    """
    while True:
        user_input = input(answer).strip()  
        try:
            num = int(user_input)
            
        except ValueError:
            print("Please enter a valid number")
            continue
        
        if minim is not None and num < minim:
            print(f"Number must be at least {minim}.")
            continue
        if maxim is not None and num > maxim:
            print(f"Number must be at most {maxim}.")
            continue
        
        return num 
    