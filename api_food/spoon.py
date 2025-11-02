import requests
from calculating_macros.verify.verify_input import get_letters,check_float
def url_api():
    """  Ask the user for a food item and return an OpenFoodFacts
    API search URL.

    Returns:
        str: Formatted API URL.
    """
    product=get_letters("Enter a food : ").lower()
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={product}&search_simple=1&action=process&page_size=5&sort_by=unique_scans_n&fields=product_name,nutriments&json=1"

    return url

 
def search  (link):
    """ Searchs if the product is available within Open food facts API
    
    If the product does not exist or the API call fails, the function returns
    None values so the caller can handle the error 

    Args:
        link (str): Calling Open food facts API

    Returns:
        float:Product macros searched (portion of 100gr)
    """
    try:
        response = requests.get(link)
        data = response.json()
    except:
         print("⚠️ Error connecting to the API.")
         return None, None, None, None, None
    
    if "products" not in data or len(data["products"]) == 0:
        return None, None, None, None, None
    
    products = data["products"]
    
    print("We found several products, choose one:")
    
    for i, item in enumerate(products):
        name = item.get("product_name", "Unknown")
        print(f"{i + 1}. {name}")
        
    try:
        choice = int(input("Enter the number of the product: ")) - 1
        item = products[choice]
    except (ValueError, IndexError):
        print("⚠️ Invalid choice.")
        return None, None, None, None, None

        
    name = item.get("product_name", "Unknown")
    nutriments = item.get("nutriments", {})
    calories = nutriments.get("energy-kcal_100g", 0)
    protein_100g = nutriments.get("proteins_100g", 0)
    carbs_100g = nutriments.get("carbohydrates_100g", 0)
    fat_100g = nutriments.get("fat_100g", 0)
        
        
    print("We found your food 🥳 !")
    return name,calories, protein_100g, carbs_100g, fat_100g

   
def portion():
    """ Asks user grams of macros 

    Returns: float  : User's portion of macros 
    """
    ask_grams=check_float("How many grams did you consume?",0.0,10000.0)
    return ask_grams
    


def calculate_gr(cal,prote_gr,carb_gr,fat_gr,grams):
    """ Calculates macros in base of user's grams output 

    Args:
        cal (float): cal (100gr)
        prote_gr (float): prote(100gr)
        carb_gr (float): carb (100gr)
        fat_gr (float): fats (100gr)
        grams (float): User's portion

    Returns:
        float: Personalized macros
    """
    total_cal=(cal*grams)/100
    total_prote=(prote_gr*grams)/100
    total_carb=(carb_gr*grams)/100
    total_fat=(fat_gr*grams)/100
    return total_cal,total_prote,total_carb,total_fat

