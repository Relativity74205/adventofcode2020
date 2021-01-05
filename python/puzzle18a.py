import re
from pathlib import Path


with open(Path(__file__).parent / "data" / "puzzle18.txt", "r") as f:
    raw_data = f.read().splitlines()

r = re.compile(r'(\([0-9\+\*\s]*\))')


def eval_simple(simple_expr: str) -> str:
    simple_expr = simple_expr.replace(' ', '')
    op_indices = [i for i, char in enumerate(simple_expr) if char in ('*', '+', )]
    sub_array = [(start, end) for start, end in zip(op_indices, op_indices[1:] + [len(simple_expr)])]
    result: int = int(simple_expr[:op_indices[0]])
    for start, end in sub_array:
        sub_expr = str(result) + simple_expr[start:end]
        result = eval(sub_expr)

    return str(result)


def eval_full(expr: str) -> int:
    expr = expr.replace(' ', '')
    while True:
        try:
            sub_expr = re.search(r, expr)[1]
            sub_expr_result = eval_simple(sub_expr[1:-1])
            expr = expr.replace(sub_expr, sub_expr_result)
        except TypeError:
            break

    return int(eval_simple(expr))


results = [eval_full(line) for line in raw_data]
print(f'{sum(results)=}')

# assert eval_full('2 * 3 + (4 * 5)') == 26
# assert eval_full('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
# assert eval_full('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
# assert eval_full('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632
