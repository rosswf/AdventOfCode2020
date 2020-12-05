def row_no(row):
    row = row.replace("F", "0").replace("B", "1")
    return int(row, 2)


def col_no(col):
    col = col.replace("L", "0").replace("R", "1")
    return int(col, 2)

def calc_ids(tickets):
    # id = col_no * 8 + row_no
    return [row_no(ticket[:7]) * 8 + col_no(ticket[7:]) for ticket in tickets]

def part1(tickets):
    return max(calc_ids(tickets))

def part2(tickets):
    sorted_ids = sorted(calc_ids(tickets))
    first_id = sorted_ids[0]
    for i, seat_id in enumerate(sorted_ids):
        # Work out which id is missing
        if seat_id != i + first_id:
            return seat_id - 1
                
if __name__ == "__main__":
    # Load file into a list
    with open("day5-input.txt") as file:
        data = file.readlines()

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = part2(data)
    print(f"Part 2: {p2}")
