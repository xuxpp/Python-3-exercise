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
    if not row_conflict(grid[row_idx], column_idx, value):
        if not col_conflict(grid, column_idx, value):
            if not box_conflict(grid, row_idx, column_idx, value):
                return False
    return True

def row_conflict(row, column_idx, value):
    for val in row:
        if val == value:
            return True
    return False

def col_conflict(grid, column_idx, value):
    for row in grid:
        if row[column_idx] == value:
            return True
    return False

def box_conflict(grid, row_idx, column_idx, value):
    row_start = row_idx - row_idx % 3  
    col_start = column_idx - column_idx % 3
    for row in grid[row_start : row_start + 3]:
        for val in row[col_start:col_start + 3]:
            if val == value:
                return True
    return False


def solve(grid, answers):
    (row_empty_idx, col_empty_idx) = get_empty_cell_index(grid)
    if row_empty_idx == -1 and col_empty_idx == -1:
        answers.append(grid)
    else:
        for n in range(1,10):
            if not is_conflict(grid, row_empty_idx, col_empty_idx, n):
                grid[row_empty_idx][col_empty_idx] = n
                solve(nested_list_copy(grid), answers)




    


    




answers = []
solve(quiz, answers)
print(len(answers))

# Print number of solutions

# print(is_conflict(quiz, 1, 2, 6))