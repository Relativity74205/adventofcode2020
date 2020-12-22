import re
from pathlib import Path
from functools import reduce
from operator import add
from collections import defaultdict

with open(Path(__file__).parent / "data" / "puzzle21.txt", "r") as f:
    raw_data = f.read().splitlines()


r = re.compile(r'(.*) \(contains (.*)\)')
ingredients = set(reduce(add, [re.search(r, recipe)[1].split(' ') for recipe in raw_data]))
allergens = set(reduce(add, [re.search(r, recipe)[2].split(', ') for recipe in raw_data]))


d = defaultdict(list)
for recipe in raw_data:
    recipe_ingredients = re.search(r, recipe)[1].split(' ')
    recipe_allergens = re.search(r, recipe)[2].split(', ')
    for allergen in recipe_allergens:
        d[allergen] += recipe_ingredients


