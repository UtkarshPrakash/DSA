# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        mul = 1
        while(l1!=None):
            n1 = n1 + l1.val*mul
            mul *= 10
            l1 = l1.next
        mul = 1
        while(l2!=None):
            n2 = n2 + l2.val*mul
            mul *= 10
            l2 = l2.next
        res = n1 + n2
        ans = ListNode()
        temp = ListNode()
        ans.next = temp
        
        
        while(res>0):
            temp.val = res%10
            res //= 10
            temp = temp.next
        return ans