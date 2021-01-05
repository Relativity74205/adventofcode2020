from puzzle04 import passports, mandatory_keys


def check_password(passport: str) -> bool:
    passport_parts = passport.split(' ')
    passport_keys = {passport_part.split(':')[0] for passport_part in passport_parts}.difference({'cid'})

    return mandatory_keys == passport_keys


valid_passports = (check_password(passport) for passport in passports)
print(f'{sum(valid_passports)=}')  # 202
