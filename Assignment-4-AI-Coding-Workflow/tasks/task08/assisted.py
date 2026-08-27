"""
task08: Binary Search (AI-Assisted Debugged implementation)
Fixed off-by-one boundary index error.
"""

def binary_search(sorted_arr: list, target: int) -> int:
    low, high = 0, len(sorted_arr) - 1
    while low <= high:
        mid = (low + high) // 2
        val = sorted_arr[mid]
        if val == target:
            return mid
        if val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
