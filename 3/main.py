priorities = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]

def get_input():
    sacks = []
    with open("input.txt", "r") as file:
        for line in file:
            line=line.strip()
            sacks.append((line[:len(line)//2], line[len(line)//2:]))
            
    return sacks

def get_cost(char):
    return priorities.index(char)+1

if __name__ == "__main__":
    sacks = get_input()
    score = 0
    for sack in sacks:
        intersection = set(sack[0]).intersection(set(sack[1]))
        score += get_cost(intersection.pop())
    print("Part 1:", score)

    score = 0
    group = []
    for index, sack in enumerate(sacks):
        group.append(sack[0]+sack[1])
        if index % 3 == 2 and index != 0:
            intersection = set(group[0]).intersection(group[1], group[2])
            group.clear()
            score += get_cost(intersection.pop())

    print("Part 2:", score)
    