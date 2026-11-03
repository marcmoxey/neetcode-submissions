# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr =  head

        while curr != None:
            # save next -> curr.next
            nxt = curr.next
            # flip arr -> curr.next = prev
            curr.next = prev
            # move prev up -> prev = curr 
            prev = curr
            # move curr up  curr = nxt
            curr = nxt
        return prev

       
        

     

        