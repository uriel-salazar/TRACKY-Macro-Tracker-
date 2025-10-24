import requests
def cal_api():
    product=input("Enter a food : ").lower()
    url = f"https://world.openfoodfacts.org/cgi/search.pl?search_terms={product}&search_simple=1&action=process&page_size=5&sort_by=unique_scans_n&json=1"

    return url


 
def search_product(link):
    """ Searchs if the product is available within Open food facts API

    Args:
        link (str): Calling Open food facts API

    Returns:
        float:d
    """
    response = requests.get(link)
    data = response.json()

    if "products" in data and len(data["products"]) > 0:
                item = data["products"][0]
                name = item.get("product_name", "Unknown")
                nutriments = item.get("nutriments", {})
                calories = nutriments.get("energy-kcal_100g", 0)
                protein_100g = nutriments.get("proteins_100g", 0)
                carbs_100g = nutriments.get("carbohydrates_100g", 0)
                fat_100g = nutriments.get("fat_100g", 0)
                print("We found your food 🥳 !")
                return calories, protein_100g, carbs_100g, fat_100g

    else:
                return None,None,None,None
        

    
    
    
def portion():
    """ Asks grams of macros 

    Returns: float  : User's portion of macros 
    """
    ask_grams=float(input("How many grams did you consume?"))
    return ask_grams
    


def personalize_gr(cal,prote_gr,carb_gr,fat_gr,grams):
    total_cal=(cal*grams)/100
    total_prote=(prote_gr*grams)/100
    total_carb=(carb_gr*grams)/100
    total_fat=(fat_gr*grams)/100
    return total_cal,total_prote,total_carb,total_fat


#    def dict_food(cal,prote_gr,carb_gr,fat_gr):
#    personalize={
##        "cal_gr":cal,
#        "prote_gr":prote_gr,
 #       "carb_gr":carb_gr,
#        "fat_gr":fat_gr
 #   }

