#Link: https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            return prev
        def length(head):
            n = 0
            while head:
                n+=1
                head = head.next
            return n
        def printer(head):
            while head:
                print(head.val,end = ' ')
                head = head.next
            print()
        n = length(head)
        if n <=1:
            return head

        k%=n
        if k == 0:
            return head
        head = reverse(head)
        #printer(head)
        temp = head
        prev = None
        while k:
            prev = temp
            temp = temp.next
            k-=1
        prev.next = None
        x = reverse(head)
        y = reverse(temp)
        head.next = y
        return x
        