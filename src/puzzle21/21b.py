import re
from itertools import permutations
from typing import Dict

from puzzle21 import parse_data, raw_data, get_candidate_ingredients, r


def check_constraints(recipes, possible_solution: Dict) -> bool:
    for recipe in recipes:
        recipe_ingredients = re.search(r, recipe)[1].split(' ')
        recipe_allergens = set(re.search(r, recipe)[2].split(', '))
        possible_allergens = {possible_solution.get(ingredient) for ingredient in recipe_ingredients
                              if possible_solution.get(ingredient)}
        if not recipe_allergens.issubset(possible_allergens):
            return False

    return True


def solve():
    allergen_ingredients, frequency_ingredients = parse_data(raw_data)
    candidates = get_candidate_ingredients(allergen_ingredients)
    non_candidate_ingredients = set(frequency_ingredients.keys()).difference(candidates)
    allergen_ingredient_candidates = {allergen: {ele for ele in ingredients if ele not in non_candidate_ingredients}
                                      for allergen, ingredients in allergen_ingredients.items()}

    allergens = allergen_ingredient_candidates.keys()
    for ingredient_candidates in permutations(allergen_ingredient_candidates['eggs'], r=8):
        possible_solution = {ingredients: allergen
                             for ingredients, allergen in zip(ingredient_candidates, allergens)}
        if check_constraints(raw_data, possible_solution):
            return possible_solution


solution = solve()
print(','.join(sorted(solution, key=solution.get)))  # cdqvp,dglm,zhqjs,rbpg,xvtrfz,tgmzqjz,mfqgx,rffqhl
