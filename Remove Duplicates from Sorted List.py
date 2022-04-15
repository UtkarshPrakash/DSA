# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return head
        prev = head
        pval = head.val
        while(prev.next!=None):
            curr = prev.next
            if (curr.next==None):
                if prev.val==curr.val:
                    prev.next=None
                break
            if prev.val==curr.val:
                while curr.val==prev.val:
                    if curr.next == None:
                        prev.next = None
                        break
                    prev.next = curr.next
                    curr = curr.next               
            
            prev = curr
            
        return head
                