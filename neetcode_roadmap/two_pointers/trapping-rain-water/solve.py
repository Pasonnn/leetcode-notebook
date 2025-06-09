class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        water = 0
        while left + 1 <= right:
            if height[left] > height[right]: # Left bigger than right, water raise to right
                temp_right = False # temp_right is False
                water_level = height[right] # water_level is the height of the right bar
                bigger_height = False # bigger_height is False
                for i in range(right-1, left, -1): # for i in range(right-1, left, -1)
                    if height[i] > water_level and not bigger_height: # if height[i] is greater than water_level and bigger_height is False
                        temp_right = i # temp_right is i
                        bigger_height = True # bigger_height is True
                        continue
                    if height[i] < water_level: # if height[i] is less than water_level
                        water += (water_level - height[i]) # water is water_level - height[i]
                        height[i] += (water_level - height[i]) # height[i] is height[i] + (water_level - height[i])
                        if not temp_right: # if not temp_right
                            continue
                right = temp_right # right is temp_right
            else: # Right bigger than left, water rise to left
                temp_left = False # temp_left is False
                water_level = height[left] # water_level is the height of the left bar
                bigger_height = False # bigger_height is False
                for i in range(left+1, right): # for i in range(left+1, right)
                    if height[i] > water_level and not bigger_height: # if height[i] is greater than water_level and bigger_height is False
                        temp_left = i # temp_left is i
                        bigger_height = True # bigger_height is True
                        continue
                    if height[i] < water_level: # if height[i] is less than water_level
                        water += (water_level - height[i]) # water is water_level - height[i]
                        height[i] += (water_level - height[i]) # height[i] is height[i] + (water_level - height[i])
                        if not temp_left: # if not temp_left
                            continue
                left = temp_left # left is temp_left
            if not bigger_height: # if not bigger_height (no temp_left or temp_right)
                break # break
        return water # return water