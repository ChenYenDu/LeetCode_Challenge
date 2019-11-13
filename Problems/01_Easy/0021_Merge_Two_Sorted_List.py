# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 or not l2:  # if one of l1 or l2 is null, reutrn theother one
            return l1 or l2
        
        head = cur = ListNode(0)  # declare a ListNodo with val = 0
        
        while l1 and l2:
            if (l1.val < l2.val):   # add l1 to next if it's smaller than l2
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2       # the opposite operation
                l2 = l2.next
            cur = cur.next
        if l1:  # when l2 return None and l1 still left nodes, pass rest of l1 to cur 
            cur.next = l1
        if l2:  # when l1 return None and l2 still left nodes, pass rest of l2 to cur
            cur.next = l2
        
        return head.next # return the ListNode without the first 0
        
