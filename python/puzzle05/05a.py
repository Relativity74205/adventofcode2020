from puzzle05 import raw_data, get_row, get_col


seat_ids = (get_row(seat[:7]) * 8 + get_col(seat[7:]) for seat in raw_data)

print(f'{max(seat_ids)=}')
