from pathlib import Path
import re

with open(Path(__file__).parent.parent / "data" / "puzzle04.txt", "r") as f:
    data = f.read()


passports = {ele.replace('\n', ' ') for ele in data.split('\n\n')}

mandatory_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def check_password(passport: str) -> bool:
    passport_parts = passport.split(' ')
    passport_keys = {passport_part.split(':')[0] for passport_part in passport_parts}.difference({'cid'})

    return mandatory_keys == passport_keys


def check_bounds(val: str, lower_bound: int, upper_bound: int):
    return int(val) in range(lower_bound, upper_bound + 1)


def check_hcl(hcl: str):
    return re.match(r'#([0-9a-f]){6}', hcl) is not None


def check_pid(pid: str):
    return re.match(r'^([0-9]){9}$', pid) is not None


def check_height(hgt: str):
    if 'in' == hgt[-2:]:
        if not check_bounds(hgt[:-2], 59, 76):
            return False
    elif 'cm' in hgt[-2:]:
        if not check_bounds(hgt[:-2], 150, 193):
            return False
    else:
        return False

    return True


def check_password_complex(passport: str) -> bool:
    passport_parts = passport.strip().split(' ')
    passport_dict = {passport_part.split(':')[0]: passport_part.split(':')[1] for passport_part in passport_parts}

    passport_keys = set(passport_dict.keys()).difference({'cid'})

    if not mandatory_keys == passport_keys:
        return False

    if not check_bounds(passport_dict['byr'], 1920, 2002):
        return False

    if not check_bounds(passport_dict['iyr'], 2010, 2020):
        return False

    if not check_bounds(passport_dict['eyr'], 2020, 2030):
        return False

    if not passport_dict['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False

    if not check_pid(passport_dict['pid']):
        return False

    if not check_height(passport_dict['hgt']):
        return False

    if not check_hcl(passport_dict['hcl']):
        return False

    return True


print(f'Solution for A is {sum(check_password(passport) for passport in passports)}')  # 202
print(f'Solution for B is {sum(check_password_complex(passport) for passport in passports)}')  # 137
