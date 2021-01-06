from pathlib import Path

with open(Path(__file__).parent / "puzzle04.txt", "r") as f:
    data = f.read()


passports = {ele.replace('\n', ' ') for ele in data.split('\n\n')}

mandatory_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
