# Open the input file
with open("input.txt") as f:
    data = f.readlines()

# Clean the data, get rid of newline, convert to int.
data = list(map(int, map(str.strip, data)))

# Loop through the data to find 3 numbers that add upto 2020
for i, num1 in enumerate(data):
    for j, num2 in enumerate(data[i:]):
        for num3 in data[j:]:
            if (num1 + num2 + num3) == 2020:
                found1 = num1
                found2 = num2
                found3 = num3
                break

print(found1, found2, found3)
print(f"{found1 * found2 * found3}")
