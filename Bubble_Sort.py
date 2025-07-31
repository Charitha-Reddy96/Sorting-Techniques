#Iterative Approach    
def bubble_Sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums

nums = [13,46,24,52,20,9]
print("Before Sorting:", nums)
print(bubble_Sort(nums))
# Output: [9, 13, 20, 24, 46, 52]
# Time Complexity: O(n^2)   
# Space Complexity: O(1)

# Recursive Approach        
def Bubble_sort_recursive(nums, n=None): 
    swap = False
    if n == 0:
        return nums
    for i in range(n):
        if nums[i] > nums[i+1]:
            nums[i],nums[i+1] = nums[i+1],nums[i]
            swap = True
    if not swap:
        return nums
    return Bubble_sort_recursive(nums, n-1)
nums = [12, 11, 13, 5, 6]
print("Before Sorting:", nums)
print(Bubble_sort_recursive(nums, len(nums)-1))
# Output: [5, 6, 11, 12, 13]
# Time Complexity: O(n^2)
# Space Complexity: O(1)
