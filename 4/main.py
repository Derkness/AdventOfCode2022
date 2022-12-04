

def get_input():
    pairs = []
    with open("input.txt", "r") as file:
        for line in file:
            pairs.append(line.strip().split(','))
    return pairs

# Initially i just compared to see if the numbers were either side,
# but this seemed more fool proof
def get_range(limits):
    (start, end) = limits.split('-')
    return set(range(int(start), int(end)+1))

def check_complete_inclusion(first, second):
    return first.issubset(second) or second.issubset(first)

def check_partial_inclusion(first, second):
    return not first.isdisjoint(second)

if __name__ == "__main__":
    pairs = get_input()
    part_1_amount = 0
    part_2_amount = 0
    for pair in pairs:
        first = get_range(pair[0])
        second = get_range(pair[1])
        part_1_amount += check_complete_inclusion(first, second)
        part_2_amount += check_partial_inclusion(first, second)

    print("Part 1:", part_1_amount)
    print("Part 2:", part_2_amount)
