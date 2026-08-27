"""
task08: Binary Search (Unassisted Debugged implementation)
Fixed off-by-one boundary index error.
"""

def binary_search(sorted_arr: list, target: int) -> int:
    low = 0
    high = len(sorted_arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
