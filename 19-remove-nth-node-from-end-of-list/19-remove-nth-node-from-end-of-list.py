# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        prev=head
        while prev:
            prev=prev.next
            count+=1
        if count==0 and n==1:
            head=None
        val=count-n
        if val==0:
            return head.next
        value=head
        p=1
        while p<val:
            value=value.next
            p+=1
        prev=value.next
        if prev.next is None:
            value.next=None
        else:
            value.next=prev.next
        return head
                
            
            