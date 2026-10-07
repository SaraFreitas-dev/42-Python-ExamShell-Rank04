"""
    A function that merges multiple sorted lists into one sorted list while
    maintaining the sort order efficiently.

    The function should:
    - Take a list of sorted integer lists as input
    - Return a single merged list in ascending order
    - Preserve all duplicate elements in the final result
    - Handle empty lists and empty input gracefully
    - Maintain optimal efficiency for large inputs

    Rules:
    - All input lists are guaranteed to be sorted in ascending order
    - Empty lists should be ignored during merging
    - Return empty list if no valid input is provided
    - Preserve duplicates across different lists
    - Handle negative numbers correctly

    Edge cases to handle:
    - Empty input list: return empty list
    - Lists containing only empty lists: return empty list
    - Single list input: return copy of that list
    - All duplicate elements: preserve all instances
    - Negative numbers: handle correctly in sort order
"""

def merge_two(a: list[int], b: list[int]) -> list[int]:
    i: int = 0
    j: int = 0
    res: list[int] = []

    while (i < len(a) and j < len(b)):
        if (a[i] <= b[j]):
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while (i < len(a)):
        res.append(a[i])
        i += 1
    while (j < len(b)):
            res.append(b[j])
            j += 1
    return (res)
        

def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    while(len(lists) > 1):
        curr_lst: list[list[int]] = []
        for i in range(0, len(lists), 2):
            if ((i + 1) < len(lists)):
                curr_lst.append(merge_two(lists[i], lists[i + 1]))
            else:
                curr_lst.append(lists[i])
        lists = curr_lst
    return (lists[0][:])

if __name__ == "__main__":
    print(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))            # -> [1, 2, 3, 4, 5, 6]
    print(merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]])) # -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(merge_sorted_lists([[5], [1, 3], [2, 4]]))             # -> [1, 2, 3, 4, 5]
    print(merge_sorted_lists([[1, 1, 2], [2, 3, 3]]))            # -> [1, 1, 2, 2, 3, 3]
    print(merge_sorted_lists([[], [1, 2, 3]]))                   # -> [1, 2, 3]
    print(merge_sorted_lists([[]]))                              # -> []
    print(merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]))         # -> [-5, -3, -1, 0, 2, 4]
    print(merge_sorted_lists([[10], [10], [10]]))                # -> [10, 10, 10]
