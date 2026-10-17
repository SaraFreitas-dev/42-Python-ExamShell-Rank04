def grid_border(rows: int, cols: int) -> list[str]:
    grid: list[str] = []
    
    if cols <= 0 or rows <= 0:
        return grid
    for r in range(rows):
        curr_line: str = ""
        for c in range(cols):
            if (r == 0 or r == (rows - 1)
                or c == 0 or c == (cols - 1)):
                curr_line += "#"
            else:
                curr_line += "."
        grid.append(curr_line)
    return grid


if __name__ == "__main__":
    print(grid_border(3, 4))  # ['####', '#..#', '####']
    print(grid_border(4, 3))  # ['###', '#.#', '#.#', '###']
    print(grid_border(1, 5))  # ['#####']
    print(grid_border(2, 2))  # ['##', '##']
    print(grid_border(1, 1))  # ['#']
    print(grid_border(0, 4))  # []
