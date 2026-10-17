# ─────────────────────────────────────────────────────────────
# EXERCISE BANK - PRACTICE (Rank 04 style)
# Original practice exercises inspired by the exam format.
# These are NOT the real exam subjects.
# ─────────────────────────────────────────────────────────────

import random

_rng = random.Random(42)

_CHAIN = {str(i): [str(i + 1)] for i in range(3000)}
_CHAIN["3000"] = []

_SHUFFLED_INTERVALS = [[i, i + 1] for i in range(0, 10000, 2)]
_rng.shuffle(_SHUFFLED_INTERVALS)

_CHECKER = ["".join("#" if (r + c) % 2 == 0 else "." for c in range(100))
            for r in range(100)]
_FULL = ["#" * 200 for _ in range(200)]

EXERCISES = {
    # ── LEVEL 1 ──────────────────────────────────────────────
    "py_rotate_right": {
        "level": 1,
        "subject": """\
Assignment name  : py_rotate_right
Expected files   : py_rotate_right.py
Allowed functions: Forbidden built-ins / modules: collections.deque.rotate().
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that rotates a list k positions to the right and returns the
result as a new list.

A rotation to the right moves every element k positions forward. Elements that
pass the end of the list come back at the beginning.
For example, rotating [1, 2, 3, 4] to the right by one position results in
[4, 1, 2, 3].

The function should:
- Return a NEW list, the original list must not be modified
- Accept a k bigger than the length of the list
- Rotate to the left when k is negative
- Return an empty list if the input list is empty

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def rotate_right(arr: list, k: int) -> list:

Examples:
    rotate_right([1, 2, 3, 4, 5], 2)  -> [4, 5, 1, 2, 3]
    rotate_right([1, 2, 3, 4], 1)     -> [4, 1, 2, 3]
    rotate_right([1, 2, 3], 0)        -> [1, 2, 3]
    rotate_right([1, 2, 3], 5)        -> [2, 3, 1]
    rotate_right([1, 2, 3, 4], -1)    -> [2, 3, 4, 1]
    rotate_right([], 3)               -> []
""",
        "function": "rotate_right",
        "tests": [
            ([[1, 2, 3, 4, 5], 2], [4, 5, 1, 2, 3]),
            ([[1, 2, 3, 4], 1], [4, 1, 2, 3]),
            ([[1, 2, 3], 0], [1, 2, 3]),
            ([[1, 2, 3], 5], [2, 3, 1]),
            ([[1, 2, 3, 4], -1], [2, 3, 4, 1]),
            ([[], 3], []),
            ([[7], 10], [7]),
            ([[1, 2, 3], 3], [1, 2, 3]),
            ([[1, 2, 3, 4, 5], -7], [3, 4, 5, 1, 2]),
            ([["a", "b", "c"], 1], ["c", "a", "b"]),
        ],
    },

    "py_grid_border": {
        "level": 1,
        "subject": """\
Assignment name  : py_grid_border
Expected files   : py_grid_border.py
Allowed functions: None
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that draws the border of a rectangular grid and returns the
visual representation as a list of strings.

The function should:
- Take the number of rows and the number of columns as integers
- Return a list of strings, one string per row
- Border cells are represented by '#' and inner cells by '.'
- A grid with only 1 or 2 rows (or columns) has no inner cells
- Return an empty list if rows or cols is 0 or negative

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def grid_border(rows: int, cols: int) -> list[str]:

Examples:
    grid_border(3, 4)
        -> ['####', '#..#', '####']
    grid_border(4, 3)
        -> ['###', '#.#', '#.#', '###']
    grid_border(1, 5)
        -> ['#####']
    grid_border(2, 2)
        -> ['##', '##']
    grid_border(1, 1)
        -> ['#']
    grid_border(0, 4)
        -> []
""",
        "function": "grid_border",
        "tests": [
            ([3, 4], ['####', '#..#', '####']),
            ([4, 3], ['###', '#.#', '#.#', '###']),
            ([1, 5], ['#####']),
            ([2, 2], ['##', '##']),
            ([1, 1], ['#']),
            ([0, 4], []),
            ([3, 0], []),
            ([-2, 3], []),
            ([3, -1], []),
            ([5, 1], ['#', '#', '#', '#', '#']),
            ([3, 3], ['###', '#.#', '###']),
        ],
    },
    "py_move_zeros_end": {
        "level": 1,
        "subject": """\
Assignment name  : py_move_zeros_end
Expected files   : py_move_zeros_end.py
Allowed functions: Forbidden built-ins / modules: sorted(), .sort().
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that moves every 0 of a list to the end, while keeping the
relative order of all the other elements.

The function should:
- Take a list of integers as input
- Return the list with all zeros at the end
- Keep the non-zero elements in the same order they had in the input
- Handle lists with no zeros, only zeros, or no elements
- Maintain optimal efficiency for large inputs

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def move_zeros_end(nums: list[int]) -> list[int]:

Examples:
    move_zeros_end([0, 1, 0, 3, 12])     -> [1, 3, 12, 0, 0]
    move_zeros_end([4, 0, -1, 0, 0, 7])  -> [4, -1, 7, 0, 0, 0]
    move_zeros_end([1, 2, 3])            -> [1, 2, 3]
    move_zeros_end([0, 0, 0])            -> [0, 0, 0]
    move_zeros_end([0])                  -> [0]
    move_zeros_end([])                   -> []
""",
        "function": "move_zeros_end",
        "tests": [
            ([[0, 1, 0, 3, 12]], [1, 3, 12, 0, 0]),
            ([[4, 0, -1, 0, 0, 7]], [4, -1, 7, 0, 0, 0]),
            ([[1, 2, 3]], [1, 2, 3]),
            ([[0, 0, 0]], [0, 0, 0]),
            ([[0]], [0]),
            ([[]], []),
            ([[5, 3, 0]], [5, 3, 0]),
            ([[0, -2, 0, -2]], [-2, -2, 0, 0]),
            ([[0, 1] * 5000], [1] * 5000 + [0] * 5000),
        ],
    },

    "py_remove_duplicates_sorted": {
        "level": 1,
        "subject": """\
Assignment name  : py_remove_duplicates_sorted
Expected files   : py_remove_duplicates_sorted.py
Allowed functions: Forbidden built-ins / modules: set(), dict.fromkeys().
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that removes the duplicate values of a sorted list.

The function should:
- Take a list of integers sorted in ascending order
- Return a NEW list where every value appears only once
- Keep the result in ascending order
- Handle empty lists and lists with a single element
- Maintain optimal efficiency for large inputs

Rules:
- The input list is guaranteed to be sorted in ascending order
- The input may contain negative numbers

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def remove_duplicates_sorted(nums: list[int]) -> list[int]:

Examples:
    remove_duplicates_sorted([1, 1, 2, 3, 3])          -> [1, 2, 3]
    remove_duplicates_sorted([2, 2, 2])                -> [2]
    remove_duplicates_sorted([-3, -3, 0, 1, 1, 1, 4])  -> [-3, 0, 1, 4]
    remove_duplicates_sorted([1, 2, 3])                -> [1, 2, 3]
    remove_duplicates_sorted([5])                      -> [5]
    remove_duplicates_sorted([])                       -> []
""",
        "function": "remove_duplicates_sorted",
        "tests": [
            ([[1, 1, 2, 3, 3]], [1, 2, 3]),
            ([[2, 2, 2]], [2]),
            ([[-3, -3, 0, 1, 1, 1, 4]], [-3, 0, 1, 4]),
            ([[1, 2, 3]], [1, 2, 3]),
            ([[5]], [5]),
            ([[]], []),
            ([[0, 0]], [0]),
            ([[-5, -5, -5, -1]], [-5, -1]),
            ([[i // 2 for i in range(10000)]], list(range(5000))),
        ],
    },

    # ── LEVEL 2 ──────────────────────────────────────────────
    "py_count_pairs_sum": {
        "level": 2,
        "subject": """\
Assignment name  : py_count_pairs_sum
Expected files   : py_count_pairs_sum.py
Allowed functions: None
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that counts how many pairs of elements of a sorted list add up
exactly to a target value.

A pair is made of two elements at different positions of the list. The same
pair must only be counted once: (1, 5) and (5, 1) are the same pair.

The function should:
- Take a sorted list of integers and a target integer
- Return the number of pairs whose sum is equal to the target
- Return 0 if no pair is found or if the list has less than 2 elements
- Maintain optimal efficiency for large inputs

Rules:
- The input list is guaranteed to be sorted in ascending order
- All the values of the list are distinct
- The list may contain negative numbers

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def count_pairs_sum(nums: list[int], target: int) -> int:

Examples:
    count_pairs_sum([1, 2, 3, 4, 5], 6)     -> 2
    count_pairs_sum([1, 2, 3, 4, 5, 6], 7)  -> 3
    count_pairs_sum([-2, 0, 2, 4], 2)       -> 2
    count_pairs_sum([1, 3, 5], 2)           -> 0
    count_pairs_sum([3], 6)                 -> 0
    count_pairs_sum([], 5)                  -> 0
""",
        "function": "count_pairs_sum",
        "tests": [
            ([[1, 2, 3, 4, 5], 6], 2),
            ([[1, 2, 3, 4, 5, 6], 7], 3),
            ([[-2, 0, 2, 4], 2], 2),
            ([[1, 3, 5], 2], 0),
            ([[3], 6], 0),
            ([[], 5], 0),
            ([[1, 2], 3], 1),
            ([[-5, -3, -1, 1, 3, 5], 0], 3),
            ([[1, 2, 3, 4], 100], 0),
            ([list(range(10000)), 9999], 5000),
        ],
    },

    "py_merge_intervals": {
        "level": 2,
        "subject": """\
Assignment name  : py_merge_intervals
Expected files   : py_merge_intervals.py
Allowed functions: None
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that merges all the overlapping intervals of a list.

An interval is represented by a list of two integers [start, end], where
start <= end. Two intervals overlap if they share at least one value, so
intervals that only touch each other (like [1, 4] and [4, 5]) are also merged.

The function should:
- Take a list of intervals, in any order
- Return a NEW list where all overlapping intervals are merged into one
- Return the result sorted by the start of each interval
- Return an empty list if the input is empty
- Maintain optimal efficiency for large inputs

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:

Examples:
    merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
        -> [[1, 6], [8, 10], [15, 18]]
    merge_intervals([[1, 4], [4, 5]])
        -> [[1, 5]]
    merge_intervals([[5, 7], [1, 2]])
        -> [[1, 2], [5, 7]]
    merge_intervals([[1, 10], [2, 3], [4, 5]])
        -> [[1, 10]]
    merge_intervals([[3, 3]])
        -> [[3, 3]]
    merge_intervals([])
        -> []
""",
        "function": "merge_intervals",
        "tests": [
            ([[[1, 3], [2, 6], [8, 10], [15, 18]]], [[1, 6], [8, 10], [15, 18]]),
            ([[[1, 4], [4, 5]]], [[1, 5]]),
            ([[[5, 7], [1, 2]]], [[1, 2], [5, 7]]),
            ([[[1, 10], [2, 3], [4, 5]]], [[1, 10]]),
            ([[[3, 3]]], [[3, 3]]),
            ([[]], []),
            ([[[6, 8], [1, 9], [2, 4]]], [[1, 9]]),
            ([[[-5, -1], [-2, 0], [3, 4]]], [[-5, 0], [3, 4]]),
            ([[[1, 2], [3, 4], [5, 6]]], [[1, 2], [3, 4], [5, 6]]),
            ([_SHUFFLED_INTERVALS], [[i, i + 1] for i in range(0, 10000, 2)]),
        ],
    },

    "py_sorted_difference": {
        "level": 2,
        "subject": """\
Assignment name  : py_sorted_difference
Expected files   : py_sorted_difference.py
Allowed functions: Forbidden built-ins / modules: set(), sorted(), .sort().
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that receives two sorted lists and returns the values of the
first list that do NOT appear in the second list.

The function should:
- Take two lists of integers sorted in ascending order
- Return a NEW list with the values of the first list missing from the second
- Keep the result in ascending order
- Remove duplicates from the result
- Handle empty lists gracefully
- Maintain optimal efficiency for large inputs

Edge cases to handle:
- First list empty: return empty list
- Second list empty: return the first list without duplicates
- Every value of the first list is in the second: return empty list

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def sorted_difference(a: list[int], b: list[int]) -> list[int]:

Examples:
    sorted_difference([1, 2, 3, 4, 5], [2, 4])
        -> [1, 3, 5]
    sorted_difference([1, 1, 2, 3, 3], [3])
        -> [1, 2]
    sorted_difference([-3, 0, 2], [-5, -3, 1])
        -> [0, 2]
    sorted_difference([1, 2], [1, 2, 3])
        -> []
    sorted_difference([4, 4, 6], [])
        -> [4, 6]
    sorted_difference([], [1, 2])
        -> []
""",
        "function": "sorted_difference",
        "tests": [
            ([[1, 2, 3, 4, 5], [2, 4]], [1, 3, 5]),
            ([[1, 1, 2, 3, 3], [3]], [1, 2]),
            ([[-3, 0, 2], [-5, -3, 1]], [0, 2]),
            ([[1, 2], [1, 2, 3]], []),
            ([[4, 4, 6], []], [4, 6]),
            ([[], [1, 2]], []),
            ([[], []], []),
            ([[10, 20, 30], [5, 15, 25, 35]], [10, 20, 30]),
            ([[1, 2, 2, 2, 5], [2, 2]], [1, 5]),
            ([list(range(10000)), list(range(0, 10000, 2))],
             list(range(1, 10000, 2))),
        ],
    },

    "py_interleave_lists": {
        "level": 2,
        "subject": """\
Assignment name  : py_interleave_lists
Expected files   : py_interleave_lists.py
Allowed functions: Forbidden built-ins / modules: zip(), itertools.
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that interleaves the elements of multiple lists into a single
list.

The result takes the first element of each list (in order), then the second
element of each list, then the third, and so on.

The function should:
- Take a list of lists as input
- Return a single list with the elements interleaved
- When a list runs out of elements, simply skip it and continue with the others
- Ignore empty lists
- Return an empty list if no elements are found

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def interleave_lists(lists: list[list]) -> list:

Examples:
    interleave_lists([[1, 2, 3], ['a', 'b', 'c']])
        -> [1, 'a', 2, 'b', 3, 'c']
    interleave_lists([[1, 2], [10, 20, 30, 40]])
        -> [1, 10, 2, 20, 30, 40]
    interleave_lists([[1, 4, 7], [2, 5], [3]])
        -> [1, 2, 3, 4, 5, 7]
    interleave_lists([[], [1, 2]])
        -> [1, 2]
    interleave_lists([[5]])
        -> [5]
    interleave_lists([])
        -> []
""",
        "function": "interleave_lists",
        "tests": [
            ([[[1, 2, 3], ['a', 'b', 'c']]], [1, 'a', 2, 'b', 3, 'c']),
            ([[[1, 2], [10, 20, 30, 40]]], [1, 10, 2, 20, 30, 40]),
            ([[[1, 4, 7], [2, 5], [3]]], [1, 2, 3, 4, 5, 7]),
            ([[[], [1, 2]]], [1, 2]),
            ([[[5]]], [5]),
            ([[]], []),
            ([[[], [], []]], []),
            ([[[1], [], [2], [], [3]]], [1, 2, 3]),
            ([[['x', 'y', 'z'], [0]]], ['x', 0, 'y', 'z']),
        ],
    },

    # ── LEVEL 3 ──────────────────────────────────────────────
    "py_longest_palindrome_length": {
        "level": 3,
        "subject": """\
Assignment name  : py_longest_palindrome_length
Expected files   : py_longest_palindrome_length.py
Allowed functions: None
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Given a string `s`, find the length of the longest substring of `s` that is a
palindrome.

A substring is a sequence of consecutive characters of the string. A palindrome
reads the same forwards and backwards.

Return this length (an integer).

Constraints:
- An empty string has no substring -> 0.
- Any single character is a palindrome, so a non-empty string returns at
  least 1.
- If the entire string is already a palindrome -> len(s).
- Inputs can be long: your solution must be efficient.

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def longest_palindrome_length(s: str) -> int:

Examples:
    longest_palindrome_length("babad")             -> 3
    longest_palindrome_length("cbbd")              -> 2
    longest_palindrome_length("racecar")           -> 7
    longest_palindrome_length("forgeeksskeegfor")  -> 10
    longest_palindrome_length("abc")               -> 1
    longest_palindrome_length("")                  -> 0
""",
        "function": "longest_palindrome_length",
        "tests": [
            (["babad"], 3),
            (["cbbd"], 2),
            (["racecar"], 7),
            (["forgeeksskeegfor"], 10),
            (["abc"], 1),
            ([""], 0),
            (["a"], 1),
            (["aaaa"], 4),
            (["abacdfgdcaba"], 3),
            (["ab" * 1000], 1999),
        ],
    },

    "py_has_cycle": {
        "level": 3,
        "subject": """\
Assignment name  : py_has_cycle
Expected files   : py_has_cycle.py
Allowed functions: Forbidden built-ins / modules: graphlib.
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that detects if a directed graph contains a cycle.

The graph is given as a dictionary: each key is a node name and its value is the
list of nodes it points to. A cycle exists when, by following the arrows, it is
possible to come back to a node already visited on the same path.

The function should:
- Take a dictionary representing the graph
- Return True if the graph contains at least one cycle, False otherwise
- Check all the nodes, even the ones that are not connected to the others
- Handle an empty graph
- Handle very deep graphs (thousands of nodes in a single chain)

Edge cases to handle:
- Empty graph: return False
- A node pointing to itself: this is a cycle
- Two paths reaching the same node (diamond shape): this is NOT a cycle
- References to nodes that are not keys of the dictionary: ignore them

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def has_cycle(graph: dict[str, list[str]]) -> bool:

Examples:
    has_cycle({"a": ["b"], "b": ["c"], "c": []})
        -> False
    has_cycle({"a": ["b"], "b": ["a"]})
        -> True
    has_cycle({"a": ["a"]})
        -> True
    has_cycle({"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []})
        -> False
    has_cycle({"a": ["b"], "b": [], "c": ["d"], "d": ["e"], "e": ["c"]})
        -> True
    has_cycle({})
        -> False
""",
        "function": "has_cycle",
        "tests": [
            ([{"a": ["b"], "b": ["c"], "c": []}], False),
            ([{"a": ["b"], "b": ["a"]}], True),
            ([{"a": ["a"]}], True),
            ([{"a": ["b", "c"], "b": ["d"], "c": ["d"], "d": []}], False),
            ([{"a": ["b"], "b": [], "c": ["d"], "d": ["e"], "e": ["c"]}], True),
            ([{}], False),
            ([{"a": ["missing"]}], False),
            ([{"x": [], "y": [], "z": []}], False),
            ([{"1": ["2"], "2": ["3"], "3": ["4"], "4": ["2"]}], True),
            ([_CHAIN], False),
        ],
    },

    "py_count_reachable": {
        "level": 3,
        "subject": """\
Assignment name  : py_count_reachable
Expected files   : py_count_reachable.py
Allowed functions: None
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that counts how many nodes of a directed graph can be reached
from a starting node.

The graph is given as a dictionary: each key is a node name and its value is the
list of nodes it points to.

The function should:
- Take a dictionary representing the graph and the name of the starting node
- Return the number of different nodes that can be reached from the start
- Count the starting node itself
- Count each node only once, even if it can be reached by several paths
- Handle cycles without looping forever
- Handle very deep graphs (thousands of nodes in a single chain)

Edge cases to handle:
- Starting node not in the graph: return 0
- Starting node with no neighbours: return 1
- References to nodes that are not keys of the dictionary: they still count as
  reached, but they have no neighbours

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def count_reachable(graph: dict[str, list[str]], start: str) -> int:

Examples:
    count_reachable({"a": ["b", "c"], "b": ["d"], "c": [], "d": []}, "a")
        -> 4
    count_reachable({"a": ["b", "c"], "b": ["d"], "c": [], "d": []}, "b")
        -> 2
    count_reachable({"a": ["b"], "b": ["a"]}, "a")
        -> 2
    count_reachable({"a": ["b"], "b": [], "c": ["a"]}, "a")
        -> 2
    count_reachable({"x": []}, "x")
        -> 1
    count_reachable({"a": []}, "z")
        -> 0
""",
        "function": "count_reachable",
        "tests": [
            ([{"a": ["b", "c"], "b": ["d"], "c": [], "d": []}, "a"], 4),
            ([{"a": ["b", "c"], "b": ["d"], "c": [], "d": []}, "b"], 2),
            ([{"a": ["b"], "b": ["a"]}, "a"], 2),
            ([{"a": ["b"], "b": [], "c": ["a"]}, "a"], 2),
            ([{"x": []}, "x"], 1),
            ([{"a": []}, "z"], 0),
            ([{}, "a"], 0),
            ([{"a": ["b", "c"], "b": ["c"], "c": ["a"]}, "c"], 3),
            ([{"a": ["ghost"]}, "a"], 2),
            ([_CHAIN, "0"], 3001),
        ],
    },

    "py_count_islands": {
        "level": 3,
        "subject": """\
Assignment name  : py_count_islands
Expected files   : py_count_islands.py
Allowed functions: None
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that counts the number of islands on a map.

The map is a list of strings where '#' represents land and '.' represents water.
An island is a group of land cells connected horizontally or vertically.
Diagonal cells are NOT connected.

The function should:
- Take the map as a list of strings (all strings have the same length)
- Return the number of separate islands
- Return 0 if there is no land or if the map is empty
- Handle big maps (up to 200 x 200) efficiently

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def count_islands(grid: list[str]) -> int:

Examples:
    count_islands(['##..', '##..', '..##'])
        -> 2
    count_islands(['#.#', '.#.', '#.#'])
        -> 5
    count_islands(['###', '#.#', '###'])
        -> 1
    count_islands(['....', '....'])
        -> 0
    count_islands(['#'])
        -> 1
    count_islands([])
        -> 0
""",
        "function": "count_islands",
        "tests": [
            ([['##..', '##..', '..##']], 2),
            ([['#.#', '.#.', '#.#']], 5),
            ([['###', '#.#', '###']], 1),
            ([['....', '....']], 0),
            ([['#']], 1),
            ([[]], 0),
            ([['.']], 0),
            ([['#.#.#']], 3),
            ([['#', '.', '#', '#']], 2),
            ([_CHECKER], 5000),
            ([_FULL], 1),
        ],
    },

    # ── LEVEL 4 ──────────────────────────────────────────────
    "py_sliding_window_sum": {
        "level": 4,
        "subject": """\
Assignment name  : py_sliding_window_sum
Expected files   : py_sliding_window_sum.py
Allowed functions: Forbidden built-ins / modules: sum().
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that computes the sum of the elements in each sliding window of
size k in an array. Return a list of sums for each window position.

The function should:
- Slide a window of size k through the array, from left to right
- Compute the sum of the elements in each window position
- Return a list of sums
- Handle edge cases (empty array, k <= 0, k > array length)
- Return empty list for invalid inputs
- Maintain optimal efficiency for large inputs

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def sliding_window_sum(nums: list[int], k: int) -> list[int]:

Examples:
    sliding_window_sum([1, 2, 3, 4, 5], 2)
        -> [3, 5, 7, 9]
    sliding_window_sum([4, -1, 2, 7, 0], 3)
        -> [5, 8, 9]
    sliding_window_sum([5, -1, 3], 1)
        -> [5, -1, 3]
    sliding_window_sum([1, 2, 3], 3)
        -> [6]
    sliding_window_sum([1, 2], 3)
        -> []
    sliding_window_sum([], 2)
        -> []
    sliding_window_sum([1, 2, 3], 0)
        -> []
""",
        "function": "sliding_window_sum",
        "tests": [
            ([[1, 2, 3, 4, 5], 2], [3, 5, 7, 9]),
            ([[4, -1, 2, 7, 0], 3], [5, 8, 9]),
            ([[5, -1, 3], 1], [5, -1, 3]),
            ([[1, 2, 3], 3], [6]),
            ([[1, 2], 3], []),
            ([[], 2], []),
            ([[1, 2, 3], 0], []),
            ([[1, 2, 3], -1], []),
            ([[-4, -2, -5, -1], 2], [-6, -7, -6]),
            ([[1] * 20000, 5000], [5000] * 15001),
        ],
    },

    "py_longest_unique_substring": {
        "level": 4,
        "subject": """\
Assignment name  : py_longest_unique_substring
Expected files   : py_longest_unique_substring.py
Allowed functions: None
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that finds the length of the longest substring of a string that
does not contain any repeated character.

A substring is a sequence of consecutive characters of the string.

The function should:
- Take a string as input
- Return the length of the longest substring with all characters different
- Treat uppercase and lowercase letters as different characters
- Return 0 for an empty string
- Maintain optimal efficiency for large inputs

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def longest_unique_substring(s: str) -> int:

Examples:
    longest_unique_substring("abcabcbb")  -> 3
    longest_unique_substring("bbbbb")     -> 1
    longest_unique_substring("pwwkew")    -> 3
    longest_unique_substring("dvdf")      -> 3
    longest_unique_substring("abba")      -> 2
    longest_unique_substring("abcdef")    -> 6
    longest_unique_substring("")          -> 0
""",
        "function": "longest_unique_substring",
        "tests": [
            (["abcabcbb"], 3),
            (["bbbbb"], 1),
            (["pwwkew"], 3),
            (["dvdf"], 3),
            (["abba"], 2),
            (["abcdef"], 6),
            ([""], 0),
            (["aA"], 2),
            (["a b c a"], 3),
            (["tmmzuxt"], 5),
            (["abcdefghijklmnopqrstuvwxyz" * 2000], 26),
        ],
    },

    "py_min_window_average": {
        "level": 4,
        "subject": """\
Assignment name  : py_min_window_average
Expected files   : py_min_window_average.py
Allowed functions: Forbidden built-ins / modules: sum(), min().
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that finds the window of k consecutive elements with the
smallest average in an array, and returns the index where that window starts.

The function should:
- Slide a window of size k through the array
- Find the window position with the smallest average
- Return the starting index of that window
- If several windows have the same smallest average, return the first one
- Return -1 for invalid inputs (empty array, k <= 0, k > array length)
- Maintain optimal efficiency for large inputs

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def min_window_average(nums: list[int], k: int) -> int:

Examples:
    min_window_average([4, 2, 1, 3, 5], 2)
        -> 1
    min_window_average([3, 7, 90, 20, 10, 50, 40], 3)
        -> 3
    min_window_average([1, 1, 1], 2)
        -> 0
    min_window_average([5], 1)
        -> 0
    min_window_average([1, 2], 3)
        -> -1
    min_window_average([], 1)
        -> -1
""",
        "function": "min_window_average",
        "tests": [
            ([[4, 2, 1, 3, 5], 2], 1),
            ([[3, 7, 90, 20, 10, 50, 40], 3], 3),
            ([[1, 1, 1], 2], 0),
            ([[5], 1], 0),
            ([[1, 2], 3], -1),
            ([[], 1], -1),
            ([[1, 2, 3], 0], -1),
            ([[-1, -8, 2, -9], 2], 0),
            ([[10, 20, 30, 1], 1], 3),
            ([list(range(10000, 0, -1)), 1000], 9000),
        ],
    },

    "py_longest_ones_flips": {
        "level": 4,
        "subject": """\
Assignment name  : py_longest_ones_flips
Expected files   : py_longest_ones_flips.py
Allowed functions: None
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that receives a list of 0s and 1s and an integer k, and finds
the length of the longest group of consecutive 1s you can get if you are
allowed to change at most k zeros into ones.

The function should:
- Take a list containing only 0s and 1s, and an integer k
- Return the length of the longest group of consecutive 1s after changing at
  most k zeros
- Return 0 for an empty list
- Treat a negative k as 0
- Maintain optimal efficiency for large inputs

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def longest_ones_flips(nums: list[int], k: int) -> int:

Examples:
    longest_ones_flips([1, 1, 0, 0, 1, 1, 1, 0, 1], 1)
        -> 5
    longest_ones_flips([1, 1, 0, 0, 1, 1, 1, 0, 1], 2)
        -> 7
    longest_ones_flips([0, 0, 0], 2)
        -> 2
    longest_ones_flips([1, 1, 1], 0)
        -> 3
    longest_ones_flips([0, 1, 0], 0)
        -> 1
    longest_ones_flips([], 3)
        -> 0
""",
        "function": "longest_ones_flips",
        "tests": [
            ([[1, 1, 0, 0, 1, 1, 1, 0, 1], 1], 5),
            ([[1, 1, 0, 0, 1, 1, 1, 0, 1], 2], 7),
            ([[0, 0, 0], 2], 2),
            ([[1, 1, 1], 0], 3),
            ([[0, 1, 0], 0], 1),
            ([[], 3], 0),
            ([[0, 0, 0], 0], 0),
            ([[0, 0, 0], 5], 3),
            ([[1, 0, 1], -2], 1),
            ([[1, 0] * 10000, 100], 201),
        ],
    },
}