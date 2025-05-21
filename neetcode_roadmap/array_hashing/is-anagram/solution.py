class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        character_s = {} # Create a dict to store character of s with amount of character
        character_t = {} # Like above
        if len(s) != len(t): # If the word len is diff, then it is not Anagram
            return False 
        for i in range(len(s)): # Loop through index of word s
            if s[i] not in character_s: # if the character is not store into the dict of s yet, give it equal 1
                character_s[s[i]] = 1
            else: # Else add 1 into value of that character
                character_s[s[i]] += 1
            
            if t[i] not in character_t: # Like above but do it for t
                character_t[t[i]] = 1
            else:
                character_t[t[i]] += 1

        for character in character_s: # Loop through each character in s (or t is also valid)
            try:
                if character_s[character] != character_t[character]: # If the amount of that character diff, return false
                    return False
            except: # If s have a character that t don't, it will raise error then we return False
                return False
        return True # If it pass all the validation above, return True :D
