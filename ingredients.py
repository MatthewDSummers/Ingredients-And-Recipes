"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    This is a simple ingredients price manager.
    The default measurement key is "item", to signify the cost of the ingredient is per item,
    but you can specify "pound" or "ounce" instead as the key to store/retrieve the ingredient
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

YELLOW = "\033[93m"
CYAN = "\033[96m"
HIGHLIGHT = "\033[42;30m"
RESET = "\033[0m"

ingredients = {
    "item": {

    },
    "pound":{

    },
    "ounce":{

    }
}

def add_ingredient(ingredient_name, cost, measurement="item"):
    if not isinstance(cost, (int, float)):
        return CYAN + "Please enter a valid number." + RESET

    choices = ingredients.keys()

    if measurement in choices:
        ingredients[measurement][ingredient_name] = cost
        return f"{CYAN}{ingredient_name} added!{RESET}"
    else:
        statement = CYAN + "Measurement must be "
        for index, item in enumerate(choices):
            if index != len(choices)-1:
                statement += item + ", "
            else:
                statement += f"or {item}."
        statement += RESET
        return statement

def get_ingredient_cost(ingredient, measurement="item"):
    keys = ingredients.keys()
    choices = [x for x in keys if x != "item"]

    if measurement in choices:
        quantifier = f"per {measurement}"
    elif measurement == "item":
        quantifier = f"per {ingredient.lower()}"
    else:
        return "The measurement type specified is invalid"

    if ingredients[measurement].get(ingredient):
        return f"The cost for {ingredient} is ${ingredients[measurement].get(ingredient)} {quantifier}"
    else:
        return f'{ingredient} not found'

def recipe_cost(ingredients_quantities):
    cost = 0
    choices = ingredients.keys()

    for ingredient, quantity in ingredients_quantities.items():
        for choice in choices:
            entry = ingredients[choice].get(ingredient)
            if entry is not None:
                cost+= entry * quantity
                break

    return f"{YELLOW}The cost for the recipe is ${cost} {RESET}"

def show_ingredients():
    statement = HIGHLIGHT + "  INGREDIENTS  " + RESET
    found = False
    for key in ingredients.keys():
        if ingredients[key] != {}:
            found = True
            statement += "\n" + YELLOW + f"  By {key}  " + RESET
            for k, v in ingredients[key].items():
                statement += f"\nIngredient: {k} \nCost: ${v}\n"
    if not found:
        statement += "\nNo ingredients have been added"
    return statement

# ADD INGREDIENTS 
print(add_ingredient("Pickle", .5))
print(add_ingredient("Ground Beef", 1.5, measurement="pound"))
print(add_ingredient("Watermelon", 2))
print(add_ingredient("Olive Oil", .4, measurement="ounce"))
print(add_ingredient("Olive Oil", .4, measurement="bounce")) # intentional mistake in measurement

# GET COST OF INGREDIENT 
print(get_ingredient_cost("Ground Beef", measurement="pound"))
print(get_ingredient_cost("Pickle"))
print(get_ingredient_cost("Olive Oil", measurement="ounce"))
print(get_ingredient_cost("Olive Oil", measurement="ouncef")) # intentional mistake in measurement
print(get_ingredient_cost("Olive Boil", measurement="ounce")) # intentional mistake in ingredient

# GET RECIPE COST ( probably not a very tasty recipe )
recipe_quantities = {
    "Pickle": 10,
    "Ground Beef": 2,
    "Watermelon": 1,
    "Olive Oil": 1
}
print(recipe_cost(recipe_quantities))

# GET ALL INGREDIENTS
print(show_ingredients())