# Selection Sort Algorithm Implementation

def SelectionSort(nums):
    n = len(nums)
    for i in range(n):
        min_pos = i
        for j in range(i+1, n):
            if nums[j] < nums[min_pos]:
                min_pos = j
        nums[i], nums[min_pos] = nums[min_pos], nums[i]
    return nums

nums = [13,46,24,52,20,9]
print("Before Sorting:", nums)
print(SelectionSort(nums))
# Output: [9, 13, 20, 24, 46, 52]
# Time Complexity: O(n^2)
# Space Complexity: O(1)
