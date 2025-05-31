class Solution:
    def isPalindrome(self, s: str) -> bool:
        full_char = [] # Create a list to store the numeric and alphabet characters
        alphabet = "qwertyuiopasdfghjklzxcvbnm" # Define the alphabet
        for char in s: # Iterate through the string
            if char.lower() in alphabet or char.isdigit(): # Check if the character is a numeric or alphabet character
                full_char.append(char.lower()) # Append the character to the list
        length = len(full_char) # Get the length of the list
        for i in range(int(length/2)): # Iterate through the list
            if full_char[i] != full_char[length-1-i]: # Check if the character is the same as the character at the end of the list
                return False
        return True