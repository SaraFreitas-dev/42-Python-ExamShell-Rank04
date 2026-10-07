# ─────────────────────────────────────────────────────────────
# EXERCISE BANK - EXAM RANK 04
# ─────────────────────────────────────────────────────────────

EXERCISES = {
    # ── LEVEL 1 ──────────────────────────────────────────────
    "py_array_rotation_detector": {
        "level": 1,
        "subject": """\
Assignment name  : py_array_rotation_detector
Expected files   : py_array_rotation_detector.py
Allowed functions: Forbidden built-ins / modules: collections.deque.rotate().
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a Python function that takes two lists (arrays) as parameters and
determines if the second list is a rotation of the first list (left or right).

A rotation means that the elements are shifted circularly.
For example, shifting [1, 2, 3] to the right by one position results in [3, 1, 2].

The function must return True if arr2 is a rotation of arr1, and False otherwise.
If the arrays have different lengths, they cannot be rotations of each other.
Two empty arrays are considered rotations of each other.

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def array_rotation_detector(arr1: list, arr2: list) -> bool:

Examples:
    array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]) -> True
    array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]) -> True
    array_rotation_detector([1, 2, 3], [3, 2, 1])             -> False
    array_rotation_detector([1, 2], [1, 2, 3])                -> False
    array_rotation_detector([], [])                            -> True
""",
        "function": "array_rotation_detector",
        "tests": [
            ([[1, 2, 3, 4, 5], [4, 5, 1, 2, 3]], True),
            ([[1, 2, 3, 4, 5], [5, 1, 2, 3, 4]], True),
            ([[1, 2, 3], [3, 2, 1]], False),
            ([[1, 2], [1, 2, 3]], False),
            ([[], []], True),
            ([[1], [1]], True),
            ([[7, 8, 9], [8, 9, 7]], True),
            ([[1, 2, 3], [1, 2, 3]], True),
            ([[1, 2, 3], [2, 3, 1]], True),
            ([[1, 2, 3], [2, 1, 3]], False),
        ],
    },

    "py_constellation_mapper": {
        "level": 1,
        "subject": """\
Assignment name  : py_constellation_mapper
Expected files   : py_constellation_mapper.py
Allowed functions: None
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that maps a constellation of stars onto a grid and returns
the visual representation as a list of strings.

The function should:
- Take a list of star coordinates as tuples (row, col) and grid size as integer
- Return a list of strings representing the grid
- Stars are represented by '*' and empty spaces by '.'
- Grid coordinates start from (0, 0) at top-left
- Ignore coordinates outside the grid boundaries
- Handle duplicate coordinates (star appears only once)

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:

Examples:
    constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)
        -> ['*..', '.*.', '..*']
    constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)
        -> ['.*.', '***', '.*.']
    constellation_mapper([], 2)
        -> ['..', '..']
    constellation_mapper([(0, 0), (0, 0), (1, 1)], 2)
        -> ['*.', '.*']
    constellation_mapper([(0, 0), (5, 5)], 3)
        -> ['*..', '...', '...']
    constellation_mapper([(1, 0), (1, 1), (1, 2)], 3)
        -> ['...', '***', '...']
""",
        "function": "constellation_mapper",
        "tests": [
            ([[(0, 0), (1, 1), (2, 2)], 3], ['*..', '.*.', '..*']),
            ([[(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3], ['.*.', '***', '.*.']),
            ([[], 2], ['..', '..']),
            ([[(0, 0), (0, 0), (1, 1)], 2], ['*.', '.*']),
            ([[(0, 0), (5, 5)], 3], ['*..', '...', '...']),
            ([[(1, 0), (1, 1), (1, 2)], 3], ['...', '***', '...']),
            ([[(-1, 0), (0, -1), (0, 0)], 2], ['*.', '..']),
            ([[], 1], ['.']),
        ],
    },

    # ── LEVEL 2 ──────────────────────────────────────────────
    "py_merge_sorted_lists": {
        "level": 2,
        "subject": """\
Assignment name  : py_merge_sorted_lists
Expected files   : py_merge_sorted_lists.py
Allowed functions: Forbidden built-ins / modules: sorted(), .sort(), heapq.merge().
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that merges multiple sorted lists into one sorted list while
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

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def merge_sorted_lists(lists: list[list[int]]) -> list[int]:

Examples:
    merge_sorted_lists([[1, 3, 5], [2, 4, 6]])
        -> [1, 2, 3, 4, 5, 6]
    merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]])
        -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
    merge_sorted_lists([[5], [1, 3], [2, 4]])
        -> [1, 2, 3, 4, 5]
    merge_sorted_lists([[1, 1, 2], [2, 3, 3]])
        -> [1, 1, 2, 2, 3, 3]
    merge_sorted_lists([[], [1, 2, 3]])
        -> [1, 2, 3]
    merge_sorted_lists([[]])
        -> []
    merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]])
        -> [-5, -3, -1, 0, 2, 4]
    merge_sorted_lists([[10], [10], [10]])
        -> [10, 10, 10]
""",
        "function": "merge_sorted_lists",
        "tests": [
            ([[[1, 3, 5], [2, 4, 6]]], [1, 2, 3, 4, 5, 6]),
            ([[[1, 5, 9], [2, 3, 8], [4, 6, 7]]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ([[[5], [1, 3], [2, 4]]], [1, 2, 3, 4, 5]),
            ([[[1, 1, 2], [2, 3, 3]]], [1, 1, 2, 2, 3, 3]),
            ([[[], [1, 2, 3]]], [1, 2, 3]),
            ([[[]]], []),
            ([[[-5, -1, 0], [-3, 2, 4]]], [-5, -3, -1, 0, 2, 4]),
            ([[[10], [10], [10]]], [10, 10, 10]),
            ([[]], []),
            ([[[1, 2, 3]]], [1, 2, 3]),
            ([[[1], [], [2], []]], [1, 2]),
            ([[[1, 2, 3, 4, 5, 6], [0]]], [0, 1, 2, 3, 4, 5, 6]),
            ([[[1, 2, 2], [1, 2, 3]]], [1, 1, 2, 2, 2, 3]),
            ([[[4, 5], [1, 2]]], [1, 2, 4, 5]),
            ([[[-9, -3], [-7, -1]]], [-9, -7, -3, -1]),
            ([[[], [], []]], []),
            ([[[2 * i, 2 * i + 1] for i in range(5000)]], list(range(10000))),
        ],
    },

    "py_list_intersection_finder": {
        "level": 2,
        "subject": """\
Assignment name  : py_list_intersection_finder
Expected files   : py_list_intersection_finder.py
Allowed functions: None
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that finds the intersection of multiple sorted lists.
Return a new list containing elements that appear in ALL input lists, in sorted order.

The function should:
- Return elements that appear in ALL lists
- Result should be sorted in ascending order
- Remove duplicates from the result
- Handle empty input or empty lists gracefully
- If any list is empty, the intersection is empty

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def list_intersection_finder(lists: list[list[int]]) -> list[int]:

Examples:
    list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]])
        -> [2, 3]
    list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]])
        -> [4]
    list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]])
        -> [1, 2, 3]
    list_intersection_finder([[1, 2, 3], [4, 5, 6]])
        -> []
    list_intersection_finder([])
        -> []
    list_intersection_finder([[1, 2, 3], []])
        -> []
    list_intersection_finder([[5]])
        -> [5]
""",
        "function": "list_intersection_finder",
        "tests": [
            ([[[1, 2, 3], [2, 3, 4], [2, 3, 5]]], [2, 3]),
            ([[[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]], [4]),
            ([[[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]], [1, 2, 3]),
            ([[[1, 2, 3], [4, 5, 6]]], []),
            ([[]], []),
            ([[[1, 2, 3], []]], []),
            ([[[5]]], [5]),
            ([[[-3, -1, 0, 2], [-3, 0, 4], [-3, 0, 8]]], [-3, 0]),
        ],
    },

    # ── LEVEL 3 ──────────────────────────────────────────────
    "py_palindrome_partitioner": {
        "level": 3,
        "subject": """\
Assignment name  : py_palindrome_partitioner
Expected files   : py_palindrome_partitioner.py
Allowed functions: None
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Given a string `s`, find the minimum number of cuts needed to partition it such
that every resulting substring is a palindrome.

A cut divides the string between two characters. With `c` cuts, the string is
split into `c + 1` substrings. We want the minimum number of cuts `c` such that
all parts are palindromes.

Return this minimum number of cuts (an integer).

Constraints:
- An empty string or a string of length 1 is already a palindrome -> 0 cuts.
- If the entire string is already a palindrome -> 0 cuts.
- In the worst case (all characters are distinct), the result is len(s) - 1 cuts.

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def palindrome_partitioner(s: str) -> int:

Examples:
    palindrome_partitioner("aab") -> 1
    palindrome_partitioner("aba") -> 0
    palindrome_partitioner("abc") -> 2
""",
        "function": "palindrome_partitioner",
        "tests": [
            (["aab"], 1),
            (["aba"], 0),
            (["abc"], 2),
            ([""], 0),
            (["a"], 0),
            (["racecar"], 0),
            (["abcd"], 3),
            (["abbae"], 1),
        ],
    },

    "py_package_dependency_resolver": {
        "level": 3,
        "subject": """\
Assignment name  : py_package_dependency_resolver
Expected files   : py_package_dependency_resolver.py
Allowed functions: Forbidden built-ins / modules: graphlib.TopologicalSorter.
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that determines a valid package installation order by resolving
dependencies. Use topological sorting to ensure dependencies are installed before
the packages that require them.

The function should:
- Take a dictionary where keys are package names and values are lists of dependencies
- Return packages in installation order (dependencies first)
- Return empty list if no valid order exists (circular dependencies)
- Handle empty input and isolated dependency chains
- Ignore references to packages not in the input dictionary

Algorithm requirements:
- Use topological sorting (e.g., Kahn's algorithm)
- Process packages with no remaining dependencies first
- Ensure deterministic output when multiple valid orders exist

Edge cases to handle:
- Empty input: return empty list
- Packages with no dependencies: include in output first
- Multiple independent chains: process all chains
- Circular dependencies: return empty list
- Non-existent dependencies: ignore missing packages
- Self-dependencies: return empty list

Notes:
- For deterministic output, process packages alphabetically when choices exist
- A package cannot be installed until all its dependencies are installed
- If any circular dependency exists, no valid installation order is possible

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:

Examples:
    package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []})
        -> ["driver", "database", "app"]
    package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]})
        -> ["A", "B", "C"]
    package_dependency_resolver({})
        -> []
    package_dependency_resolver({"X": ["Y"], "Y": ["X"]})
        -> []
    package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]})
        -> ["api", "web", "backend", "frontend"]
""",
        "function": "package_dependency_resolver",
        "tests": [
            ([{"app": ["database"], "database": ["driver"], "driver": []}], ["driver", "database", "app"]),
            ([{"A": [], "B": ["A"], "C": ["A", "B"]}], ["A", "B", "C"]),
            ([{}], []),
            ([{"X": ["Y"], "Y": ["X"]}], []),
            ([{"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}], ["api", "web", "backend", "frontend"]),
            ([{"A": ["MISSING"], "B": ["A"]}], ["A", "B"]),
            ([{"A": ["A"]}], []),
            ([{"B": [], "A": []}], ["A", "B"]),
        ],
    },

    # ── LEVEL 4 ──────────────────────────────────────────────
    "py_sliding_window_maximum": {
        "level": 4,
        "subject": """\
Assignment name  : py_sliding_window_maximum
Expected files   : py_sliding_window_maximum.py
Allowed functions: None
Use only permitted built-in functions to avoid getting 0 on exam day.

--------------------------------------------------------------------------------

Write a function that finds the maximum element in each sliding window of size k
in an array. Return a list of maximums for each window position.

The function should:
- Slide a window of size k through the array
- Find the maximum element in each window position
- Return a list of maximum values
- Handle edge cases (empty array, k <= 0, k > array length)
- Return empty list for invalid inputs

--------------------------------------------------------------------------------

Your function must be declared as follows:

    def sliding_window_maximum(nums: list[int], k: int) -> list[int]:

Examples:
    sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3)
        -> [3, 3, 5, 5, 6, 7]
    sliding_window_maximum([1, 2, 3, 4, 5], 2)
        -> [2, 3, 4, 5]
    sliding_window_maximum([5, 4, 3, 2, 1], 1)
        -> [5, 4, 3, 2, 1]
    sliding_window_maximum([1, 2, 3], 3)
        -> [3]
    sliding_window_maximum([1, 2, 3], 4)
        -> []
    sliding_window_maximum([], 2)
        -> []
    sliding_window_maximum([1, 2, 3], 0)
        -> []
""",
        "function": "sliding_window_maximum",
        "tests": [
            ([[1, 3, -1, -3, 5, 3, 6, 7], 3], [3, 3, 5, 5, 6, 7]),
            ([[1, 2, 3, 4, 5], 2], [2, 3, 4, 5]),
            ([[5, 4, 3, 2, 1], 1], [5, 4, 3, 2, 1]),
            ([[1, 2, 3], 3], [3]),
            ([[1, 2, 3], 4], []),
            ([[], 2], []),
            ([[1, 2, 3], 0], []),
            ([[1, 2, 3], -1], []),
            ([[-4, -2, -5, -1], 2], [-2, -2, -1]),
        ],
    },
}
