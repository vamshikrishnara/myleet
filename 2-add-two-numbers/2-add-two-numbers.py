# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        dumm=ListNode()
        curr=dumm
        while l1 and l2:
            k=ListNode((l1.val+l2.val+carry) % 10)
            carry=(l1.val+l2.val+carry)//10
            l1=l1.next
            l2=l2.next
            dumm.next=k
            dumm=dumm.next
        while l1:
            k=ListNode((l1.val+carry)%10)
            carry=(l1.val+carry)//10
            l1=l1.next
            dumm.next=k
            dumm=dumm.next
        while l2:
            k=ListNode((l2.val+carry)%10)
            carry=(l2.val+carry)//10
            l2=l2.next
            dumm.next=k
            dumm=dumm.next
        if carry:
            dumm.next=ListNode(carry,None)
        return curr.next