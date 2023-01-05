# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        while head is not None:
            arr.append(head.val)
            head=head.next
        head=cur=ListNode(0)
        l=len(arr)
        start=0
        end=0
        while l-k>=0:
            l=l-k
            start=end
            end=start+k
            a=arr[start:end]
            if l-k<0:
                start=end
            a=a[::-1]
            for i in range(k):
                    cur.next=ListNode(a[i])
                    cur=cur.next
        if start<len(arr):
            while start<len(arr):
                cur.next=ListNode(arr[start])
                start=start+1
                cur=cur.next
        return head.next