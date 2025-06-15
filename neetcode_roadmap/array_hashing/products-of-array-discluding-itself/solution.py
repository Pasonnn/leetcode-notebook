class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Step 1: Calculate the total product of all non-zero numbers
        total_product = 1 # initialize total product
        zero_count = 0 # initialize zero count
        
        for num in nums: # iterate through nums
            if num == 0: # if num is 0
                zero_count += 1  # count how many zeros
            else: # if num is not 0
                total_product *= num  # multiply only non-zero numbers

        # Step 2: Handle case where more than one zero exists
        if zero_count > 1: # if zero count is greater than 1
            # More than one zero means every product will be 0
            return [0] * len(nums) # return a list of 0s

        # Step 3: Build the result list
        result = [] # initialize result
        for num in nums: # iterate through nums
            if zero_count == 0: # if zero count is 0
                # No zeros: just divide total product by the current number
                result.append(total_product // num) # append the result
            else: # if zero count is not 0
                # One zero: only the zero position gets the total product
                if num == 0: # if num is 0
                    result.append(total_product) # append the result
                else: # if num is not 0
                    result.append(0) # append 0
        
        return result # return the result