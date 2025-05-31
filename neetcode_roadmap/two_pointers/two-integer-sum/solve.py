class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)): # Loop through the numbers
            if numbers[i] + numbers[-1] < target: # If the sum of the numbers is less than the target
                continue # Continue to the next number
            left = target - numbers[i] # Subtract the number from the target
            for j in range(i+1, len(numbers)): # Loop through the numbers
                if numbers[j] == left: # If the number is the left number
                    return [i+1, j+1] # Return the indices
        return False # Return False