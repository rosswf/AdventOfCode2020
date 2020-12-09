from itertools import combinations

def part_1(data, preamble):
    """Loop through each number and use combinations to calculate the sum of
    groups of 2 numbers in the preamble for each number.
    Return the number which is not the sum of 2 numbers in the preamble"""
    for i in range(preamble, len(data)):
        combs = combinations(data[i-preamble:i], 2)
        combs = list(map(sum, combs))
        if data[i] not in combs:
            return data[i]

def part_2(data, number):
    """Loop through every number in the data and find a continuous set of
    numbers which add up to the number calculated in part 1.
    Return the sum of the highest and lowest number in this set. """
    numbers = []
    current_total = 0
    for i, _ in enumerate(data):
        for num in data[i:]:
            # Add each number to the list and create a running total
            numbers.append(num)
            current_total += num
            # If the total is the same as the number from part 1, return
            if current_total == number:
                return (sorted_nums := sorted(numbers))[0] + sorted_nums[-1]
            # If the total goes higher than the number, reset
            elif current_total > number:
                numbers = []
                current_total = 0
                break

if __name__ == "__main__":
    # Load the file
    with open("day9-input.txt") as file:
        data = file.readlines()

    # Remove newline characters and convert to integer
    data = map(str.strip, data)
    data = list(map(int, data))

    p1 = part_1(data, 25)
    print(f"Part 1: {p1}")

    p2 = part_2(data, p1)
    print(f"Part 2: {p2}")
