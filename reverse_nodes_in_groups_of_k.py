# Link: https://leetcode.com/problems/reverse-nodes-in-k-group/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            return prev
        prev = None
        def nexus(head):
            if not head:
                return None
            start = head
            for i in range(k):

                if head:
                    temp = head
                    head = head.next
                else:
                    return start
            temp.next = None
            rev = reverse(start)
            start.next = nexus(head)
            return rev
        return nexus(head)
        
        


                
