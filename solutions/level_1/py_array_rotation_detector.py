def array_rotation_detector(arr1: list, arr2: list) -> bool:
    """
    Function that takes two lists (arrays) as parameters and
    determines if the second list is a rotation of the first list (left or right).
    
    A rotation means that the elements are shifted circularly.
    For example, shifting [1, 2, 3] to the right by one position results in [3, 1, 2].
    
    The function must return True if arr2 is a rotation of arr1, and False otherwise.
    If the arrays have different lengths, they cannot be rotations of each other.
    Two empty arrays are considered rotations of each other.
    """
    if not arr1 and not arr2:
        return True
    for i in range(len(arr1)):
        if (arr1[i:] + arr1[:i]) == arr2:
            return True
    return False


if __name__ == "__main__":
    print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])) # -> True
    print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4])) # -> True
    print(array_rotation_detector([1, 2, 3], [3, 2, 1]))             # -> False
    print(array_rotation_detector([1, 2], [1, 2, 3]))                # -> False
    print(array_rotation_detector([1, 2, 3, 4, 5], [1, 2, 3, 4]))    # -> False
    print(array_rotation_detector([7, 8, 9], [8, 9, 7]))             # -> True
    print(array_rotation_detector([], []))                           # -> True