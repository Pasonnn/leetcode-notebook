class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_check = [] # Create an array to store duplicate
        for num in nums: # Loop through each element in nums
            if num in duplicate_check: # If element appear in duplicate list return True
                return True
            duplicate_check.append(num) # Because num not in duplicate, then add it into the check duplicate list
            continue 
        return False # Return false if go through the nums list without any duplication