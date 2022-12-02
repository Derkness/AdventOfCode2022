

def readInput():
    moves = []
    with open("input.txt", "r") as file:
        for line in file:
            moves.append((line[0], line[2]))
            
    return moves
    
# If I had thought of it at the time, I would have used the options list below and done scode being something like
# distance between index * 3
def calculate_score_part_1(theirs, mine):
    score = 0
    if mine == 'X':
        score+=1
        if theirs == 'A':
            score+=3
        elif theirs == 'C':
            score+=6
    elif mine == 'Y':
        score+=2
        if theirs == 'B':
            score+=3
        elif theirs == 'A':
            score+=6
    elif mine == 'Z':
        score+=3
        if theirs == 'C':
            score+=3
        elif theirs == 'B':
            score+=6
    return score

options = ['A','B','C']

def calculate_score_part_2(theirs, outcome):
    score = 0
    if outcome == 'X':
       score += (options.index(theirs)-1+3)%3 + 1
    elif outcome == 'Y':
        score+=3
        score += (options.index(theirs))%3 + 1
    elif outcome == 'Z':
        score+=6
        score += (options.index(theirs)+1)%3 + 1
    return score
    


if __name__ == "__main__":
    moves = readInput()
    
    score = 0
    for pair in moves:
        score += calculate_score_part_1(pair[0], pair[1])
    print("Part 1:",score)
    
    score = 0
    for pair in moves:
        score += calculate_score_part_2(pair[0], pair[1])
    print("Part 2:",score)