def sorted_difference(a: list[int], b: list[int]) -> list[int]:
    new_lst: list[int] = []

    for num in a:
        if (num not in b) and (num not in new_lst):
            new_lst.append(num)
    
    return new_lst

if __name__ == "__main__":
    print(sorted_difference([1, 1, 2, 3, 3], [3]))      # [1, 2]
    print(sorted_difference([1, 2, 3, 4, 5], [2, 4]))   # [1, 3, 5]
    print(sorted_difference([-3, 0, 2], [-5, -3, 1]))   # [0, 2]
    print(sorted_difference([1, 2], [1, 2, 3]))         # []
    print(sorted_difference([4, 4, 6], []))             # [4, 6]
    print(sorted_difference([], [1, 2]))                # []
