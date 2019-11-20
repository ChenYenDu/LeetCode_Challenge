# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
Solviing logic:
check if the next val is equal to current one, pass the next value
'''

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:  # if head or head.next is None, head is the result itself
            return head
        
        cur = head  # assign cur to head 
        
        while cur.next != None: 
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head  
	## Q: why is here returning head, does it mean head is also changed in the memory as cur loops ?
