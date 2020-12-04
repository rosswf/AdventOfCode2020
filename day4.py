import re

def check_pass_p1(passport):
    if len(passport) < 8:
        if len(passport) == 7 and 'cid' not in passport.keys():
            return True
        return False
    return True

def check_pass_p2(passport):
    # check keys exist and store into easier to use variables
    try:
        byr = int(passport['byr'])
        iyr = int(passport['iyr'])
        eyr = int(passport['eyr'])
        hgt = passport['hgt']
        hcl = passport['hcl']
        ecl = passport['ecl']
        pid = passport['pid']
    except KeyError:
        return False
    # Check byr
    if not 1920 <= byr <= 2002:
        return False
    # Check iyr
    if not 2010 <= iyr <= 2020:
        return False
    # Check eyr
    if not 2020 <= eyr <= 2030:
        return False
    # Check hgt
    if not ((hgt[-2:] == "cm" and 150 <= int(hgt[:-2]) <= 193) or (hgt[-2:] == "in" and  59 <= int(hgt[:-2]) <= 76)):
        return False
    # Check hcl
    if not re.match(r"^#[0-9a-f]{6}$", hcl):
        return False
    # Check ecl
    if not ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    # Check pid
    if not re.match(r"^\d{9}$", pid):
        return False
    return True

if __name__ == '__main__':
    # Open file
    with open("day4-input.txt") as file:
        data = file.readlines()

    # Passports will be a list of dictionaries
    passports = [{}]
    i = 0
    # Load each passport into a list of lists
    for row in data:
        if row == '\n':
            i += 1
            passports.append({})
        else:
            for info in row.strip().split():
                x = info.split(':')
                passports[i][x[0]] = x[1]
    
    part1 = sum([check_pass_p1(passport) for passport in passports])
    print(f"Part1: {part1}")
    part2 = sum([check_pass_p2(passport) for passport in passports])
    print(f"Part2: {part2}")
