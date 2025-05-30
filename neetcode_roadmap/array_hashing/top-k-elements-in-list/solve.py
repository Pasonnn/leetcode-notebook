class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_key = [] # List to store the keys
        num_val = [] # List to store the values
        num_dict = {} # Dictionary to store the keys and values

        def findKeyIndex(target): # Function to find the index of the key
            index = 0
            for num in num_key:
                if target == num:
                    return index
                index += 1
            return -1

        def findKeyByValue(value): # Function to find the key by the value
            output = False
            for k in num_dict:
                if num_dict[k] == value:
                    output = k
                    num_dict[k] = -1
                    break
            return output
        
        for num in nums: # Loop through the nums
            if num not in num_key: # If the num is not in the num_key
                num_dict[num] = 1 # Add the num to the num_dict
                num_key.append(num) # Add the num to the num_key
                num_val.append(1) # Add the num to the num_val
            else: # If the num is in the num_key
                num_dict[num] += 1 # Add the num to the num_dict
                key_index = findKeyIndex(num) # Find the index of the num
                num_val[key_index] += 1 # Add the num to the num_val
                
        desc_val = sorted(num_val, reverse=True) # Sort the num_val in descending order
        output_arr = [] # List to store the output
        for i in range(k): # Loop through the k
            value = desc_val[i] # Get the value
            key_output = findKeyByValue(value) # Find the key by the value
            output_arr.append(key_output) # Add the key to the output_arr
        return (output_arr) # Return the output_arr
