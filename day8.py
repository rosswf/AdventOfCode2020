def nop(arg: str, current_op: int, accumulator: int) -> (int, int):
    """ no op, increment current_op index and return it """
    current_op += 1
    return current_op, accumulator

def acc(arg: str, current_op: int, accumulator: int) -> (int, int):
    """ Increase accumulator, incrent current_op and accumaltor by arg
    and return them """
    current_op += 1
    accumulator += int(arg)
    return current_op, accumulator

def jmp(arg: str, current_op: int, accumulator: int) -> (int, int):
    """ Jump, increment current_op by arg and return it """
    current_op += int(arg)
    return current_op, accumulator

def part_1(instructions: list[list[str]]) -> (bool, int):
    """ Process the list of instructions, ensuring no repetition.
    Return the accumulator and True or False.
    True if the list of instructions is reached, if not return False.
    """
    current_op = 0
    accumulator = 0
    used_ops = []
    # While the end of the instructions has not been reached
    while instructions[current_op][0] != "0":
        # If the operation to be processed next has already been processed
        # return False. Used in p2
        if current_op in used_ops:
            return False, accumulator
        op = instructions[current_op][0]
        arg = instructions[current_op][1]
        # Add the current operation to the list of used operations.
        used_ops.append(current_op)
        # Call the relevant operation
        current_op, accumulator = ops[op](arg, current_op, accumulator)
    else:
        # If the end of the loop is reached naturally, return True. Used in p2
        return True, accumulator

def part_2(instructions: list[list[str]]) -> int:
    """ Try changing each nop to jmp or jmp to nop one by one.
    Run these new instructions through part_1 to determine if the end
    of the instructions can be reached. Once they can, return accumulator.
    """
    for i in range(len(instructions)):
        # Change jmp to nop and nop to jump
        if instructions[i][0] == 'jmp':
            instructions[i][0] = 'nop'
        elif instructions[i][0] == 'nop':
            instructions[i][0] = 'jmp'

        # If part_1 returns True, then there is no longer an infinite loop.
        if (result:= part_1(instructions))[0]:
            return result[1]
        else:
            # Change instructions back to what they were originally.
            if instructions[i][0] == 'jmp':
                instructions[i][0] = 'nop'
            elif instructions[i][0] == 'nop':
                instructions[i][0] = 'jmp'
            
if __name__ == "__main__":
    # Open the file and read the information into data
    with open("day8-input.txt") as file:
        data = file.readlines()
        
    # Split each line and store in a list of lists [operation, argument]
    instructions = [instruction.split() for instruction in data]
    # Add a blank instruction at the end of the file to determine
    # if the end of the file is reached.
    instructions.append("0")

    # Store each operation function in a dictionary to use later.
    ops = {"nop": nop, "acc": acc, "jmp": jmp}
    
    print(f"Part 1: {part_1(list(instructions))[1]}")
    print(f"Part 2: {part_2(list(instructions))}")
