# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
class Solution:
    # Iterative
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        prev = ListNode(0)
        curr = head
        while curr:
            nextTemp = curr.next 
            curr.next = prev
            prev, curr = curr, nextTemp
        
        return prev

'''
    
    
class Solution:
    # Recursive
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
