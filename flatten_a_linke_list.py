#User function Template for python3

# Link: https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1
'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def flatten(root):
    #Your code here
    def merge(a,b):
        if a is None:
            return b
        if b is None:
            return a
        ans = None
        if a.data<b.data:
            ans = a
            ans.bottom = merge(a.bottom,b)
        else:
            ans = b
            ans.bottom = merge(a,b.bottom)
        return ans
            
    def flatten(root):
        if root is None:
            return None
        root.next = flatten(root.next)
        root = merge(root,root.next)
        return root
    return flatten(root)
        
    return dummy.bottom
