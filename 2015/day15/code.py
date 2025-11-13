from math import prod

def read_file(filename):
    with open(filename, 'r') as file:
        file_content = []
        for line in file:
            file_content.append(line.rstrip())
        
    return file_content

def parse_ingredients(file):
    ingredients = {}
    for line in file:
        ing, rest = line.split(': ')
        rest = rest.split(', ')
        values = {k: int(v) for k, v in [pair.split() for pair in rest]}
        ingredients[ing] = values
    
    return ingredients

def get_cookie_values(combo, ingredients):
    props = ['capacity', 'durability', 'flavor', 'texture']
    prop_scores = {k: 0 for k in props}
    calories = 0

    for ing, tsp in combo.items():
        prop_scores['capacity'] += tsp * ingredients[ing]['capacity']
        prop_scores['durability'] += tsp * ingredients[ing]['durability']
        prop_scores['flavor'] += tsp * ingredients[ing]['flavor']
        prop_scores['texture'] += tsp * ingredients[ing]['texture']
        calories += tsp * ingredients[ing]['calories']

    prop_scores = {k: 0 if v < 0 else v for k, v in prop_scores.items()}

    return prod(prop_scores.values()), calories


# not really satisfied with this because it only works for 4 ingredients, but oh well
def get_best_score(ingredients, teaspoons):
    combo = {}
    keys = list(ingredients.keys())
    best_score = 0
    best_calories = 0

    for ing1 in range(teaspoons):
        for ing2 in range(teaspoons-ing1):
            for ing3 in range(teaspoons-ing1-ing2):
                combo[keys[0]] = ing1
                combo[keys[1]] = ing2
                combo[keys[2]] = ing3
                combo[keys[3]] = teaspoons-ing1-ing2-ing3
                score, calories = get_cookie_values(combo, ingredients)
                
                if score > best_score:
                    best_score = score

                if calories == 500 and score > best_calories:
                    best_calories = score

    return best_score, best_calories

def main():
    file = read_file('input.txt')
    ingredients = parse_ingredients(file)
    best_score, best_calories = get_best_score(ingredients, teaspoons=100)
    print(f'Part 1: {best_score}')
    print(f'Part 2: {best_calories}')

if __name__ == '__main__':
    main()