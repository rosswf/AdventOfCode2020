import csv

# Check the password meets the policy for part 1
def check_policy_p1(num, letter, passw):
    if int(num[0]) <= passw.count(letter) <= int(num[1]):
        return True
    else:
        return False

# Check the password meets the policy for part 2
def check_policy_p2(num, letter, passw):
    loc0 = int(num[0]) - 1
    loc1 = int(num[1]) - 1
    if passw[loc0] == letter and passw[loc1] == letter:
        return False
    elif passw[loc0] == letter or passw[loc1] == letter:
        return True
    return False

# Open the file and use the csv module to load it into a dictionary
with open("day2-input.txt") as file:
    reader = csv.DictReader(file, fieldnames=('num', 'letter', 'passw'), delimiter=' ')
    data = [{'num': row['num'].split('-'),
             'letter' : row['letter'][0],
             'passw' : row['passw']} for row in reader]

# Check part 1, return True of False and use sum() to count
p1 = sum([check_policy_p1(row['num'], row['letter'], row['passw']) for row in data])

# Check part 2, return True or False and use sum() to count.
p2 = sum([check_policy_p2(row['num'], row['letter'], row['passw']) for row in data])

print(p1)
print(p2)
