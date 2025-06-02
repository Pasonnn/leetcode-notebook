class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        h = len(matrix)-1
        w = len(matrix[0])-1

        l = [0, 0] # Set left pointer equal x(0), y(0)
        r = [h, w] # Set the right pointer equal x(max), y(max)

        for line in matrix:
            print(line)

        print(h, w)

        while (matrix[l[0]][l[1]] < matrix[r[0]][r[1]]): # While the left pointer is smaller than righ pointer
            p = [int((sum(r)-sum(l))/w), int((sum(r)-sum(l))%w)] # Set pointer as middle
            print(l, r)
            print(p)
            if matrix[p[0]][p[1]] == target: # If found target
                return True
            elif matrix[p[0]][p[1]] > target: # If the target is on the left side
                p_h = p[0] 
                p_w = p[1]
                if p_w <= 0:
                    p_h -= 1
                    p_w = w
                r = [p_h, p_w-1]
            else:
                p_h = p[0] 
                p_w = p[1]
                if p_w >= w:
                    p_h += 1
                    p_w = 0
                l = [p_h, p_w+1]
        return False

            
            
