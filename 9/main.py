import math


def get_input():
    with open('input.txt', 'r') as f:
        return [line.strip().split() for line in f.readlines()]


def distance(ax, ay, bx, by):
    return math.sqrt((bx - ax)**2 + (by - ay)**2)


def print_map(tail_x, tail_y, head_x, head_y):
    print()
    for x in range(tail_x-20, tail_x+20):
        for y in range(tail_y-20, tail_y+20):
            if (tail_x == x and tail_y == y):
                print('T', end="")
            elif (head_x == x and head_y == y):
                print('H', end="")
            else:
                print('.', end="")
        print()


if __name__ == "__main__":
    locations = set()
    commands = get_input()
    tail_x = 0
    tail_y = 0
    head_x = 0
    head_y = 0
    locations.add((tail_x, tail_y))
    for command in commands:
        direction = command[0]
        for _ in range(0, int(command[1])):
            
            if direction == 'R':
                head_x += 1
            elif direction == 'L':
                head_x -= 1
            elif direction == 'U':
                head_y -= 1
            elif direction == 'D':
                head_y += 1
            if (distance(tail_x, tail_y, head_x, head_y) >= 2):
                tail_x += -1 if (head_x - tail_x) < 0 else 1 if (head_x - tail_x) > 0 else 0
                tail_y += -1 if (head_y - tail_y) < 0 else 1 if (head_y - tail_y) > 0 else 0
            locations.add((tail_x, tail_y))
            # commented for performance
            # print_map(tail_x, tail_y, head_x, head_y)
    print("Part 1:",len(locations))