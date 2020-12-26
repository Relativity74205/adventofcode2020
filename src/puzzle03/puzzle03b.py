from puzzle03 import raw_data, solve
from functools import reduce
from operator import mul


strategies = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2), )
amount_trees = [solve(raw_data, strategy) for strategy in strategies]
print(reduce(mul, amount_trees))  # 3584591857
