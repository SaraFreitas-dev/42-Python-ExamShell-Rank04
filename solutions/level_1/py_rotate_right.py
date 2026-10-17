def rotate_right(arr: list, k: int) -> list:
    if k == 0 or not arr:
        return (arr)
    else:
        k %= len(arr)
        return(arr[-k:] + arr[:-k])
    
    

if __name__ == "__main__":
    print(rotate_right([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
    print(rotate_right([1, 2, 3, 4], 1))     # [4, 1, 2, 3]
    print(rotate_right([1, 2, 3], 0))        # [1, 2, 3]
    print(rotate_right([1, 2, 3], 5))        # [2, 3, 1]
    print(rotate_right([1, 2, 3, 4], -1))    # [2, 3, 4, 1]
    print(rotate_right([], 3))               # []