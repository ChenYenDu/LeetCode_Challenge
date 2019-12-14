# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    # Solution:
    # loop through all node and keep the previous node at the same time,
    # if node equals to val, remove it 
    
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_head = pre = ListNode(0) # create a fake ListNode for convencience
        pre.next = head 
        while head:
            if head.val == val:
                pre.next = head.next  # If head.val == val, pre.next will be passed to head.next
            else:
                pre = pre.next # If head.val != val, pre.next will be pre.next(same as head.next)
            head = head.next # head pass to next anywhy
        return new_head.next # new_head equals to pre but their first node is 0
    
    
    
    # Solution II: Quick & Slow Pointer
    # Quick pointer will loop through all node and pass node that do not equal to val to slow pointer
    # while the loop ends
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        slow, fast = new_head, head
        while fast:
            if fast.val != val:
                slow.next.val = fast.val # pass fast val to slow.next.val if fast is not equal to val
                slow = slow.next # slow pass to next if fast val is not val
            fast = fast.next # fast will pass to next anyway
        slow.next = None     # turn slow.next to None anyway
        return new_head.next
    '''
    # Recursion solution
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        head.next = self.removeElements(head.next, val)
        return head if head.val != val else head.next
    
