def remove_duplicates_sorted(nums: list[int]) -> list[int]:
    new_lst: list[int] = []
    
    for num in nums:
        if num in new_lst:
            continue
        else:
            new_lst.append(num)
    return new_lst


if __name__ == "__main__":
    print(remove_duplicates_sorted([1, 1, 2, 3, 3]))          # [1, 2, 3]
    print(remove_duplicates_sorted([2, 2, 2]))                # [2]
    print(remove_duplicates_sorted([-3, -3, 0, 1, 1, 1, 4]))  # [-3, 0, 1, 4]
    print(remove_duplicates_sorted([1, 2, 3]))                # [1, 2, 3]
    print(remove_duplicates_sorted([5]))                      # [5]
    print(remove_duplicates_sorted([]))                       # []