from typing import Any

def max_len(lists: list[list]) -> int:
    max: int = 0

    for lst in lists:
        if len(lst) > max:
            max = len(lst)
    return max


def interleave_lists(lists: list[list]) -> list:
    max_l = max_len(lists)
    new_lst: list[Any] = []
    
    for i in range(max_l):
        for lst in lists:
            if i < len(lst):
                new_lst.append(lst[i])
    return new_lst
        

if __name__ == "__main__":
    print(interleave_lists([[1, 2, 3], ['a', 'b', 'c']]))  # [1, 'a', 2, 'b', 3, 'c']
    print(interleave_lists([[1, 2], [10, 20, 30, 40]]))    # [1, 10, 2, 20, 30, 40]
    print(interleave_lists([[1, 4, 7], [2, 5], [3]]))      # [1, 2, 3, 4, 5, 7]
    print(interleave_lists([[], [1, 2]]))                  # [1, 2]
    print(interleave_lists([[5]]))                         # [5]
    print(interleave_lists([]))                            # []