# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast == None or fast.next == None:
                return False

            slow = slow.next
            fast = fast.next.next

        return True


"""
Fast and Slow Pointers:
    fast -> 每次跨2格
    slow -> 每次跨1格
如果有circle:
    fast 先進入循環 slow後進入循環 但兩者一定會在循環中相遇 -> return true

如果沒有circle:
    fast 會遇到 None -> return false
"""
