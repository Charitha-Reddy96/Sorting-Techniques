
#Iterative Approach
def Insertion_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i,0,-1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break
    return nums
            
nums = [12, 11, 13, 5, 6]
print("Before Sorting:", nums)
print("After Sorting:", (Insertion_sort(nums)))
# Output: [5, 6, 11, 12, 13]
# Time Complexity: O(n^2)
# Space Complexity: O(1)


#Recursive Approach

def Insertion_sort_recursive(nums,i, n=None):
    if i == n:
        return nums
    
    j = i
    while nums[j-1] > nums[j] and j > 0:
        nums[j], nums[j-1] = nums[j-1], nums[j]
        j -= 1
    return Insertion_sort_recursive(nums, i + 1, n)
        
nums = [12, 11, 13, 5, 6]
print("Before Sorting:", nums)
print("After Sorting:",Insertion_sort_recursive(nums, 1, len(nums)))
# Output: [5, 6, 11, 12, 13]
# Time Complexity: O(n^2)
# Space Complexity: O(1)
        
        
            

        
        
        
            
    
    