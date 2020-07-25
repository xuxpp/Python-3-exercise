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

quiz = [
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

def nested_list_copy(l):
    return [ r[:] for r in l ]

def is_conflict(grid, row_idx, column_idx, value):
    pass

def solve(grid, answers):
    pass

answers = []
solve(quiz, answers)

# Print number of solutions