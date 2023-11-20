"""
the process of solving this problem includes:
1. identifying where the unsorted subarray starts, assuming it ascending
2. identifying where the unsorted subarray ends, still assuming its ascending
3. find the max and minimum value in the unsorted subarray and pick the indexes right before and after the unsorted start and end respectively
4. cater for the descending scenario in case the subarray is the same as the origin, reverse the earlier code using similar logic
"""


def find_unsorted_subarray(arr):
    n = len(arr)

    # Edge case: if the array is empty or has only one element, it's already sorted
    if n <= 1:
        return [0, 0]

    # Find the left boundary of the unsorted subarray
    left = 0
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1

    # If the array is already sorted, return [0, 0]
    if left == n - 1:
        return [0, 0]

    # Find the right boundary of the unsorted subarray
    right = n - 1
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1

    # Find the minimum and maximum values in the unsorted subarray
    min_val = min(arr[left:right + 1])
    max_val = max(arr[left:right + 1])

    # Extend the subarray to the left until the minimum value is in its correct position
    while left > 0 and arr[left - 1] > min_val:
        left -= 1

    # Extend the subarray to the right until the maximum value is in its correct position
    while right < n - 1 and arr[right + 1] < max_val:
        right += 1


    # In case it's a descending array
    if left == 0 and right == n-1:
        left = 0
        while left < n - 1 and arr[left] >= arr[left + 1]:
            left += 1

        # If the array is already sorted, return [0, 0]
        if left == n - 1:
            return [0, 0]
        
            # Find the right boundary of the unsorted subarray
        right = n - 1
        while right > 0 and arr[right] <= arr[right - 1]:
            right -= 1

            # Find the minimum and maximum values in the unsorted subarray
        min_val = min(arr[left:right + 1])
        max_val = max(arr[left:right + 1])

        # Extend the subarray to the left until the minimum value is in its correct position
        while left > 0 and arr[left - 1] < min_val:
            left -= 1

        # Extend the subarray to the right until the maximum value is in its correct position
        while right < n - 1 and arr[right + 1] > max_val:
            right += 1

        return [left, right]

    else:
        return [left, right]

arr = [11,10]
result = find_unsorted_subarray(arr)
print(result)
