def count_pairs_sum(nums: list[int], target: int) -> int:
    counter: int = 0

    if len(nums) < 2:
        return 0
    i: int = 0
    j: int = len(nums) - 1
    while i < j:
        if (nums[i] + nums[j]) == target:
            counter += 1
            i += 1
            j -= 1
        elif (nums[i] + nums[j]) > target:
            j -= 1
        else:
            i += 1
    return counter
    
if __name__ == "__main__":
    print(count_pairs_sum([1, 2, 3, 4, 5], 6))     # 2
    print(count_pairs_sum([1, 2, 3, 4, 5, 6], 7))  # 3
    print(count_pairs_sum([-2, 0, 2, 4], 2))       # 2
    print(count_pairs_sum([1, 3, 5], 2))           # 0
    print(count_pairs_sum([3], 6))                 # 0
    print(count_pairs_sum([], 5))                  # 0