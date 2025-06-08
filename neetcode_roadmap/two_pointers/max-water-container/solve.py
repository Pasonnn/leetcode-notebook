class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 # left pointer
        right = len(heights)-1 # right pointer
        water = [] # list of water volumes
        while left < right: # while left pointer is less than right pointer
            left_bar = heights[left] # left bar height
            right_bar = heights[right] # right bar height
            if left_bar < right_bar: # if left bar height is less than right bar height
                water.append(left_bar*(right-left)) # add water volume to list
                left += 1 # move left pointer to the right
            else: # if left bar height is greater than right bar height
                water.append(right_bar*(right-left)) # add water volume to list
                right -= 1 # move right pointer to the left
        return max(water) # return the maximum water volume