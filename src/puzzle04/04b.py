import re

from puzzle04 import passports, mandatory_keys


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


def check_password(passport: str) -> bool:
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


valid_passports = (check_password(passport) for passport in passports)
print(f'{sum(valid_passports)=}')  # 137
