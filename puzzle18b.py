import re
from pathlib import Path


with open(Path(__file__).parent / "data" / "puzzle18.txt", "r") as f:
    raw_data = f.read().splitlines()

r = re.compile(r'(\([0-9\+\*\s]*\))')


def eval_simple(simple_expr: str) -> str:
    simple_expr = simple_expr.replace(' ', '')

    while True:
        if (add_index := simple_expr.find('+')) == -1:
            break
        op_indices = [i for i, char in enumerate(simple_expr) if char in ('*', '+',)]
        op_indices_pos = op_indices.index(add_index)

        if op_indices_pos == 0:
            start_index = 0
        else:
            start_index = op_indices[op_indices_pos - 1] + 1

        if op_indices_pos == (len(op_indices) - 1):
            end_index = len(simple_expr)
        else:
            end_index = op_indices[op_indices_pos + 1]

        sub_expr = simple_expr[start_index:end_index]
        sub_result = eval(sub_expr)
        simple_expr = simple_expr.replace(sub_expr, str(sub_result), 1)

    return str(eval(simple_expr))


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

# assert eval_full('2 + 9 * 5 * (2 * 3 * 9 * 9 + 5 + 9) + (4 + 5)') == 68805
# assert eval_full('4 + (5 + 3 + 3 * 7 * 4 + 7)') == 851
# assert eval_full('7 + 9') == 16
# assert eval_full('2 + (5 * 2 * 3 + 3) * 8 + 3 * 8 + 6') == 9548
# assert eval_full('1 + 2 * 3 + 4 * 5 + 6') == 231
# assert eval_full('1 + (2 * 3) + (4 * (5 + 6))') == 51
# assert eval_full('2 * 3 + (4 * 5)') == 46
# assert eval_full('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 1445
# assert eval_full('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 669060
# assert eval_full('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340

