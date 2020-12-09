from pathlib import Path
from dataclasses import dataclass
from collections import defaultdict
from functools import reduce

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

valid_passports = 0
for passport in passports:
    passport_parts = passport.split(' ')
    passport_keys = [passport_part.split(':')[0] for passport_part in passport_parts]

    try:
        passport_keys.remove('cid')
    except ValueError:
        pass

    if mandatory_keys == set(passport_keys):
        valid_passports += 1

print(f'{valid_passports=}')
