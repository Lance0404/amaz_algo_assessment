"""
I misunderstand the question by not paying attention during the online test
The below should be the functional, but time complexity not yet optimized
"""


def grid_update_alog(row, col, grid):
    max_row_index = row - 1
    max_col_index = col - 1

    def grid_update_complete(grid_to_check):
        for i in range(row):
            for j in range(col):
                if grid_to_check[i][j] != 1:
                    return False
        return True

    def get_seeds_from_grid(grid_to_check):
        tmp_seeds = []
        for i in range(row):
            for j in range(col):
                if grid_to_check[i][j] == 1:
                  tmp_seeds.append((i, j))
        return tmp_seeds

    def get_adject_cells_index_from_seeds(seeds_to_check):
        dedup_cells = set()
        for i, j in seeds_to_check:
            # work on for corner first
            if i == 0 and j == 0:
                dedup_cells.add((i, j + 1))
                dedup_cells.add((i + 1, j))
            elif i == 0 and j == max_col_index:
                dedup_cells.add((i, j - 1))
                dedup_cells.add((i - 1, j))
            elif i == max_row_index and j == 0:
                dedup_cells.add((i - 1, j))
                dedup_cells.add((i, j + 1))
            elif i == max_row_index and j == max_col_index:
                dedup_cells.add((i - 1, j))
                dedup_cells.add((i, j - 1))
            elif i == 0:
                dedup_cells.add((i, j - 1))
                dedup_cells.add((i, j + 1))
                dedup_cells.add((i + 1, j))
            elif i == max_row_index:
                dedup_cells.add((i - 1, j))
                dedup_cells.add((i, j - 1))
                dedup_cells.add((i, j + 1))
            elif j == 0:
                dedup_cells.add((i - 1, j))
                dedup_cells.add((i, j + 1))
                dedup_cells.add((i + 1, j))
            elif j == max_col_index:
                dedup_cells.add((i - 1, j))
                dedup_cells.add((i, j - 1))
                dedup_cells.add((i + 1, j))
            else:
                dedup_cells.add((i - 1, j))
                dedup_cells.add((i, j - 1))
                dedup_cells.add((i, j + 1))
                dedup_cells.add((i + 1, j))
        return sorted(list(dedup_cells), key=lambda tup: (tup[0], tup[1]))

    def update_grid_with_seeds(grid_to_check, seeds_to_check):
        cells_to_update = get_adject_cells_index_from_seeds(seeds_to_check)
        print(f'cells_to_update {cells_to_update}')
        for i, j in cells_to_update:
            grid_to_check[i][j] = 1

    if grid_update_complete(grid):
        return 0

    min_day = 0
    seeds = []
    print(f'grid: {grid}')
    while not grid_update_complete(grid):
        min_day += 1
        seeds = get_seeds_from_grid(grid)
        print(f'seeds: {seeds}')
        update_grid_with_seeds(grid, seeds)
        print(f'grid: {grid}')

        # if min_day > 3:
        #     break
    return min_day


# test0
row = 5
col = 5
input = [
    [1,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,1]
]
# expect return 4
print(grid_update_alog(row, col, input))

# test1
row = 5
col = 6
input = [
    [0,0,1,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0],
    [0,1,0,0,0,0]
]
# expect return 3
print(grid_update_alog(row, col, input))