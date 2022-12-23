
def read_input():
    with open('input.txt', 'r') as f:
        return [line.strip().split() for line in f.readlines()]
    
def main():
    commands = read_input()
    value = 1
    signal_strength = 0
    # Cycle is 0 for part 2, 1 for part 1. idk why.
    cycle = 0
    for command in commands:
        if command[0] == "addx":
            if (cycle%40 == 20):
                signal_strength+=cycle*value
            if (cycle%40 == 0):
                print()
            char = '#' if abs(value-cycle%40) <=1 else '.'
            print(char, end='')
            cycle+=1
            if (cycle%40 == 20):
                signal_strength+=cycle*value
            if (cycle%40 == 0):
                print()
            char = '#' if abs(value-cycle%40) <=1 else '.'
            print(char, end='')
            cycle+=1
            value+=int(command[1])
                
        else:
            if (cycle%40 == 20):
                signal_strength+=cycle*value
            if (cycle%40 == 0):
                print()
            char = '#' if abs(value-cycle%40) <=1 else '.'
            print(char, end='')
            cycle+=1
    print("Signal Strength:", signal_strength)

    
    
    
if __name__ == "__main__":
    main()