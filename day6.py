def part1(data):
    # answers will be a list of sets
    answers = [set()]
    i = 0
    # Load each answer into a list of sets
    for row in data:
        if row == '\n':
            i += 1
            answers.append(set())
        for answer in row.strip():
            answers[i].add(answer.strip())
        
    return sum([len(answer) for answer in answers])


def get_overlap(list_of_sets):
    """ Returns the number of overlapping answers """
    overlap = list_of_sets[0].intersection(*list_of_sets)
    return len(overlap)


def part2(data):
    count = 0
    # Temporarily store the answers for each group
    group_answers = []
    for row in data:
        if row == '\n':
            count += get_overlap(group_answers)
            group_answers = []
        else:
            group_answers.append(set(row.strip()))
    # Ensure final group is processed
    count += get_overlap(group_answers)
    return count

if __name__ == "__main__":
    # Open file
    with open("day6-input.txt") as file:
        data = file.readlines()

    print(f"p1: {part1(data)}")
    print(f"p2: {part2(data)}")
