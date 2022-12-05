import re

def get_starting_structure():
    first_lines = []
    amount_of_lines = 0
    with open("input.txt", "r") as file:
        for line in file:
            if '1' in line:
                amount_of_lines = int(line[-2])
                break
            else:
                first_lines.append(line)
    structure = [[] for _ in range(amount_of_lines)]
    for line in reversed(first_lines):
        for index, char in enumerate(line[:-1]):
            if (char != ' '):
                structure[index].insert(len(structure[index]),char)
    
    return structure
            
def move_boxes_1(structure, script):
    for i in range(int(script[0])):
        box = structure[int(script[1])-1].pop()
        structure[int(script[2])-1].append(box)
    return structure


def move_boxes_2(structure, script):
    boxes = structure[int(script[1])-1][-int(script[0]):]
    del structure[int(script[1])-1][-int(script[0]):]
    structure[int(script[2])-1].extend(boxes)
    return structure
    

if __name__ == "__main__":
    structure1 = get_starting_structure()
    with open("input.txt", "r") as file:
        for line in file:
            if line[0] == "m":
                values = re.split("move | from | to |\n", line)
                values = values[1:4]
                structure1 = move_boxes_1(structure1, values)

    print("Part 1")
    for struct in structure1:
        print(struct)
        
    structure2 = get_starting_structure()
    with open("input.txt", "r") as file:
        for line in file:
            if line[0] == "m":
                values = re.split("move | from | to |\n", line)
                values = values[1:4]
                structure2 = move_boxes_2(structure2, values)
                
    print("Part 2")
    for struct in structure2:
        print(struct)
    