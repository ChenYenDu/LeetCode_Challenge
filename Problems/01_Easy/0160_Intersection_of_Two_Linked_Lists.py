# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        串連 headA 跟 headB, 在利用fast/slow pointer去找出loop node 
        參考 Easy 144
        '''
        if not headA or not headB:
            return None
        
        # Concatenate A and B 
        last = headA
        while last.next:
            last = last.next
        last.next = headB
        
        # Find the start of the loop, if excit there is an intersection
        # use slow fast pointers
        fast = slow = headA
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = headA
                while fast != slow:
                    slow, fast = slow.next, fast.next
                last.next = None
                return slow
        
        # No loop found
        last.next = None
        return None


'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        
        A_pointer = headA
        B_pointer = headB
        
        while A_pointer != B_pointer:
            A_pointer = headB if A_pointer == None else A_pointer.next
            B_pointer = headA if B_pointer == None else B_pointer.next
            
        return A_pointer
'''

