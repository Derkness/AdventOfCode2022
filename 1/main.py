
def get_list_of_input():
    numbers=[]
    with open("input.txt", "r") as file:
        count = 0
        for line in file:
            line = line[:-1]
            if line == "":
                numbers.append(count)
                count=0
            else:
                count+=int(line)
    return numbers
        

if __name__ == "__main__":
    calories = get_list_of_input()
    
    print("Part 1:", max(calories))
    
    first = calories.pop(calories.index(max(calories)))
    second = calories.pop(calories.index(max(calories)))
    third = calories.pop(calories.index(max(calories)))
    
    print("Part 2:", first+second+third)