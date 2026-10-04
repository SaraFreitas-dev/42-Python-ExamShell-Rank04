def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    """
    A function that maps a constellation of stars onto a grid and returns
    the visual representation as a list of strings.
      
    What it does:
    - Take a list of star coordinates as tuples (row, col) and grid size as integer
    - Return a list of strings representing the grid
    - Stars are represented by '*' and empty spaces by '.'
    - Grid coordinates start from (0, 0) at top-left
    - Ignore coordinates outside the grid boundaries
    - Handle duplicate coordinates (star appears only once)
    """
    
    

if __name__ == "__main__":
    print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))                 # -> ['*..', '.*.', '..*']
    print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)) # -> ['.*.', '***', '.*.']
    print(constellation_mapper([], 2))                                       # -> ['..', '..']
    print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))                 # -> ['*.', '.*']
    print(constellation_mapper([(0, 0), (5, 5)], 3))                         # -> ['*..', '...', '...']
    print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))                 # -> ['...', '***', '...']
