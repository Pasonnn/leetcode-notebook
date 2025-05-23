class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # Loop 1: through the array
            value_need = target - nums[i] # Calculate the value needed to reach the target
            for j in range(i+1, len(nums)): # Loop 2: from the next element to the end of the array
                if nums[j] == value_need: # If the current element is the value needed
                    return [i, j] # Return the indices of the two numbers
        return [] # If no solution is found, return an empty list