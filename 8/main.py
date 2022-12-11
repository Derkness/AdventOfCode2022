

def get_inp():
    with open('input.txt', 'r') as f:
        return [f.strip() for f in f.readlines()]


def check_visible(x, y, grid, tree):
    blockers = 0
    for tracker in range(0, x):
        if grid[tracker][y] >= tree:
            blockers += 1
            break

    for tracker in range(x+1, len(grid)):
        if grid[tracker][y] >= tree:
            blockers += 1
            break

    for tracker in range(0, y):
        if grid[x][tracker] >= tree:
            blockers += 1
            break

    for tracker in range(y+1, len(grid[0])):
        if grid[x][tracker] >= tree:
            blockers += 1
            break
    return blockers < 4

def get_score(x,y,grid,tree):
    base = 1
    for index, tracker in enumerate(range(x-1, 0, -1)):
        if grid[tracker][y] >= tree:
            base = base*(index+1)
            break
    else:
        base=base*(x)
        
    for index, tracker in enumerate(range(x+1, len(grid))):
        if grid[tracker][y] >= tree:
            base = base*(index+1)
            break
    else:
        base=base*(len(range(x+1, len(grid))))
            

    for index, tracker in enumerate(range(y-1, 0, -1)):
        if grid[x][tracker] >= tree:
            base = base*(index+1)
            break
    else:
        base=base*(y)

    for index, tracker in enumerate(range(y+1, len(grid[0]))):
        if grid[x][tracker] >= tree:
            base = base*(index+1)
            break
    else:
        base=base*(len(range(y+1, len(grid[0]))))
    return base


if __name__ == "__main__":
    grid = get_inp()
    amount_visible = 0
    score = 0
    for x, row in enumerate(grid):
        for y, tree in enumerate(row):
            amount_visible += check_visible(x, y, grid, tree)
            score = max(score,get_score(x,y,grid,tree))

    print('Part 1:', amount_visible)
    print('Part 2:', score)