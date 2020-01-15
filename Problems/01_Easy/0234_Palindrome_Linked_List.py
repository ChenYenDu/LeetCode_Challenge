# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        # Get the mid point (slow)
        slow = fast = cur = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            
        # Push the second half into the stack
        stack = [slow.val]
        while slow.next:
            slow = slow.next
            stack.append(slow.val)
            
        # Comparison
        while stack:
            if stack.pop() != cur.val:
                return False
            cur = cur.next
        
        return True
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]
