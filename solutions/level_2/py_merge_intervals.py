def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    new_lst: list[list[int]] = []
    s_intervals: list[list[int]] = sorted(intervals)
    
    if not intervals:
        return []
    
    temp_lst: list[int] = s_intervals[0]
    for i in range(1, len(s_intervals)):
        end: int = temp_lst[1]
        if (s_intervals[i][0] <= end and s_intervals[i][1] >= end):
            temp_lst[1] = s_intervals[i][1]
        elif (s_intervals[i][0] >= end):
            new_lst.append(temp_lst)
            temp_lst = s_intervals[i]

    new_lst.append(temp_lst)

    return new_lst
        
if __name__ == "__main__":
    print(merge_intervals([[5, 7], [1, 2]]))                     # [[1, 2], [5, 7]]
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1, 6], [8, 10], [15, 18]]
    print(merge_intervals([[1, 4], [4, 5]]))                     # [[1, 5]]
    print(merge_intervals([[1, 10], [2, 3], [4, 5]]))            # [[1, 10]]
    print(merge_intervals([[3, 3]]))                             # [[3, 3]]
    print(merge_intervals([]))                                   # []
