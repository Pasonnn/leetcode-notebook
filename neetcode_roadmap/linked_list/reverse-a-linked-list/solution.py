# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: # if the list is empty
            return None
        left = None # left pointer
        mid = head # middle pointer
        while mid != None: # while the middle pointer is not at the end of the list
            right = mid.next # right pointer
            mid.next = left # reverse the link
            left = mid # move the left pointer to the middle pointer
            mid = right # move the middle pointer to the right pointer  
        return left # return the new beginning of the list