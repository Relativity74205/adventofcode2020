import re
from typing import Set, Dict
from pathlib import Path
from collections import defaultdict, Counter

with open(Path(__file__).parent / "puzzle21.txt", "r") as f:
    raw_data = f.read().splitlines()


r = re.compile(r'(.*) \(contains (.*)\)')


def parse_data(data):
    allergens_dict = defaultdict(list)
    freq_ingredients = Counter()
    for recipe in data:
        recipe_ingredients = re.search(r, recipe)[1].split(' ')
        recipe_allergens = re.search(r, recipe)[2].split(', ')
        freq_ingredients.update(recipe_ingredients)
        for allergen in recipe_allergens:
            allergens_dict[allergen] += recipe_ingredients

    return allergens_dict, freq_ingredients


def get_candidate_ingredients(allergen_ingredients: Dict) -> Set:
    candidates = set()
    for allergen in allergen_ingredients.keys():
        frequency_allergen = Counter(allergen_ingredients[allergen])
        candidates = candidates.union(
            {k for k, v in frequency_allergen.items() if v == frequency_allergen.most_common(1)[0][1]}
        )

    return candidates
