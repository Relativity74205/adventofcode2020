from puzzle21 import parse_data, raw_data, get_candidate_ingredients


def solve():
    allergen_ingredients, frequency_ingredients = parse_data(raw_data)
    candidates = get_candidate_ingredients(allergen_ingredients)
    non_candidate_ingredients = set(frequency_ingredients.keys()).difference(candidates)

    return sum(frequency_ingredients[ingredient] for ingredient in non_candidate_ingredients)


print(f'{solve()=}')  # 2061
