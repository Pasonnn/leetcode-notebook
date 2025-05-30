class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {} # Dictionary to store the anagrams

        def to_string(arr): # Function to convert a list of characters to a string
            output = ""
            for char in arr:
                output += char
            return output
        
        for word in strs:
            s_word = to_string(sorted(word)) # Convert the sorted word to a string
            if s_word not in ana_dict: # If the sorted word is not in the dictionary
                ana_dict[s_word] = [word] # Add the word to the dictionary
            else:
                ana_dict[s_word].append(word) # Add the word to the list of anagrams

        output_arr = [] # List to store the output
        for sort_word in ana_dict:
            output_arr.append(ana_dict[sort_word]) # Add the list of anagrams to the output list
        return output_arr # Return the output list