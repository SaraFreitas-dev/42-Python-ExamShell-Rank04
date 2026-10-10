"""
    Write a function that finds the intersection of multiple sorted lists.
    Return a new list containing elements that appear in ALL input lists, in sorted order.
  
    The function should:
    - Return elements that appear in ALL lists
    - Result should be sorted in ascending order
    - Remove duplicates from the result
    - Handle empty input or empty lists gracefully
    - If any list is empty, the intersection is empty
  
"""


def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    res: list[int] = []

    if not lists:
        return []
    for elem in lists[0]:
        is_present: bool = True
        for lst in lists[1:]:
            if elem not in lst:
                is_present = False
                break
        if is_present and (elem not in res):
            res.append(elem)
    return res


if __name__ == "__main__":
    print(list_intersection_finder([[1, 2, 3], [2, 3, 4]]))          # -> [2, 3]
    print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))   # -> [4]
    print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]])) # -> [1, 2, 3]
    print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))                     # -> []
    print(list_intersection_finder([]))                                         # -> []
    print(list_intersection_finder([[1, 2, 3], []]))                            # -> []
    print(list_intersection_finder([[5]]))                                      # -> [5]
