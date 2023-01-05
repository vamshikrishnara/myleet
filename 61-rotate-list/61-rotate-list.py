# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        cur=head
        count=0
        while cur:
            count+=1
            cur=cur.next
        k=k%count
        fir=head
        sec=head
        for _ in range(k):
            fir=fir.next
        while fir.next:
            fir=fir.next
            sec=sec.next
        fir.next=head
        head=sec.next
        sec.next=None
        return head
            
            