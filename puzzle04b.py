from pathlib import Path
import re

with open(Path(__file__).parent / "data" / "puzzle04.txt", "r") as f:
    data = f.read()


passports = [ele.replace('\n', ' ') for ele in data.split('\n\n')]


mandatory_keys = {'byr',
                  'iyr',
                  'eyr',
                  'hgt',
                  'hcl',
                  'ecl',
                  'pid',
                  # 'cid',
                  }


def check_bounds(val: str, lower_bound: int, upper_bound: int):
    return lower_bound <= int(val) <= upper_bound


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


valid_passports = 0
for passport in passports:
    passport_parts = passport.strip().split(' ')
    passport_dict = {passport_part.split(':')[0]: passport_part.split(':')[1] for passport_part in passport_parts}

    passport_keys = list(passport_dict.keys())
    try:
        passport_keys.remove('cid')
    except ValueError:
        pass

    if not mandatory_keys == set(passport_keys):
        continue

    if not check_bounds(passport_dict['byr'], 1920, 2002):
        continue

    if not check_bounds(passport_dict['iyr'], 2010, 2020):
        continue

    if not check_bounds(passport_dict['eyr'], 2020, 2030):
        continue

    if not passport_dict['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        continue

    if not check_pid(passport_dict['pid']):
        continue

    if not check_height(passport_dict['hgt']):
        continue

    if not check_hcl(passport_dict['hcl']):
        continue

    valid_passports += 1

print(f'{valid_passports=}')
