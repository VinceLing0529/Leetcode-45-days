#153. Find Minimum in Rotated Sorted Array
def findMin(self, nums):
    if len(nums) == 1:
        return nums[0]
    left = 0
    right = len(nums)-1
    if nums[right]> nums[0]:
        return nums[0]
    while right >= left:
        mid = left + (right - left) / 2
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        if nums[mid-1]>nums[mid]:
            return nums[mid]
        if nums[mid] > nums[0]:
            left = mid+1
        else:
            right = mid-1
#162. Find Peak Element
def findPeakElement(self, nums):
    if len(nums) == 1:
        return 0
    left = 0
    right = len(nums)-1
    while right>left:
        mid = (right+left)//2
        if nums[mid]>nums[mid+1]:
            right = mid
        else:
            left = mid+1
    return left
#33. Search in Rotated Sorted Array
def search(self, nums, target):
    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left)//2

        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            # if this is true, [left..mid] is sorted and strictly increasing since no-dups
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # if [left..mid] not sorted, [mid..right] must be sorted
            if target <= nums[right] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
#81. Search in Rotated Sorted Array II
def search(self, nums, target):

    left, right = 0, len(nums)-1
    while left<=right:
        mid = left+(right-left)//2
        if nums[mid]==target:
            return True
        elif nums[mid]==nums[left] and nums[left]==nums[right]:
            left+=1
            right-=1
        elif nums[left]<=nums[mid]:
            if target>=nums[left] and target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        else:
            if target>nums[mid] and target<=nums[right]:
                left=mid+1
            else:
                right=mid-1
    return False       
#74. Search a 2D Matrix
def searchMatrix(self, matrix, target):
    if len(matrix) == 1 and len(matrix[0])==1:
        return True if matrix[0][0] == target else False
    left = 0
    right = len(matrix[0])-1
    box = 0
    while left<=right:
        
        while target > matrix[box][-1]:
            box+=1
            if box == len(matrix):return False
        
        mid = left+(right-left)//2

        if matrix[box][mid] == target:
            return True
        elif matrix[box][mid]<target:
            left = mid +1
        else:
            right = mid-1
    return False
#240. Search a 2D Matrix II
def searchMatrix(self, matrix, target):
    if len(matrix) == 1 and len(matrix[0])==1:
        return True if matrix[0][0] == target else False

    box = 0
    while target > matrix[box][-1]:
        box+=1
        if box == len(matrix):return False
    while True:  
        left = 0
        right = len(matrix[0])-1
        while left<=right:
            mid = left+(right-left)//2
            if matrix[box][mid] == target:
                return True
            elif matrix[box][mid]<target:
                left = mid +1
            else:
                right = mid-1
        if target < matrix[box][0] :return False
        box +=1
        if  box == len(matrix) : return False
    return False