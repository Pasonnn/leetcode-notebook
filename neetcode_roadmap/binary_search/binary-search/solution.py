class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0  # left pointer
        r = len(nums)-1 # right pointer
        pointer = int((r+1)/2) # pointer
        while l <= r: # while the left pointer is less than or equal to the right pointer
            if nums[pointer] == target: # if the target is found
                return pointer # return the pointer
            elif nums[pointer] > target: # if the target is less than the pointer
                r = pointer-1 # move the right pointer to the left of the pointer
                pointer = int((l + r)/2) # move the pointer to the middle of the left and right pointers
            else: # if the target is greater than the pointer
                l = pointer+1 # move the left pointer to the right of the pointer
                pointer = int((l + r)/2) # move the pointer to the middle of the left and right pointers
        return -1 # if the target is not found, return -1
