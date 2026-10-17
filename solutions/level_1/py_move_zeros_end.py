def move_zeros_end(nums: list[int]) -> list[int]:
    zeros_counter: int = 0
    new_lst: list[int] = []

    for num in nums:
        if num == 0:
            zeros_counter += 1
        else:
            new_lst.append(num)

    new_lst += [0] * zeros_counter
    return new_lst

if __name__ == "__main__":
    print(move_zeros_end([0, 1, 0, 3, 12]))     # [1, 3, 12, 0, 0]
    print(move_zeros_end([4, 0, -1, 0, 0, 7]))  # [4, -1, 7, 0, 0, 0]
    print(move_zeros_end([1, 2, 3]))            # [1, 2, 3]
    print(move_zeros_end([0, 0, 0]))            # [0, 0, 0]
    print(move_zeros_end([0]))                  # [0]
    print(move_zeros_end([]))                   # []