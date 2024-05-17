def load_recipes(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def parse_recipes(data):
    # Assuming recipes are separated by double newlines
    recipes = data.strip().split('\n\n')
    return recipes

def find_recipes_with_ingredient(recipes, ingredient):
    matching_recipes = [recipe for recipe in recipes if ingredient.lower() in recipe.lower()]
    return matching_recipes

def main():
    file_path = 'baby_recipes.txt'
    recipes_data = load_recipes(file_path)
    recipes = parse_recipes(recipes_data)
    
    ingredient = input("Enter an ingredient: ").strip()
    matching_recipes = find_recipes_with_ingredient(recipes, ingredient)
    
    if matching_recipes:
        print("\nRecipes containing '{}':".format(ingredient))
        for recipe in matching_recipes:
            print(recipe)
            print()  # Print a newline for better readability
    else:
        print("No recipes found containing '{}'".format(ingredient))

if __name__ == "__main__":
    main()