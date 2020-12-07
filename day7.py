class Bag:
    def __init__(self, name):
        self.name = name
        self.contents = {}

    def add_bag(self, qty, bag):
        """ Takes in a Bag object and the qty of that bag and add's it to the contents
        of the bag """
        self.contents[bag] = int(qty)

    @classmethod
    def traverse_part1(cls, bags, starting_bag, valid_bags):
        """ Loop through each bag and each inner bag, checking for shiny gold bag.
        If it is found, add the starting_bag to the set and return it. """
        for bag in bags.keys():
            if bag.name == "shiny gold bag":
                valid_bags.add(starting_bag)
            cls.traverse_part1(bag.contents, starting_bag, valid_bags)
        return valid_bags
    
    @classmethod
    def traverse_part2(cls, bag):
        """ Loop through each bag recursively and count the number of bags.
        The final(empty) bag/s will return 1, this will be multipled by the qty of that bag and
        added to count. This will again be multipled by qty and returned, etc. until getting
        back to the gold shiny bag"""
        count = 1
        for bag_name, qty in bag.contents.items():
            count += qty * (cls.traverse_part2(bag_name))
        return count

    @staticmethod
    def process_bags(data):
        # Create a new dictionary
        bags = {}
        for bag in data:
            # Parse the current line to get the information in a usable format
            current_bag = bag.strip().split(" contain ")
            bag_name = current_bag[0].removesuffix('s')
            # If the bag doesn't already exist, create it
            if bag_name not in bags:
                bags[bag_name] = Bag(bag_name)

            # Get each of the inner bags in a usable format
            inner_bags = current_bag[1].split(', ')

            # Loop through each inner bag
            for inner_bag in inner_bags:
                # Make sure the bag isn't empty
                if inner_bag != "no other bags.":
                    # Get the bag name and qty of each inner bag
                    inner_bag = inner_bag.replace('.', '').removesuffix('s').split(' ', maxsplit=1)
                    inner_bag_qty = inner_bag[0]
                    inner_bag_name = inner_bag[1]
                    
                    # If the inner bag doesn't exist, create it and add it to the outer bag.
                    if inner_bag_name not in bags:
                        new_bag = Bag(inner_bag_name)
                        bags[inner_bag_name] = new_bag
                        bags[bag_name].add_bag(inner_bag_qty, new_bag)
                    else:
                    # If it does exist, simply add it to the outer bag
                        bags[bag_name].add_bag(inner_bag_qty, bags[inner_bag_name])
        return bags

def part1():
    # Create an empty set to store valid bags
    valid_bags = set()
    # Loop through each bag in the bags dictionary and loop through inner bags
    for bag in bags.values():
        # Union is required as multiple sets are returned
        valid_bags.union(Bag.traverse_part1(bag.contents, bag.name, valid_bags))
    return len(valid_bags)

def part2():
    # Minus one so as not to count the shiny gold bag itself.
    return Bag.traverse_part2(bags['shiny gold bag']) - 1
    

if __name__ == "__main__":
    with open("day7-input.txt") as file:
        data = file.readlines()

    # Process the data and return a dictionary of bags
    bags = Bag.process_bags(data)

print(f"Part1: {part1()}")

print(f"Part2: {part2()}")
