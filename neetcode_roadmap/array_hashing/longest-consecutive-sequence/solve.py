class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Find length of longest consecutive sequence in array.
        
        Algorithm:
        1. Sort array to get numbers in ascending order
        2. Iterate through sorted array keeping track of current sequence length
        3. Skip duplicates to avoid counting same number twice
        4. When sequence breaks, store length and reset counter
        5. Return max length found
        
        Time: O(nlogn) for sorting, O(n) for iteration
        Space: O(n) for storing sequence lengths
        
        Args:
            nums: List of integers
            
        Returns:
            Length of longest consecutive sequence
        """
        # Handle empty input
        if not nums:
            return 0
            
        # Sort to get numbers in order
        sorted_seq = sorted(nums)
        
        # Track current sequence length
        longest = 0
        # Store lengths of all sequences found
        longest_list = []
        
        # Iterate through sorted array
        for i in range(1, len(sorted_seq)):
            # Skip duplicates
            if sorted_seq[i] == (sorted_seq[i-1]):
                continue
            # Extend sequence if consecutive
            if sorted_seq[i] == (sorted_seq[i-1]+1):
                longest += 1
                continue
            # Sequence breaks, store length and reset
            longest_list.append(longest+1)
            longest = 0
            
        # Add length of last sequence
        longest_list.append(longest+1)
        
        # Return longest sequence found
        return max(longest_list)