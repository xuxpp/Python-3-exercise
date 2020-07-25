import cProfile

full_grid = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 1, 4, 3, 6, 5, 8, 9, 7],
    [3, 6, 5, 8, 9, 7, 2, 1, 4],
    [8, 9, 7, 2, 1, 4, 3, 6, 5],
    [5, 3, 1, 6, 4, 2, 9, 7, 8],
    [6, 4, 2, 9, 7, 8, 5, 3, 1],
    [9, 7, 8, 5, 3, 1, 6, 4, 2],
]

quzz = [
    [0, 0, 0, 0, 0, 1, 0, 9, 4],
    [3, 0, 0, 0, 0, 7, 1, 0, 0],
    [0, 0, 0, 0, 9, 0, 0, 0, 0],

    [7, 0, 6, 5, 0, 0, 2, 0, 9],
    [0, 3, 0, 0, 2, 0, 0, 6, 0],
    [9, 0, 2, 0, 0, 6, 3, 0, 1],

    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 7, 3, 0, 0, 0, 0, 2],
    [4, 1, 0, 7, 0, 0, 0, 8, 0],
]

def get_empty_cell_index(grid):
    for row_idx, row in enumerate(grid):
        for column_idx, val in enumerate(row):
            if val == 0: return (row_idx, column_idx)
    return -1, -1 # -1 means no empty cell

def is_row_conflict(grid, r, val):
    for x in grid[r]:
        if x == val: return True
    return False

def is_column_conflict(grid, c, val):
    for row in grid:
        if row[c] == val: return True
    return False

def is_squre_conflict(grid, r, c, val):
    squre_start_r_idx = r - (r % 3)
    squre_start_c_idx = c - (c % 3)
    for row in grid[squre_start_r_idx:squre_start_r_idx+3]:
        for x in row[squre_start_c_idx:squre_start_c_idx+3]:
            if x == val: return True
    return False

def is_conflict(grid, row_idx, column_idx, value):
    return is_row_conflict   (grid, row_idx, value)    or \
           is_column_conflict(grid, column_idx, value) or \
           is_squre_conflict (grid, row_idx, column_idx, value)

def nested_list_copy(l):
    return [ r[:] for r in l ]

def solve(grid, answers):
    empty_r, empty_c = get_empty_cell_index(grid)
    if empty_r != -1 and empty_c != -1:
        for i in range(1, 10):
            if not is_conflict(grid, empty_r, empty_c, i):
                grid[empty_r][empty_c] = i
                solve(nested_list_copy(grid), answers) # make a copy of the grid to find all solutions
    else:
        answers.append(grid)

answers = []
cProfile.run("solve(quzz, answers)") # See how fast you run

print(len(answers))