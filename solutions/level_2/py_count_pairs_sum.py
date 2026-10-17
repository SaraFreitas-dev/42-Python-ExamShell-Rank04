def count_pairs_sum(nums: list[int], target: int) -> int:
    counter: int = 0
    
    if len(nums) < 2:
        return 0
    for i in range(len(nums) - 1):
        for j in range((i + 1), len(nums)):
            if (nums[i] + nums[j]) == target:
                counter += 1
                break
            elif (nums[i] + nums[j]) > target:
                break
    return counter
    
if __name__ == "__main__":
    print(count_pairs_sum([1, 2, 3, 4, 5], 6))     # 2
    print(count_pairs_sum([1, 2, 3, 4, 5, 6], 7))  # 3
    print(count_pairs_sum([-2, 0, 2, 4], 2))       # 2
    print(count_pairs_sum([1, 3, 5], 2))           # 0
    print(count_pairs_sum([3], 6))                 # 0
    print(count_pairs_sum([], 5))                  # 0