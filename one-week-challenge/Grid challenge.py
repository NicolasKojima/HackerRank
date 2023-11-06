

def make_arr(grid):
    arr = [char for char in grid]
    print(arr, 2)
    return arr

def newgrid(grid, num_grid):
    orig_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for j in range(len(orig_alph)):
        for i in range(len(grid)):
            for k in range(len(grid[i])):
                if grid[i][k] == orig_alph[j]:
                    num_grid[i][k] = j
    return num_grid 

def checkvertical(num_grid):
    for i in range(len(num_grid)-1):
        for j in range(len(num_grid[i])):
            if num_grid[i][j] > num_grid[i+1][j]:
                return "NO"
    return "YES"
            

def gridChallenge(grid):
    for i in range(len(grid)):
        arr = make_arr(grid[i])
        grid[i] = arr
        print(grid)

    for i in range(len(grid)):
        grid[i].sort()
        print(grid)
    
    num_grid = grid
    num_grid = newgrid(grid, num_grid)
    print(num_grid, "num grid")
    
    ans = checkvertical(num_grid)
    print(ans)
    return ans


grid = [
    "eibjbwsp",
    "ptfxehaq",
    "jxipvfga",
    "rkefiyub",
    "kalwfhfj",
    "lktajiaq",
    "srdgoros",
    "nflvjznh"
]

gridChallenge(grid)